---
name: distributed-training
description: Distributed training strategies for scaling large model training across GPUs and nodes
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, distributed-training, deepspeed, fsdp, parallelism, scaling]
---

# Distributed Training

## Overview

Distributed training enables training of large-scale AGI/ASI models that exceed single GPU memory by distributing computation across multiple GPUs and nodes. This skill covers parallelism strategies, frameworks (DeepSpeed, FSDP), and practical implementation patterns for scaling OMEGA ASI training.

## Core Concepts

### Parallelism Taxonomy

```
┌─────────────────────────────────────────────────────────────────┐
│                    Parallelism Strategies                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Data Parallelism (DP)                                          │
│  ├── Replicate model across GPUs                                │
│  ├── Split batch across replicas                                │
│  └── Sync gradients via all-reduce                              │
│                                                                  │
│  Tensor Parallelism (TP)                                        │
│  ├── Split individual layers across GPUs                        │
│  ├── Column-wise or row-wise partitioning                       │
│  └── Requires high-bandwidth interconnect                       │
│                                                                  │
│  Pipeline Parallelism (PP)                                      │
│  ├── Split model layers across stages                           │
│  ├── Micro-batch pipelining                                     │
│  └── Reduces memory per GPU                                     │
│                                                                  │
│  Sequence Parallelism (SP)                                      │
│  ├── Split sequence dimension                                   │
│  ├── Reduces activation memory                                  │
│  └── Often combined with TP                                     │
│                                                                  │
│  Expert Parallelism (EP)                                        │
│  ├── Distribute MoE experts across GPUs                         │
│  ├── All-to-all communication for routing                       │
│  └── Scales model capacity efficiently                          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Memory Breakdown

Understanding memory usage is critical for distributed strategy selection:

```python
def estimate_training_memory(
    params_billions: float,
    batch_size: int,
    seq_length: int,
    hidden_size: int,
    num_layers: int,
    precision: str = "bf16",
    optimizer: str = "adamw"
) -> dict:
    """
    Estimate GPU memory requirements for training.
    
    Returns memory breakdown in GB.
    """
    bytes_per_param = 2 if precision in ["fp16", "bf16"] else 4
    
    # Model parameters
    param_memory = params_billions * 1e9 * bytes_per_param / 1e9  # GB
    
    # Gradients (same size as parameters)
    gradient_memory = param_memory
    
    # Optimizer states
    if optimizer == "adamw":
        # AdamW: 2 states (momentum, variance) in fp32
        optimizer_memory = params_billions * 1e9 * 4 * 2 / 1e9
    elif optimizer == "sgd":
        optimizer_memory = params_billions * 1e9 * 4 / 1e9
    else:
        optimizer_memory = 0
    
    # Activations (rough estimate)
    # Per layer: batch_size * seq_length * hidden_size * 2 (forward + backward)
    activation_per_layer = batch_size * seq_length * hidden_size * 2 * bytes_per_param
    activation_memory = num_layers * activation_per_layer / 1e9
    
    total = param_memory + gradient_memory + optimizer_memory + activation_memory
    
    return {
        "parameters_gb": param_memory,
        "gradients_gb": gradient_memory,
        "optimizer_states_gb": optimizer_memory,
        "activations_gb": activation_memory,
        "total_gb": total
    }
```

---

## Data Parallelism

### Distributed Data Parallel (DDP)

Standard PyTorch DDP - replicate model, split data:

```python
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup_ddp(rank, world_size):
    """Initialize DDP process group."""
    dist.init_process_group(
        backend="nccl",
        init_method="env://",
        rank=rank,
        world_size=world_size
    )
    torch.cuda.set_device(rank)

def train_ddp(rank, world_size, model, dataloader, epochs):
    """Training loop with DDP."""
    setup_ddp(rank, world_size)
    
    # Wrap model with DDP
    model = model.to(rank)
    model = DDP(model, device_ids=[rank])
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(epochs):
        # Sampler ensures each rank gets different data
        dataloader.sampler.set_epoch(epoch)
        
        for batch in dataloader:
            batch = {k: v.to(rank) for k, v in batch.items()}
            
            outputs = model(**batch)
            loss = outputs.loss
            
            loss.backward()  # Gradients synced automatically
            optimizer.step()
            optimizer.zero_grad()
    
    dist.destroy_process_group()

# Launch with torchrun
# torchrun --nproc_per_node=8 train.py
```

### When to Use DDP
- Model fits on single GPU
- Batch size scaling is primary goal
- Simple setup requirements
- Maximum compute efficiency

---

## Fully Sharded Data Parallel (FSDP)

Shard model parameters, gradients, and optimizer states across GPUs:

```python
import torch
from torch.distributed.fsdp import (
    FullyShardedDataParallel as FSDP,
    MixedPrecision,
    BackwardPrefetch,
    ShardingStrategy,
    CPUOffload,
)
from torch.distributed.fsdp.wrap import (
    transformer_auto_wrap_policy,
    size_based_auto_wrap_policy,
)

def setup_fsdp(model, shard_strategy="full"):
    """Configure FSDP with appropriate settings."""
    
    # Mixed precision policy
    mixed_precision = MixedPrecision(
        param_dtype=torch.bfloat16,
        reduce_dtype=torch.bfloat16,
        buffer_dtype=torch.bfloat16,
    )
    
    # Sharding strategy
    strategies = {
        "full": ShardingStrategy.FULL_SHARD,       # ZeRO-3 equivalent
        "grad_op": ShardingStrategy.SHARD_GRAD_OP, # ZeRO-2 equivalent
        "no_shard": ShardingStrategy.NO_SHARD,     # DDP equivalent
        "hybrid": ShardingStrategy.HYBRID_SHARD,   # Shard within node
    }
    
    # Auto-wrap policy for transformer blocks
    from transformers.models.llama.modeling_llama import LlamaDecoderLayer
    auto_wrap_policy = functools.partial(
        transformer_auto_wrap_policy,
        transformer_layer_cls={LlamaDecoderLayer}
    )
    
    # CPU offloading for extreme memory savings
    cpu_offload = CPUOffload(offload_params=True) if shard_strategy == "full" else None
    
    # Wrap model
    model = FSDP(
        model,
        sharding_strategy=strategies[shard_strategy],
        mixed_precision=mixed_precision,
        auto_wrap_policy=auto_wrap_policy,
        backward_prefetch=BackwardPrefetch.BACKWARD_PRE,
        cpu_offload=cpu_offload,
        device_id=torch.cuda.current_device(),
    )
    
    return model

def train_fsdp(model, dataloader, epochs):
    """FSDP training loop."""
    model = setup_fsdp(model)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(epochs):
        for batch in dataloader:
            batch = {k: v.cuda() for k, v in batch.items()}
            
            outputs = model(**batch)
            loss = outputs.loss
            
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
```

### FSDP Sharding Strategies

| Strategy | Memory Savings | Communication | Use Case |
|----------|---------------|---------------|----------|
| FULL_SHARD | Maximum | High | Large models, limited GPU memory |
| SHARD_GRAD_OP | Medium | Medium | Medium models, faster training |
| HYBRID_SHARD | Medium-High | Optimized | Multi-node, reduce cross-node comm |
| NO_SHARD | None | Low | Small models (like DDP) |

### FSDP Checkpointing

```python
from torch.distributed.checkpoint import (
    save_state_dict,
    load_state_dict,
)
from torch.distributed.fsdp import (
    FullStateDictConfig,
    StateDictType,
)

def save_fsdp_checkpoint(model, optimizer, path):
    """Save FSDP checkpoint with sharded state dict."""
    with FSDP.state_dict_type(
        model,
        StateDictType.SHARDED_STATE_DICT,
    ):
        state_dict = {
            "model": model.state_dict(),
            "optimizer": FSDP.optim_state_dict(model, optimizer),
        }
        save_state_dict(state_dict, path)

def load_fsdp_checkpoint(model, optimizer, path):
    """Load FSDP checkpoint."""
    with FSDP.state_dict_type(
        model,
        StateDictType.SHARDED_STATE_DICT,
    ):
        state_dict = {"model": model.state_dict()}
        load_state_dict(state_dict, path)
        model.load_state_dict(state_dict["model"])
```

---

## DeepSpeed ZeRO

### ZeRO Stages

```
┌─────────────────────────────────────────────────────────────────┐
│                      ZeRO Optimization Stages                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ZeRO-1: Optimizer State Partitioning                           │
│  ├── Partition optimizer states across GPUs                     │
│  ├── ~4x memory reduction for AdamW                             │
│  └── Minimal communication overhead                             │
│                                                                  │
│  ZeRO-2: + Gradient Partitioning                                │
│  ├── Partition gradients after reduce-scatter                   │
│  ├── ~8x memory reduction                                       │
│  └── Slightly more communication                                │
│                                                                  │
│  ZeRO-3: + Parameter Partitioning                               │
│  ├── Partition model parameters                                 │
│  ├── Linear memory scaling with GPUs                            │
│  └── All-gather before forward/backward                         │
│                                                                  │
│  ZeRO-Infinity: + CPU/NVMe Offloading                          │
│  ├── Offload to CPU RAM or NVMe SSD                            │
│  ├── Train trillion-parameter models                            │
│  └── Slower but memory-unlimited                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### DeepSpeed Configuration

```python
# ds_config.json
deepspeed_config = {
    "train_batch_size": 256,
    "train_micro_batch_size_per_gpu": 4,
    "gradient_accumulation_steps": 8,
    
    "bf16": {
        "enabled": True
    },
    
    "zero_optimization": {
        "stage": 3,
        "offload_optimizer": {
            "device": "cpu",
            "pin_memory": True
        },
        "offload_param": {
            "device": "cpu",
            "pin_memory": True
        },
        "overlap_comm": True,
        "contiguous_gradients": True,
        "sub_group_size": 1e9,
        "reduce_bucket_size": "auto",
        "stage3_prefetch_bucket_size": "auto",
        "stage3_param_persistence_threshold": "auto",
        "stage3_max_live_parameters": 1e9,
        "stage3_max_reuse_distance": 1e9,
        "stage3_gather_16bit_weights_on_model_save": True
    },
    
    "gradient_clipping": 1.0,
    
    "optimizer": {
        "type": "AdamW",
        "params": {
            "lr": 1e-4,
            "betas": [0.9, 0.95],
            "eps": 1e-8,
            "weight_decay": 0.1
        }
    },
    
    "scheduler": {
        "type": "WarmupCosineDecay",
        "params": {
            "warmup_num_steps": 1000,
            "total_num_steps": 100000
        }
    },
    
    "activation_checkpointing": {
        "partition_activations": True,
        "cpu_checkpointing": True,
        "contiguous_memory_optimization": True,
        "number_checkpoints": 4
    }
}
```

### DeepSpeed Training

```python
import deepspeed

def train_deepspeed(model_fn, dataloader, config_path):
    """Training with DeepSpeed."""
    
    # Initialize DeepSpeed
    model, optimizer, _, scheduler = deepspeed.initialize(
        model=model_fn(),
        config=config_path,
        model_parameters=model.parameters()
    )
    
    for epoch in range(num_epochs):
        for step, batch in enumerate(dataloader):
            batch = {k: v.to(model.device) for k, v in batch.items()}
            
            # Forward pass
            outputs = model(**batch)
            loss = outputs.loss
            
            # Backward pass (DeepSpeed handles gradient sync)
            model.backward(loss)
            
            # Optimizer step
            model.step()
            
            if step % 100 == 0:
                print(f"Step {step}, Loss: {loss.item()}")
    
    # Save checkpoint
    model.save_checkpoint("checkpoints/", tag=f"epoch_{epoch}")
```

---

## Tensor Parallelism

Split individual layers across GPUs:

```python
import torch
import torch.distributed as dist
from torch.distributed.tensor.parallel import (
    parallelize_module,
    ColwiseParallel,
    RowwiseParallel,
)

def setup_tensor_parallel(model, tp_size=8):
    """
    Apply tensor parallelism to transformer model.
    
    Column-wise: Split output dimension (Q, K, V, MLP up)
    Row-wise: Split input dimension (O projection, MLP down)
    """
    from torch.distributed.device_mesh import init_device_mesh
    
    # Create device mesh for TP
    tp_mesh = init_device_mesh("cuda", (tp_size,))
    
    # Parallelize each transformer layer
    for layer in model.layers:
        # Attention projections
        parallelize_module(
            layer.self_attn.q_proj,
            tp_mesh,
            ColwiseParallel()
        )
        parallelize_module(
            layer.self_attn.k_proj,
            tp_mesh,
            ColwiseParallel()
        )
        parallelize_module(
            layer.self_attn.v_proj,
            tp_mesh,
            ColwiseParallel()
        )
        parallelize_module(
            layer.self_attn.o_proj,
            tp_mesh,
            RowwiseParallel()
        )
        
        # MLP projections
        parallelize_module(
            layer.mlp.gate_proj,
            tp_mesh,
            ColwiseParallel()
        )
        parallelize_module(
            layer.mlp.up_proj,
            tp_mesh,
            ColwiseParallel()
        )
        parallelize_module(
            layer.mlp.down_proj,
            tp_mesh,
            RowwiseParallel()
        )
    
    return model
```

### When to Use Tensor Parallelism
- Single layers too large for one GPU
- High-bandwidth interconnect (NVLink, InfiniBand)
- Combined with PP for very large models
- Typical TP size: 2, 4, or 8 within a node

---

## Pipeline Parallelism

Partition model into stages across GPUs:

```python
from deepspeed.pipe import PipelineModule, LayerSpec

class PipelineTransformer(PipelineModule):
    """Pipeline-parallel transformer model."""
    
    def __init__(self, config, num_stages=4):
        # Define layer specifications
        specs = [
            LayerSpec(EmbeddingLayer, config.vocab_size, config.hidden_size),
        ]
        
        # Distribute transformer layers across stages
        layers_per_stage = config.num_layers // num_stages
        for i in range(config.num_layers):
            specs.append(
                LayerSpec(TransformerBlock, config)
            )
        
        specs.append(
            LayerSpec(OutputLayer, config.hidden_size, config.vocab_size)
        )
        
        super().__init__(
            layers=specs,
            num_stages=num_stages,
            partition_method='uniform',  # or 'parameters' for balanced params
            activation_checkpoint_interval=1
        )

def train_pipeline(model_config, dataloader):
    """Pipeline parallel training with micro-batches."""
    
    model = PipelineTransformer(model_config, num_stages=4)
    
    engine, _, _, _ = deepspeed.initialize(
        model=model,
        config="ds_config_pipeline.json"
    )
    
    for batch in dataloader:
        # DeepSpeed handles micro-batch scheduling
        loss = engine.train_batch(batch)
```

### Pipeline Schedules

```
┌─────────────────────────────────────────────────────────────────┐
│                      Pipeline Schedules                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  GPipe (Synchronous):                                           │
│  ┌─────┬─────┬─────┬─────┐                                      │
│  │ F0  │ F1  │ F2  │ F3  │ B3  │ B2  │ B1  │ B0  │              │
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘              │
│  Stage 0: ████                        ████                      │
│  Stage 1:     ████                ████                          │
│  Stage 2:         ████        ████                              │
│  Stage 3:             ████████                                  │
│                                                                  │
│  1F1B (Interleaved):                                            │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐                    │
│  │ F0  │ F1  │ F2  │ F3  │ B0  │ F4  │ B1  │...                 │
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┘                    │
│  Reduces bubble overhead with better overlap                    │
│                                                                  │
│  Virtual Pipeline (Interleaved Stages):                         │
│  GPU 0: [Stage 0, Stage 4]                                      │
│  GPU 1: [Stage 1, Stage 5]                                      │
│  GPU 2: [Stage 2, Stage 6]                                      │
│  GPU 3: [Stage 3, Stage 7]                                      │
│  Further reduces pipeline bubble                                │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3D Parallelism

Combine DP, TP, and PP for maximum scale:

```python
class Parallelism3D:
    """
    3D Parallelism configuration for large-scale training.
    
    Total GPUs = DP_size × TP_size × PP_size
    """
    
    def __init__(self, dp_size, tp_size, pp_size):
        self.dp_size = dp_size
        self.tp_size = tp_size
        self.pp_size = pp_size
        self.world_size = dp_size * tp_size * pp_size
    
    def get_rank_config(self, global_rank):
        """Get parallelism configuration for a rank."""
        # PP group: ranks handling same pipeline stage
        pp_rank = global_rank // (self.dp_size * self.tp_size)
        
        # TP group: ranks in same TP group
        tp_rank = (global_rank % (self.dp_size * self.tp_size)) // self.dp_size
        
        # DP group: ranks with same model partition
        dp_rank = global_rank % self.dp_size
        
        return {
            "dp_rank": dp_rank,
            "tp_rank": tp_rank,
            "pp_rank": pp_rank
        }
    
    def create_process_groups(self):
        """Create all necessary process groups."""
        # Data parallel groups
        for tp in range(self.tp_size):
            for pp in range(self.pp_size):
                dp_ranks = [
                    pp * self.dp_size * self.tp_size + tp * self.dp_size + dp
                    for dp in range(self.dp_size)
                ]
                dist.new_group(dp_ranks)
        
        # Tensor parallel groups
        for dp in range(self.dp_size):
            for pp in range(self.pp_size):
                tp_ranks = [
                    pp * self.dp_size * self.tp_size + tp * self.dp_size + dp
                    for tp in range(self.tp_size)
                ]
                dist.new_group(tp_ranks)
        
        # Pipeline parallel groups
        for dp in range(self.dp_size):
            for tp in range(self.tp_size):
                pp_ranks = [
                    pp * self.dp_size * self.tp_size + tp * self.dp_size + dp
                    for pp in range(self.pp_size)
                ]
                dist.new_group(pp_ranks)

# Example: 64 GPUs with 3D parallelism
# 8 nodes × 8 GPUs each
config_3d = Parallelism3D(
    dp_size=4,   # 4-way data parallel
    tp_size=4,   # 4-way tensor parallel (within node)
    pp_size=4    # 4-way pipeline parallel (across nodes)
)
```

---

## Optimization Techniques

### Gradient Accumulation

```python
def train_with_accumulation(model, dataloader, accumulation_steps=8):
    """Simulate larger batch size with gradient accumulation."""
    optimizer = torch.optim.AdamW(model.parameters())
    
    for step, batch in enumerate(dataloader):
        outputs = model(**batch)
        loss = outputs.loss / accumulation_steps
        loss.backward()
        
        if (step + 1) % accumulation_steps == 0:
            optimizer.step()
            optimizer.zero_grad()
```

### Activation Checkpointing

```python
from torch.utils.checkpoint import checkpoint

class CheckpointedTransformerBlock(nn.Module):
    """Transformer block with activation checkpointing."""
    
    def __init__(self, config):
        super().__init__()
        self.attention = Attention(config)
        self.mlp = MLP(config)
        self.ln1 = nn.LayerNorm(config.hidden_size)
        self.ln2 = nn.LayerNorm(config.hidden_size)
    
    def forward(self, x, use_checkpoint=True):
        if use_checkpoint and self.training:
            # Recompute activations during backward
            attn_out = checkpoint(
                self._attention_forward, 
                x, 
                use_reentrant=False
            )
            mlp_out = checkpoint(
                self._mlp_forward, 
                attn_out, 
                use_reentrant=False
            )
        else:
            attn_out = self._attention_forward(x)
            mlp_out = self._mlp_forward(attn_out)
        
        return mlp_out
    
    def _attention_forward(self, x):
        return x + self.attention(self.ln1(x))
    
    def _mlp_forward(self, x):
        return x + self.mlp(self.ln2(x))
```

### Mixed Precision Training

```python
from torch.cuda.amp import autocast, GradScaler

def train_mixed_precision(model, dataloader):
    """Training with automatic mixed precision."""
    scaler = GradScaler()
    optimizer = torch.optim.AdamW(model.parameters())
    
    for batch in dataloader:
        optimizer.zero_grad()
        
        # Forward pass in mixed precision
        with autocast(dtype=torch.bfloat16):
            outputs = model(**batch)
            loss = outputs.loss
        
        # Backward pass with gradient scaling
        scaler.scale(loss).backward()
        scaler.step(optimizer)
        scaler.update()
```

---

## Strategy Selection Guide

```
┌─────────────────────────────────────────────────────────────────┐
│           Distributed Training Strategy Decision Tree            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Does model fit on single GPU?                                  │
│  ├── YES → Use DDP (simplest, most efficient)                  │
│  └── NO ↓                                                       │
│                                                                  │
│  Does model fit with activation checkpointing?                  │
│  ├── YES → DDP + Activation Checkpointing                      │
│  └── NO ↓                                                       │
│                                                                  │
│  Can model fit with ZeRO-2/FSDP SHARD_GRAD_OP?                 │
│  ├── YES → Use ZeRO-2 or FSDP SHARD_GRAD_OP                   │
│  └── NO ↓                                                       │
│                                                                  │
│  Can model fit with ZeRO-3/FSDP FULL_SHARD?                    │
│  ├── YES → Use ZeRO-3 or FSDP FULL_SHARD                      │
│  └── NO ↓                                                       │
│                                                                  │
│  Need CPU offloading?                                           │
│  ├── YES → ZeRO-Infinity or FSDP + CPU Offload                │
│  └── NO ↓                                                       │
│                                                                  │
│  Single layer too large?                                        │
│  ├── YES → Tensor Parallelism (TP)                             │
│  └── NO → Pipeline Parallelism (PP)                            │
│                                                                  │
│  Very large model (100B+)?                                      │
│  └── YES → 3D Parallelism (DP + TP + PP)                       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Neo4j Integration

### Schema
```cypher
// Training run tracking
CREATE CONSTRAINT training_run_id IF NOT EXISTS
FOR (t:TrainingRun) REQUIRE t.id IS UNIQUE;

(:TrainingRun {
    id: String,
    model_name: String,
    parallelism_strategy: String,  // "ddp", "fsdp", "deepspeed", "3d"
    dp_size: Integer,
    tp_size: Integer,
    pp_size: Integer,
    total_gpus: Integer,
    batch_size: Integer,
    precision: String,
    throughput_tokens_per_sec: Float,
    gpu_memory_used_gb: Float,
    training_time_hours: Float,
    final_loss: Float,
    timestamp: DateTime
})

(:ClusterConfig {
    name: String,
    num_nodes: Integer,
    gpus_per_node: Integer,
    gpu_type: String,
    interconnect: String,  // "nvlink", "infiniband", "ethernet"
    memory_per_gpu_gb: Integer
})

(:ParallelismConfig {
    strategy: String,
    dp_size: Integer,
    tp_size: Integer,
    pp_size: Integer,
    zero_stage: Integer,
    activation_checkpointing: Boolean,
    cpu_offload: Boolean
})

// Relationships
(:TrainingRun)-[:USES_CLUSTER]->(:ClusterConfig)
(:TrainingRun)-[:USES_PARALLELISM]->(:ParallelismConfig)
(:TrainingRun)-[:TRAINS]->(:Model)
```

### Query Examples
```cypher
// Find optimal parallelism for model size
MATCH (t:TrainingRun)-[:TRAINS]->(m:Model)
WHERE m.parameters > 70e9 AND t.throughput_tokens_per_sec > 10000
RETURN t.parallelism_strategy, t.dp_size, t.tp_size, t.pp_size,
       AVG(t.throughput_tokens_per_sec) as avg_throughput
ORDER BY avg_throughput DESC;

// Compare FSDP vs DeepSpeed for same model
MATCH (t:TrainingRun)-[:TRAINS]->(m:Model {name: "OMEGA-ASI-v500"})
RETURN t.parallelism_strategy, 
       AVG(t.throughput_tokens_per_sec) as throughput,
       AVG(t.gpu_memory_used_gb) as memory
GROUP BY t.parallelism_strategy;
```

---

## Integration with Other Skills

### experiment-tracker
- Log distributed training configurations
- Track throughput and efficiency metrics
- Compare parallelism strategies

### neural-architecture-search
- Search for architectures optimized for distributed training
- Consider communication patterns in architecture design
- Hardware-aware NAS for specific clusters

### benchmark-creator
- Create scaling efficiency benchmarks
- Measure strong/weak scaling
- Communication overhead analysis

### safety-alignment-researcher
- Verify model behavior consistent across parallelism strategies
- Checkpoint safety for resumable training
- Gradient synchronization correctness

---

## Best Practices

1. **Start Simple**: Begin with DDP, add complexity only when needed
2. **Profile First**: Measure memory and compute before choosing strategy
3. **Match Hardware**: TP within node (NVLink), PP across nodes
4. **Checkpoint Frequently**: Distributed training is prone to failures
5. **Monitor Memory**: Use `torch.cuda.memory_summary()` for debugging
6. **Gradient Clipping**: Essential for stability with large batch sizes
7. **Learning Rate Scaling**: Scale LR with effective batch size
8. **Warmup**: Longer warmup for larger batch sizes

---

## References

1. Xu, J., et al. (2025). "Comprehensive Survey on Distributed Deep Learning Training"
2. Rajbhandari, S., et al. (2020). "ZeRO: Memory Optimizations Toward Training Trillion Parameter Models"
3. Zhao, Y., et al. (2023). "PyTorch FSDP: Experiences on Scaling Fully Sharded Data Parallel"
4. Narayanan, D., et al. (2021). "Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM"
5. Shoeybi, M., et al. (2019). "Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism"
6. Hegde, S. (2024). "Everything about Distributed Training and Efficient Finetuning"

---
name: long-context-processing
description: Techniques for extending and efficiently processing long context windows in LLMs
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, long-context, rope, attention, context-extension, memory]
---

# Long Context Processing

## Overview

Long context processing enables AGI/ASI systems to handle extensive inputs spanning millions of tokens. This skill covers positional encoding extensions (RoPE scaling, YaRN), efficient attention mechanisms (Ring Attention, sparse attention), memory architectures, and retrieval-augmented approaches for OMEGA ASI context handling.

## Core Concepts

### Context Length Evolution

```
┌─────────────────────────────────────────────────────────────────┐
│              Context Length Evolution (2017-2025)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  2017: Original Transformer      512 tokens                    │
│  2020: GPT-3                     2,048 tokens                   │
│  2022: GPT-3.5                   4,096 tokens                   │
│  2023: Claude 2                  100,000 tokens                 │
│  2023: GPT-4 Turbo               128,000 tokens                 │
│  2024: Gemini 1.5 Pro            1,000,000 tokens               │
│  2024: Claude 3                  200,000 tokens                 │
│  2025: Gemini 2.0                2,000,000 tokens               │
│  2025: LongRoPE2                 2,048,000 tokens               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Challenges of Long Context

| Challenge | Description | Impact |
|-----------|-------------|--------|
| **Quadratic Attention** | O(n²) memory and compute | Limits batch size |
| **Positional Encoding** | OOD positions at inference | Degraded performance |
| **Attention Dilution** | Attention spread too thin | Lost in the middle |
| **Memory Bandwidth** | KV cache transfer bottleneck | Slow generation |
| **Training Data** | Scarcity of long documents | Poor long-range learning |

---

## Positional Encoding Extensions

### Rotary Position Embedding (RoPE)

Base positional encoding used by most modern LLMs:

```python
import torch
import torch.nn as nn
import math

class RotaryPositionEmbedding:
    """
    Rotary Position Embedding (RoPE).
    Encodes position through rotation in complex plane.
    """
    
    def __init__(self, dim: int, base: int = 10000, max_seq_len: int = 8192):
        self.dim = dim
        self.base = base
        self.max_seq_len = max_seq_len
        
        # Compute rotation frequencies
        inv_freq = 1.0 / (base ** (torch.arange(0, dim, 2).float() / dim))
        self.register_buffer("inv_freq", inv_freq)
        
        # Precompute sin/cos for efficiency
        self._build_cache(max_seq_len)
    
    def _build_cache(self, seq_len: int):
        """Precompute sin/cos cache."""
        t = torch.arange(seq_len, dtype=self.inv_freq.dtype)
        freqs = torch.einsum("i,j->ij", t, self.inv_freq)
        
        # [seq_len, dim/2] -> [seq_len, dim]
        emb = torch.cat((freqs, freqs), dim=-1)
        
        self.cos_cache = emb.cos()
        self.sin_cache = emb.sin()
    
    def apply_rotary(self, x: torch.Tensor, positions: torch.Tensor) -> torch.Tensor:
        """
        Apply rotary embedding to input tensor.
        
        Args:
            x: Input tensor [batch, seq, heads, dim]
            positions: Position indices [batch, seq]
        """
        cos = self.cos_cache[positions]  # [batch, seq, dim]
        sin = self.sin_cache[positions]
        
        # Rotate pairs of dimensions
        x1, x2 = x[..., ::2], x[..., 1::2]
        rotated = torch.cat([
            x1 * cos[..., ::2] - x2 * sin[..., ::2],
            x1 * sin[..., 1::2] + x2 * cos[..., 1::2]
        ], dim=-1)
        
        return rotated
```

### Position Interpolation (PI)

Linear interpolation for context extension:

```python
class PositionInterpolation:
    """
    Position Interpolation for RoPE extension.
    Linearly interpolates positions to fit training range.
    """
    
    def __init__(self, original_max_len: int, target_max_len: int):
        self.original_max_len = original_max_len
        self.target_max_len = target_max_len
        self.scale = original_max_len / target_max_len
    
    def interpolate_positions(self, positions: torch.Tensor) -> torch.Tensor:
        """
        Scale positions to fit original training range.
        
        position' = position * (original_max / target_max)
        """
        return positions * self.scale
    
    def apply_to_rope(self, rope: RotaryPositionEmbedding):
        """Modify RoPE to use interpolated positions."""
        # Scale inverse frequencies
        rope.inv_freq = rope.inv_freq * self.scale
        rope._build_cache(self.target_max_len)
        return rope
```

### NTK-Aware Scaling

Better interpolation through base frequency adjustment:

```python
class NTKAwareScaling:
    """
    NTK-Aware RoPE Scaling.
    Adjusts base frequency instead of position interpolation.
    """
    
    def __init__(self, dim: int, original_base: int = 10000, scale: float = 1.0):
        self.dim = dim
        self.original_base = original_base
        self.scale = scale
    
    def compute_scaled_base(self) -> float:
        """
        Compute NTK-scaled base.
        
        base' = base * scale^(dim/(dim-2))
        """
        exponent = self.dim / (self.dim - 2)
        return self.original_base * (self.scale ** exponent)
    
    def get_scaled_inv_freq(self) -> torch.Tensor:
        """Get inverse frequencies with scaled base."""
        scaled_base = self.compute_scaled_base()
        return 1.0 / (scaled_base ** (torch.arange(0, self.dim, 2).float() / self.dim))


class DynamicNTKScaling:
    """
    Dynamic NTK Scaling.
    Adjusts scale based on current sequence length.
    """
    
    def __init__(self, dim: int, base: int = 10000, original_max_len: int = 4096):
        self.dim = dim
        self.base = base
        self.original_max_len = original_max_len
    
    def get_inv_freq(self, seq_len: int) -> torch.Tensor:
        """Dynamically compute inv_freq based on sequence length."""
        if seq_len <= self.original_max_len:
            # No scaling needed
            scale = 1.0
        else:
            # Scale based on extension ratio
            scale = seq_len / self.original_max_len
        
        # NTK-aware base scaling
        scaled_base = self.base * (scale ** (self.dim / (self.dim - 2)))
        
        return 1.0 / (scaled_base ** (torch.arange(0, self.dim, 2).float() / self.dim))
```

### YaRN (Yet another RoPE extensioN)

State-of-the-art RoPE extension combining multiple techniques:

```python
class YaRN:
    """
    YaRN: Yet another RoPE extensioN method.
    Combines NTK interpolation with attention scaling.
    """
    
    def __init__(
        self,
        dim: int,
        base: int = 10000,
        original_max_len: int = 4096,
        target_max_len: int = 32768,
        beta_fast: float = 32,
        beta_slow: float = 1,
        extrapolation_factor: float = 1.0
    ):
        self.dim = dim
        self.base = base
        self.original_max_len = original_max_len
        self.target_max_len = target_max_len
        self.scale = target_max_len / original_max_len
        
        self.beta_fast = beta_fast
        self.beta_slow = beta_slow
        self.extrapolation_factor = extrapolation_factor
        
        # Compute dimension-wise interpolation factors
        self.ramp_func = self._compute_ramp()
    
    def _compute_ramp(self) -> torch.Tensor:
        """
        Compute per-dimension interpolation ramp.
        Low dimensions: full interpolation
        High dimensions: no interpolation (extrapolation)
        """
        pos_freqs = self.base ** (torch.arange(0, self.dim, 2).float() / self.dim)
        
        # Wavelength for each dimension
        wavelengths = 2 * math.pi * pos_freqs
        
        # Determine if dimension should interpolate or extrapolate
        low = max(0, math.floor(
            self.dim * math.log(self.original_max_len / (self.beta_fast * 2 * math.pi)) 
            / (2 * math.log(self.base))
        ))
        high = min(self.dim // 2, math.ceil(
            self.dim * math.log(self.original_max_len / (self.beta_slow * 2 * math.pi))
            / (2 * math.log(self.base))
        ))
        
        # Linear ramp between low and high dimensions
        ramp = torch.zeros(self.dim // 2)
        for i in range(self.dim // 2):
            if i < low:
                ramp[i] = self.extrapolation_factor
            elif i > high:
                ramp[i] = 1.0  # Full interpolation
            else:
                # Linear interpolation between
                ramp[i] = (i - low) / (high - low)
        
        return ramp
    
    def get_inv_freq(self) -> torch.Tensor:
        """Compute YaRN-scaled inverse frequencies."""
        # Base inverse frequencies
        inv_freq = 1.0 / (self.base ** (torch.arange(0, self.dim, 2).float() / self.dim))
        
        # Apply per-dimension scaling
        inv_freq = inv_freq / (
            self.ramp_func * (self.scale - 1) + 1
        )
        
        return inv_freq
    
    def get_attention_scale(self) -> float:
        """
        Compute attention scaling factor.
        Counteracts attention score increase from longer sequences.
        """
        # YaRN uses sqrt(1/t) * 0.1 * ln(s) + 1 where s is scale
        return 0.1 * math.log(self.scale) + 1.0
```

### LongRoPE

Progressive extension to 2M+ tokens:

```python
class LongRoPE:
    """
    LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens.
    Uses progressive extension and non-uniform interpolation.
    """
    
    def __init__(
        self,
        dim: int,
        original_max_len: int = 4096,
        target_max_len: int = 2048000,  # 2M tokens
        base: int = 10000
    ):
        self.dim = dim
        self.original_max_len = original_max_len
        self.target_max_len = target_max_len
        self.base = base
        
        # Search for optimal rescale factors
        self.rescale_factors = self._search_rescale_factors()
    
    def _search_rescale_factors(self) -> torch.Tensor:
        """
        Search for non-uniform rescale factors per dimension.
        Uses evolutionary search guided by perplexity.
        """
        # Initialize with uniform scaling
        scale = self.target_max_len / self.original_max_len
        factors = torch.ones(self.dim // 2) * scale
        
        # LongRoPE identifies two non-uniformities:
        # 1. First few dimensions need different scaling
        # 2. Higher dimensions more sensitive to changes
        
        # Apply learned non-uniform scaling
        # These values are typically found via search
        factors[:2] = factors[:2] * 0.5   # Lower scaling for first dims
        factors[-4:] = factors[-4:] * 1.5  # Higher scaling for last dims
        
        return factors
    
    def get_inv_freq(self) -> torch.Tensor:
        """Get non-uniformly scaled inverse frequencies."""
        inv_freq = 1.0 / (self.base ** (torch.arange(0, self.dim, 2).float() / self.dim))
        return inv_freq / self.rescale_factors
    
    def progressive_extension(self, model, stages: list = [256000, 2048000]):
        """
        Progressive extension strategy.
        
        Stage 1: Extend to 256k with fine-tuning
        Stage 2: Extend to 2M with second interpolation
        """
        current_len = self.original_max_len
        
        for target_len in stages:
            print(f"Extending from {current_len} to {target_len}")
            
            # Compute rescale factors for this stage
            stage_scale = target_len / current_len
            stage_factors = self._search_rescale_factors_for_stage(stage_scale)
            
            # Update model's RoPE
            self._update_model_rope(model, stage_factors)
            
            # Fine-tune if not final stage
            if target_len != stages[-1]:
                self._finetune_stage(model, target_len)
            
            current_len = target_len
        
        return model
```

---

## Efficient Attention Mechanisms

### Ring Attention

Distribute sequence across devices with ring communication:

```python
class RingAttention:
    """
    Ring Attention for distributed long sequences.
    Splits sequence across devices, computes attention in ring pattern.
    """
    
    def __init__(self, num_devices: int, hidden_dim: int, num_heads: int):
        self.num_devices = num_devices
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
    
    def forward(self, q: torch.Tensor, k: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        """
        Compute attention with ring communication.
        
        Each device holds a block of the sequence.
        KV blocks are passed around the ring.
        
        Args:
            q: Query tensor [block_size, num_heads, head_dim]
            k: Key tensor [block_size, num_heads, head_dim]
            v: Value tensor [block_size, num_heads, head_dim]
        """
        block_size = q.shape[0]
        device_id = self.get_device_id()
        
        # Initialize accumulators
        out = torch.zeros_like(q)
        max_score = torch.full((block_size, self.num_heads), float('-inf'))
        sum_exp = torch.zeros(block_size, self.num_heads)
        
        # Current KV block
        k_block, v_block = k, v
        
        # Ring communication
        for step in range(self.num_devices):
            # Compute attention for current KV block
            scores = torch.einsum('qhd,khd->qkh', q, k_block) / math.sqrt(self.hidden_dim // self.num_heads)
            
            # Online softmax update
            new_max = torch.maximum(max_score, scores.max(dim=1).values)
            
            # Rescale previous accumulator
            scale = torch.exp(max_score - new_max)
            out = out * scale.unsqueeze(-1)
            sum_exp = sum_exp * scale
            
            # Add current block contribution
            exp_scores = torch.exp(scores - new_max.unsqueeze(1))
            out = out + torch.einsum('qkh,khd->qhd', exp_scores, v_block)
            sum_exp = sum_exp + exp_scores.sum(dim=1)
            
            max_score = new_max
            
            # Send KV to next device, receive from previous
            k_block = self.ring_send_recv(k_block)
            v_block = self.ring_send_recv(v_block)
        
        # Final normalization
        out = out / sum_exp.unsqueeze(-1)
        
        return out
    
    def ring_send_recv(self, tensor: torch.Tensor) -> torch.Tensor:
        """Send tensor to next device, receive from previous."""
        import torch.distributed as dist
        
        device_id = self.get_device_id()
        next_device = (device_id + 1) % self.num_devices
        prev_device = (device_id - 1) % self.num_devices
        
        recv_buffer = torch.empty_like(tensor)
        
        # Async send and receive
        send_op = dist.isend(tensor, dst=next_device)
        recv_op = dist.irecv(recv_buffer, src=prev_device)
        
        send_op.wait()
        recv_op.wait()
        
        return recv_buffer
```

### Sparse Attention Patterns

```python
class SparseAttention:
    """
    Sparse attention patterns for long sequences.
    Reduces O(n²) to O(n√n) or O(n log n).
    """
    
    @staticmethod
    def sliding_window(seq_len: int, window_size: int) -> torch.Tensor:
        """
        Sliding window attention pattern.
        Each token attends to window_size neighbors.
        """
        mask = torch.zeros(seq_len, seq_len, dtype=torch.bool)
        
        for i in range(seq_len):
            start = max(0, i - window_size // 2)
            end = min(seq_len, i + window_size // 2 + 1)
            mask[i, start:end] = True
        
        return mask
    
    @staticmethod
    def global_sliding(
        seq_len: int, 
        window_size: int, 
        global_tokens: int
    ) -> torch.Tensor:
        """
        Sliding window + global tokens.
        First global_tokens can attend to all.
        """
        # Start with sliding window
        mask = SparseAttention.sliding_window(seq_len, window_size)
        
        # Add global attention
        mask[:global_tokens, :] = True  # Global tokens attend to all
        mask[:, :global_tokens] = True  # All attend to global tokens
        
        return mask
    
    @staticmethod
    def dilated_sliding(
        seq_len: int,
        window_size: int,
        dilation_rates: list = [1, 2, 4]
    ) -> torch.Tensor:
        """
        Dilated sliding window with multiple rates.
        Different attention heads use different dilation.
        """
        masks = []
        
        for dilation in dilation_rates:
            mask = torch.zeros(seq_len, seq_len, dtype=torch.bool)
            
            for i in range(seq_len):
                for j in range(seq_len):
                    distance = abs(i - j)
                    if distance <= (window_size // 2) * dilation and distance % dilation == 0:
                        mask[i, j] = True
            
            masks.append(mask)
        
        return masks
    
    @staticmethod
    def blockwise_sparse(
        seq_len: int,
        block_size: int,
        num_random_blocks: int = 2
    ) -> torch.Tensor:
        """
        Block sparse attention (BigBird style).
        Local blocks + random blocks + global tokens.
        """
        num_blocks = seq_len // block_size
        mask = torch.zeros(seq_len, seq_len, dtype=torch.bool)
        
        for i in range(num_blocks):
            block_start = i * block_size
            block_end = (i + 1) * block_size
            
            # Local attention within block
            mask[block_start:block_end, block_start:block_end] = True
            
            # Random blocks
            random_blocks = torch.randperm(num_blocks)[:num_random_blocks]
            for rb in random_blocks:
                rb_start = rb * block_size
                rb_end = (rb + 1) * block_size
                mask[block_start:block_end, rb_start:rb_end] = True
        
        return mask
```

### Flash Attention for Long Sequences

```python
class FlashAttentionLong:
    """
    Flash Attention optimized for long sequences.
    Uses tiling to reduce memory bandwidth requirements.
    """
    
    def __init__(self, block_size: int = 1024):
        self.block_size = block_size
    
    def forward(
        self,
        q: torch.Tensor,  # [batch, seq, heads, dim]
        k: torch.Tensor,
        v: torch.Tensor,
        causal: bool = True
    ) -> torch.Tensor:
        """
        Memory-efficient attention via tiling.
        
        Uses online softmax to avoid materializing full attention matrix.
        """
        batch, seq_len, num_heads, head_dim = q.shape
        
        # Output and statistics
        out = torch.zeros_like(q)
        lse = torch.zeros(batch, num_heads, seq_len)  # Log-sum-exp
        
        # Tile over sequence
        for i in range(0, seq_len, self.block_size):
            q_block = q[:, i:i+self.block_size]
            
            block_out = torch.zeros_like(q_block)
            block_max = torch.full((batch, num_heads, self.block_size), float('-inf'))
            block_sum = torch.zeros(batch, num_heads, self.block_size)
            
            for j in range(0, seq_len, self.block_size):
                if causal and j > i:
                    continue
                    
                k_block = k[:, j:j+self.block_size]
                v_block = v[:, j:j+self.block_size]
                
                # Compute attention scores
                scores = torch.einsum('bqhd,bkhd->bhqk', q_block, k_block)
                scores = scores / math.sqrt(head_dim)
                
                # Apply causal mask
                if causal and i == j:
                    causal_mask = torch.triu(
                        torch.ones(self.block_size, self.block_size),
                        diagonal=1
                    ).bool()
                    scores.masked_fill_(causal_mask, float('-inf'))
                
                # Online softmax update
                new_max = torch.maximum(block_max, scores.max(dim=-1).values)
                
                scale = torch.exp(block_max - new_max)
                block_out = block_out * scale.unsqueeze(-1)
                block_sum = block_sum * scale
                
                exp_scores = torch.exp(scores - new_max.unsqueeze(-1))
                block_out = block_out + torch.einsum('bhqk,bkhd->bqhd', exp_scores, v_block)
                block_sum = block_sum + exp_scores.sum(dim=-1)
                
                block_max = new_max
            
            # Normalize and store
            out[:, i:i+self.block_size] = block_out / block_sum.unsqueeze(-1)
            lse[:, :, i:i+self.block_size] = block_max + torch.log(block_sum)
        
        return out
```

---

## Memory Architectures

### KV Cache Optimization

```python
class PagedKVCache:
    """
    Paged Attention KV Cache (vLLM style).
    Manages KV cache as pages for efficient memory utilization.
    """
    
    def __init__(
        self,
        num_layers: int,
        num_heads: int,
        head_dim: int,
        page_size: int = 16,
        max_pages: int = 1000
    ):
        self.num_layers = num_layers
        self.num_heads = num_heads
        self.head_dim = head_dim
        self.page_size = page_size
        self.max_pages = max_pages
        
        # Page pool
        self.k_pages = torch.zeros(max_pages, num_layers, page_size, num_heads, head_dim)
        self.v_pages = torch.zeros(max_pages, num_layers, page_size, num_heads, head_dim)
        
        # Page allocation
        self.free_pages = list(range(max_pages))
        self.sequence_pages = {}  # seq_id -> list of page indices
    
    def allocate_pages(self, seq_id: int, num_tokens: int) -> list:
        """Allocate pages for a sequence."""
        num_pages = math.ceil(num_tokens / self.page_size)
        
        if len(self.free_pages) < num_pages:
            raise RuntimeError("Out of KV cache pages")
        
        allocated = [self.free_pages.pop() for _ in range(num_pages)]
        self.sequence_pages[seq_id] = allocated
        
        return allocated
    
    def free_sequence(self, seq_id: int):
        """Free pages for a completed sequence."""
        if seq_id in self.sequence_pages:
            self.free_pages.extend(self.sequence_pages[seq_id])
            del self.sequence_pages[seq_id]
    
    def get_kv(self, seq_id: int, layer: int) -> tuple:
        """Get KV cache for a sequence at a layer."""
        pages = self.sequence_pages[seq_id]
        
        k_cache = torch.cat([self.k_pages[p, layer] for p in pages], dim=0)
        v_cache = torch.cat([self.v_pages[p, layer] for p in pages], dim=0)
        
        return k_cache, v_cache
    
    def append_kv(self, seq_id: int, layer: int, k: torch.Tensor, v: torch.Tensor):
        """Append new KV to cache."""
        pages = self.sequence_pages[seq_id]
        current_page = pages[-1]
        
        # Find position in current page
        total_tokens = len(pages) * self.page_size
        # Simplified: append to last page
        # Real implementation handles page boundaries
        
        pos = total_tokens % self.page_size
        self.k_pages[current_page, layer, pos] = k
        self.v_pages[current_page, layer, pos] = v


class StreamingKVCache:
    """
    Streaming KV Cache with sliding window.
    Discards old KV pairs to maintain fixed memory.
    """
    
    def __init__(
        self,
        num_layers: int,
        num_heads: int,
        head_dim: int,
        window_size: int,
        sink_size: int = 4  # Keep first N tokens always
    ):
        self.window_size = window_size
        self.sink_size = sink_size
        
        # Fixed size cache: sink + window
        cache_size = sink_size + window_size
        self.k_cache = torch.zeros(num_layers, cache_size, num_heads, head_dim)
        self.v_cache = torch.zeros(num_layers, cache_size, num_heads, head_dim)
        
        self.current_pos = 0
    
    def append(self, layer: int, k: torch.Tensor, v: torch.Tensor):
        """Append new KV, maintaining sliding window."""
        if self.current_pos < self.sink_size + self.window_size:
            # Cache not full yet
            self.k_cache[layer, self.current_pos] = k
            self.v_cache[layer, self.current_pos] = v
        else:
            # Shift window, keep sink
            self.k_cache[layer, self.sink_size:-1] = self.k_cache[layer, self.sink_size+1:]
            self.v_cache[layer, self.sink_size:-1] = self.v_cache[layer, self.sink_size+1:]
            
            self.k_cache[layer, -1] = k
            self.v_cache[layer, -1] = v
        
        self.current_pos += 1
```

### Hierarchical Memory

```python
class HierarchicalMemory:
    """
    Hierarchical memory for very long contexts.
    Combines fast cache, compressed memory, and external storage.
    """
    
    def __init__(
        self,
        l1_size: int = 8192,      # Recent context (full precision)
        l2_size: int = 65536,     # Compressed summaries
        l3_size: int = 1000000    # External retrieval
    ):
        self.l1_cache = []  # Recent tokens
        self.l2_memory = []  # Compressed chunks
        self.l3_index = None  # Vector index for retrieval
        
        self.l1_size = l1_size
        self.l2_size = l2_size
        self.l3_size = l3_size
        
        self.compressor = self._init_compressor()
    
    def _init_compressor(self):
        """Initialize memory compressor."""
        # Could be a learned compression model
        return MemoryCompressor(compression_ratio=8)
    
    def add_context(self, tokens: torch.Tensor, embeddings: torch.Tensor):
        """Add new context to memory hierarchy."""
        # Add to L1 cache
        self.l1_cache.append({
            'tokens': tokens,
            'embeddings': embeddings
        })
        
        # Check if L1 overflow
        if len(self.l1_cache) > self.l1_size:
            # Compress and move to L2
            oldest = self.l1_cache.pop(0)
            compressed = self.compressor.compress(oldest)
            self.l2_memory.append(compressed)
        
        # Check if L2 overflow
        if len(self.l2_memory) > self.l2_size:
            # Move to L3 (vector store)
            oldest = self.l2_memory.pop(0)
            self._add_to_l3(oldest)
    
    def retrieve(self, query: torch.Tensor, k: int = 10) -> list:
        """
        Retrieve relevant context from all memory levels.
        
        Returns combined context from L1 (exact), L2 (compressed), L3 (retrieved).
        """
        results = []
        
        # L1: Return all recent context
        results.extend(self.l1_cache)
        
        # L2: Score and return top compressed chunks
        if self.l2_memory:
            l2_scores = [
                self._score_chunk(query, chunk) 
                for chunk in self.l2_memory
            ]
            top_l2 = sorted(
                zip(self.l2_memory, l2_scores),
                key=lambda x: x[1],
                reverse=True
            )[:k]
            results.extend([chunk for chunk, _ in top_l2])
        
        # L3: Vector retrieval
        if self.l3_index is not None:
            l3_results = self.l3_index.search(query, k=k)
            results.extend(l3_results)
        
        return results
```

---

## Retrieval-Augmented Long Context

### RAG for Context Extension

```python
class RetrievalAugmentedContext:
    """
    Use retrieval to extend effective context beyond model limits.
    """
    
    def __init__(
        self,
        model,
        retriever,
        context_window: int = 8192,
        retrieval_chunks: int = 5
    ):
        self.model = model
        self.retriever = retriever
        self.context_window = context_window
        self.retrieval_chunks = retrieval_chunks
    
    def process_long_document(self, document: str, query: str) -> str:
        """Process document longer than context window."""
        # Chunk document
        chunks = self.chunk_document(document, chunk_size=1000)
        
        # Index chunks
        self.retriever.index(chunks)
        
        # Retrieve relevant chunks
        relevant_chunks = self.retriever.retrieve(query, k=self.retrieval_chunks)
        
        # Construct context
        context = "\n\n".join([
            f"[Chunk {i+1}]\n{chunk}" 
            for i, chunk in enumerate(relevant_chunks)
        ])
        
        # Generate response
        prompt = f"""Based on the following excerpts from a document, answer the question.

{context}

Question: {query}

Answer:"""
        
        return self.model.generate(prompt)
    
    def iterative_retrieval(self, document: str, query: str, iterations: int = 3) -> str:
        """
        Iterative retrieval for complex queries.
        Each iteration refines the query based on previous results.
        """
        chunks = self.chunk_document(document, chunk_size=1000)
        self.retriever.index(chunks)
        
        current_query = query
        all_retrieved = []
        
        for i in range(iterations):
            # Retrieve with current query
            relevant = self.retriever.retrieve(current_query, k=self.retrieval_chunks)
            all_retrieved.extend(relevant)
            
            # Generate refined query
            context = "\n".join(relevant)
            refined = self.model.generate(f"""
Based on these excerpts:
{context}

Original question: {query}

What additional information would help answer this question? 
Generate a refined search query:""")
            
            current_query = refined
        
        # Final answer with all retrieved context
        all_context = "\n\n".join(list(set(all_retrieved))[:10])
        return self.model.generate(f"""
{all_context}

Question: {query}
Answer:""")
```

---

## Neo4j Integration

### Schema
```cypher
// Long context experiments
CREATE CONSTRAINT long_context_exp_id IF NOT EXISTS
FOR (e:LongContextExperiment) REQUIRE e.id IS UNIQUE;

(:LongContextExperiment {
    id: String,
    model_name: String,
    extension_method: String,  // "yarn", "longrope", "pi"
    original_length: Integer,
    target_length: Integer,
    achieved_length: Integer,
    perplexity_short: Float,
    perplexity_long: Float,
    needle_accuracy: Float,
    timestamp: DateTime
})

(:PositionalEncoding {
    type: String,           // "rope", "alibi", "absolute"
    base: Integer,
    scaling_method: String,
    scaling_factor: Float
})

(:AttentionPattern {
    type: String,           // "full", "sparse", "ring"
    sparsity_ratio: Float,
    memory_reduction: Float
})

// Relationships
(:LongContextExperiment)-[:USES_ENCODING]->(:PositionalEncoding)
(:LongContextExperiment)-[:USES_ATTENTION]->(:AttentionPattern)
(:LongContextExperiment)-[:EVALUATES]->(:Model)
```

### Query Examples
```cypher
// Find best context extension method
MATCH (e:LongContextExperiment)
WHERE e.target_length >= 1000000
RETURN e.extension_method, 
       AVG(e.needle_accuracy) as avg_needle,
       AVG(e.perplexity_long / e.perplexity_short) as ppl_ratio
ORDER BY avg_needle DESC;

// Track context length progression
MATCH (e:LongContextExperiment)-[:EVALUATES]->(m:Model {name: "OMEGA-ASI"})
RETURN e.target_length, e.needle_accuracy, e.extension_method, e.timestamp
ORDER BY e.timestamp;
```

---

## Integration with Other Skills

### distributed-training
- Ring attention requires distributed infrastructure
- Coordinate sequence sharding across nodes
- Gradient synchronization for long sequences

### neural-architecture-search
- Search for optimal attention patterns
- Architecture for efficient long context
- Memory-compute tradeoffs

### mechanistic-interpretability
- Analyze attention patterns in long context
- Understand positional encoding behavior
- Feature propagation over long distances

### evaluation-framework
- Needle-in-haystack benchmarks
- Long-range dependency tests
- Perplexity at various context lengths

---

## Best Practices

1. **Progressive Extension**: Extend in stages, not all at once
2. **Short Context Preservation**: Verify performance on short tasks
3. **Needle Testing**: Always test with needle-in-haystack
4. **Memory Monitoring**: Track VRAM usage carefully
5. **Batch Size Adjustment**: Reduce batch for longer contexts
6. **Attention Scaling**: Apply attention temperature correction
7. **Hybrid Approaches**: Combine extension with retrieval

---

## References

1. Ding, Y., et al. (2024). "LongRoPE: Extending LLM Context Window Beyond 2 Million Tokens" (ICML 2024)
2. Shang, N., et al. (2025). "LongRoPE2: Near-Lossless LLM Context Window Scaling"
3. Peng, B., et al. (2023). "YaRN: Efficient Context Window Extension of Large Language Models"
4. Liu, H., et al. (2023). "Ring Attention with Blockwise Transformers for Near-Infinite Context"
5. Chen, S., et al. (2023). "Extending Context Window of Large Language Models via Positional Interpolation"
6. Arora, A. (2025). "How LLMs Scaled from 512 to 2M Context: A Technical Deep Dive"

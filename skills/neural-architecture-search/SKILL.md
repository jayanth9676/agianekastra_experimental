---
name: neural-architecture-search
description: Automate the design and optimization of neural network architectures using NAS techniques. Covers search spaces, search strategies (RL, evolutionary, gradient-based), and efficiency-aware NAS for AGI research.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, nas, architecture, automl, optimization, neural-network, design]
---

# Neural Architecture Search (NAS)

## Overview

Neural Architecture Search (NAS) automates the design of neural network architectures by treating architecture design as a machine learning problem. This skill provides frameworks for defining search spaces, implementing search strategies, and evaluating architectures efficiently for AGI research.

## When to Use

- Designing optimal neural network architectures automatically
- Exploring novel architecture designs beyond human intuition
- Optimizing architectures for specific hardware or constraints
- Comparing architecture families systematically
- Finding efficient architectures (accuracy vs compute trade-off)
- Discovering new architectural patterns for AGI
- Automating architecture iteration in OMEGA ASI development

## Core Components

### 1. Search Space

Definition of possible architectures to explore:

```yaml
search_space_types:
  macro_search:
    description: "Search over entire network topology"
    includes: ["layer types", "connections", "depth", "width"]
    flexibility: "Maximum"
    search_cost: "Very high"
    
  cell_based:
    description: "Search for repeatable cell/block patterns"
    includes: ["cell operations", "cell connections"]
    flexibility: "Medium"
    search_cost: "Medium"
    example: "NASNet, DARTS"
    
  hierarchical:
    description: "Multi-level search (cells → blocks → network)"
    includes: ["operations", "cells", "macro structure"]
    flexibility: "High with structure"
    search_cost: "High"
    
  chain_structured:
    description: "Sequential layer stacking"
    includes: ["layer types", "layer configs"]
    flexibility: "Low"
    search_cost: "Low"
```

### 2. Search Strategy

Algorithms for exploring the search space:

```python
search_strategies = {
    "reinforcement_learning": {
        "description": "Controller RNN generates architectures, trained via RL",
        "examples": ["NAS (Zoph & Le)", "ENAS", "MetaQNN"],
        "pros": ["Can discover novel architectures", "Flexible"],
        "cons": ["High computational cost", "Sample inefficient"],
        "compute_cost": "Very High (1000s GPU-hours)"
    },
    "evolutionary": {
        "description": "Population-based search with mutation and selection",
        "examples": ["AmoebaNet", "NEAT", "Regularized Evolution"],
        "pros": ["Parallel evaluation", "No gradients needed"],
        "cons": ["Slow convergence", "Many evaluations"],
        "compute_cost": "High (100s GPU-hours)"
    },
    "gradient_based": {
        "description": "Continuous relaxation, optimize with gradients",
        "examples": ["DARTS", "ProxylessNAS", "SNAS"],
        "pros": ["Fast (single GPU-days)", "Differentiable"],
        "cons": ["May collapse to simple ops", "Memory intensive"],
        "compute_cost": "Low (1-10 GPU-days)"
    },
    "bayesian_optimization": {
        "description": "Surrogate model predicts performance",
        "examples": ["BANANAS", "BONAS", "NASBOT"],
        "pros": ["Sample efficient", "Uncertainty quantification"],
        "cons": ["Scales poorly", "Surrogate accuracy"],
        "compute_cost": "Medium"
    },
    "predictor_based": {
        "description": "Train predictor on architecture-performance pairs",
        "examples": ["NAO", "Predictor-guided NAS"],
        "pros": ["Fast evaluation", "Reusable predictor"],
        "cons": ["Requires training data", "Generalization"],
        "compute_cost": "Medium (after predictor training)"
    }
}
```

### 3. Performance Estimation

Strategies for evaluating candidate architectures:

```python
estimation_strategies = {
    "full_training": {
        "method": "Train each architecture to completion",
        "accuracy": "Highest",
        "cost": "Very High",
        "use_when": "Final evaluation only"
    },
    "early_stopping": {
        "method": "Train partially, extrapolate final performance",
        "accuracy": "Medium",
        "cost": "Medium",
        "use_when": "Ranking candidates"
    },
    "weight_sharing": {
        "method": "Share weights across architectures (supernet)",
        "accuracy": "Medium (order may differ)",
        "cost": "Low",
        "use_when": "Large-scale exploration",
        "examples": ["ENAS", "Once-for-All"]
    },
    "zero_cost_proxies": {
        "method": "Compute metrics without training",
        "accuracy": "Low-Medium",
        "cost": "Very Low",
        "use_when": "Initial filtering",
        "examples": ["Synflow", "NASWOT", "GradNorm"]
    },
    "predictor": {
        "method": "Learned model predicts performance",
        "accuracy": "Medium",
        "cost": "Low (after training)",
        "use_when": "Repeat searches, known domains"
    }
}
```

## NAS Frameworks

### DARTS (Differentiable Architecture Search)

```python
darts_workflow = {
    "concept": "Continuous relaxation of discrete architecture choices",
    "process": [
        "1. Define mixed operation (weighted sum of all ops)",
        "2. Jointly optimize architecture weights (α) and network weights (w)",
        "3. Bilevel optimization: inner loop trains w, outer loop trains α",
        "4. Discretize: select ops with highest α weights",
        "5. Retrain discretized architecture from scratch"
    ],
    "implementation": {
        "mixed_op": "sum(softmax(α) * op(x) for op in operations)",
        "inner_optimization": "SGD on weights w",
        "outer_optimization": "Adam on architecture params α",
        "memory_trick": "First-order approximation to reduce memory"
    },
    "variants": [
        "DARTS+: Early stopping to prevent collapse",
        "PC-DARTS: Partial channel sampling",
        "FairDARTS: Fairer operation competition",
        "DARTS-PT: Perturbation-based training"
    ]
}
```

### One-Shot NAS / Supernet

```python
supernet_approach = {
    "concept": "Train single supernet containing all architectures",
    "steps": [
        "1. Define supernet with all possible paths",
        "2. Train supernet with path dropout/sampling",
        "3. Search by evaluating subnets (no retraining)",
        "4. Fine-tune selected architecture"
    ],
    "benefits": [
        "Amortized training cost",
        "Fast architecture evaluation",
        "Transferable across tasks"
    ],
    "challenges": [
        "Weight coupling between subnets",
        "Order-preserving may be poor",
        "Training stability"
    ],
    "examples": ["Once-for-All", "BigNAS", "AttentiveNAS"]
}
```

### NADER (NeurIPS/CVPR 2024-2025)

Multi-agent approach to neural architecture design:

```python
nader_framework = {
    "concept": "LLM-based multi-agent collaboration for architecture design",
    "teams": {
        "research_team": {
            "reader_agent": "Learns from academic literature",
            "proposer_agent": "Generates architecture modifications"
        },
        "development_team": {
            "modifier_agent": "Implements proposed changes",
            "reflector_agent": "Analyzes feedback, guides iteration"
        }
    },
    "process": [
        "1. Reader continuously learns from new papers",
        "2. Proposer generates architecture ideas based on knowledge",
        "3. Modifier implements changes to base architecture",
        "4. Reflector analyzes results, informs next iteration"
    ],
    "key_innovation": "Not constrained by predefined search space"
}
```

## Search Space Design

### Cell-Based Search Space

```python
cell_search_space = {
    "nodes": 4,  # Intermediate nodes in cell
    "input_nodes": 2,  # Previous cells' outputs
    "operations": [
        "none",
        "skip_connect",
        "sep_conv_3x3",
        "sep_conv_5x5",
        "dil_conv_3x3",
        "dil_conv_5x5",
        "avg_pool_3x3",
        "max_pool_3x3"
    ],
    "cell_types": ["normal", "reduction"],
    "structure": {
        "per_node": "Select 2 inputs + operations from previous nodes",
        "output": "Concatenate all unused nodes"
    }
}
```

### Macro Search Space

```python
macro_search_space = {
    "stages": [
        {
            "input_resolution": 224,
            "channels": [16, 32, 64],
            "depth": [1, 2, 3, 4],
            "block_types": ["conv", "mbconv", "transformer"]
        },
        {
            "input_resolution": 112,
            "channels": [64, 128, 256],
            "depth": [2, 3, 4, 5],
            "block_types": ["conv", "mbconv", "transformer"]
        }
        # ... more stages
    ],
    "connections": ["sequential", "skip", "dense"]
}
```

### Transformer Search Space

```python
transformer_search_space = {
    "global": {
        "num_layers": [6, 8, 10, 12],
        "hidden_dim": [256, 384, 512, 768],
        "mlp_ratio": [2, 3, 4],
        "num_heads": [4, 6, 8, 12]
    },
    "per_layer": {
        "attention_type": ["full", "sparse", "linear", "local"],
        "ffn_type": ["mlp", "glu", "moe"],
        "normalization": ["pre_ln", "post_ln", "rmsnorm"],
        "activation": ["relu", "gelu", "swish"]
    }
}
```

## Hardware-Aware NAS

### Latency-Aware Search

```python
hardware_aware_nas = {
    "objectives": ["accuracy", "latency", "energy", "memory"],
    "methods": {
        "latency_predictor": {
            "approach": "Learn mapping from arch to latency",
            "data": "Profile operations on target hardware",
            "model": "MLP, GNN, or lookup table"
        },
        "latency_constraint": {
            "approach": "Only evaluate archs meeting constraint",
            "implementation": "Reject or penalize slow architectures"
        },
        "multi_objective": {
            "approach": "Pareto optimization",
            "output": "Pareto frontier of accuracy vs latency"
        }
    },
    "examples": ["ProxylessNAS", "MnasNet", "EfficientNet"]
}
```

### Carbon-Efficient NAS (CE-NAS, NeurIPS 2024)

```python
ce_nas = {
    "objective": "Reduce carbon footprint of NAS",
    "methods": {
        "carbon_intensity_aware_scheduling": {
            "approach": "Schedule compute during low-carbon periods",
            "implementation": "RL agent monitors grid carbon intensity"
        },
        "search_space_reduction": {
            "approach": "Multi-objective optimizer reduces search space",
            "benefit": "Fewer evaluations needed"
        }
    },
    "results": {
        "carbon_reduction": "Up to 7.22X",
        "accuracy": "Maintains SOTA performance"
    }
}
```

## NAS for AGI Research

### Architecture Discovery Protocol

```markdown
## NAS Experiment: [Architecture Goal]

### 1. Define Objectives
- **Primary**: [e.g., Reasoning accuracy]
- **Secondary**: [e.g., Compute efficiency]
- **Constraints**: [e.g., Max 10B parameters]

### 2. Design Search Space
- **Base architecture**: [e.g., Transformer]
- **Search dimensions**: [What to vary]
- **Fixed components**: [What to keep constant]

### 3. Select Search Strategy
- **Strategy**: [e.g., DARTS, Evolutionary]
- **Budget**: [GPU-hours available]
- **Parallelism**: [Number of workers]

### 4. Performance Estimation
- **Method**: [e.g., Weight sharing + fine-tuning]
- **Proxy tasks**: [Smaller tasks for fast evaluation]
- **Final evaluation**: [Full training on target task]

### 5. Execution Plan
- **Phase 1**: Search with proxy
- **Phase 2**: Top-K evaluation
- **Phase 3**: Final training and validation

### 6. Analysis
- **Best architecture**: [Description]
- **Key discoveries**: [Novel patterns found]
- **Comparison to baseline**: [Improvement %]
```

### Integrating NAS with OMEGA ASI

```python
omega_nas_integration = {
    "search_targets": [
        "Attention mechanism variants",
        "Memory module architectures",
        "Reasoning circuit designs",
        "Multi-modal fusion strategies"
    ],
    "process": [
        "1. Identify architecture bottleneck in current version",
        "2. Define targeted search space for that component",
        "3. Run NAS with AGI-relevant benchmarks",
        "4. Validate top candidates on safety + capability",
        "5. Integrate into next OMEGA ASI version"
    ],
    "benchmarks": [
        "Reasoning benchmarks (ARC, BIG-Bench)",
        "Few-shot learning",
        "Transfer efficiency",
        "Long-context handling"
    ]
}
```

## Implementation Template

```python
class NASExperiment:
    """Template for NAS experiments in AGI research."""
    
    def __init__(self, config):
        self.search_space = SearchSpace(config.space_config)
        self.search_strategy = SearchStrategy(config.strategy)
        self.evaluator = PerformanceEstimator(config.estimation)
        self.hardware = HardwareConstraints(config.hardware)
        
    def run_search(self, budget):
        """Execute NAS search."""
        best_architectures = []
        
        for iteration in range(budget.iterations):
            # Generate candidate architectures
            candidates = self.search_strategy.propose(
                self.search_space, 
                batch_size=budget.batch_size
            )
            
            # Filter by hardware constraints
            valid_candidates = [
                c for c in candidates 
                if self.hardware.satisfies(c)
            ]
            
            # Evaluate candidates
            results = self.evaluator.evaluate(valid_candidates)
            
            # Update search strategy
            self.search_strategy.update(results)
            
            # Track best
            best_architectures.extend(
                self.get_top_k(results, k=5)
            )
        
        return self.final_evaluation(best_architectures)
    
    def final_evaluation(self, candidates):
        """Full training evaluation of top candidates."""
        final_results = []
        for arch in candidates:
            # Train to convergence
            performance = self.evaluator.full_train(arch)
            final_results.append((arch, performance))
        return sorted(final_results, key=lambda x: x[1], reverse=True)
```

## Tools and Libraries

```yaml
nas_tools:
  frameworks:
    - NNI: "Microsoft's AutoML toolkit with NAS support"
    - AutoGluon: "AWS AutoML with NAS"
    - NASLib: "Modular NAS library"
    - NATS-Bench: "NAS benchmarks"
    
  benchmarks:
    - NAS-Bench-101: "Exhaustive cell search space"
    - NAS-Bench-201: "Smaller, multi-dataset"
    - NAS-Bench-301: "Surrogate benchmark for DARTS"
    - TransNAS-Bench-101: "Transformer architectures"
    
  search_spaces:
    - MobileNet space: "Efficient mobile architectures"
    - DARTS space: "Cell-based CNN"
    - AutoFormer space: "Transformer variants"
```

## Integration with Other Skills

```
1. Use agi-hypothesis-generator:
   - Hypothesize which architecture components to search
   
2. Use neural-architecture-search (THIS SKILL):
   - Define search space based on hypothesis
   - Run NAS experiments
   
3. Use experiment-tracker:
   - Log all architecture evaluations
   - Track search progress
   
4. Use benchmark-creator:
   - Create AGI-relevant evaluation benchmarks
   
5. Use safety-alignment-researcher:
   - Evaluate safety properties of discovered architectures
   
6. Use memory-manager:
   - Store discovered architectures in Neo4j
```

## Knowledge Graph Integration

```cypher
// Store NAS experiment
CREATE (nas:NASExperiment {
  id: 'nas_001',
  search_space: 'transformer_attention',
  strategy: 'DARTS',
  budget_gpu_hours: 48,
  completed_date: datetime()
})

// Store discovered architecture
CREATE (arch:DiscoveredArchitecture {
  id: 'arch_001',
  name: 'SparseAttention_v1',
  performance: 0.847,
  parameters: '125M',
  latency_ms: 45
})
CREATE (nas)-[:DISCOVERS]->(arch)

// Link to OMEGA ASI
MATCH (omega:Architecture {name: 'OMEGA_ASI_v560'})
CREATE (arch)-[:INTEGRATED_INTO]->(omega)
```

## Best Practices

1. **Start with Baselines**: Understand manual design performance first
2. **Use Proxies Wisely**: Validate proxy correlation with final performance
3. **Multi-objective**: Consider efficiency alongside accuracy
4. **Reproduce and Verify**: NAS results can be noisy
5. **Search Space Matters**: Often more important than search strategy
6. **Avoid Overfitting**: Use held-out data for architecture selection
7. **Document Everything**: Track all architecture evaluations
8. **Hardware Awareness**: Target your actual deployment platform
9. **Combine with Transfer**: Apply discovered architectures across tasks
10. **Safety Review**: Evaluate safety properties of novel architectures

## Version History

- **v1.0.0** (2026-01-31): Initial release with search spaces, strategies, hardware-aware NAS, and AGI integration

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

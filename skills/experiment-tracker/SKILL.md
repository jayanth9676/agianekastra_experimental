---
name: experiment-tracker
description: Track, log, and manage ML experiments including configurations, metrics, results, and relationships to research questions and architectures
---

# Experiment Tracker Skill

This skill provides comprehensive tools for tracking, logging, and managing machine learning experiments. It captures experiment configurations, metrics, results, and maintains relationships to research questions and OMEGA ASI architectures.

## When to Use This Skill

Use this skill when you need to:
- Design and configure new experiments
- Log experiment parameters and configurations
- Track metrics and results over time
- Compare experiments across different runs
- Reproduce previous experiments
- Link experiments to research questions
- Test OMEGA ASI architecture variants
- Benchmark model performance

## Experiment Lifecycle

### Phase 1: Design

Define experiment scope and hypothesis:

```
Experiment Design:
- Question: What architecture performs best on [task]?
- Hypothesis: OMEGA_ASI_v300 outperforms v200
- Variables:
  - Independent: Architecture version
  - Dependent: Performance metrics
  - Controlled: Dataset, training procedure
- Metrics: Accuracy, efficiency, scalability
- Success Criteria: >5% improvement over baseline
```

### Phase 2: Configuration

Document all experiment parameters:

```json
{
  "experiment_id": "exp_2024_001",
  "name": "OMEGA_ASI_v300_vs_v200_benchmark",
  "hypothesis": "v300 shows 5% improvement",
  "architecture": "OMEGA_ASI_v300",
  "baseline": "OMEGA_ASI_v200",
  
  "configuration": {
    "model": {
      "type": "OMEGA_ASI_v300",
      "parameters": "2.5B",
      "components": ["module_a", "module_b", "module_c"]
    },
    "training": {
      "dataset": "agibenchmark_v1",
      "epochs": 100,
      "batch_size": 32,
      "learning_rate": 0.001,
      "optimizer": "adamw"
    },
    "environment": {
      "hardware": "A100_80GB",
      "framework": "PyTorch 2.1",
      "cuda_version": "12.1"
    }
  },
  
  "metrics": [
    "accuracy",
    "perplexity",
    "training_time",
    "inference_latency",
    "memory_usage"
  ]
}
```

### Phase 3: Execution

Run experiment and capture real-time data:

```
Execution Log:
- Start time: 2024-01-30 10:00:00
- Checkpoints: Every 10 epochs
- Observations:
  - Epoch 10: Loss 2.5, learning well
  - Epoch 50: Loss 1.2, converging
  - Epoch 100: Loss 0.8, training complete
- Issues encountered: None
- Adaptations made: Reduced LR at epoch 80
```

### Phase 4: Results

Compile comprehensive results:

```json
{
  "results": {
    "performance": {
      "accuracy": 0.947,
      "perplexity": 12.3,
      "f1_score": 0.938
    },
    "efficiency": {
      "training_time_hours": 48.5,
      "inference_latency_ms": 45,
      "memory_usage_gb": 16.2
    },
    "scalability": {
      "max_sequence_length": 8192,
      "batch_size_tested": [16, 32, 64]
    }
  },
  
  "comparison_to_baseline": {
    "accuracy_improvement": "+7.2%",
    "speed_improvement": "+12%",
    "memory_efficiency": "-8%"
  },
  
  "hypothesis_validated": true,
  "confidence": 0.92,
  "conclusion": "v300 significantly outperforms v200"
}
```

### Phase 5: Storage

Store in knowledge graph:

```
Store in neo4j-memory:
- Experiment node with config and results
- Relationships to Architecture nodes
- Relationships to Question nodes
- Link to related Papers
- Create Finding nodes from results
```

## Experiment Configuration Template

### Standard Fields

Every experiment should include:

```yaml
experiment:
  id: "exp_YYYY_NNN"           # Unique identifier
  name: "descriptive_name"      # Human-readable name
  date: "2024-01-30"            # Start date
  status: "running|completed|failed"
  
  research_context:
    question: "What is being tested?"
    hypothesis: "Expected outcome"
    motivation: "Why this matters"
  
  subject:
    architecture: "OMEGA_ASI_vXXX"
    version: "3.0.1"
    components: [list of modules]
  
  methodology:
    dataset: "name_and_version"
    metrics: [list of metrics]
    evaluation_protocol: "description"
  
  configuration:
    hyperparameters: {dict}
    environment: {hardware, software}
    random_seed: 42
  
  results:
    metrics: {dict of values}
    artifacts: [model weights, logs, plots]
    observations: [text notes]
  
  analysis:
    conclusion: "summary"
    limitations: [list]
    next_steps: [recommendations]
```

## Tracking Metrics

### Performance Metrics

Track model capability:

```
Core Metrics:
- Accuracy / Precision / Recall / F1
- Perplexity (for language models)
- BLEU / ROUGE (for generation)
- MSE / MAE (for regression)

AGI-Specific:
- Generalization across tasks
- Few-shot learning ability
- Transfer learning performance
- Reasoning benchmark scores
```

### Efficiency Metrics

Track resource usage:

```
Efficiency Metrics:
- Training time (hours)
- Inference latency (ms)
- Memory usage (GB)
- Energy consumption (kWh)
- FLOPs (computational cost)
- Parameter count (M/B)
```

### Scalability Metrics

Track scaling behavior:

```
Scalability Metrics:
- Performance vs dataset size
- Performance vs model size
- Performance vs sequence length
- Parallelization efficiency
- Distributed training speedup
```

### Reliability Metrics

Track consistency:

```
Reliability Metrics:
- Variance across runs (std dev)
- Robustness to perturbations
- Stability over time
- Reproducibility score
```

## Comparison Framework

### A/B Testing

Compare two variants:

```
Test Setup:
- Variant A: OMEGA_ASI_v300 (baseline)
- Variant B: OMEGA_ASI_v350 (new)
- Dataset: Same for both
- Seeds: Multiple (5 runs each)
- Metric: Primary comparison on accuracy

Statistical Test:
- t-test for significance
- Effect size calculation
- Confidence intervals
```

### Multi-Variant Testing

Compare several approaches:

```
Variants:
- Control: OMEGA_ASI_v300
- Treatment 1: v300 + new module
- Treatment 2: v300 + different optimizer
- Treatment 3: v350 baseline

Analysis:
- ANOVA across all variants
- Pairwise comparisons
- Best performer identification
- Trade-off analysis
```

### Longitudinal Tracking

Track across versions:

```
Timeline:
v100 (2023-01): Accuracy 85.2%
v150 (2023-06): Accuracy 88.1% (+2.9%)
v200 (2023-09): Accuracy 90.5% (+2.4%)
v300 (2024-01): Accuracy 94.7% (+4.2%)

Trend: Consistent improvement, accelerating
```

## Reproducibility Checklist

Ensure experiments are reproducible:

- ✅ **Code version**: Git commit hash
- ✅ **Environment**: Docker image or requirements.txt
- ✅ **Data**: Dataset version and preprocessing steps
- ✅ **Random seed**: Set and recorded
- ✅ **Hardware**: GPU/CPU specifications
- ✅ **Configuration**: All hyperparameters documented
- ✅ **Logs**: Training logs with timestamps
- ✅ **Artifacts**: Model checkpoints saved
- ✅ **Results**: Raw metrics and processed results

## Integration with Research Questions

Link experiments to questions:

```
Before Experiment:
Question: "Does adding attention improve performance?"
Hypothesis: "Yes, by 5%"

After Experiment:
Result: "+7.2% improvement"
Confidence: 0.92

Update Question:
Status: "answered"
Answer: Finding node with results
New Questions: "What attention mechanism is optimal?"
```

## Best Practices

1. **Unique IDs** - Use consistent format (exp_YYYY_NNN)
2. **Version Control** - Tag code for each experiment
3. **Comprehensive Logging** - Capture everything, filter later
4. **Multiple Runs** - Run 3-5 times for reliability
5. **Baseline Comparison** - Always compare to baseline
6. **Statistical Tests** - Don't rely on single metrics
7. **Document Failures** - Failed experiments are valuable
8. **Store Immediately** - Don't wait to store results
9. **Link Everything** - Connect to papers, questions, concepts
10. **Archive Old** - Mark superseded experiments

## Tools to Use

During experimentation:
1. **neo4j-memory** - Store and retrieve experiments
2. **huggingface** - Access models and datasets
3. **kaggle** - Run competitions and benchmarks
4. **memory-manager** - Store experiment data
5. **knowledge-graph-query** - Find related experiments
6. **filesystem** - Save large artifacts

## Example Workflows

### Example 1: Benchmarking New Architecture

```
1. Design experiment:
   - Test OMEGA_ASI_v400 vs v300
   - Use AGI benchmark suite
   - Metrics: accuracy, speed, efficiency

2. Configure:
   - Set hyperparameters
   - Fix random seed
   - Document environment

3. Execute:
   - Run on huggingface infrastructure
   - Log checkpoints every 10 epochs
   - Monitor for issues

4. Analyze:
   - Compare to baseline (v300)
   - Calculate improvement %
   - Test statistical significance

5. Store:
   - Create Experiment node
   - Link to Architecture nodes
   - Create Finding: "v400 shows 7% improvement"
   - Link to Question: "Does v400 outperform v300?"
```

### Example 2: Hyperparameter Search

```
1. Define search space:
   - Learning rate: [1e-4, 1e-3, 1e-2]
   - Batch size: [16, 32, 64]
   - Optimizer: [Adam, AdamW, SGD]

2. Run grid search:
   - 27 combinations (3x3x3)
   - 3 runs per combination
   - Total: 81 experiments

3. Track results:
   - Log all configurations
   - Store all metrics
   - Note convergence patterns

4. Identify best:
   - Best overall config
   - Best accuracy config
   - Best efficiency config
   - Pareto frontier

5. Store findings:
   - Summary of all experiments
   - Recommendation for best config
   - Trade-off analysis
```

## Troubleshooting

### Experiment won't reproduce?
- Check random seed
- Verify environment matches
- Confirm data preprocessing identical

### Metrics inconsistent?
- Run multiple times
- Check for hardware differences
- Verify evaluation code

### Results not as expected?
- Check for bugs
- Verify hyperparameters
- Compare with similar experiments in memory

### Storage issues?
- Check Neo4j connection
- Verify disk space
- Archive old experiments

## Dependencies

This skill uses:
- **neo4j-memory** - For storing experiment data
- **memory-manager** - For creating experiment nodes
- **knowledge-graph-query** - For finding related experiments
- **huggingface** - For running experiments
- **filesystem** - For storing large artifacts

## Related Skills

- **memory-manager** - For storing experiment data
- **knowledge-graph-query** - For retrieving past experiments
- **paper-synthesis** - For comparing with published results
- **agi-researcher** - For AGI-specific experimental design

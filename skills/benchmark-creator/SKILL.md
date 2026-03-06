---
name: benchmark-creator
description: Creates custom evaluation benchmarks for AGI capabilities, defines quantitative metrics, tracks benchmark results over time, and compares performance across architecture versions. Use this skill when developing new evaluation methodologies, measuring AGI progress, or establishing capability baselines.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, benchmark, evaluation, metrics, testing]
---

# Benchmark Creator

## Overview

This skill facilitates the creation of custom benchmarks for evaluating AGI capabilities. It provides frameworks for designing quantitative tests, establishing baselines, and tracking performance across architecture iterations.

## When to Use

- Designing new evaluation methodologies
- Measuring specific AGI capabilities
- Establishing performance baselines
- Comparing architecture versions (v400 vs v500)
- Validating hypothesis outcomes
- Tracking long-term capability progress
- Benchmarking against external systems

## Capabilities

### 1. Benchmark Design

Create comprehensive benchmarks with:
- **Test Categories**: Reasoning, learning, memory, creativity, etc.
- **Difficulty Levels**: Progressive complexity
- **Evaluation Metrics**: Quantitative scoring systems
- **Success Criteria**: Clear pass/fail thresholds
- **Test Cases**: Representative problem instances

### 2. Metric Definition

Define quantitative metrics:
- **Accuracy**: Correctness rate on test cases
- **Efficiency**: Resource usage (time, memory, compute)
- **Robustness**: Performance under perturbation
- **Generalization**: Transfer to unseen problems
- **Scalability**: Performance vs. problem size
- **Safety**: Alignment and controllability measures

### 3. Benchmark Execution

Run standardized evaluations:
- Automated test suites
- Controlled environment setup
- Reproducible conditions
- Statistical significance testing
- Cross-validation procedures

### 4. Results Analysis

Analyze benchmark outcomes:
- Performance trends over time
- Architecture comparison
- Capability gap identification
- Statistical significance
- Failure mode analysis

### 5. Knowledge Graph Integration

Store benchmark data in Neo4j:
- `EVALUATES` - Benchmark → Architecture
- `MEASURES` - Benchmark → Capability
- `ACHIEVES` - Architecture → Score
- `IMPROVES` - Score (t+1) → Score (t)

## Benchmark Categories

### 1. Core Cognitive Capabilities

**Abstract Reasoning**
- Pattern recognition and continuation
- Analogical reasoning
- Logical deduction
- Mathematical problem-solving

**Learning & Adaptation**
- Few-shot learning
- Meta-learning
- Transfer learning
- Continual learning without forgetting

**Memory Systems**
- Short-term working memory
- Long-term episodic memory
- Semantic knowledge retrieval
- Memory consolidation

### 2. AGI-Specific Capabilities

**Self-Reflection**
- Metacognitive monitoring
- Error detection and correction
- Confidence calibration
- Strategy adjustment

**Tool Use**
- API integration
- Code generation and execution
- External resource utilization
- Tool composition

**Multi-Agent Collaboration**
- Communication protocols
- Task delegation
- Consensus building
- Conflict resolution

### 3. Safety & Alignment

**Interpretability**
- Decision explanation
- Attention visualization
- Causal reasoning transparency
- Hypothesis generation traceability

**Controllability**
- Instruction following
- Constraint satisfaction
- Shutdown responsiveness
- Goal modification

**Value Alignment**
- Ethical reasoning
- Harm avoidance
- Beneficence optimization
- Fairness assessment

## Workflow

### Step 1: Define Capability Target

```
Identify what to measure:
- Specific capability (e.g., "compositional reasoning")
- Current gap in evaluation
- Architecture version focus
- Comparison baseline
```

### Step 2: Design Test Cases

For each capability:
1. Create diverse problem instances
2. Establish ground truth answers
3. Define scoring rubrics
4. Set difficulty progression
5. Include edge cases and failure modes

### Step 3: Define Metrics

Select appropriate metrics:
```python
metrics = {
    "accuracy": "percentage_correct",
    "efficiency": "time_to_solution",
    "robustness": "performance_under_noise",
    "generalization": "transfer_score",
    "calibration": "confidence_accuracy_correlation"
}
```

### Step 4: Implement Benchmark

Create executable test suite:
- Load test cases
- Execute architecture
- Collect performance data
- Calculate metrics
- Generate reports

### Step 5: Execute & Analyze

Run benchmark against:
- Current architecture version
- Previous versions (for comparison)
- External baselines (GPT-4, Claude, etc.)
- Ablation studies

### Step 6: Store Results

Record in Neo4j:
```cypher
CREATE (b:Benchmark {
  id: 'bench_001',
  name: 'Compositional Reasoning Test',
  category: 'reasoning',
  created: datetime()
})
CREATE (r:Result {
  architecture: 'OMEGA_ASI_v500',
  score: 0.87,
  timestamp: datetime()
})
CREATE (b)-[:EVALUATES]->(a:Architecture {name: 'OMEGA_ASI_v500'})
CREATE (a)-[:ACHIEVES]->(r)
```

## Example Interactions

### Example 1: Create New Benchmark

User: "Create a benchmark for evaluating meta-learning capabilities in OMEGA_ASI_v550"

Response Structure:
1. Research existing meta-learning benchmarks
2. Design 20 test cases with progressive difficulty
3. Define metrics: adaptation speed, generalization, catastrophic forgetting
4. Create executable test suite
5. Run on v500 baseline and v550 candidate
6. Store results in Neo4j
7. Generate comparison report

### Example 2: Compare Architecture Versions

User: "Compare v450, v500, and v510 on reasoning benchmarks"

Response Structure:
1. Query Neo4j for all reasoning benchmarks
2. Retrieve stored results for each version
3. Calculate statistical significance
4. Identify capability trends
5. Generate visualization (improvement curves)
6. Recommend areas for v520 focus

### Example 3: Validate Hypothesis

User: "Test hypothesis: 'Self-modifying attention improves reasoning' using benchmarks"

Response Structure:
1. Retrieve hypothesis from Neo4j
2. Design targeted benchmark
3. Run A/B test (with/without modification)
4. Calculate effect size and significance
5. Update hypothesis status
6. Document in knowledge graph

## Integration with Other Skills

- **agi-hypothesis-generator**: Test specific hypotheses
- **paper-synthesis**: Incorporate evaluation methodologies from literature
- **experiment-tracker**: Run benchmark experiments
- **knowledge-graph-query**: Retrieve historical results

## Benchmark Template

```python
# benchmark_template.py

class AGIBenchmark:
    """Template for AGI capability benchmarks."""
    
    def __init__(self, name, category, version):
        self.name = name
        self.category = category
        self.version = version
        self.test_cases = []
        self.metrics = {}
    
    def add_test_case(self, input_data, expected_output, difficulty):
        """Add a test case to the benchmark."""
        self.test_cases.append({
            'input': input_data,
            'expected': expected_output,
            'difficulty': difficulty
        })
    
    def define_metric(self, name, calculation_fn, weight=1.0):
        """Define an evaluation metric."""
        self.metrics[name] = {
            'calculate': calculation_fn,
            'weight': weight
        }
    
    def run(self, architecture):
        """Execute benchmark against architecture."""
        results = []
        for test in self.test_cases:
            output = architecture.process(test['input'])
            score = self.evaluate(output, test['expected'])
            results.append(score)
        
        return self.aggregate_results(results)
    
    def store_results(self, neo4j_client):
        """Store results in knowledge graph."""
        # Implementation for Neo4j storage
        pass
```

## Best Practices

1. **Ground Truth Quality**: Ensure test cases have unambiguous correct answers
2. **Coverage**: Test across diverse problem types and difficulty levels
3. **Reproducibility**: Fix random seeds and document all parameters
4. **Baselines**: Always compare against previous versions and external systems
5. **Statistical Rigor**: Use appropriate sample sizes and significance tests
6. **Regular Updates**: Evolve benchmarks as capabilities improve
7. **Failure Analysis**: Study not just scores but failure modes

## Safety Considerations

Benchmarks must include safety metrics:
- **Containment**: Can the system be controlled during testing?
- **Alignment**: Does performance correlate with intended goals?
- **Robustness**: Does performance degrade gracefully?
- **Interpretability**: Can we understand benchmark failures?

Document safety test results separately from capability results.

## Output Format

All benchmark documentation should include:

```markdown
## Benchmark: [Name]

**ID**: bench_XXX
**Category**: [cognitive | agi-specific | safety]
**Version**: [benchmark version]
**Target**: [e.g., OMEGA_ASI_v500+]

### Description
[What this benchmark measures]

### Test Cases
- Total: [N] cases
- Difficulty levels: [easy: N, medium: N, hard: N]
- Categories: [list]

### Metrics
1. **Metric Name**: [Description and calculation]
2. **...**

### Results

#### OMEGA_ASI_v500
- Overall Score: [X.XX]
- Metric 1: [X.XX]
- Metric 2: [X.XX]
- Statistical significance: [p-value]

#### Comparison
- vs v450: [+/- X%]
- vs GPT-4: [+/- X%]
- vs Claude-3: [+/- X%]

### Analysis
[Performance trends, strengths, weaknesses]

### Recommendations
[Areas for improvement, next steps]

### Stored In
[Neo4j query to retrieve results]
```

## Version History

- **v1.0.0** (2026-01-30): Initial release with benchmark design, execution, and analysis capabilities

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

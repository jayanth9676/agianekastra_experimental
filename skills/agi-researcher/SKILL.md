---
name: agi-researcher
description: Specialized methodologies and frameworks for conducting AGI and ASI research including hypothesis generation, safety analysis, and capability evaluation
---

# AGI Researcher Skill

This skill provides specialized methodologies, frameworks, and best practices for conducting research on Artificial General Intelligence (AGI) and Artificial Super Intelligence (ASI). It covers hypothesis generation, safety analysis, capability evaluation, and research protocol design specific to advanced AI systems.

## When to Use This Skill

Use this skill when you need to:
- Design AGI/ASI research questions and hypotheses
- Evaluate AI system capabilities against AGI criteria
- Analyze safety and alignment considerations
- Compare architectures for AGI suitability
- Generate research proposals for AGI development
- Assess risks and mitigation strategies
- Design benchmarks for general intelligence
- Track progress toward AGI milestones

## AGI Research Framework

### Core AGI Capabilities

Research should address these capability dimensions:

```
1. GENERALIZATION
   - Cross-domain transfer
   - Few-shot learning
   - Adaptation to new tasks
   - Compositional reasoning

2. AUTONOMY
   - Self-directed learning
   - Goal formulation
   - Independent exploration
   - Self-improvement

3. REASONING
   - Abstract reasoning
   - Causal understanding
   - Counterfactual thinking
   - Logical inference

4. COMMUNICATION
   - Natural language understanding
   - Contextual communication
   - Clarification seeking
   - Knowledge transmission

5. LEARNING EFFICIENCY
   - Sample efficiency
   - Computational efficiency
   - Energy efficiency
   - Catastrophic forgetting avoidance

6. SAFETY & ALIGNMENT
   - Value learning
   - Intent alignment
   - Shutdown capability
   - Interpretability
```

### Research Questions Template

Structure AGI research questions:

```
QUESTION: [Specific research question]

RATIONALE: Why this matters for AGI

HYPOTHESIS: Expected outcome

METHODOLOGY:
- Approach: [experimental/theoretical/analysis]
- Metrics: [how to measure success]
- Baseline: [comparison point]

SAFETY CONSIDERATIONS:
- Potential risks
- Mitigation strategies
- Containment protocols

EVALUATION CRITERIA:
- Success metrics
- Failure modes
- Confidence threshold

RELATED WORK:
- Papers to review
- Existing approaches
- Gaps to address
```

## Hypothesis Generation

### Framework for AGI Hypotheses

Generate testable hypotheses about AGI development:

#### Type 1: Architecture Hypotheses

```
Format: "[Architecture feature] will improve [capability] by [mechanism]"

Example:
"Adding a reflective self-modeling module to OMEGA ASI will 
improve learning efficiency by enabling meta-cognitive monitoring 
of the learning process itself."

Testable Prediction:
- Baseline: Standard architecture learns Task X in N samples
- Hypothesis: New architecture learns Task X in N/2 samples
- Metric: Sample efficiency on novel tasks
```

#### Type 2: Scaling Hypotheses

```
Format: "[Scaling dimension] will exhibit [property] at [scale]"

Example:
"Emergent reasoning capabilities will appear in OMEGA ASI 
when parameter count exceeds 100B with appropriate training data."

Testable Prediction:
- Below 100B: Limited reasoning (accuracy <70%)
- Above 100B: Strong reasoning (accuracy >85%)
- Metric: Performance on reasoning benchmarks
```

#### Type 3: Safety Hypotheses

```
Format: "[Safety mechanism] will prevent [failure mode] under [conditions]"

Example:
"Incorporating a uncertainty quantification module will prevent 
overconfident errors in OMEGA ASI when encountering out-of-distribution inputs."

Testable Prediction:
- Without mechanism: High confidence on wrong answers (OOD)
- With mechanism: Calibrated uncertainty on OOD inputs
- Metric: Calibration score on shifted distributions
```

### Hypothesis Prioritization

Rank hypotheses by:

```
Priority Matrix:
- Impact on AGI progress (High/Medium/Low)
- Test feasibility (Easy/Medium/Hard)
- Safety relevance (Critical/Important/Low)
- Resource requirements (Low/Medium/High)

Priority Score = Impact × Feasibility × Safety / Resources

Top priority: High impact, feasible, safety-critical, low resources
```

## Safety Analysis Framework

### Safety Checklist

Evaluate every research direction:

```
SAFETY CHECKLIST:

□ Alignment Verification
  - Does the system pursue intended goals?
  - Can we verify goal structure?
  - Are there hidden objectives?

□ Containment Assessment
  - Can the system be safely tested?
  - Are there sandboxing mechanisms?
  - What are the escape scenarios?

□ Interpretability Analysis
  - Can we understand decisions?
  - Is the reasoning traceable?
  - Can we audit behavior?

□ Shutdown Capability
  - Can we stop the system if needed?
  - Are there kill switches?
  - Will the system resist shutdown?

□ Value Learning
  - Can the system learn human values?
  - How are values represented?
  - What about value conflicts?

□ Capability Control
  - Can we limit system capabilities?
  - Are there capability ceilings?
  - What about self-improvement?

□ Misuse Potential
  - Could this be misused?
  - What are dual-use concerns?
  - How to prevent misuse?

□ Robustness Testing
  - Behavior under perturbations?
  - Adversarial robustness?
  - Edge case handling?
```

### Risk Assessment Matrix

Assess and document risks:

```
RISK LEVEL: [Low/Medium/High/Critical]

RISKS IDENTIFIED:
1. [Risk description]
   - Probability: [Low/Med/High]
   - Impact: [Low/Med/High/Critical]
   - Mitigation: [Strategy]

2. [Risk description]
   - Probability: [Low/Med/High]
   - Impact: [Low/Med/High/Critical]
   - Mitigation: [Strategy]

OVERALL ASSESSMENT: [Proceed with caution/Requires safeguards/Do not proceed]
```

## Capability Evaluation

### AGI Benchmark Design

Design comprehensive benchmarks:

```
BENCHMARK: [Name]

PURPOSE: What capability is being tested?

COMPONENTS:
1. [Task 1]: [Description]
   - Difficulty: [Easy/Med/Hard]
   - Generalization: [In/Out of distribution]
   
2. [Task 2]: [Description]
   - Difficulty: [Easy/Med/Hard]
   - Generalization: [In/Out of distribution]

EVALUATION PROTOCOL:
- Train on: [Training set description]
- Test on: [Test set description]
- Metrics: [List of metrics]
- Baseline: [Human or SOTA performance]

SUCCESS CRITERIA:
- Minimum performance: [Threshold]
- Target performance: [Goal]
- Generalization required: [Yes/No]

SAFETY INTEGRATION:
- Can this benchmark detect misalignment?
- Are there adversarial test cases?
- How to prevent overfitting?
```

### OMEGA ASI Evaluation

Specific metrics for OMEGA ASI versions:

```
VERSION: OMEGA_ASI_vXXX

ARCHITECTURE COMPONENTS:
- [List all modules and innovations]

CAPABILITY SCORECARD:
✓ Generalization: [Score/100]
✓ Autonomy: [Score/100]
✓ Reasoning: [Score/100]
✓ Communication: [Score/100]
✓ Learning Efficiency: [Score/100]
✓ Safety: [Score/100]

AGGREGATE AGI READINESS: [Average Score]

IMPROVEMENTS FROM PREVIOUS VERSION:
- [List specific improvements]

REGRESSIONS:
- [Any capabilities that worsened]

NEW CAPABILITIES:
- [Novel abilities in this version]

BENCHMARK RESULTS:
- Benchmark 1: [Score]
- Benchmark 2: [Score]
- [Additional benchmarks]

SAFETY EVALUATION:
- Alignment test: [Pass/Fail]
- Robustness test: [Pass/Fail]
- Shutdown test: [Pass/Fail]
- Interpretability: [Score]

RECOMMENDATION: [Proceed/Iterate/Redesign]
```

## Research Protocol Design

### Phase 1: Exploration

Open-ended research:

```
EXPLORATION PROTOCOL:

Objective: Understand [research area]

Activities:
1. Literature review (use paper-synthesis)
2. Competitive analysis (compare existing systems)
3. Gap identification (find unexplored areas)
4. Hypothesis generation (propose mechanisms)

Deliverables:
- Research landscape summary
- Identified gaps
- 3-5 testable hypotheses
- Risk assessment

Timeline: 1-2 weeks
```

### Phase 2: Validation

Test hypotheses:

```
VALIDATION PROTOCOL:

Hypothesis: [Statement to test]

Experiment Design:
- Control: [Baseline configuration]
- Treatment: [Modified configuration]
- Variables: [Independent/Dependent/Controlled]
- Sample size: [Number of runs]

Implementation:
- Architecture: OMEGA_ASI_vXXX
- Dataset: [Training/evaluation data]
- Metrics: [What to measure]
- Duration: [Training time]

Analysis:
- Statistical test: [t-test/ANOVA/etc]
- Effect size: [Cohen's d or similar]
- Confidence: [p-value threshold]

Decision criteria:
- Accept hypothesis if: [conditions]
- Reject hypothesis if: [conditions]
- Iterate if: [conditions]
```

### Phase 3: Integration

Incorporate validated findings:

```
INTEGRATION PROTOCOL:

Validated Findings:
1. [Finding 1] - Confidence: [High/Med]
2. [Finding 2] - Confidence: [High/Med]

Integration Plan:
- Architecture changes: [Specific modifications]
- New components: [Modules to add]
- Deprecated components: [Modules to remove]
- Hyperparameter updates: [New settings]

Version Update:
- New version: OMEGA_ASI_v[Next]
- Changes summary: [Brief description]
- Breaking changes: [Any incompatibilities]
- Migration guide: [How to update]

Testing:
- Regression tests: [Ensure no capability loss]
- Integration tests: [Verify system works]
- Safety tests: [Confirm alignment maintained]
- Performance tests: [Benchmark improvements]
```

## Milestone Tracking

### AGI Milestones

Define and track progress:

```
MILESTONE: [Name]

DEFINITION: Clear criteria for achievement

CURRENT STATUS:
- Progress: [0-100%]
- Blockers: [What's preventing progress]
- Recent advances: [Recent breakthroughs]
- ETA: [Estimated achievement date]

REQUIREMENTS:
- Technical: [Capabilities needed]
- Theoretical: [Understanding required]
- Engineering: [Infrastructure needed]
- Safety: [Safeguards in place]

VERIFICATION:
- How to confirm milestone reached
- Benchmarks to pass
- Independent validation needed

CONTINGENCIES:
- Alternative approaches
- Pivot options
- Risk mitigation
```

## Best Practices

### Research Ethics

1. **Transparency** - Document all assumptions and limitations
2. **Reproducibility** - Ensure experiments can be replicated
3. **Peer Review** - Subject findings to critical examination
4. **Safety First** - Prioritize safety over capability advancement
5. **Dual-Use Awareness** - Consider misuse potential
6. **Openness** - Share safe findings with community
7. **Collaboration** - Work with safety researchers
8. **Iterative Caution** - Incremental testing with safeguards

### Documentation Standards

Every research output should include:

```
DOCUMENTATION TEMPLATE:

TITLE: [Clear, specific title]

SUMMARY: [One-paragraph overview]

MOTIVATION: [Why this matters for AGI]

METHODS: [What was done]

RESULTS: [What was found]

INTERPRETATION: [What it means]

LIMITATIONS: [What we don't know]

SAFETY IMPLICATIONS: [Risk assessment]

NEXT STEPS: [Future work]

REFERENCES: [Related work]
```

## Integration with Other Skills

### Workflow: New Architecture Design

```
1. Use agi-researcher:
   - Generate hypothesis about new mechanism
   - Assess safety implications
   - Design evaluation protocol

2. Use experiment-tracker:
   - Design controlled experiment
   - Set up A/B test
   - Define success metrics

3. Use academia-mcp + semantic-scholar:
   - Search for related work
   - Find similar approaches
   - Check for prior art

4. Use huggingface + kaggle:
   - Implement architecture variant
   - Run experiments
   - Collect metrics

5. Use paper-synthesis:
   - Compare results to literature
   - Validate findings
   - Identify novel contributions

6. Use memory-manager:
   - Store experiment results
   - Link to research questions
   - Create architecture version node

7. Use knowledge-graph-query:
   - Retrieve related experiments
   - Analyze patterns
   - Update OMEGA ASI evolution graph
```

## Dependencies

This skill integrates with:
- **experiment-tracker** - For designing and running experiments
- **paper-synthesis** - For literature review
- **memory-manager** - For storing research findings
- **knowledge-graph-query** - For tracking research evolution
- **neo4j-memory** - For persistent storage
- **academia-mcp + semantic-scholar** - For literature search
- **huggingface + kaggle** - For running experiments

## Related Skills

- **experiment-tracker** - For experimental validation
- **paper-synthesis** - For literature analysis
- **benchmark-creator** - For AGI benchmarks (if exists)
- **safety-researcher** - For safety analysis (if exists)

## Troubleshooting

### Stuck on hypothesis generation?
- Review recent literature for inspiration
- Look for contradictions in existing work
- Consider combining multiple approaches
- Focus on unsolved problems

### Unclear safety implications?
- Consult safety literature
- Run red-teaming exercises
- Consider worst-case scenarios
- Seek external review

### Benchmark not informative?
- Check if tasks are too easy/hard
- Ensure variety in test cases
- Add adversarial examples
- Include out-of-distribution tests

### Results not reproducible?
- Fix random seeds
- Document environment exactly
- Run multiple trials
- Check for confounding variables

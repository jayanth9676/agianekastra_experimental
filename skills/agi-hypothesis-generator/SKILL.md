---
name: agi-hypothesis-generator
description: Generates and prioritizes research hypotheses for AGI/ASI development, tracks experiment outcomes, and maintains a structured hypothesis database in Neo4j knowledge graph. Use this skill when designing new experiments, brainstorming architectural innovations, or evaluating research directions.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, research, hypothesis, experimentation]
---

# AGI Hypothesis Generator

## Overview

This skill assists in generating, evaluating, and tracking research hypotheses for AGI/ASI development. It maintains a structured hypothesis database and provides frameworks for systematic experimentation.

## When to Use

- Brainstorming new architectural innovations
- Designing experiments to test AGI capabilities
- Evaluating competing research directions
- Prioritizing experimental work
- Documenting assumptions and predictions
- Reviewing past hypotheses and outcomes

## Capabilities

### 1. Hypothesis Generation

Generate structured hypotheses with:
- Clear research question
- Underlying assumptions
- Testable predictions
- Success/failure criteria
- Expected impact on AGI capabilities

### 2. Hypothesis Prioritization

Evaluate hypotheses using multi-criteria analysis:
- **Feasibility**: Technical difficulty and resource requirements
- **Impact**: Potential contribution to AGI development
- **Novelty**: Degree of innovation beyond existing approaches
- **Risk**: Probability of failure and consequences
- **Alignment**: Consistency with safety and ethical guidelines

### 3. Experiment Tracking

Maintain records of:
- Hypothesis tested
- Experimental design
- Results and observations
- Conclusions and next steps
- Related hypotheses and dependencies

### 4. Knowledge Graph Integration

Store hypotheses in Neo4j with relationships:
- `GENERATES` - Architecture → Hypothesis
- `TESTS` - Experiment → Hypothesis
- `REFINES` - Hypothesis → Hypothesis
- `CONTRADICTS` - Hypothesis → Hypothesis
- `SUPPORTS` - Finding → Hypothesis

## Workflow

### Step 1: Define Research Context

```
Query existing knowledge:
- Current architecture version (e.g., OMEGA_ASI_v500)
- Recent findings from Neo4j
- Open questions and gaps
- Competing approaches in literature
```

### Step 2: Generate Hypotheses

For each research direction:
1. Formulate clear, testable statement
2. Identify underlying assumptions
3. Define specific predictions
4. Establish evaluation criteria
5. Estimate resource requirements

### Step 3: Prioritize

Apply weighted scoring:
```
Priority Score = (Impact × 0.4) + (Feasibility × 0.3) + (Novelty × 0.2) + (Alignment × 0.1)
```

### Step 4: Design Experiments

For top-priority hypotheses:
1. Define experimental methodology
2. Identify required resources
3. Set timeline and milestones
4. Establish success metrics
5. Plan for failure modes

### Step 5: Execute and Track

Use `experiment-tracker` skill to:
- Run experiments
- Record observations
- Analyze results
- Update hypothesis status

### Step 6: Store Findings

Store in Neo4j:
```cypher
CREATE (h:Hypothesis {
  id: 'hyp_001',
  statement: 'Self-modifying attention mechanisms improve...',
  status: 'tested',
  outcome: 'validated',
  priority: 8.5,
  created: datetime(),
  tested: datetime()
})
```

## Example Interactions

### Example 1: Generate Hypotheses for Autopoietic Systems

User: "Generate hypotheses for implementing autopoietic (self-producing) capabilities in OMEGA_ASI_v550"

Response Structure:
1. Query Neo4j for existing autopoiesis research
2. Generate 5-7 specific hypotheses
3. Prioritize by feasibility and impact
4. Suggest experimental designs for top 3
5. Store hypotheses in knowledge graph

### Example 2: Evaluate Competing Approaches

User: "Compare hypothesis: 'Transformer alternatives improve efficiency' vs 'Scaling transformers is optimal'"

Response Structure:
1. Retrieve related hypotheses from Neo4j
2. Analyze supporting evidence for each
3. Identify key differentiators
4. Suggest experiments to discriminate
5. Recommend prioritization

### Example 3: Review Past Outcomes

User: "What hypotheses have been validated in the v400-v500 evolution?"

Response Structure:
1. Query Neo4j for hypotheses linked to architecture versions
2. Summarize validation rates
3. Identify patterns in successful hypotheses
4. Suggest lessons for future work

## Integration with Other Skills

- **paper-synthesis**: Incorporate latest research findings
- **knowledge-graph-query**: Retrieve related work and context
- **experiment-tracker**: Execute and monitor experiments
- **memory-manager**: Store and retrieve hypothesis history

## Best Practices

1. **Be Specific**: Vague hypotheses are untestable
2. **Start Small**: Test component hypotheses before system-level claims
3. **Track Assumptions**: Document what you're assuming vs. testing
4. **Embrace Failure**: Invalidated hypotheses are valuable learnings
5. **Build Chains**: Connect related hypotheses into research programs
6. **Stay Current**: Regularly review and update hypothesis database

## Output Format

All hypothesis documentation should include:

```markdown
## Hypothesis: [Brief Title]

**ID**: hyp_XXX
**Status**: [proposed | testing | validated | invalidated | superseded]
**Priority**: [1-10 score]
**Related Architectures**: [e.g., v450, v500]

### Statement
[Clear, testable hypothesis statement]

### Assumptions
- [Assumption 1]
- [Assumption 2]

### Predictions
1. [Specific, measurable prediction]
2. [Another prediction]

### Evaluation Criteria
- Success: [What confirms the hypothesis]
- Failure: [What refutes it]

### Experiment Design
[Link to experiment documentation]

### Results
[Populated after testing]

### Conclusions
[Populated after analysis]

### Related Work
- Depends on: [hyp IDs]
- Refines: [hyp IDs]
- Contradicts: [hyp IDs]
```

## Safety Considerations

Before testing hypotheses:
- [ ] **Alignment Check**: Does this advance safe AGI development?
- [ ] **Containment Review**: Can experiments be safely conducted?
- [ ] **Dual-Use Assessment**: Could results be misused?
- [ ] **Interpretability**: Will we understand why it works/fails?

Document all safety considerations in the hypothesis record.

## Version History

- **v1.0.0** (2026-01-30): Initial release with hypothesis generation, prioritization, and tracking capabilities

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

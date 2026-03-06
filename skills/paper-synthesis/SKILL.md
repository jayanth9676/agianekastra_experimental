---
name: paper-synthesis
description: Synthesize and cross-reference multiple research papers to identify patterns, gaps, contradictions, and generate comprehensive literature reviews
---

# Paper Synthesis Skill

This skill provides methodologies for synthesizing and cross-referencing multiple research papers to identify patterns, contradictions, research gaps, and generate comprehensive literature reviews.

## When to Use This Skill

Use this skill when you need to:
- Cross-reference findings from multiple papers
- Identify patterns across research literature
- Find contradictions or conflicting results
- Discover research gaps and opportunities
- Generate comprehensive literature reviews
- Compare methodologies across papers
- Track evolution of ideas over time
- Build knowledge graphs from literature

## Synthesis Methodology

### Phase 1: Paper Collection

Gather relevant papers from memory and external sources:

```
1. Query neo4j-memory for existing papers on topic
2. Use academia-mcp to search arXiv/Semantic Scholar
3. Use exa for latest web-based research
4. Collect 5-20 papers depending on scope
```

### Phase 2: Individual Analysis

For each paper, extract:

**Core Information:**
- Research question/hypothesis
- Methodology and approach
- Key findings and results
- Limitations and assumptions
- Citations to related work

**Metadata:**
- Publication date (track evolution)
- Citation count (impact assessment)
- Authors (expertise tracking)
- Venue (quality indicator)

Store in memory using memory-manager skill.

### Phase 3: Cross-Reference Analysis

Compare papers across dimensions:

**Methodology Comparison:**
```
Compare approaches:
- Paper A: Uses transformer architecture
- Paper B: Uses CNN with attention
- Paper C: Novel graph-based approach
Analysis: Trade-offs in computational efficiency vs accuracy
```

**Findings Synthesis:**
```
Synthesize results:
- 3 papers report positive results
- 1 paper reports negative results
- 1 paper inconclusive
Analysis: Investigate conditions causing different outcomes
```

**Citation Network:**
```
Map citation relationships:
- Central paper: Attention is All You Need (most cited)
- Influenced by: Earlier RNN/LSTM papers
- Influences: Recent transformer variants
Analysis: Evolution of architecture design
```

### Phase 4: Gap Identification

Find unanswered questions:

```
Identify gaps:
- No papers address [specific scenario]
- Limited evaluation on [dataset type]
- Missing comparison with [baseline]
- No analysis of [failure mode]
```

### Phase 4.5: Benchmark Aggregation (PaperLantern-Inspired)

Aggregate and compare benchmarks across papers with comparability analysis:

**Step 1: Extract Benchmarks from Each Paper**
```
For each paper, extract:
- Task/benchmark name (e.g., MMLU, ARC-AGI, GSM8K)
- Metric used (accuracy, F1, pass@k, etc.)
- Score achieved
- Model size / compute budget
- Evaluation conditions (few-shot, zero-shot, fine-tuned)
- Dataset version / split used
```

**Step 2: Build Cross-Paper Comparison Table**
```
Benchmark Comparison: [Topic]
                    Paper A     Paper B     Paper C     Comparable?
MMLU (5-shot):      0.89        0.91        0.87        YES - same setup
GSM8K (CoT):        0.78        N/A         0.82        PARTIAL - diff prompts
ARC-AGI:            0.45        0.52        N/A         YES - standard eval
Custom Task:        0.93        0.78        0.85        NO - different metrics
```

**Step 3: Comparability Notes**

For each comparison, assess:
```
Comparability Assessment:
- COMPARABLE: Same benchmark, same metric, same conditions
- PARTIALLY COMPARABLE: Same benchmark but different conditions
  → Note: "Paper A uses 5-shot, Paper B uses 0-shot"
- NOT COMPARABLE: Different benchmarks or metrics
  → Note: "Paper A reports accuracy, Paper C reports F1"
- MISSING: Paper does not evaluate on this benchmark
  → Note: "Gap: No evaluation on safety benchmarks"
```

**Step 4: Aggregated Insights**
```
Cross-Paper Benchmark Summary:
1. Best performing approach: [Method] from Paper [X] (score on key benchmark)
2. Most consistent performer: [Method] (stable across benchmarks)
3. Efficiency-accuracy trade-off: [Method] achieves 95% of best with 50% compute
4. Gaps in evaluation: [List benchmarks missing from most papers]
```

### Phase 4.6: OMEGA-ASI Contextualization

For every synthesis, explicitly map findings to OMEGA-ASI relevance:

**"Why This Matters for OMEGA-ASI" Template:**
```markdown
## OMEGA-ASI Impact Assessment

### Direct Applicability
- **Architecture Component:** Which OMEGA-ASI module does this affect?
  (e.g., attention mechanism, memory system, self-improvement loop, safety layer)
- **Pipeline Stage:** Where in the OMEGA SICAS 9-phase loop is this relevant?
  (e.g., Phase 3: Architecture Design, Phase 7: Safety Verification)
- **Implementation Priority:** [High/Medium/Low] based on current roadmap

### Pipeline-Stage Mapping
Map each synthesized finding to OMEGA SICAS pipeline stages:
| Finding | SICAS Phase | Agent Responsible | Action Required |
|---------|-------------|-------------------|-----------------|
| Finding 1 | Phase 3 (Design) | ARCH-DESIGNER | Evaluate for v5+ |
| Finding 2 | Phase 7 (Safety) | SAFETY-AUDITOR | Add to checklist |
| Finding 3 | Phase 5 (Experiment) | EXPERIMENT-RUNNER | Benchmark test |

### Adoption Recommendation
- **Start with:** [Specific technique] + [Specific technique]
- **Avoid for now:** [Technique] because [reason]
- **Monitor:** [Technique] - promising but needs more validation
```

### Phase 5: Synthesis Report

Generate comprehensive synthesis:

**Structure:**
1. Executive summary
2. Literature landscape overview
3. Methodology comparison matrix
4. Findings synthesis
5. Contradictions and conflicts
6. Research gaps
7. Future directions
8. Recommendations

## Synthesis Patterns

### Pattern 1: Evolution Tracking

Track how ideas evolve over time:

```
Timeline Analysis:
2020: Paper A introduces concept X
2021: Paper B extends X with Y
2022: Paper C challenges X, proposes Z
2023: Paper D reconciles X and Z
2024: Current state: Integration of X, Y, Z

Trend: Progressive refinement with occasional paradigm shifts
```

### Pattern 2: Methodological Convergence

Identify when different approaches converge:

```
Convergence Analysis:
Approach A (NLP) and Approach B (Vision) independently discover:
- Same underlying principle
- Similar architectural patterns
- Comparable performance gains

Insight: Universal principle transcends domain boundaries
```

### Pattern 3: Conflicting Results

Analyze contradictory findings:

```
Conflict Analysis:
Paper X: Method M works well on dataset D
Paper Y: Method M fails on dataset D

Investigate differences:
- Implementation details
- Hyperparameter choices
- Evaluation metrics
- Data preprocessing

Resolution: M is sensitive to [specific condition]
```

### Pattern 4: Citation Clustering

Group papers by citation patterns:

```
Citation Analysis:
Cluster 1: Theoretical foundations (cited by everyone)
Cluster 2: Methodological innovations (moderate citations)
Cluster 3: Application papers (domain-specific)

Insight: Strong theoretical base with active methodology development
```

## Cross-Referencing Techniques

### Technique 1: Matrix Comparison

Create comparison matrices:

```
                    Paper A   Paper B   Paper C   Paper D
Architecture:       Trans.    CNN       Graph     Hybrid
Dataset:            ImageNet  CIFAR     Custom    Mixed
Accuracy:           95.2%     93.1%     94.5%     96.0%
Efficiency:         Medium    High      Low       Medium
Scalability:        High      Medium    Low       High
```

### Technique 2: Citation Graph Analysis

Build and analyze citation networks:

```
Graph Metrics:
- Hub papers (most cited)
- Authority papers (cite many)
- Bridge papers (connect clusters)
- Island papers (isolated)

Analysis:
- Central themes
- Emerging subfields
- Forgotten ideas worth revisiting
```

### Technique 3: Temporal Analysis

Analyze publication timelines:

```
Publication Trends:
2020-2021: Exploratory phase (few papers)
2022: Rapid growth (breakthrough results)
2023: Refinement phase (incremental improvements)
2024: Consolidation (survey papers, benchmarks)

Prediction: Mature field approaching plateau
```

### Technique 4: Author Network

Analyze author collaborations:

```
Author Analysis:
- Key researchers (high output)
- Collaborative clusters
- Institution patterns
- Expertise distribution

Insight: Community structure and knowledge flow
```

## Gap Identification Methods

### Method 1: Question Mapping

Map answered vs unanswered questions:

```
Question Matrix:
                        Q1    Q2    Q3    Q4    Q5
Paper A (2020):         ✓     ✗     ?     ✓     ✗
Paper B (2021):         ✓     ✓     ✗     ✓     ✗
Paper C (2022):         ?     ✓     ✓     ?     ✗
Paper D (2023):         ✓     ?     ✓     ✓     ?

Gaps: Q5 unanswered by all, Q3 partially answered
```

### Method 2: Evaluation Coverage

Check evaluation completeness:

```
Evaluation Matrix:
                    Standard  Robustness  Scalability  Efficiency
Paper A:            ✓         ✗           ✗            ✗
Paper B:            ✓         ✓           ✗            ✓
Paper C:            ✓         ✗           ✓            ✗
Paper D:            ✓         ✓           ✓            ✓

Gaps: Robustness (3/4), Efficiency (2/4)
```

### Method 3: Scenario Coverage

Identify missing scenarios:

```
Scenario Analysis:
                    Low-data  Noisy   Adversarial  Multi-modal
Current papers:     ✓         ✓       ✗            ✗

Gap: Adversarial robustness and multi-modal approaches
```

## Synthesis Report Template

### Executive Summary

```markdown
## Synthesis: [Topic Name]

**Scope:** [Number] papers from [Year Range]
**Key Finding:** [One-sentence summary]
**Confidence:** [High/Medium/Low]

### Main Conclusions
1. [Conclusion 1]
2. [Conclusion 2]
3. [Conclusion 3]

### Critical Gaps
1. [Gap 1]
2. [Gap 2]

### Recommendations
- [Recommendation 1]
- [Recommendation 2]
```

### Detailed Sections

**1. Literature Landscape**
- Number of papers analyzed
- Time distribution
- Venue distribution
- Author diversity

**2. Methodology Comparison**
- Approach taxonomy
- Trade-off analysis
- Innovation timeline

**3. Findings Synthesis**
- Consistent results
- Contradictory results
- Context-dependent results

**4. Gap Analysis**
- Theoretical gaps
- Methodological gaps
- Evaluation gaps
- Application gaps

**5. Future Directions**
- Immediate opportunities
- Long-term challenges
- Emerging trends

## Integration with Memory

Always store synthesis results:

```
1. Create Finding nodes for each synthesis conclusion
2. Create Question nodes for identified gaps
3. Link to all papers used in synthesis
4. Update related Concept nodes
5. Store synthesis report in filesystem
```

## Best Practices

1. **Diverse Sources** - Include papers from different venues/years
2. **Minimum Sample** - Synthesize at least 5 papers for validity
3. **Quality Filter** - Prioritize peer-reviewed, highly-cited work
4. **Date Range** - Include both recent and foundational papers
5. **Bias Check** - Look for author/institution clustering
6. **Quantify When Possible** - Use metrics, not just descriptions
7. **Acknowledge Limitations** - Note scope constraints
8. **Actionable Output** - Provide clear recommendations

## Tools to Use

During synthesis:
1. **neo4j-memory** - Retrieve stored papers and concepts
2. **academia-mcp** - Search for additional papers
3. **sequential-thinking** - Complex reasoning about patterns
4. **memory-manager** - Store synthesis results
5. **knowledge-graph-query** - Explore relationships

## Example Workflows

### Example 1: Transformer Alternatives Synthesis

```
1. Query memory: Find papers on "transformer alternatives"
2. Find 8 papers: 2020-2024 range
3. Extract methodologies:
   - 3 papers: State space models
   - 2 papers: Linear attention
   - 2 papers: Mixture of experts
   - 1 paper: Graph-based
4. Compare performance:
   - State space: Good long sequences
   - Linear attention: Fast but less accurate
   - MoE: Scalable but complex
5. Identify gap: No comparison on AGI-scale tasks
6. Generate synthesis report
7. Store in memory with relationships
```

### Example 2: OMEGA ASI Architecture Evolution

```
1. Query memory: Find all OMEGA_ASI versions
2. Collect papers evaluating each version
3. Track evolution:
   - v100: Baseline transformer
   - v150: Added memory module
   - v200: Multi-agent coordination
   - v300: Physical world interface
4. Identify progression pattern:
   - Increasing modularity
   - Growing complexity
   - Better benchmarks
5. Find gap: Limited safety evaluation
6. Store synthesis as Finding node
```

## Dependencies

This skill integrates with:
- **knowledge-graph-query** - Retrieve papers and concepts
- **memory-manager** - Store synthesis results
- **academia-mcp** - Search external papers
- **neo4j-memory** - Access persistent storage

## Related Skills

- **knowledge-graph-query** - For retrieving literature
- **agi-researcher** - For AGI-specific synthesis
- **experiment-tracker** - For comparing experimental results
- **research-to-implementation** - For translating synthesis into code decisions
- **research-frontier-tracker** - For monitoring when synthesis becomes stale

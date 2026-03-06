---
name: research-to-implementation
description: Bridge research papers to actionable implementation guidance - translates engineering problems into academic queries, synthesizes papers with benchmarks, and generates implementation-ready recommendations for OMEGA-ASI architecture development
author: AGI Research Team
version: 1.0.0
tags: [research, implementation, synthesis, benchmarks, paper-lantern-inspired]
---

# Research-to-Implementation Skill

> **Inspired by [PaperLantern](https://code.paperlantern.ai/)**: This skill bridges the gap between academic research and production implementation. Instead of just finding papers, it translates engineering problems into research-backed solutions with benchmarks, tradeoffs, and implementation details your coding agent can act on immediately.

## Overview

The Research-to-Implementation skill solves the critical disconnect between:
1. **How engineers describe problems** ("our attention mechanism is too slow for long sequences")
2. **How papers describe solutions** ("sub-quadratic sequence modeling via structured state spaces")

It provides a structured pipeline that:
- Detects the current architecture context from the OMEGA-ASI codebase
- Translates engineering problems into multiple academic query framings
- Searches across all available research sources (Semantic Scholar, arXiv, Exa, HuggingFace)
- Synthesizes findings with cross-paper benchmark aggregation
- Generates implementation-ready recommendations with tradeoffs
- Logs all decisions in the Research Decision Log

## When to Use This Skill

Use this skill when you need to:
- Find the best research-backed approach for an engineering problem
- Compare multiple research methods with benchmarks before implementing
- Translate a vague engineering goal into specific techniques
- Verify if a proposed approach has been studied/benchmarked
- Update an existing architecture decision with newer research
- Generate implementation guidance from research papers
- Make architecture decisions backed by empirical evidence

## Core Methodology

### Phase 1: Context Detection

Before searching for research, understand the current engineering context:

```
Context Detection Protocol:
1. Identify the OMEGA-ASI component being worked on
   - Which module? (core/backbone, core/memory, alignment, self_improve, etc.)
   - Which version? (v2, v4/PINNACLE, v5)
   - Current approach? (what's already implemented)

2. Characterize the engineering problem
   - Problem type: [performance | accuracy | scalability | safety | memory | efficiency]
   - Constraints: [compute budget | latency requirements | memory limits | hardware]
   - Quality bar: [research prototype | production-ready | SOTA-competitive]

3. Identify adjacent context
   - What other components interact with this one?
   - What data flows through this component?
   - What are the upstream/downstream dependencies?
```

**Output Format:**
```
CONTEXT: {component} in OMEGA-ASI {version}
CURRENT APPROACH: {brief description of existing implementation}
PROBLEM: {engineering problem in plain language}
CONSTRAINTS: {list of constraints}
PROBLEM TYPE: {classification}
```

### Phase 2: Query Translation (Engineer-speak to Academic-speak)

Translate the engineering problem into multiple academic query framings:

```
Translation Protocol:
For each engineering problem, generate 3-5 academic query variants:

ENGINEERING: "Our attention mechanism is too slow for long sequences"
ACADEMIC QUERIES:
  1. "sub-quadratic attention mechanisms long sequence modeling"
  2. "linear attention alternatives to softmax self-attention"
  3. "efficient transformer architectures O(n) complexity"
  4. "state space models sequence modeling efficiency"
  5. "sparse attention patterns computational efficiency scaling"

ENGINEERING: "The model keeps forgetting earlier context"
ACADEMIC QUERIES:
  1. "long-range dependency preservation in neural networks"
  2. "memory-augmented architectures catastrophic forgetting"
  3. "recurrent memory mechanisms for extended context"
  4. "KV cache compression context retention"
  5. "hierarchical memory systems neural sequence models"
```

**Translation Heuristics:**
| Engineer Term | Academic Equivalents |
|---|---|
| "too slow" | computational complexity, inference latency, throughput |
| "bad accuracy" | evaluation metrics, benchmark performance, generalization |
| "keeps crashing" | numerical stability, gradient flow, training dynamics |
| "runs out of memory" | memory efficiency, activation checkpointing, parameter efficiency |
| "doesn't scale" | scaling laws, distributed computation, parallelism strategies |
| "hallucinates" | factual grounding, calibration, retrieval augmentation |
| "can't reason" | chain-of-thought, compositional generalization, systematic reasoning |
| "alignment issues" | value alignment, RLHF, constitutional AI, reward modeling |
| "not safe enough" | containment, corrigibility, interpretability, adversarial robustness |

### Phase 3: Multi-Source Research Search

Search across ALL available sources with translated queries:

```
Search Protocol (in priority order):

1. NEO4J MEMORY (check existing knowledge first)
   Tool: neo4j-memory_search_memories
   Purpose: Avoid re-searching what we already know
   Query: Each translated query
   
2. SEMANTIC SCHOLAR (academic rigor)
   Tool: AI-Research-Assistant_papers-search-basic
   Purpose: Peer-reviewed papers with citation metrics
   Query: Top 2-3 academic query variants
   Filter: Recent 2 years + seminal papers
   Get: abstracts, citation counts, influence metrics
   
3. ARXIV (cutting edge)
   Tool: AI-Research-Assistant_search-arxiv
   Purpose: Latest preprints not yet in Semantic Scholar
   Query: All academic query variants
   Filter: Last 6 months
   
4. EXA WEB SEARCH (industry implementations)
   Tool: exa_web_search_exa
   Purpose: Blog posts, implementations, benchmarks from industry
   Query: Engineering problem + "implementation" / "benchmark"
   
5. HUGGINGFACE (model cards & benchmarks)
   Tool: huggingface-official_hub_repo_search
   Purpose: Pre-trained models, benchmark results, real implementations
   Query: Relevant model architectures
   
6. CONTEXT7 (library documentation)
   Tool: context7_query-docs
   Purpose: Implementation details for specific libraries
   Query: Framework-specific implementation queries
```

**Source Credibility Hierarchy:**
| Source | Credibility | Best For |
|---|---|---|
| Peer-reviewed papers (ICML, NeurIPS, ICLR) | Highest | Validated methods |
| arXiv preprints | High | Cutting-edge techniques |
| Official model cards (HuggingFace) | High | Benchmark numbers |
| Industry tech blogs (Google AI, Meta AI) | Medium-High | Practical insights |
| Library documentation | Medium | Implementation details |
| General web search | Medium | Community experience |
| Social media / forums | Low | Anecdotal evidence |

### Phase 4: Cross-Paper Benchmark Aggregation

This is where we go beyond simple paper listing. For each relevant paper, extract and compare benchmarks:

```
Benchmark Aggregation Template:

TECHNIQUE COMPARISON: [Problem Domain]
Papers Analyzed: N papers from [date range]

| Technique | Paper(s) | Key Metric | Value | Dataset | Hardware | Notes |
|-----------|----------|------------|-------|---------|----------|-------|
| Method A  | arxiv:XX | Perplexity | 4.2   | WikiText | A100     | SOTA  |
| Method B  | arxiv:YY | Perplexity | 4.5   | WikiText | A100     | 2x faster |
| Method C  | arxiv:ZZ | Perplexity | 4.3   | WikiText | V100     | less memory |
| Baseline  | arxiv:WW | Perplexity | 5.1   | WikiText | A100     | standard |

COMPARABILITY NOTES:
- Methods A and B use same evaluation protocol (comparable)
- Method C uses different hardware (partially comparable)
- Dataset preprocessing differs between A and C (caveat)

AGGREGATE FINDING:
Method A achieves SOTA but Method B offers better speed/quality tradeoff
for our use case given [specific constraint].
```

**Benchmark Extraction Rules:**
1. Always note the dataset and evaluation protocol
2. Flag when different papers use different metrics
3. Distinguish between self-reported and independently reproduced results
4. Note hardware/compute requirements for fair comparison
5. Check if results are statistically significant (confidence intervals, p-values)

### Phase 5: Relevance Scoring for OMEGA-ASI

Score each technique by relevance to our specific architecture:

```
Relevance Scoring Matrix:

| Factor | Weight | Score (0-10) | Weighted |
|--------|--------|-------------|----------|
| Problem fit | 0.30 | ? | ? |
| Benchmark quality | 0.20 | ? | ? |
| Implementation feasibility | 0.20 | ? | ? |
| Compatibility with OMEGA-ASI | 0.15 | ? | ? |
| Recency (< 6 months bonus) | 0.10 | ? | ? |
| Safety implications | 0.05 | ? | ? |
| **TOTAL** | **1.00** | | **?/10** |

Scoring Guidelines:
- Problem fit: Does this directly address our engineering problem?
- Benchmark quality: Reproducible results on standard benchmarks?
- Implementation feasibility: Can we implement this in <1 week?
- Compatibility: Works with Mamba-Transformer hybrid / Active Inference / HD Computing?
- Recency: Published in last 6 months?
- Safety: No alignment concerns? Maintains containment properties?
```

### Phase 6: Implementation Recommendation

Generate the final recommendation in a structured format:

```markdown
## Research-Backed Recommendation: [Problem Title]

**Context:** [OMEGA-ASI component] | [Problem type] | [Constraints]

### Top Recommendation: [Technique Name]
- **Paper:** [arxiv ID] | [Title] | [Authors] | [Date]
- **Why this:** [2-3 sentences explaining fit to our specific context]
- **Key benchmark:** [Most relevant metric] = [value] vs baseline [value]
- **Implementation effort:** [Low/Medium/High] | Estimated [X] days
- **Relevance score:** [X/10]

### Implementation Guide
```python
# Pseudo-implementation or key integration points
# Specific to OMEGA-ASI codebase

# File: workspace/omega_asi_{version}/core/{component}.py
# Integration point: {function/class name}
# Key changes:
#   1. {change 1}
#   2. {change 2}
#   3. {change 3}
```

### Alternative Approaches
| Rank | Technique | Relevance | Tradeoff |
|------|-----------|-----------|----------|
| 2 | [Method B] | X/10 | [key tradeoff] |
| 3 | [Method C] | X/10 | [key tradeoff] |

### What We Explicitly Rejected (and Why)
- [Method D]: [reason for rejection]
- [Method E]: [reason for rejection]

### Synthesis Across Papers
[How recommended techniques can be combined, which address different
stages/aspects of the problem, and in what order to implement them]

### Open Questions
- [Question the research doesn't answer for our case]
- [Experiment we'd need to run to validate]
```

### Phase 7: Decision Logging

Every recommendation MUST be logged. See `workspace/RESEARCH_DECISIONS.md` format:

```
After generating recommendation:
1. Append entry to workspace/RESEARCH_DECISIONS.md
2. Create/update Neo4j entities:
   - ResearchDecision entity with full metadata
   - Link to Paper entities (INFORMED_BY relationship)
   - Link to Architecture entity (APPLIES_TO relationship)
   - Link to Experiment entity if validation planned (VALIDATED_BY relationship)
3. Set decision status: PROPOSED | ACCEPTED | REJECTED | IMPLEMENTED | SUPERSEDED
```

## Multi-Source Research Hierarchy

Different sources serve different purposes. Use them strategically:

```
RESEARCH DEPTH LEVELS:

Level 1: QUICK SCAN (5 minutes)
  → Neo4j memory check
  → 1 Semantic Scholar query
  → 1 Exa search
  Outputs: 3-5 relevant papers, quick recommendation

Level 2: STANDARD RESEARCH (15 minutes)
  → Neo4j memory check
  → 3 Semantic Scholar queries (translated variants)
  → 2 arXiv searches (recent + seminal)
  → 1 Exa search (industry)
  → 1 HuggingFace search (models)
  Outputs: 8-15 papers, benchmark comparison, recommendation

Level 3: DEEP DIVE (30+ minutes)
  → Full Neo4j graph traversal
  → 5 Semantic Scholar queries + citation network analysis
  → 3 arXiv searches + reference chasing
  → 2 Exa searches (industry + benchmarks)
  → HuggingFace model exploration
  → Context7 implementation docs
  Outputs: 20+ papers, full benchmark matrix, detailed recommendation
           with implementation guide and validation plan

Default: Level 2 for most architecture decisions
Use Level 3 for: new components, paradigm shifts, safety-critical changes
Use Level 1 for: incremental improvements, known problem domains
```

## Integration with Neo4j Memory

### Entity Schema

```cypher
(:ResearchDecision {
  id: "RD-{YYYYMMDD}-{short_name}",
  problem: "engineering problem description",
  context: "OMEGA-ASI component and version",
  recommended_technique: "technique name",
  relevance_score: 8.5,
  status: "PROPOSED",  // PROPOSED | ACCEPTED | REJECTED | IMPLEMENTED | SUPERSEDED
  decision_date: datetime(),
  implementation_date: null,
  outcome: null,
  notes: "additional context"
})

// Relationships
(:ResearchDecision)-[:INFORMED_BY {relevance: 0.9}]->(:Paper)
(:ResearchDecision)-[:APPLIES_TO]->(:Architecture)
(:ResearchDecision)-[:SUPERSEDES]->(:ResearchDecision)
(:ResearchDecision)-[:VALIDATED_BY]->(:Experiment)
(:ResearchDecision)-[:REJECTED_ALTERNATIVE {reason: "..."}]->(:Paper)
```

### Query Patterns

```cypher
// Find all decisions for a component
MATCH (rd:ResearchDecision)-[:APPLIES_TO]->(a:Architecture)
WHERE a.name CONTAINS "v2" AND rd.status = "IMPLEMENTED"
RETURN rd.id, rd.recommended_technique, rd.outcome

// Find decisions that may need updating (older than 6 months)
MATCH (rd:ResearchDecision)
WHERE rd.decision_date < datetime() - duration({months: 6})
AND rd.status IN ["ACCEPTED", "IMPLEMENTED"]
RETURN rd.id, rd.problem, rd.recommended_technique

// Find papers that informed multiple decisions
MATCH (p:Paper)<-[:INFORMED_BY]-(rd:ResearchDecision)
WITH p, count(rd) as decision_count
WHERE decision_count > 1
RETURN p.title, decision_count ORDER BY decision_count DESC

// Trace decision lineage
MATCH path = (rd1:ResearchDecision)-[:SUPERSEDES*]->(rd2:ResearchDecision)
WHERE rd1.id = "RD-20260228-attention"
RETURN path
```

## Example Workflows

### Example 1: Improving OMEGA-ASI Attention Efficiency

```
PROBLEM: "Attention in omega_asi_v2 backbone is O(n^2), limiting context to 8K tokens"

Phase 1 - Context:
  CONTEXT: core/hybrid_backbone.py in OMEGA-ASI v2
  CURRENT: Standard multi-head attention with Flash Attention v2
  PROBLEM: Quadratic scaling prevents >8K context
  CONSTRAINTS: Must maintain >95% accuracy on existing benchmarks
  TYPE: performance + scalability

Phase 2 - Query Translation:
  1. "sub-quadratic attention alternatives transformer efficiency"
  2. "linear attention mechanisms long context modeling 2025 2026"
  3. "state space models Mamba hybrid attention architectures"
  4. "sparse attention patterns efficient sequence modeling"
  5. "sliding window attention grouped query attention scaling"

Phase 3 - Search across all sources... [executed]

Phase 4 - Benchmark Aggregation:
  | Technique | Perplexity | Speed (vs baseline) | Max Context |
  |-----------|-----------|---------------------|-------------|
  | Mamba-2 SSD | 4.1 | 3.2x faster | 128K+ |
  | Linear Attention | 4.5 | 4x faster | unlimited |
  | Sliding Window + GQA | 4.2 | 2.5x faster | 32K |
  | Baseline (MHA) | 4.0 | 1x | 8K |

Phase 5 - Relevance Scoring:
  Mamba-2 SSD: 9.2/10 (already partially in v4 PINNACLE)
  Sliding Window + GQA: 7.8/10 (simpler, proven)
  Linear Attention: 6.5/10 (quality tradeoff too high)

Phase 6 - Recommendation:
  TOP: Mamba-2 SSD hybrid (combine with existing attention for critical layers)
  WHY: Already validated in our v4 PINNACLE architecture, 3.2x speed with
       minimal quality loss, proven at 128K+ context
  ALTERNATIVE: Sliding Window + GQA for simpler initial implementation

Phase 7 - Logged to RESEARCH_DECISIONS.md and Neo4j
```

### Example 2: Finding Better Self-Improvement Safety Bounds

```
PROBLEM: "Darwin-Godel machine mutation bounds feel arbitrary (10% max change)"

Phase 1 - Context:
  CONTEXT: self_improve/darwin_godel.py in OMEGA-ASI v2
  CURRENT: Fixed 10% parameter change limit, 5 iterations/session
  PROBLEM: No empirical basis for safety bounds
  TYPE: safety + meta-learning

Phase 2 - Query Translation:
  1. "safe self-modification bounds neural networks empirical"
  2. "evolutionary self-improvement convergence guarantees"
  3. "parameter perturbation stability neural architecture"
  4. "self-play training safety constraints scaling"
  5. "iterated amplification safe capability improvement"

[... continues through all phases ...]
```

## Best Practices

1. **Always start with Neo4j** - Check what we already know before searching externally
2. **Multiple query framings** - Never search with just one query; translate engineer-speak
3. **Benchmark over claims** - Trust numbers over prose; aggregate across papers
4. **Note comparability** - Always flag when benchmarks use different setups
5. **Context is king** - Score relevance to OUR specific architecture, not general applicability
6. **Log every decision** - Even rejected alternatives are valuable knowledge
7. **Date everything** - Research has a half-life; track when findings were current
8. **Validate before implementing** - Design a quick experiment to verify the recommendation
9. **Check for contradictions** - If papers disagree, understand why before picking a side
10. **Compound knowledge** - Link new decisions to old ones; build on what we've learned

## Tools Used

| Tool | Phase | Purpose |
|------|-------|---------|
| neo4j-memory | 1, 3, 7 | Context check, existing knowledge, decision storage |
| AI-Research-Assistant | 3 | Semantic Scholar search, citation analysis |
| exa_web_search_exa | 3 | Industry implementations, benchmarks |
| huggingface-official | 3 | Model benchmarks, pre-trained weights |
| context7 | 3, 6 | Library docs, implementation details |
| sequential-thinking | 4, 5 | Analysis, scoring, synthesis |
| filesystem | 7 | Write to RESEARCH_DECISIONS.md |

## Dependencies

This skill integrates with:
- **paper-synthesis** - For cross-paper analysis (Phase 4)
- **memory-manager** - For Neo4j storage (Phase 7)
- **agi-hypothesis-generator** - When recommendations become testable hypotheses
- **experiment-tracker** - For validation experiments
- **safety-alignment-researcher** - For safety-critical decisions
- **evaluation-framework** - For benchmark validation

## Related Skills

- **paper-synthesis** - Provides the synthesis methodology we build upon
- **semantic-scholar-search** - Powers the academic search phase
- **arxiv-search** - Provides arXiv-specific search
- **benchmark-creator** - For designing validation benchmarks
- **code-generation-advanced** - For implementing recommendations

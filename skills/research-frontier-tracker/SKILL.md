---
name: research-frontier-tracker
description: Monitor and track the frontier of AGI-relevant research - detect emerging trends, flag superseded decisions, and maintain a living map of the research landscape for OMEGA-ASI development
author: AGI Research Team
version: 1.0.0
tags: [research, trends, monitoring, frontier, paper-lantern-inspired]
---

# Research Frontier Tracker Skill

> **Inspired by PaperLantern's "Trend Spotting"**: This skill goes beyond paper search to actively monitor the research frontier, detect emerging trends before they become mainstream, and flag when our existing architecture decisions may be outdated.

## Overview

The Research Frontier Tracker maintains a living map of the AGI research landscape. It:
1. Monitors key research areas for new developments
2. Detects emerging trends and paradigm shifts early
3. Flags when stored decisions may be superseded by newer research
4. Tracks the competitive landscape of AGI architectures
5. Identifies cross-domain breakthroughs applicable to OMEGA-ASI

## When to Use This Skill

Use this skill when you need to:
- Start a new research session (run frontier check first)
- Determine if existing architecture decisions are still current
- Identify what's changed in a specific research area since last check
- Discover cross-domain techniques applicable to AGI
- Assess whether a "new" idea has already been explored
- Track competitors and alternative AGI approaches
- Plan next research priorities based on frontier movements

## Core Methodology

### Frontier Monitoring Protocol

#### Step 1: Define Watch Areas

Maintain a list of research areas critical to OMEGA-ASI:

```yaml
OMEGA-ASI Frontier Watch List:

CORE_ARCHITECTURE:
  - query: "state space models transformer hybrid architectures"
    component: core/hybrid_backbone.py
    last_checked: null
    known_sota: "Mamba-2 SSD + selective attention"
    
  - query: "active inference free energy principle neural networks"
    component: core/active_inference.py
    last_checked: null
    known_sota: "variational free energy minimization"
    
  - query: "hyperdimensional computing vector symbolic architectures"
    component: core/hd_computing.py
    last_checked: null
    known_sota: "MAP-Elites + VSA binding"

MEMORY_SYSTEMS:
  - query: "hierarchical memory neural architectures episodic semantic"
    component: core/memory
    last_checked: null
    known_sota: "Titans + Infini-Attention + Product-Key Memory"
    
  - query: "memory consolidation replay neural networks continual learning"
    component: core/memory
    last_checked: null
    known_sota: "hippocampal-neocortical transfer"

SELF_IMPROVEMENT:
  - query: "self-improving AI systems safe self-modification"
    component: self_improve/darwin_godel.py
    last_checked: null
    known_sota: "evolutionary self-improvement with rollback"
    
  - query: "neural architecture search automated ML efficiency"
    component: self_improve/
    last_checked: null
    known_sota: "DARTS + hardware-aware NAS"

ALIGNMENT_SAFETY:
  - query: "AI alignment scalable oversight interpretability"
    component: alignment/
    last_checked: null
    known_sota: "Constitutional AI + RLHF"
    
  - query: "AI containment corrigibility shutdown problem"
    component: alignment/
    last_checked: null
    known_sota: "containment levels L0-L4"

SCALING_EFFICIENCY:
  - query: "mixture of experts sparse activation efficient scaling"
    component: core/moe
    last_checked: null
    known_sota: "Ultra-Fine MoE 96%+ sparsity"
    
  - query: "ternary quantization 1-bit LLM efficient inference"
    component: core/bitnet
    last_checked: null
    known_sota: "BitNet b1.58 ternary weights"

REASONING:
  - query: "chain of thought reasoning scaling inference compute"
    component: core/reasoning
    last_checked: null
    known_sota: "test-time compute scaling + MCTS"
    
  - query: "world models predictive coding causal reasoning"
    component: core/world_model.py
    last_checked: null
    known_sota: "predictive coding + causal discovery"

EMERGING_PARADIGMS:
  - query: "neuromorphic computing spiking neural networks AGI"
    component: future
    last_checked: null
    known_sota: null
    
  - query: "quantum machine learning hybrid quantum-classical"
    component: future
    last_checked: null
    known_sota: null
    
  - query: "consciousness artificial systems integrated information theory"
    component: future
    last_checked: null
    known_sota: null
```

#### Step 2: Frontier Scan Execution

For each watch area, run a structured scan:

```
Frontier Scan Protocol:

1. RECALL: Query Neo4j for last scan results on this area
   → What was SOTA last time?
   → When was the last scan?
   → What papers were known?

2. SEARCH: Run queries across sources (recent 3-6 months only)
   → Semantic Scholar: sorted by citation velocity
   → arXiv: sorted by submission date
   → Exa: "latest" + "breakthrough" + area terms
   → HuggingFace: trending models in category

3. COMPARE: Diff new results against stored knowledge
   → New papers not in our Neo4j?
   → New benchmarks exceeding our stored SOTA?
   → New techniques we haven't evaluated?
   → Papers contradicting our assumptions?

4. ASSESS: Classify each finding
   → INCREMENTAL: Small improvement, no action needed
   → SIGNIFICANT: Notable advance, should evaluate
   → PARADIGM_SHIFT: Fundamentally changes approach, urgent review
   → VALIDATES: Confirms our current approach
   → CONTRADICTS: Challenges our assumptions

5. OUTPUT: Generate frontier report
```

#### Step 3: Staleness Detection

Check if any existing decisions are potentially outdated:

```
Staleness Check Protocol:

1. Query all ResearchDecision entities with status IMPLEMENTED or ACCEPTED
2. For each decision older than 3 months:
   a. Search for newer papers on the same topic
   b. Check if any newer techniques outperform the chosen one
   c. Check if the chosen technique has known issues discovered since decision
3. Flag decisions as:
   → CURRENT: Still best available approach
   → REVIEW_RECOMMENDED: Newer alternatives exist, worth evaluating
   → LIKELY_OUTDATED: Significantly better approaches published
   → SUPERSEDED: Clear replacement available
```

### Frontier Report Format

```markdown
## Frontier Report: [Date]

### Summary
- Areas scanned: X
- New significant papers: Y
- Stale decisions detected: Z
- Paradigm shifts: W

### Area: [Research Area Name]
**Component:** {OMEGA-ASI component}
**Last SOTA:** {what we knew}
**Current SOTA:** {what's new}
**Delta:** {improvement or change description}

#### New Papers of Note
| Paper | Date | Key Contribution | Impact Level | Action |
|-------|------|-----------------|--------------|--------|
| arxiv:XXXX | Jan 2026 | New method Y | SIGNIFICANT | Evaluate |
| arxiv:YYYY | Feb 2026 | Scaling law Z | INCREMENTAL | Monitor |

#### Stale Decision Alerts
| Decision ID | Original Date | Technique | Issue | Recommended Action |
|-------------|--------------|-----------|-------|-------------------|
| RD-20250815-attention | Aug 2025 | Flash Attention v2 | v3 released | REVIEW_RECOMMENDED |

### Cross-Domain Discoveries
Papers from outside our primary watch areas that may apply:
- [Paper title]: Originally for [domain], applicable to our [component] because [reason]

### Research Priority Update
Based on frontier movements, recommended priority changes:
1. [Area X]: Priority UP (paradigm shift detected)
2. [Area Y]: Priority DOWN (mature, incremental only)
3. [Area Z]: NEW priority (emerging opportunity)
```

## Frontier Metrics

Track these metrics over time to understand research velocity:

```
Frontier Velocity Metrics:

1. Paper Rate: New relevant papers per month per watch area
2. SOTA Turnover: How often the best-known technique changes
3. Citation Velocity: Rate of citation accumulation for key papers
4. Convergence Index: Are methods converging or diverging?
5. Our Staleness Score: Average age of our implemented decisions
6. Coverage Ratio: % of known techniques we've evaluated
```

## Integration with Neo4j Memory

### Entity Schema

```cypher
(:FrontierScan {
  id: "FS-{YYYYMMDD}",
  date: datetime(),
  areas_scanned: ["list of areas"],
  new_papers_found: 15,
  stale_decisions: 2,
  paradigm_shifts: 0,
  summary: "brief summary"
})

(:FrontierWatch {
  area: "research area name",
  query: "primary search query",
  component: "OMEGA-ASI component",
  last_checked: datetime(),
  known_sota: "current best known technique",
  paper_rate: 5.2,  // papers per month
  convergence: "converging"  // converging | diverging | stable
})

(:TrendAlert {
  id: "TA-{YYYYMMDD}-{short_name}",
  area: "research area",
  level: "SIGNIFICANT",  // INCREMENTAL | SIGNIFICANT | PARADIGM_SHIFT
  description: "what changed",
  papers: ["arxiv IDs"],
  action_required: true,
  resolved: false
})

// Relationships
(:FrontierScan)-[:SCANNED]->(:FrontierWatch)
(:FrontierScan)-[:DETECTED]->(:TrendAlert)
(:TrendAlert)-[:AFFECTS]->(:ResearchDecision)
(:TrendAlert)-[:REFERENCES]->(:Paper)
(:FrontierWatch)-[:MONITORS]->(:Architecture)
```

### Automated Queries

```cypher
// Find all unresolved trend alerts
MATCH (ta:TrendAlert)
WHERE ta.resolved = false AND ta.action_required = true
RETURN ta ORDER BY ta.level DESC, ta.id DESC

// Find watch areas not checked in 30+ days
MATCH (fw:FrontierWatch)
WHERE fw.last_checked < datetime() - duration({days: 30})
RETURN fw.area, fw.component, fw.last_checked

// Find decisions affected by trend alerts
MATCH (ta:TrendAlert)-[:AFFECTS]->(rd:ResearchDecision)
WHERE ta.resolved = false
RETURN rd.id, rd.recommended_technique, ta.description, ta.level

// Frontier velocity by area
MATCH (fs:FrontierScan)-[:SCANNED]->(fw:FrontierWatch)
WHERE fs.date > datetime() - duration({months: 3})
RETURN fw.area, avg(fs.new_papers_found) as avg_papers, 
       count(fs) as scans ORDER BY avg_papers DESC
```

## Session Start Protocol

Run this at the beginning of every research session:

```
QUICK FRONTIER CHECK (2-3 minutes):

1. neo4j-memory: Read all unresolved TrendAlerts
   → Are there urgent items to address?

2. neo4j-memory: Check FrontierWatch staleness
   → Any areas not checked in 30+ days?

3. For the most stale area:
   → Quick arXiv search (last 30 days)
   → Quick Semantic Scholar search
   → Any new significant papers?

4. Update session priorities based on findings

OUTPUT: "Frontier is [STABLE / SHIFTING / URGENT]"
  → If URGENT: Address trend alert before other work
  → If SHIFTING: Note for discussion, continue planned work
  → If STABLE: Proceed with planned research
```

## AGI Competitive Landscape Tracking

Monitor alternative AGI projects and architectures:

```yaml
Competitive Watch:
  - name: "DeepMind Gemini"
    queries: ["Gemini architecture advances", "Google DeepMind AGI"]
    last_checked: null
    
  - name: "OpenAI GPT Series"
    queries: ["GPT-5 architecture", "OpenAI reasoning scaling"]
    last_checked: null
    
  - name: "Anthropic Claude"
    queries: ["Anthropic constitutional AI advances", "Claude architecture"]
    last_checked: null
    
  - name: "Meta LLaMA"
    queries: ["LLaMA architecture improvements", "Meta AI open source LLM"]
    last_checked: null
    
  - name: "Open Source AGI"
    queries: ["open source AGI projects", "community AGI architectures"]
    last_checked: null
    
  - name: "Neuromorphic AGI"
    queries: ["neuromorphic AGI approaches", "brain-inspired computing AGI"]
    last_checked: null
```

## Best Practices

1. **Regular scanning** - Check frontier at least once per research session
2. **Prioritize paradigm shifts** - These demand immediate attention
3. **Track velocity not just state** - How fast is a field moving matters
4. **Cross-pollinate** - Best ideas often come from adjacent fields
5. **Be skeptical of hype** - Not every "breakthrough" paper holds up
6. **Maintain the watch list** - Add/remove areas as OMEGA-ASI evolves
7. **Link alerts to decisions** - Every trend should map to affected decisions
8. **Quantify impact** - Use benchmark comparisons, not just qualitative claims
9. **Archive resolved alerts** - Keep history for pattern analysis
10. **Share findings** - Store in Neo4j so all agents benefit

## Tools Used

| Tool | Purpose |
|------|---------|
| neo4j-memory | Store/retrieve frontier state, alerts, decisions |
| AI-Research-Assistant | Semantic Scholar paper velocity tracking |
| exa_web_search_exa | Industry trend detection |
| huggingface-official | Model landscape tracking |
| sequential-thinking | Trend analysis and impact assessment |

## Dependencies

This skill integrates with:
- **research-to-implementation** - Frontier findings feed into implementation decisions
- **paper-synthesis** - For deep analysis of frontier papers
- **memory-manager** - For Neo4j storage
- **agi-researcher** - For research priority setting
- **safety-alignment-researcher** - For safety frontier monitoring

## Related Skills

- **research-to-implementation** - Acts on frontier findings
- **agi-hypothesis-generator** - Frontier gaps become hypotheses
- **paper-synthesis** - Cross-references frontier papers
- **evaluation-framework** - Benchmarks frontier claims

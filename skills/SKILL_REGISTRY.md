# AGI/ASI Research Agent Skills Registry

## Overview

This registry documents all available skills for the AGI/ASI research agent. Each skill provides specialized capabilities for autonomous research, experimentation, and development of artificial general intelligence systems, specifically the OMEGA ASI architecture.

**Total Skills: 26**
- **Original Skills:** 10
- **Enhanced Skills (2024-2025):** 14
- **PaperLantern-Inspired Skills (2026):** 2

---

## Quick Reference

| Category | Skill | Primary Function |
|----------|-------|------------------|
| **Research** | agi-researcher | Core AGI research methodologies |
| **Research** | agi-hypothesis-generator | Generate and prioritize hypotheses |
| **Research** | paper-synthesis | Cross-reference papers, find patterns |
| **Search** | arxiv-search | Search arXiv preprints |
| **Search** | semantic-scholar-search | Search Semantic Scholar API |
| **Data** | knowledge-graph-query | Query Neo4j knowledge graph |
| **Data** | memory-manager | Manage persistent memory |
| **Experiment** | experiment-tracker | Track ML experiments |
| **Experiment** | benchmark-creator | Create custom benchmarks |
| **Meta** | meta-learning-protocol | Self-improvement workflows |
| **Safety** | safety-alignment-researcher | Alignment and containment |
| **Interpretability** | mechanistic-interpretability | Understand model internals |
| **Architecture** | neural-architecture-search | Automated architecture design |
| **Architecture** | cognitive-architecture | Cognitive system design |
| **Orchestration** | multi-agent-orchestrator | Multi-agent coordination |
| **Reasoning** | advanced-reasoning | CoT, ToT, GoT techniques |
| **Training** | knowledge-distillation | Model compression, capability transfer |
| **Training** | distributed-training | Multi-GPU/node training strategies |
| **Evaluation** | evaluation-framework | AGI benchmarks and assessment |
 | **Context** | long-context-processing | Extend context windows, efficient attention |
| **Memory** | advanced-memory-system | Brain-inspired episodic/semantic/procedural memory (10000x human capacity) |
| **Orchestration** | tool-use-learner | Autonomous tool discovery, learning, and orchestration |
| **Modeling** | world-model-builder | Predictive world models, causal discovery, and simulation |
| **Code** | code-generation-advanced | Multi-file code generation, refactoring, and testing |
| **Research** | research-to-implementation | Bridge research papers to implementation-ready decisions |
| **Research** | research-frontier-tracker | Monitor research frontiers, detect stale decisions |
| 
---

## Skill Categories

### 1. Research Skills

#### agi-researcher
**Path:** `skills/agi-researcher/SKILL.md`
**Purpose:** Core AGI research methodologies including literature review, capability evaluation, and safety analysis.

**Key Capabilities:**
- Structured research workflows
- Capability gap analysis
- Safety assessment protocols
- Research documentation standards

**Integrates With:** agi-hypothesis-generator, paper-synthesis, safety-alignment-researcher

---

#### agi-hypothesis-generator
**Path:** `skills/agi-hypothesis-generator/SKILL.md`
**Purpose:** Generate and prioritize research hypotheses with Neo4j integration for tracking.

**Key Capabilities:**
- Hypothesis generation from research gaps
- Priority scoring (impact × feasibility × novelty)
- Evidence tracking and updating
- Neo4j persistence

**Integrates With:** agi-researcher, experiment-tracker, knowledge-graph-query

---

#### paper-synthesis
**Path:** `skills/paper-synthesis/SKILL.md`
**Purpose:** Cross-reference academic papers to identify patterns, contradictions, and research gaps.

**Key Capabilities:**
- Multi-paper comparison
- Methodology extraction
- Gap identification
- Citation network analysis

**Integrates With:** arxiv-search, semantic-scholar-search, agi-hypothesis-generator

---

### 2. Search Skills

#### arxiv-search
**Path:** `skills/arxiv-search/SKILL.md`
**Implementation:** `skills/arxiv-search/arxiv_search.py`
**Purpose:** Search arXiv preprints using the arXiv API.

**Key Capabilities:**
- Query construction (title, author, abstract, category)
- Result parsing and formatting
- Category filtering (cs.AI, cs.LG, cs.CL, etc.)
- Python script for automation

**Integrates With:** paper-synthesis, semantic-scholar-search, memory-manager

---

#### semantic-scholar-search
**Path:** `skills/semantic-scholar-search/SKILL.md`
**Purpose:** Search Semantic Scholar for papers, authors, and citation analysis.

**Key Capabilities:**
- Paper and author search
- Citation and reference traversal
- Influence metrics (h-index, citation velocity)
- Batch paper lookups

**Integrates With:** arxiv-search, paper-synthesis, knowledge-graph-query

---

### 3. Data Management Skills

#### knowledge-graph-query
**Path:** `skills/knowledge-graph-query/SKILL.md`
**Purpose:** Query the Neo4j knowledge graph for stored research findings.

**Key Capabilities:**
- Cypher query construction
- Path finding between concepts
- Aggregation and analytics
- Schema exploration

**Integrates With:** memory-manager, agi-researcher, all skills that store data

---

#### memory-manager
**Path:** `skills/memory-manager/SKILL.md`
**Purpose:** Manage persistent memory in Neo4j, store findings, create relationships.

**Key Capabilities:**
- Entity creation (Paper, Concept, Experiment, etc.)
- Relationship management
- Observation tracking
- Memory search and retrieval

**Integrates With:** knowledge-graph-query, all research and experiment skills

---

### 4. Experimentation Skills

#### experiment-tracker
**Path:** `skills/experiment-tracker/SKILL.md`
**Purpose:** Track machine learning experiments including configurations, metrics, and results.

**Key Capabilities:**
- Experiment logging
- Hyperparameter tracking
- Metric visualization
- Result comparison

**Integrates With:** benchmark-creator, neural-architecture-search, memory-manager

---

#### benchmark-creator
**Path:** `skills/benchmark-creator/SKILL.md`
**Purpose:** Create custom benchmarks for evaluating AGI capabilities.

**Key Capabilities:**
- Benchmark specification
- Test case generation
- Scoring rubrics
- Performance tracking

**Integrates With:** experiment-tracker, safety-alignment-researcher, agi-researcher

---

### 5. Meta-Learning Skills

#### meta-learning-protocol
**Path:** `skills/meta-learning-protocol/SKILL.md`
**Purpose:** Self-improvement workflows and capability expansion with safety constraints.

**Key Capabilities:**
- Capability assessment
- Learning curriculum design
- Safety-bounded self-modification
- Progress tracking

**Integrates With:** safety-alignment-researcher, experiment-tracker, cognitive-architecture

---

### 6. Safety & Alignment Skills (NEW)

#### safety-alignment-researcher
**Path:** `skills/safety-alignment-researcher/SKILL.md`
**Purpose:** Comprehensive safety research including alignment verification, containment, and red-teaming.

**Key Capabilities:**
- Alignment verification checklists
- Containment level protocols (L0-L4)
- Red-teaming attack vectors
- Safety benchmark suite
- Value alignment methods (Constitutional AI, RLHF)
- Escalation procedures (5 levels)
- Corrigibility testing

**Neo4j Schema:**
```cypher
(:SafetyAssessment {id, architecture, level, passed, concerns, timestamp})
(:ContainmentConfig {level, sandboxing, monitoring, shutdownLatency})
(:RedTeamResult {attack, success, mitigation, severity})
```

**Integrates With:** All skills (safety is cross-cutting)

---

### 7. Interpretability Skills (NEW)

#### mechanistic-interpretability
**Path:** `skills/mechanistic-interpretability/SKILL.md`
**Purpose:** Understand model internals through circuit discovery, feature analysis, and activation patching.

**Key Capabilities:**
- Activation patching methodology
- Sparse Autoencoder (SAE) training
- Logit Lens / Tuned Lens analysis
- Circuit discovery and validation
- TransformerLens integration
- Safety-relevant feature identification

**Neo4j Schema:**
```cypher
(:Circuit {name, function, layers, heads, validated})
(:Feature {id, description, activation_pattern, sae_index})
(:AttentionHead {layer, head, function, importance})
```

**Integrates With:** safety-alignment-researcher, cognitive-architecture, neural-architecture-search

---

### 8. Architecture Design Skills (NEW)

#### neural-architecture-search
**Path:** `skills/neural-architecture-search/SKILL.md`
**Purpose:** Automated neural architecture design using evolutionary, gradient-based, and multi-agent methods.

**Key Capabilities:**
- Search space definition (macro, cell, hierarchical)
- Search strategies (RL, evolutionary, DARTS, Bayesian)
- Performance estimation methods
- NADER framework (multi-agent NAS)
- Hardware-aware NAS
- Carbon-efficient NAS (CE-NAS)
- Transformer search spaces

**Neo4j Schema:**
```cypher
(:NASExperiment {id, searchSpace, strategy, bestArch, fitness})
(:Architecture {genes, performance, parameters, latency})
(:SearchSpace {type, operations, constraints})
```

**Integrates With:** experiment-tracker, benchmark-creator, safety-alignment-researcher

---

#### cognitive-architecture
**Path:** `skills/cognitive-architecture/SKILL.md`
**Purpose:** Design cognitive systems using established frameworks (OpenCog, SOAR, ACT-R) and novel approaches.

**Key Capabilities:**
- OpenCog Hyperon (Atomspace, MeTTa, PLN, MOSES, ECAN, NARS)
- SOAR architecture (production system, decision cycle)
- ACT-R (hybrid symbolic-subsymbolic)
- Neural-symbolic integration
- PRIMUS architecture
- Cognitive cycle design (8 phases)
- Memory systems (working, episodic, semantic, procedural)
- Autopoietic/self-modifying systems

**Neo4j Schema:**
```cypher
(:CognitiveArchitecture {name, type, components, capabilities})
(:CognitiveModule {name, function, inputs, outputs})
(:MemorySystem {type, capacity, decayRate, retrieval})
```

**Integrates With:** multi-agent-orchestrator, mechanistic-interpretability, meta-learning-protocol

---

### 9. Multi-Agent Skills (NEW)

#### multi-agent-orchestrator
**Path:** `skills/multi-agent-orchestrator/SKILL.md`
**Purpose:** Coordinate multiple AI agents using various orchestration patterns and protocols.

**Key Capabilities:**
- Agent taxonomy (by autonomy, role, organization)
- 5 orchestration patterns (sequential, parallel, hierarchical, mesh, swarm)
- Communication protocols (MCP, A2A)
- Task allocation strategies
- Consensus mechanisms (voting, BFT)
- DEPART framework (NeurIPS 2024)
- Emergence detection
- Failure prevention

**Neo4j Schema:**
```cypher
(:MultiAgentSystem {id, pattern, agents, protocol})
(:Agent {id, role, capabilities, autonomyLevel})
(:Interaction {source, target, messageType, timestamp})
```

**Integrates With:** cognitive-architecture, safety-alignment-researcher, experiment-tracker

---

### 10. Reasoning Skills (NEW)

#### advanced-reasoning
**Path:** `skills/advanced-reasoning/SKILL.md`
**Purpose:** Implement advanced reasoning techniques for complex problem-solving.

**Key Capabilities:**
- Chain-of-Thought (Zero-shot, Few-shot, Auto-CoT)
- Tree-of-Thought (BFS, DFS, Best-first, MCTS)
- Graph-of-Thought (Generate, Aggregate, Refine)
- Self-Consistency with voting
- CPO (Chain of Preference Optimization)
- Reasoning benchmarks (GSM8K, MATH, ARC)
- Inference-time scaling

**Neo4j Schema:**
```cypher
(:ReasoningTrace {id, method, problem, steps, solution, correct})
(:ThoughtNode {id, content, score, parent, children})
(:ReasoningExperiment {method, benchmark, accuracy, tokens})
```

**Integrates With:** cognitive-architecture, benchmark-creator, experiment-tracker

---

### 11. Training Skills (NEW)

#### knowledge-distillation
**Path:** `skills/knowledge-distillation/SKILL.md`
**Purpose:** Compress large models while preserving capabilities through distillation techniques.

**Key Capabilities:**
- White-box distillation (logit, feature, attention-based)
- Black-box distillation (response, CoT, API-based)
- On-Policy Self-Distillation (OPSD)
- Domain-specific distillation (DDK)
- Difficulty-aware distillation (DA-KD)
- Multi-teacher distillation
- Dataset distillation and coreset selection
- Progressive and curriculum distillation

**Neo4j Schema:**
```cypher
(:DistillationExperiment {id, method, teacher, student, retention})
(:TeacherModel {name, parameters, capabilities})
(:StudentModel {name, parameters, compression_ratio})
```

**Integrates With:** benchmark-creator, experiment-tracker, safety-alignment-researcher

---

#### distributed-training
**Path:** `skills/distributed-training/SKILL.md`
**Purpose:** Scale training across multiple GPUs and nodes using parallelism strategies.

**Key Capabilities:**
- Data Parallelism (DDP)
- Fully Sharded Data Parallel (FSDP)
- DeepSpeed ZeRO (stages 1-3, Infinity)
- Tensor Parallelism (TP)
- Pipeline Parallelism (PP)
- 3D Parallelism (DP + TP + PP)
- Gradient accumulation and checkpointing
- Mixed precision training

**Neo4j Schema:**
```cypher
(:TrainingRun {id, parallelism_strategy, gpus, throughput})
(:ClusterConfig {nodes, gpus_per_node, interconnect})
(:ParallelismConfig {dp_size, tp_size, pp_size, zero_stage})
```

**Integrates With:** experiment-tracker, neural-architecture-search, benchmark-creator

---

### 12. Evaluation Skills (NEW)

#### evaluation-framework
**Path:** `skills/evaluation-framework/SKILL.md`
**Purpose:** Comprehensive AGI/ASI evaluation across multiple capability dimensions.

**Key Capabilities:**
- Standard benchmarks (MMLU, ARC-AGI, HumanEval, SWE-bench)
- Reasoning benchmarks (MATH, GSM8K, LogiQA)
- Agent benchmarks (GAIA, WebArena)
- Safety evaluations (TruthfulQA, harmlessness)
- Custom benchmark design
- AGI capability assessment protocol
- Metrics and aggregation (pass@k, calibration)
- Leaderboard tracking

**Neo4j Schema:**
```cypher
(:EvaluationRun {id, model, timestamp})
(:Benchmark {name, category, num_tasks})
(:BenchmarkResult {accuracy, pass_at_k, cost_per_task})
(:CapabilityAssessment {dimension, level, score})
```

**Integrates With:** benchmark-creator, safety-alignment-researcher, experiment-tracker

---

### 13. Context Processing Skills (NEW)

#### long-context-processing
**Path:** `skills/long-context-processing/SKILL.md`
**Purpose:** Extend and efficiently process long context windows for LLMs.

**Key Capabilities:**
- RoPE extensions (Position Interpolation, NTK, YaRN, LongRoPE)
- Efficient attention (Ring Attention, sparse patterns, Flash Attention)
- KV cache optimization (paged, streaming)
- Hierarchical memory architectures
- Retrieval-augmented long context
- Context length scaling (up to 2M+ tokens)

**Neo4j Schema:**
```cypher
(:LongContextExperiment {id, method, target_length, needle_accuracy})
(:PositionalEncoding {type, base, scaling_method})
(:AttentionPattern {type, sparsity_ratio, memory_reduction})
```

**Integrates With:** distributed-training, neural-architecture-search, evaluation-framework

---

### 14. Memory Skills (NEW)

#### advanced-memory-system
**Path:** `skills/advanced-memory-system/SKILL.md`
**Purpose:** Brain-inspired 10000x human memory architecture with episodic/semantic/procedural memory, hippocampal indexing, memory consolidation, and associative retrieval.

**Key Capabilities:**
- Episodic memory (autobiographical events with temporal context)
- Semantic memory (factual knowledge graphs, concept relationships)
- Procedural memory (skills, workflows, routines)
- Hippocampal indexing (pattern separation/completion, sparse representations)
- Memory consolidation (hippocampal-neocortical transfer, sleep-like replay)
- Associative retrieval (multi-hop reasoning, spreading activation)
- Forgetting curves (Ebbinghaus decay, adaptive thresholds)
- Dream-like generative replay for memory strengthening

**Neo4j Schema:**
```cypher
(:Episode {id, content, timestamp, emotional_salience, consolidation_status})
(:SemanticMemory {id, fact, confidence, temporal_context})
(:Procedure {id, preconditions, actions, postconditions, success_rate})
(:Episode)-[:EXTRACTED_AS]->(:SemanticMemory)
(:Episode)-[:LEARNED_AS]->(:Procedure)
(:SemanticMemory)-[:RELATED_TO]->(:SemanticMemory)
```

**Integrates With:** knowledge-graph-query, experiment-tracker, meta-learning-protocol, multi-agent-orchestrator

---

### 15. Orchestration Skills (NEW)

#### tool-use-learner
**Path:** `skills/tool-use-learner/SKILL.md`
**Purpose:** Autonomous tool discovery, learning, and orchestration for AGI agents - discover APIs, learn tool interfaces, optimize tool chains.

**Key Capabilities:**
- Tool discovery (documentation-based, usage-based, registry-based)
- Interface learning (parameter inference, success patterns, constraints)
- Tool orchestration (ReAct framework, chain-of-thought selection)
- Reinforcement learning for tool policies (MDP formulation, Q-learning)
- Tool chaining and composition (compatibility graphs, chain optimization)
- Performance tracking (success rates, latency, cost)

**Neo4j Schema:**
```cypher
(:Tool {name, description, parameters, output_schema, confidence, success_rate})
(:Tool)-[:COMPATIBLE_WITH]->(:Tool)
(:Tool)-[:LEADS_TO]->(:Tool)
(:ToolChain {sequence, task, quality_score})
```

**Integrates With:** multi-agent-orchestrator, experiment-tracker, advanced-memory-system, cognitive-architecture

---

### 16. Model Skills (NEW)

#### world-model-builder
**Path:** `skills/world-model-builder/SKILL.md`
**Purpose:** Learn and maintain predictive world models for AGI agents - environment understanding, causal modeling, and simulation.

**Key Capabilities:**
- Transition modeling (state-action → next_state)
- Reward prediction (state-action → expected_reward)
- Termination modeling (goal detection)
- Causal discovery (NOTEARS, GIES, PC algorithms)
- Model-predictive control (MPC planning)
- Imagination and simulation (dream rollouts, counterfactual reasoning)
- Bayesian model updates (uncertainty quantification)

**Neo4j Schema:**
```cypher
(:CausalVariable {name, type, values, confidence})
(:CausalVariable)-[:CAUSES {strength, confidence, mechanism}]->(:CausalVariable)
(:Intervention {variable, value, timestamp})
(:Intervention)-[:AFFECTS]->(:CausalVariable)
(:WorldModel {id, type, components, performance})
```

**Integrates With:** advanced-memory-system, meta-learning-protocol, distributed-training, experiment-tracker

---

### 17. Code Skills (NEW)

#### code-generation-advanced
**Path:** `skills/code-generation-advanced/SKILL.md`
**Purpose:** Advanced autonomous code synthesis with multi-file understanding, refactoring, testing, and optimization.

**Key Capabilities:**
- Multi-file codebase understanding (AST analysis, cross-file references)
- Automated refactoring (pattern-based, code smell detection)
- Test generation (unit, edge cases, integration tests)
- Code optimization (performance profiling, bottleneck identification)
- Documentation generation (docstring synthesis, API docs)
- Project-wide generation (complete codebase from specs)
- Code quality metrics (complexity, duplication, coverage)

**Neo4j Schema:**
```cypher
(:Function {name, signature, file_path, line_number, complexity, test_coverage})
(:Class {name, file_path, line_number, methods, attributes})
(:Function)-[:CALLS]->(:Function)
(:Class)-[:INHERITS_FROM]->(:Class)
(:Function)-[:USES]->(:Class)
(:Refactoring {type, description, priority, location})
```

**Integrates With:** advanced-memory-system, experiment-tracker, evaluation-framework, knowledge-distillation

---

### 18. Research-to-Implementation Skills (NEW - PaperLantern-Inspired)

#### research-to-implementation
**Path:** `skills/research-to-implementation/SKILL.md`
**Purpose:** Bridge the gap between academic research and OMEGA-ASI implementation by translating engineering problems into research queries, aggregating benchmarks, and delivering implementation-ready recommendations.

**Key Capabilities:**
- Context-aware query translation (engineer language → academic framing)
- Multi-source search orchestration (Semantic Scholar + arXiv + Exa + HuggingFace)
- Cross-paper benchmark aggregation with comparability notes
- Relevance scoring (4-factor: directApplicability, benchmarkStrength, recency, communityValidation)
- Implementation recommendation with "Start with X + Y" guidance
- Decision logging to workspace/RESEARCH_DECISIONS.md and Neo4j
- Pipeline-stage mapping to OMEGA SICAS 9-phase loop

**Neo4j Schema:**
```cypher
(:ResearchDecision {id, decision, context, confidence, status, timestamp})
(:ResearchDecision)-[:INFORMED_BY]->(:Paper)
(:ResearchDecision)-[:AFFECTS]->(:Architecture)
(:ResearchDecision)-[:SUPERSEDES]->(:ResearchDecision)
```

**Integrates With:** paper-synthesis, memory-manager, agi-researcher, arxiv-search, semantic-scholar-search, research-frontier-tracker

---

#### research-frontier-tracker
**Path:** `skills/research-frontier-tracker/SKILL.md`
**Purpose:** Monitor AGI research frontiers, detect when existing decisions become stale, and track the competitive landscape to keep OMEGA-ASI at the cutting edge.

**Key Capabilities:**
- Research frontier watch list (topics, last-checked dates, velocity indicators)
- Staleness detection for research-backed decisions (age thresholds, citation velocity)
- Competitive landscape tracking (labs, architectures, breakthrough monitoring)
- Session-start frontier check protocol
- Alert generation for decisions needing re-evaluation
- Trend velocity classification (accelerating, steady, decelerating, dormant)

**Neo4j Schema:**
```cypher
(:ResearchFrontier {name, status, velocity, lastChecked, keyPapers})
(:FrontierAlert {type, message, severity, timestamp, resolved})
(:ResearchFrontier)-[:TRACKS]->(:Concept)
(:FrontierAlert)-[:CONCERNS]->(:ResearchDecision)
```

**Integrates With:** research-to-implementation, paper-synthesis, agi-researcher, memory-manager

---

## Integration Workflows

### Research Pipeline
```
arxiv-search / semantic-scholar-search
        ↓
    paper-synthesis
        ↓
agi-hypothesis-generator
        ↓
    experiment-tracker
        ↓
    benchmark-creator
        ↓
    memory-manager → knowledge-graph-query
```

### Architecture Development Pipeline
```
cognitive-architecture (design)
        ↓
neural-architecture-search (optimize)
        ↓
mechanistic-interpretability (understand)
        ↓
safety-alignment-researcher (verify)
        ↓
benchmark-creator (evaluate)
```

### Multi-Agent Research Pipeline
```
agi-researcher (define objectives)
        ↓
multi-agent-orchestrator (coordinate agents)
        ↓
advanced-reasoning (solve problems)
        ↓
experiment-tracker (track results)
        ↓
safety-alignment-researcher (verify safety)
```

### Self-Improvement Pipeline
```
meta-learning-protocol (identify gaps)
        ↓
agi-hypothesis-generator (propose improvements)
        ↓
safety-alignment-researcher (safety check)
        ↓
experiment-tracker (test improvements)
        ↓
cognitive-architecture (integrate)
```

### Model Training Pipeline
```
neural-architecture-search (design architecture)
        ↓
distributed-training (train at scale)
        ↓
evaluation-framework (benchmark performance)
        ↓
knowledge-distillation (compress for deployment)
        ↓
safety-alignment-researcher (final safety check)
```

### Long Context Development Pipeline
```
long-context-processing (extend context)
         ↓
distributed-training (train with ring attention)
         ↓
evaluation-framework (needle-in-haystack tests)
         ↓
mechanistic-interpretability (analyze attention)
```

### Memory Development Pipeline
```
advanced-memory-system (brain-inspired memory)
         ↓
meta-learning-protocol (memory self-improvement)
         ↓
world-model-builder (world model integration)
         ↓
experiment-tracker (memory consolidation experiments)
```

### Tool Orchestration Development Pipeline
```
tool-use-learner (discover and learn tools)
         ↓
multi-agent-orchestrator (tool coordination)
         ↓
advanced-reasoning (tool use planning)
         ↓
experiment-tracker (tool use experiments)
```

### Model Development Pipeline
```
world-model-builder (predictive modeling)
         ↓
distributed-training (scale training)
         ↓
evaluation-framework (benchmark performance)
         ↓
code-generation-advanced (implement in code)
```

### Code Generation Pipeline
```
code-generation-advanced (generate codebase)
         ↓
knowledge-distillation (compress for deployment)
         ↓
experiment-tracker (code quality tests)
         ↓
evaluation-framework (code quality benchmarks)
```

### Research-to-Implementation Pipeline (PaperLantern-Inspired)
```
research-to-implementation (detect context, translate query)
         ↓
arxiv-search / semantic-scholar-search (multi-source search)
         ↓
paper-synthesis (cross-paper synthesis + benchmark aggregation)
         ↓
research-to-implementation (relevance scoring + recommendation)
         ↓
memory-manager (store decision + deduplication check)
         ↓
research-frontier-tracker (register for staleness monitoring)
```

### Frontier Monitoring Pipeline (PaperLantern-Inspired)
```
research-frontier-tracker (session-start frontier check)
         ↓
arxiv-search / exa (scan for new papers on watched topics)
         ↓
paper-synthesis (compare new findings vs existing decisions)
         ↓
research-frontier-tracker (generate alerts if stale)
         ↓
research-to-implementation (re-evaluate flagged decisions)
         ↓
memory-manager (update decision status + knowledge graph)
```

---

## Neo4j Schema Summary

### Core Node Types
```cypher
// Research entities
(:Paper {id, title, authors, year, abstract, url})
(:Concept {name, description, domain, importance})
(:Question {text, type, priority, status})
(:Finding {summary, evidence, confidence, timestamp})

// Experiment entities
(:Experiment {id, name, config, metrics, status})
(:Hypothesis {id, statement, evidence, priority, status})
(:Benchmark {id, name, tasks, metrics, baseline})

// Architecture entities
(:Architecture {id, name, components, capabilities})
(:NASExperiment {id, searchSpace, strategy, bestArch})
(:CognitiveArchitecture {name, type, components})
(:Circuit {name, function, layers, validated})

// Agent entities
(:Agent {id, role, capabilities, autonomyLevel})
(:MultiAgentSystem {id, pattern, agents, protocol})

// Memory entities
(:Episode {id, content, timestamp, emotional_salience, consolidation_status})
(:SemanticMemory {id, fact, confidence, temporal_context})
(:Procedure {id, preconditions, actions, postconditions, success_rate})

// Tool entities
(:Tool {name, description, parameters, output_schema, confidence, success_rate})
(:ToolChain {sequence, task, quality_score})

// World model entities
(:CausalVariable {name, type, values, confidence})
(:Intervention {variable, value, timestamp})

// Code entities
(:Function {name, signature, file_path, line_number, complexity, test_coverage})
(:Class {name, file_path, line_number, methods, attributes})

// Research decision entities (PaperLantern-inspired)
(:ResearchDecision {id, decision, context, confidence, status, timestamp})
(:ResearchFrontier {name, status, velocity, lastChecked, keyPapers})
(:FrontierAlert {type, message, severity, timestamp, resolved})

// Safety entities
(:SafetyAssessment {id, level, passed, concerns})
(:ContainmentConfig {level, sandboxing, monitoring})
(:RedTeamResult {attack, success, mitigation})

// Reasoning entities
(:ReasoningTrace {id, method, problem, solution})
(:ThoughtNode {id, content, score, parent})
```

### Core Relationship Types
```cypher
// Knowledge relationships
(Paper)-[:CITES]->(Paper)
(Paper)-[:INTRODUCES]->(Concept)
(Concept)-[:RELATED_TO]->(Concept)
(Finding)-[:SUPPORTS|CONTRADICTS]->(Hypothesis)

// Research relationships
(Experiment)-[:TESTS]->(Hypothesis)
(Experiment)-[:USES]->(Architecture)
(Benchmark)-[:EVALUATES]->(Architecture)

// Safety relationships
(SafetyAssessment)-[:ASSESSES]->(Architecture)
(Architecture)-[:REQUIRES]->(ContainmentConfig)
(RedTeamResult)-[:TARGETS]->(Architecture)

// Agent relationships
(Agent)-[:MEMBER_OF]->(MultiAgentSystem)
(Agent)-[:COMMUNICATES_WITH]->(Agent)
(MultiAgentSystem)-[:FOLLOWS]->(Protocol)

// Memory relationships
(Episode)-[:EXTRACTED_AS]->(:SemanticMemory)
(Episode)-[:LEARNED_AS]->(:Procedure)
(SemanticMemory)-[:RELATED_TO]->(:SemanticMemory)

// Tool relationships
(Tool)-[:COMPATIBLE_WITH]->(:Tool)
(Tool)-[:LEADS_TO]->(:Tool)
(ToolChain)-[:COMPRISES]->(:Tool)

// World model relationships
(CausalVariable)-[:CAUSES {strength, confidence, mechanism}]->(:CausalVariable)
(Intervention)-[:AFFECTS]->(:CausalVariable)

// Code relationships
(Function)-[:CALLS]->(:Function)
(Class)-[:INHERITS_FROM]->(:Class)
(Function)-[:USES]->(:Class)

// Research decision relationships (PaperLantern-inspired)
(ResearchDecision)-[:INFORMED_BY]->(:Paper)
(ResearchDecision)-[:AFFECTS]->(:Architecture)
(ResearchDecision)-[:SUPERSEDES]->(:ResearchDecision)
(ResearchFrontier)-[:TRACKS]->(:Concept)
(FrontierAlert)-[:CONCERNS]->(:ResearchDecision)
```

---

## Usage Examples

### Loading a Skill
```python
# Skills are invoked by the agent when relevant tasks are detected
# Each skill provides structured workflows and templates

# Example: Invoke safety-alignment-researcher for architecture review
workflow = """
1. Run pre-deployment checklist
2. Perform containment level assessment
3. Execute red-teaming protocol
4. Generate safety report
5. Store results in Neo4j
"""
```

### Skill Chaining
```python
# Chain multiple skills for complex workflows
pipeline = [
    "arxiv-search",           # Find relevant papers
    "paper-synthesis",         # Synthesize findings
    "agi-hypothesis-generator", # Generate hypotheses
    "safety-alignment-researcher", # Safety check
    "experiment-tracker",      # Track experiments
    "memory-manager"           # Store results
]
```

### Neo4j Integration
```python
# All skills use consistent Neo4j patterns
from neo4j import GraphDatabase

# Create research finding
CREATE (f:Finding {
    summary: "Novel attention mechanism improves reasoning",
    evidence: ["paper1", "paper2", "experiment1"],
    confidence: 0.85,
    timestamp: datetime()
})

# Link to hypothesis
MATCH (h:Hypothesis {id: "hyp-001"})
CREATE (f)-[:SUPPORTS {strength: 0.8}]->(h)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024-01 | Initial 10 skills |
| 2.0 | 2025-01 | Added 6 new skills (safety, interpretability, NAS, cognitive, multi-agent, reasoning) |
| 2.1 | 2025-01 | Created skill registry, enhanced integration documentation |
 | 3.0 | 2025-01 | Added 4 new skills (advanced-memory-system, tool-use-learner, world-model-builder, code-generation-advanced). Total: 24 skills |
| 3.1 | 2026-02 | Added 2 PaperLantern-inspired skills (research-to-implementation, research-frontier-tracker). Enhanced paper-synthesis with benchmark aggregation. Enhanced memory-manager with deduplication protocol. Total: 26 skills |

---

## Future Skills (Planned)

| Skill | Purpose | Priority |
|-------|---------|----------|
| continual-learning | Lifelong learning without forgetting | Medium |
| reward-modeling | Human preference learning for RLHF | Low |
| synthetic-data-generator | High-quality training data generation | Low |

---

## Contributing

To add a new skill:

1. Create directory: `skills/[skill-name]/`
2. Create `SKILL.md` following the template structure
3. Add optional Python implementation: `[skill-name].py`
4. Update this registry
5. Add Neo4j schema definitions
6. Document integrations with existing skills

### Skill Template Structure
```markdown
---
name: skill-name
description: Brief description
author: AGI Research Team
version: 1.0.0
tags: [relevant, tags]
---

# Skill Name

## Overview
## Core Concepts
## Methodologies / Workflows
## Implementation Templates
## Neo4j Integration
## Integration with Other Skills
## Best Practices
## References
```

---

## Maintenance

- **Review Frequency:** Monthly
- **Owner:** AGI Research Team
- **Last Updated:** February 2026

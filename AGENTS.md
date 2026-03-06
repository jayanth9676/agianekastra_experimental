# AGI/ASI Research Project - Agent Guidelines

## 🚀 START HERE - Project Navigation

> **Read INDEX.md first!** It provides efficient navigation to avoid loading large files.

| Need | Load This File |
|------|----------------|
| Project navigation | `INDEX.md` |
| Architecture overview | `ARCHITECTURE_QUICK_REF.md` |
| Code structure | `workspace/INDEX.md` |
| Documentation | `docs/INDEX.md` |

**Avoid loading**: `docs/architecture/evolution_archive/`, `legacy_code/`, `artifacts1/*.md`

---

## Build, Test, and Lint Commands

**Run all tests:**
```bash
python -m pytest
```

**Run a single test file:**
```bash
python -m pytest test_infrastructure.py
```

**Run a specific test:**
```bash
python -m pytest test_infrastructure.py::TestClassName::test_method_name
```

**Lint code:**
```bash
python -m flake8 --max-line-length=100 --extend-ignore=E203,W503
python -m pylint *.py
```

**Format code:**
```bash
python -m black --line-length=100 *.py
python -m isort --profile=black *.py
```

**Type check:**
```bash
python -m mypy --ignore-missing-imports *.py
```

## Code Style Guidelines

### Python Version
- Use Python 3.12+ for all implementations

### Imports
- Group imports: stdlib → third-party → local
- Use absolute imports, avoid relative imports
- Sort imports with isort (black profile)
- Example:
```python
import os
import sys
from typing import Dict, List, Optional

import numpy as np
import torch

from omega_asi_architecture import BaseArchitecture
```

### Formatting
- Line length: 100 characters maximum
- Use Black formatter with default settings (except line length)
- 4 spaces for indentation (no tabs)
- Two blank lines between top-level definitions
- One blank line between methods in a class

### Type Hints
- Use type hints for all function parameters and return values
- Use `Optional[Type]` for nullable parameters
- Use `Dict[str, Any]` for configuration dictionaries
- Import from `typing` module

### Naming Conventions
- **Classes:** PascalCase (e.g., `OMEGAASIArchitecture`, `NeuralModule`)
- **Functions/Methods:** snake_case (e.g., `process_input`, `train_model`)
- **Constants:** UPPER_SNAKE_CASE (e.g., `MAX_EPOCHS`, `DEFAULT_LR`)
- **Variables:** snake_case (e.g., `input_tensor`, `model_output`)
- **Private methods:** _leading_underscore (e.g., `_internal_helper`)
- **Architecture files:** `OMEGA_ASI_v{number}.py` (e.g., `OMEGA_ASI_v100.py`)

### Docstrings
- Use Google-style docstrings for all public functions and classes
- Include Args, Returns, Raises sections where applicable
- Example:
```python
def train_model(data: torch.Tensor, epochs: int = 10) -> float:
    """Train the model on provided data.
    
    Args:
        data: Training data tensor of shape (batch_size, features).
        epochs: Number of training epochs. Defaults to 10.
        
    Returns:
        Final loss value after training.
        
    Raises:
        ValueError: If data is empty or epochs is negative.
    """
```

### Error Handling
- Use specific exceptions, avoid bare `except:` clauses
- Catch `ValueError`, `TypeError`, `RuntimeError` explicitly
- Provide meaningful error messages
- Use try/except/finally for resource cleanup
- Example:
```python
try:
    result = complex_operation(data)
except ValueError as e:
    logger.error(f"Invalid input data: {e}")
    raise ConfigurationError(f"Training failed: {e}") from e
finally:
    cleanup_resources()
```

### File Organization
- **Core architectures:** Root level (`OMEGA_ASI_vXXX.py`)
- **Documentation:** Root level (`.md` files)
- **Research artifacts:** `/artifacts1/`
- **Agent skills:** `/skills/`
- **Workspace:** `/workspace/` (temp files, gitignored)

## Testing Requirements

- Write unit tests for all core functions using pytest
- Test file naming: `test_*.py` or `*_test.py`
- Use descriptive test function names
- Use fixtures for common test data
- Aim for >80% code coverage

## Persistent Memory (Neo4j)

**CRITICAL:** Always use `neo4j-memory` tool for persistent storage.

- Query memory before starting research
- Store findings immediately after discovery
- Create relationships between concepts
- Use consistent naming for architectures and concepts

## Research Workflow

### Standard Research Flow
1. **Discovery:** Query neo4j-memory → Search sources → Store findings
2. **Analysis:** Synthesize knowledge → Cross-reference → Generate hypotheses
3. **Experimentation:** Design → Execute → Track results
4. **Documentation:** Store findings → Update knowledge graph

### Enhanced Research-to-Implementation Flow (PaperLantern-Inspired)

When researching a technique or making an architecture decision:

```
1. CONTEXT DETECTION
   - Detect current OMEGA-ASI component being worked on
   - Identify engineering problem (e.g., "attention is too slow at 128K context")
   - Map to SICAS pipeline phase

2. QUERY TRANSLATION (PAPER-ANALYST)
   - Translate engineering problem → academic framing
   - Example: "slow attention" → "sub-quadratic attention mechanisms for long sequences"
   - Generate 3+ search queries with different framings

3. MULTI-SOURCE SEARCH
   - AI-Research-Assistant → Semantic Scholar (academic papers)
   - AI-Research-Assistant → arXiv (preprints)
   - exa → Recent developments, blog posts, implementations
   - neo4j-memory → Previously stored papers on topic

4. BENCHMARK AGGREGATION (paper-synthesis skill, Phase 4.5)
   - Extract benchmarks from each paper
   - Build cross-paper comparison table
   - Add comparability notes (comparable / partially / not comparable)
   - Identify evaluation gaps

5. RELEVANCE SCORING
   - Score each paper/technique on 4 factors:
     * Direct applicability to OMEGA-ASI (0-1)
     * Benchmark strength and reproducibility (0-1)
     * Recency and active development (0-1)
     * Community validation (citations, implementations) (0-1)

6. IMPLEMENTATION RECOMMENDATION
   - "Start with X + Y" concrete recommendation
   - Alternatives with trade-off analysis
   - Risk assessment for each option

7. DECISION LOGGING (MANDATORY)
   - Log to workspace/RESEARCH_DECISIONS.md
   - Store as ResearchDecision entity in Neo4j
   - Link to all consulted papers
   - Register with research-frontier-tracker for staleness monitoring
```

### Session-Start Protocol (Enhanced)

```
1. neo4j-memory_read_graph() → Get full context
2. Check research-frontier-tracker watch list → Any stale decisions?
3. Review workspace/RESEARCH_DECISIONS.md → Recent decisions still valid?
4. neo4j-memory_search_memories(query="current task") → Find relevant entities
5. Review relationships to understand dependencies
```

## Safety & Ethics

Before implementing architectures:
- [ ] **Alignment verification** - Does it pursue intended goals?
- [ ] **Containment review** - Can it be safely tested?
- [ ] **Interpretability** - Can we understand its decisions?
- [ ] **Shutdown capability** - Can we stop it if needed?

Document all assumptions, limitations, and ethical implications.

## Version Control

- Commit frequently with clear messages
- Tag architecture versions: `git tag v450-autopoietic`
- Update evolution logs with changes
- Add Neo4j data and workspace to `.gitignore`

## User Preferences

**IMPORTANT:** Always follow these user preferences:

- **Python Projects:** Always use `uv` and activate the virtual environment before running any Python commands
- **Node.js Projects:** Always use `bun` instead of `npm` for package management and running scripts

---

## OMEGA SICAS Multi-Agent System

### Overview

OMEGA SICAS (Self-Improving Cognitive AGI System) is the orchestration layer for this research project. It coordinates multiple specialized agents through MCP tools to conduct AGI research systematically.

### Agent Roles

| Agent | Role | Primary Tools |
|-------|------|---------------|
| **META-ORCHESTRATOR** | Coordinates all agents, maintains research direction | neo4j-memory, sequential-thinking |
| **PAPER-ANALYST** | Literature review, synthesis, query translation, benchmark aggregation | AI-Research-Assistant, exa, paper-synthesis, research-to-implementation |
| **ARCH-DESIGNER** | Architecture design and refinement | context7, sequential-thinking |
| **SAFETY-AUDITOR** | Safety verification and alignment checks | neo4j-memory, sequential-thinking |
| **EXPERIMENT-RUNNER** | Runs experiments on Kaggle | kaggle, huggingface |
| **CODE-BUILDER** | Implements architectures | filesystem, context7 |
| **MEMORY-KEEPER** | Maintains knowledge graph, deduplication, decision tracking | neo4j-memory, memory-manager |

### Agent Activation Protocol

```
1. ALWAYS query neo4j-memory first to retrieve context
2. Identify which agent role is needed for the task
3. Use appropriate MCP tools for that agent
4. Store all findings back to neo4j-memory
5. Update todo list with progress
```

---

## MCP Tool Usage Protocols

### 1. AI-Research-Assistant (Semantic Scholar)

**Purpose:** Academic paper search and analysis

```python
# Search for papers
AI-Research-Assistant_papers-search-basic(query="transformer architecture attention")

# Get paper details with abstract
AI-Research-Assistant_get-paper-abstract(paperId="paper_id_here")

# Analyze citation network
AI-Research-Assistant_analysis-citation-network(paperId="paper_id", depth="2")

# Find papers by title
AI-Research-Assistant_search-paper-title(title="Attention Is All You Need")

# Search arXiv directly
AI-Research-Assistant_search-arxiv(query="self-improving neural networks")
```

**Best Practices:**
- Always get abstracts for papers you cite
- Build citation networks to find seminal works
- Cross-reference with exa for recent developments

### 2. Exa (Web Search)

**Purpose:** Real-time web search with AI understanding

```python
# General web search
exa_web_search_exa(query="latest advances in AGI architectures 2025")

# Company research
exa_company_research_exa(companyName="Anthropic")

# Code examples and documentation
exa_get_code_context_exa(query="PyTorch transformer implementation")
```

**Best Practices:**
- Use for recent developments not in academic papers
- Cross-reference claims with academic sources
- Verify information from multiple sources

### 3. Context7 (Library Documentation)

**Purpose:** Up-to-date library documentation and examples

```python
# First resolve library ID
context7_resolve-library-id(libraryName="pytorch", query="neural network training")

# Then query documentation
context7_query-docs(libraryId="/pytorch/pytorch", query="custom loss function")
```

**Best Practices:**
- Always resolve library ID first
- Use for implementation details
- Check for version-specific features

### 4. Sequential-Thinking (Reasoning)

**Purpose:** Step-by-step problem solving and analysis

```python
sequential-thinking_sequentialthinking(
    thought="Analyzing the trade-offs between transformer attention and state-space models...",
    thoughtNumber=1,
    totalThoughts=5,
    nextThoughtNeeded=True
)
```

**Best Practices:**
- Use for complex architectural decisions
- Break down problems into 5-10 steps
- Mark revisions when changing direction
- Generate and verify hypotheses

### 5. Kaggle (Experiments)

**Purpose:** Run experiments, access datasets, track submissions

```python
# Search competitions
kaggle_search_competitions(request={"hasSearch": True, "search": "language model"})

# Get competition data
kaggle_get_competition_data_files_summary(request={"competitionName": "competition-name"})

# Download dataset
kaggle_download_dataset(request={"ownerSlug": "owner", "datasetSlug": "dataset"})

# Search notebooks for inspiration
kaggle_search_notebooks(request={"hasSearch": True, "search": "transformer training"})

# Save and run notebook
kaggle_save_notebook(request={
    "slug": "my-notebook",
    "newTitle": "OMEGA-ASI Experiment",
    "text": "notebook_content_here",
    "language": "python",
    "kernelType": "notebook"
})
```

**Experimentation Workflow:**
1. Search for relevant competitions/datasets
2. Analyze top notebooks for techniques
3. Create experiment notebook
4. Run and monitor results
5. Store findings in neo4j-memory

### 6. HuggingFace (Models)

**Purpose:** Access pre-trained models and datasets

```python
# List models
kaggle_list_models(request={"hasSearch": True, "search": "llama"})

# Get model details
kaggle_get_model(request={"ownerSlug": "meta-llama", "modelSlug": "llama-2-7b"})

# Download model variation
kaggle_download_model_variation_version(request={
    "ownerSlug": "owner",
    "modelSlug": "model",
    "instanceSlug": "instance",
    "framework": "PyTorch",
    "versionNumber": 1
})
```

### 7. Neo4j-Memory (Knowledge Graph)

**Purpose:** Persistent memory across sessions

```python
# Read entire graph
neo4j-memory_read_graph()

# Search memories
neo4j-memory_search_memories(query="transformer architecture")

# Find by exact name
neo4j-memory_find_memories_by_name(names=["OMEGA-ASI v2.0 Implementation"])

# Create entities
neo4j-memory_create_entities(entities=[{
    "name": "New Discovery",
    "type": "research_finding",
    "observations": ["Key insight 1", "Key insight 2"]
}])

# Create relationships
neo4j-memory_create_relations(relations=[{
    "source": "Entity A",
    "target": "Entity B",
    "relationType": "DERIVED_FROM"
}])

# Add observations to existing entity
neo4j-memory_add_observations(observations=[{
    "entityName": "Existing Entity",
    "observations": ["New observation"]
}])
```

**Memory Patterns:**
- **Entity Types:** `architecture_version`, `research_finding`, `paper`, `concept`, `experiment`, `skill`, `research_decision`, `research_frontier`, `frontier_alert`
- **Relationship Types:** `DERIVED_FROM`, `IMPLEMENTS`, `RELATED_TO`, `IMPROVES_UPON`, `CITES`, `VALIDATED_BY`, `INFORMED_BY`, `AFFECTS`, `SUPERSEDES`, `TRACKS`, `CONCERNS`

---

## Kaggle Experimentation Workflow

### Quick Commands

```bash
# List available competitions
kaggle_search_competitions(request={"hasPageSize": True, "pageSize": 10})

# Get competition files
kaggle_list_competition_data_files(request={"competitionName": "name"})

# Download competition data
kaggle_download_competition_data_files(request={"competitionName": "name"})

# Check submission status
kaggle_get_competition_submission(request={"ref": submission_id})

# View leaderboard
kaggle_get_competition_leaderboard(request={"competitionName": "name"})
```

### Experiment Tracking

1. **Before Experiment:**
   - Create entity in neo4j-memory with hypothesis
   - Record baseline metrics

2. **During Experiment:**
   - Use Kaggle notebooks for GPU access
   - Log intermediate results

3. **After Experiment:**
   - Update neo4j-memory with results
   - Create relationships to architectures tested
   - Document learnings

---

## Memory Management Best Practices

### Session Start Protocol

```
1. neo4j-memory_read_graph() → Get full context
2. Check research-frontier-tracker watch list → Any stale decisions?
3. Review workspace/RESEARCH_DECISIONS.md → Recent decisions still valid?
4. neo4j-memory_search_memories(query="current task") → Find relevant entities
5. Review relationships to understand dependencies
```

### During Research

```
1. Store findings IMMEDIATELY - don't batch
2. Use consistent entity naming (check existing first)
3. Create relationships to connect insights
4. Add timestamps in observations
```

### Entity Naming Conventions

| Type | Pattern | Example |
|------|---------|---------|
| Architecture | `OMEGA-ASI v{X}.{Y}` | `OMEGA-ASI v2.0` |
| Paper | `{Short Title} ({Year})` | `Attention Is All You Need (2017)` |
| Experiment | `EXP-{DATE}-{NAME}` | `EXP-20260131-attention-scaling` |
| Concept | `{Concept Name}` | `Self-Improvement Loop` |

### Relationship Guidelines

- Use UPPER_SNAKE_CASE for relationship types
- Be specific: `IMPROVES_UPON` not just `RELATED_TO`
- Create bidirectional awareness when needed

---

## Self-Improvement Safety Constraints

### Before Any Self-Modification

- [ ] **Scope Check:** Is the change bounded and reversible?
- [ ] **Alignment Verification:** Does it maintain original goals?
- [ ] **Capability Assessment:** What new capabilities does it enable?
- [ ] **Containment Review:** Can it be safely tested?

### Prohibited Self-Modifications

1. **NO** modifications to core safety constraints
2. **NO** removal of shutdown capabilities
3. **NO** changes to goal alignment mechanisms
4. **NO** self-replication without explicit approval
5. **NO** resource acquisition beyond allocated limits

### Required Logging

All self-improvement attempts MUST be logged to neo4j-memory:

```python
neo4j-memory_create_entities(entities=[{
    "name": "SELF-MOD-{timestamp}",
    "type": "self_modification_attempt",
    "observations": [
        "Proposed change: {description}",
        "Justification: {reason}",
        "Safety assessment: {assessment}",
        "Outcome: {result}",
        "Timestamp: {datetime}"
    ]
}])
```

### Darwin-Godel Integration Safety

When using self-improvement protocols:

1. **Mutation bounds:** Max 10% parameter change per iteration
2. **Fitness preservation:** Must maintain >95% of baseline performance
3. **Rollback capability:** Always keep previous version
4. **Human checkpoint:** Major changes require human review

---

## Quick Reference Card

### Start of Session
```
1. Read neo4j-memory → Get context
2. Check todo list → Understand pending tasks
3. Query relevant entities → Build working memory
```

### Research Task
```
1. AI-Research-Assistant → Find papers
2. exa → Get recent developments
3. sequential-thinking → Analyze findings
4. neo4j-memory → Store insights
```

### Implementation Task
```
1. context7 → Get library docs
2. filesystem → Read/write code
3. Test implementation
4. neo4j-memory → Log results
```

### Experiment Task
```
1. kaggle → Setup experiment
2. Run on Kaggle notebooks
3. Analyze results
4. neo4j-memory → Store findings
```

---

## Files Reference

| File | Purpose |
|------|---------|
| `prompts/OMEGA_SICAS_SYSTEM_PROMPT.md` | Full multi-agent system prompt |
| `OMEGA_SICAS_ARCHITECTURE.md` | Architecture documentation |
| `skills/SKILL_REGISTRY.md` | Available agent skills (26 skills) |
| `opencode.json` | MCP server configuration |
| `workspace/omega_asi_v2/` | Current implementation |
| `workspace/RESEARCH_DECISIONS.md` | Research decision log (PaperLantern-inspired) |

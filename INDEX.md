# OMEGA-ASI Project Index

> **FOR LLMs**: Read THIS file first. Do NOT load other files unless specifically needed.

## Quick Decision Tree

```
What do you need?
|
|--- Write/modify code
|    |--- omega_asi_v6/ -------> CURRENT: v6.1 optimized (118 tests)
|    |--- omega_asi_v2/ -------> Legacy: Full 8-phase ASI (505 tests)
|    \--- omega_asi_v4/ -------> Legacy: PINNACLE prototype (58 tests)
|--- Understand architecture --> ARCHITECTURE_QUICK_REF.md
|--- Architecture spec -------> OMEGA_ASI_v6.0_EMPIRICAL_FOUNDATION.md (v6.1, 1256 lines)
|--- Run tests ---------------> workspace/omega_asi_v6/tests/test_v6.py
|--- Research context ---------> workspace/RESEARCH_SUMMARY.md
|--- Knowledge graph ----------> Neo4j @ localhost:7687
|--- Agent system prompt ------> prompts/OMEGA_SICAS_SYSTEM_PROMPT.md
\--- Historical context -------> docs/architecture/evolution_archive/ (AVOID - large)
```

## Folder Purpose Map

| Folder | Purpose | When to Access |
|--------|---------|----------------|
| `workspace/omega_asi_v6/` | **CURRENT production code (v6.1)** | Writing/testing code |
| `workspace/omega_asi_v2/` | Legacy v2.0 implementation | Historical reference only |
| `workspace/omega_asi_v4/` | Legacy PINNACLE prototype | Historical reference only |
| `workspace/kaggle_experiment/` | GPU profiling notebook | Kaggle/Colab experiments |
| `workspace/data/` | JSON exports | Need structured data |
| `docs/architecture/` | Architecture specs | Understanding design |
| `docs/setup/` | MCP configuration | Setup issues |
| `artifacts1/` | Theoretical research | Deep research only |
| `legacy_code/` | Old prototypes | **NEVER** (deprecated) |
| `prompts/` | System prompts (SICAS) | Prompt engineering |
| `skills/` | Agent skills (26 skills) | Extending capabilities |

## Files to AVOID Loading (Large/Redundant)

```
docs/architecture/evolution_archive/*  (17 files, 600KB - historical only)
legacy_code/*                          (11 files - deprecated)
artifacts1/OMEGA_ASI_v*.md             (theoretical, superseded)
node_modules/*                         (npm packages)
memory/*                               (database files)
workspace/omega_asi_v2/*               (superseded by v6)
workspace/omega_asi_v4/*               (superseded by v6)
```

## Files to Load First (Small/Essential)

| Priority | File | Size | Purpose |
|----------|------|------|---------|
| 1 | `INDEX.md` (this) | 3KB | Navigation |
| 2 | `ARCHITECTURE_QUICK_REF.md` | 4KB | Architecture summary |
| 3 | `OMEGA_ASI_v6.0_EMPIRICAL_FOUNDATION.md` | 50KB | Full v6.1 spec (1256 lines) |
| 4 | `workspace/omega_asi_v6/config.py` | 40KB | NexusConfig (all hyperparams) |
| 5 | `AGENTS.md` | 15KB | Agent guidelines & tool protocols |

## Key Commands

```bash
# Run v6.1 tests (batch 1: 66 tests)
".venv/Scripts/python.exe" -m pytest workspace/omega_asi_v6/tests/test_v6.py -v --tb=short -k "TestConfig or TestCommonComponents or TestMixers or TestPEERMoE or TestBackbone or TestMemorySystem or TestAdaptiveReasoning or TestAlignmentSystem"

# Run v6.1 tests (batch 2: 51 tests, skip known segfault)
".venv/Scripts/python.exe" -m pytest workspace/omega_asi_v6/tests/test_v6.py -v --tb=short --deselect "workspace/omega_asi_v6/tests/test_v6.py::TestGodelAgent::test_godel_single_step" -k "not (TestConfig or TestCommonComponents or TestMixers or TestPEERMoE or TestBackbone or TestMemorySystem or TestAdaptiveReasoning or TestAlignmentSystem)"

# Neo4j
docker-compose up -d

# Install deps (use uv)
uv pip install torch --index-url https://download.pytorch.org/whl/cpu
```

## Project Stats (v6.1)

- **Architecture**: OMEGA-ASI v6.1 (6-layer empirical foundation)
- **Tests**: 118 total, 117 PASS, 1 pre-existing PyTorch Windows segfault
- **Parameters**: 3B target (1B unique, 60-100M active per token)
- **Optimizations**: 5 implemented (V6-OPT1 through V6-OPT5), 2 optional remaining
- **Knowledge Graph**: 200+ entities, 150+ relationships
- **Feasibility**: 90%+ with 2026 hardware

## v6.1 Optimization Status

| ID | Optimization | Priority | Status |
|----|-------------|----------|--------|
| V6-OPT1 | DepthRouter init bias (depth 32 -> 4) | P0 | DONE |
| V6-OPT2 | BitLinear eval-mode weight caching | P1 | DONE |
| V6-OPT3 | SharedReasoningBlock nn.MHA -> SDPA | P1 | DONE |
| V6-OPT4 | flat_x.clone() -> scatter | P2 | DONE |
| V6-OPT5 | Mamba2 parallel scan (O(L) -> O(log L)) | P0 | DONE |
| V6-OPT6 | CrossExpertAttention batched bmm | P2 | Optional |
| V6-OPT7 | PEERMoE output_proj batching | P3 | Optional |

## Navigation by Task

### "I need to understand the codebase"
1. Read `ARCHITECTURE_QUICK_REF.md`
2. Read `OMEGA_ASI_v6.0_EMPIRICAL_FOUNDATION.md` (sections 1-3)
3. Browse `workspace/omega_asi_v6/core/`

### "I need to fix a bug"
1. Read this file for structure
2. Find relevant module in `workspace/omega_asi_v6/core/`
3. Run specific test batch (see Key Commands)

### "I need research context"
1. Query Neo4j: `neo4j-memory_search_memories(query="topic")`
2. Read `workspace/RESEARCH_SUMMARY.md`
3. Only then check `artifacts1/ARTIFACTS_SUMMARY.md`

### "I need to run GPU experiments"
1. Read `workspace/kaggle_experiment/` for profiling notebook
2. Upload .ipynb to Kaggle web UI (API GPU allocation is broken)
3. Or use Google Colab with GPU runtime

---
**Last Updated**: 2026-02-28 | **Current Version**: v6.1

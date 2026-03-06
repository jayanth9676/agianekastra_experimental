# CLAUDE.md - LLM Context File

> **AUTO-LOADED**: This file is read by LLMs/agents on session start.

## ⚡ TL;DR

This is the **OMEGA-ASI** AGI research project with **two** working implementations.

```
omega_asi_v2: workspace/omega_asi_v2/  (505 tests) - Full ASI architecture
omega_asi_v4: workspace/omega_asi_v4/  (28 tests)  - PINNACLE: BitNet+Mamba2+MoE
Architecture: ARCHITECTURE_QUICK_REF.md (50 lines)
Navigation:   INDEX.md
```

## 🧭 Navigation Rules

1. **START** with `INDEX.md` - it tells you what to load
2. **NEVER** load `docs/architecture/evolution_archive/*` (600KB historical)
3. **NEVER** load `legacy_code/*` (deprecated)
4. **PREFER** small index files over large specs

## 📁 Key Files (Sorted by Priority)

| Priority | File | Size | Purpose |
|----------|------|------|---------|
| 1 | `INDEX.md` | 2KB | Project navigation |
| 2 | `ARCHITECTURE_QUICK_REF.md` | 3KB | Architecture in 50 lines |
| 3 | `workspace/INDEX.md` | 3KB | Code navigation |
| 4 | `workspace/omega_asi_v2/README.md` | 2KB | Implementation |

## 🎯 Quick Answers

| Question | Answer |
|----------|--------|
| What is this? | AGI/ASI architecture research + implementation |
| Is it working? | Yes, 505 tests passing |
| Main code? | `workspace/omega_asi_v2/` |
| Architecture? | Mamba-Transformer + Active Inference + HD Computing |
| What failed? | v450+ designs (Gödel violations, physics impossible) |

## 🔧 Commands

```bash
# Run v2 tests
cd workspace/omega_asi_v2 && pytest tests/ -v

# Run v4 tests  
cd workspace/omega_asi_v4 && pytest tests/ -v

# Start Neo4j
docker-compose up -d

# Install
cd workspace/omega_asi_v2 && pip install -e .
```

## 🚫 Context Optimization

To keep context small:
- Use `INDEX.md` files as entry points
- Load specific module files, not entire folders
- Query Neo4j for entities instead of reading data files
- Use `ARCHITECTURE_QUICK_REF.md` instead of full architecture docs

## 📊 Project Stats

- **omega_asi_v2**: 505 tests, 8 phases complete
- **omega_asi_v4**: 28 tests, PINNACLE Phase 1 complete
- **Feasibility**: 90% with 2026 tech
- **Knowledge Graph**: 110+ entities in Neo4j

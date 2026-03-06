# 📚 Documentation Index

> **FOR LLMs**: Navigate documentation efficiently. Most answers are in architecture/.

## 📁 Structure

```
docs/
├── INDEX.md              ← You are here
│
├── architecture/         ← 🎯 CURRENT DESIGN (load these)
│   ├── README.md
│   ├── OMEGA_ASI_v2_ULTIMATE_ARCHITECTURE.md   ← THE definitive design
│   ├── OMEGA_ASI_v2_IMPLEMENTATION_PLAN.md     ← 8-phase roadmap
│   ├── OMEGA_SICAS_ARCHITECTURE.md             ← Multi-agent system
│   └── evolution_archive/                       ← Historical (AVOID)
│
├── research/             ← Research synthesis
│   ├── ASI_RESEARCH_SYNTHESIS_2024_2025.md
│   ├── RUTHLESS_ASI_CRITIQUE.md                ← Critical analysis
│   └── ...
│
└── setup/                ← Configuration guides
    ├── MCP_SETUP_SUMMARY.md
    ├── QUICK_REFERENCE.md
    └── ...
```

## 🎯 Which File to Load?

| Question | Load This |
|----------|-----------|
| "What is the architecture?" | `architecture/OMEGA_ASI_v2_ULTIMATE_ARCHITECTURE.md` |
| "How to implement?" | `architecture/OMEGA_ASI_v2_IMPLEMENTATION_PLAN.md` |
| "What's the multi-agent system?" | `architecture/OMEGA_SICAS_ARCHITECTURE.md` |
| "Why these design choices?" | `research/RUTHLESS_ASI_CRITIQUE.md` |
| "What papers were used?" | `research/ASI_RESEARCH_SYNTHESIS_2024_2025.md` |
| "How to set up MCP?" | `setup/MCP_SETUP_SUMMARY.md` |

## 📊 File Sizes (Load Smaller First)

| File | Lines | Load Priority |
|------|-------|---------------|
| `architecture/README.md` | 60 | ⬆️ High |
| `setup/QUICK_REFERENCE.md` | 200 | ⬆️ High |
| `architecture/OMEGA_ASI_v2_ULTIMATE_ARCHITECTURE.md` | 550 | Medium |
| `architecture/OMEGA_ASI_v2_IMPLEMENTATION_PLAN.md` | 940 | Medium |
| `architecture/OMEGA_SICAS_ARCHITECTURE.md` | 860 | Medium |
| `research/RUTHLESS_ASI_CRITIQUE.md` | 900 | Low |
| `architecture/evolution_archive/*` | 17K+ | ❌ Avoid |

## 🚫 Avoid Loading

```
❌ architecture/evolution_archive/  (17 files, 600KB - superseded)
```

These are historical explorations (v1-v400) that led to v2.0. Only load if specifically researching the evolution of ideas.

## 🔍 Quick Answers

**Q: What's the main architecture?**
A: Mamba-Transformer hybrid with Active Inference, HD Computing, Constitutional AI.

**Q: What was removed as impossible?**
A: Liquid FPGA, Neural Quine, Godelian Judge, CTCs, Infinite Turing Machines.

**Q: How many tests?**
A: 505 tests across 8 phases.

**Q: Is it implementable?**
A: Yes, 90% feasible with 2026 technology.

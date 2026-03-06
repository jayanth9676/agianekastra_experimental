# OMEGA-ASI v6.1 - Architecture Quick Reference

> **Full spec**: `OMEGA_ASI_v6.0_EMPIRICAL_FOUNDATION.md` (1256 lines)
> **Code**: `workspace/omega_asi_v6/`

## Core Design

```
Input IDs
    |
    v
[Embedding] -----> token + position
    |
    v
[HybridBackbone] -----> 50/50 Mamba-2 / GQA interleaved blocks
    |                     BitNet b1.58 ternary weights
    |                     PEER 65K product-key MoE (top-16 active)
    |                     CrossExpertAttention
    v
[MemorySystem] --------> 3-tier: ATLAS + PersistentStore + MemoryRouter
    |
    v
[AdaptiveReasoning] ---> MoR with DepthRouter, buckets [4,16,32,64]
    |                     SharedReasoningBlock (SDPA, Flash-ready)
    |                     R_max=64 depth per token
    v
[AlignmentSystem] -----> SRS + E2E SAE + ConstitutionalGuard (9 rules)
    |
    v
[SafetyMonitor] -------> DeceptionDetector (20 probes)
    |                     DriftTracker (Bonferroni)
    |                     3-tier monitor + kill switch
    v
[Output Head] ---------> logits + aux_losses
```

## Key Components

| Component | Class | File | Tests |
|-----------|-------|------|-------|
| Config | `NexusConfig` | `config.py` | 3 |
| Common | `BitLinear`, `RMSNorm` | `core/common/__init__.py` | 7 |
| Mixers | `Mamba2Mixer`, `GQAMixer` | `core/backbone/mixers.py` | 8 |
| MoE | `PEERMoE`, `CrossExpertAttention` | `core/backbone/moe.py` | 8 |
| Backbone | `HybridBackbone` | `core/backbone/backbone.py` | 12 |
| Memory | `MemorySystem`, `ATLASMemory` | `core/memory/__init__.py` | 10 |
| Reasoning | `AdaptiveReasoning`, `DepthRouter` | `core/reasoning/adaptive_reasoning.py` | 18 |
| Alignment | `AlignmentSystem`, `E2ESAE` | `core/alignment/alignment.py` | 12 |
| Safety | `SafetyMonitor`, `DeceptionDetector` | `core/safety/safety_monitor.py` | 10 |
| Self-Improve | `GodelAgent`, `SSRRehearsal` | `core/self_improvement/` | 12 |
| Training | `NexusTrainer` | `training/trainer.py` | 8 |
| Top-level | `OmegaASI` | `core/omega_asi.py` | 10 |

## Parameter Budget

| Scale | Total Params | Unique | Active/Token |
|-------|-------------|--------|-------------|
| Tiny (test) | ~14M | ~14M | ~2M |
| Target | 3B | 1B | 60-100M |

## v6.1 Optimizations (5/7 implemented)

| ID | What | Where | Impact |
|----|------|-------|--------|
| OPT1 | DepthRouter bias -> depth 4 default | `adaptive_reasoning.py` | 8x less wasted compute |
| OPT2 | BitLinear eval weight caching | `common/__init__.py` | Skip 3 ops/matmul in eval |
| OPT3 | nn.MHA -> F.scaled_dot_product_attention | `adaptive_reasoning.py` | Flash Attention on GPU |
| OPT4 | clone+index -> scatter | `adaptive_reasoning.py` | Fused single op |
| OPT5 | Sequential scan -> parallel prefix-sum | `mixers.py` | O(L) -> O(log L) serial |

## Test Summary

```
Total: 118 tests (117 PASS, 1 known PyTorch Windows segfault)

TestConfig .................. 3   TestPEERMoE .............. 8
TestCommonComponents ....... 7   TestBackbone ............ 12
TestMixers ................ 8   TestMemorySystem ........ 10
TestAdaptiveReasoning ..... 18   TestAlignmentSystem ..... 12
TestSafetyMonitor ......... 10   TestGodelAgent .......... 12
TestSSRRehearsal ........... 4   TestTrainer .............. 8
TestCrossCuttingConcerns .... 5   TestMamba2Scan ........... 1
```

## Run Tests

```bash
# Batch 1 (66 tests - fast)
".venv/Scripts/python.exe" -m pytest workspace/omega_asi_v6/tests/test_v6.py -v -k "TestConfig or TestCommonComponents or TestMixers or TestPEERMoE or TestBackbone or TestMemorySystem or TestAdaptiveReasoning or TestAlignmentSystem"

# Batch 2 (51 tests - skip segfault)
".venv/Scripts/python.exe" -m pytest workspace/omega_asi_v6/tests/test_v6.py -v --deselect "workspace/omega_asi_v6/tests/test_v6.py::TestGodelAgent::test_godel_single_step" -k "not (TestConfig or TestCommonComponents or TestMixers or TestPEERMoE or TestBackbone or TestMemorySystem or TestAdaptiveReasoning or TestAlignmentSystem)"
```

## API Signatures (Quick Reference)

```python
model = OmegaASI(NexusConfig.tiny())
out = model(input_ids)              # -> OmegaASIOutput(.logits, .aux_losses)

backbone_out = model.backbone(input_ids=ids)           # -> Tensor [B,S,d]
mem_out, stats = model.memory(x, do_memory_write=True)  # -> (Tensor, Dict)
reas_out, depth = model.reasoning(x, budget=0.5)        # -> (Tensor, DepthStats)
align_out, ast = model.alignment(x, layer_idx=0)        # -> (Tensor, AlignmentStats)
safety = model.safety_monitor(hidden_states=x)           # -> SafetyResult
```

## Legacy Versions (reference only)

| Version | Location | Tests | Status |
|---------|----------|-------|--------|
| v2.0 | `workspace/omega_asi_v2/` | 505 | Superseded |
| v4.0 | `workspace/omega_asi_v4/` | 58 | Superseded |
| **v6.1** | **`workspace/omega_asi_v6/`** | **118** | **CURRENT** |

---
**Last Updated**: 2026-02-28 | **Version**: v6.1 (5/7 optimizations complete)

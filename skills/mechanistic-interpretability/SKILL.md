---
name: mechanistic-interpretability
description: Reverse-engineer neural network internals to understand computational mechanisms, discover features and circuits, and enable AI safety through transparency. Based on latest 2024-2025 research from Anthropic, DeepMind, and the interpretability community.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, interpretability, mechanistic, circuits, features, safety, transparency]
---

# Mechanistic Interpretability

## Overview

Mechanistic Interpretability (MI) aims to reverse-engineer the computational mechanisms and representations learned by neural networks into human-understandable algorithms. This skill provides frameworks for feature discovery, circuit analysis, and understanding model internals for AGI safety.

## When to Use

- Understanding how a model makes specific decisions
- Discovering learned features and representations
- Tracing circuits and computational pathways
- Identifying potential safety issues in model behavior
- Validating alignment through transparency
- Debugging unexpected model behaviors
- Evaluating self-modification proposals
- Conducting model audits

## Core Concepts

### Features and Representations

**Features**: Fundamental, interpretable units of representation in neural networks.

```
FEATURE TYPES:
- Mono-semantic: Single, clear meaning (rare)
- Poly-semantic: Multiple unrelated meanings (common)
- Superposition: Multiple features encoded in overlapping neuron combinations

LINEAR REPRESENTATION HYPOTHESIS:
- Features are represented as directions in activation space
- Linear combinations of neurons encode concepts
- Allows for feature extraction via linear probes
```

### Circuits

**Circuits**: Connected pathways through the network that implement specific computations.

```
CIRCUIT COMPONENTS:
- Input features: What the circuit responds to
- Attention patterns: How information flows
- MLP computations: Transformations applied
- Output features: What the circuit produces

CIRCUIT TYPES:
- Copy/suppression circuits
- Induction circuits
- Factual recall circuits
- Reasoning circuits
- Safety-relevant circuits
```

### Superposition

**Superposition Hypothesis**: Networks encode more features than they have neurons by using almost-orthogonal combinations.

```
IMPLICATIONS:
- Neurons are not the right unit of analysis
- Must extract features from neuron combinations
- Sparse autoencoders (SAEs) can disentangle features
- Feature dictionaries enable interpretation
```

## Interpretability Methods

### 1. Activation Patching

Identify which components are causally important:

```python
activation_patching_protocol = {
    "method": "Activation Patching / Causal Tracing",
    "steps": [
        "1. Run model on clean input, cache activations",
        "2. Run model on corrupted input, cache activations",
        "3. For each component, patch clean activation into corrupted run",
        "4. Measure restoration of correct behavior",
        "5. Components with high restoration are causally important"
    ],
    "variants": [
        "Mean ablation (replace with dataset mean)",
        "Zero ablation (set to zero)",
        "Resample ablation (replace with other examples)",
        "Path patching (trace specific paths)"
    ],
    "tools": ["TransformerLens", "Pyvene", "nnsight"]
}
```

### 2. Sparse Autoencoders (SAEs)

Extract interpretable features from activations:

```python
sae_workflow = {
    "purpose": "Disentangle superposed features into interpretable dictionary",
    "architecture": {
        "encoder": "Linear layer with ReLU → sparse feature activations",
        "decoder": "Linear layer → reconstructed activations",
        "sparsity": "L1 penalty encourages sparse feature use"
    },
    "training": {
        "data": "Large dataset of model activations",
        "objective": "Reconstruction loss + sparsity penalty",
        "scaling": "Train separate SAE per layer/component"
    },
    "analysis": {
        "feature_interpretation": "Examine max-activating examples",
        "feature_steering": "Amplify/suppress features to modify behavior",
        "circuit_discovery": "Trace feature-to-feature connections"
    }
}
```

### 3. Logit Lens / Tuned Lens

Decode intermediate representations into vocabulary:

```python
logit_lens_protocol = {
    "logit_lens": {
        "method": "Apply final unembedding to intermediate residual stream",
        "purpose": "See what tokens model is 'thinking about' at each layer",
        "limitation": "Assumes representation space is consistent across layers"
    },
    "tuned_lens": {
        "method": "Train per-layer affine transforms to improve decoding",
        "purpose": "Account for representation drift across layers",
        "advantage": "More accurate intermediate predictions"
    },
    "applications": [
        "Track how predictions evolve through layers",
        "Identify where factual information is retrieved",
        "Understand multi-step reasoning progression"
    ]
}
```

### 4. Probing

Train simple classifiers to detect information in representations:

```python
probing_framework = {
    "linear_probes": {
        "purpose": "Test if information is linearly accessible",
        "method": "Train linear classifier on frozen activations",
        "interpretation": "High accuracy → information is represented"
    },
    "probe_types": [
        "Syntactic probes (grammar, structure)",
        "Semantic probes (meaning, concepts)",
        "Factual probes (knowledge, entities)",
        "Safety probes (harmful content, alignment)"
    ],
    "best_practices": [
        "Use held-out test sets",
        "Compare to baselines (random, majority)",
        "Test across multiple layers",
        "Consider selectivity (what probe doesn't detect)"
    ]
}
```

### 5. Attention Pattern Analysis

Understand information flow through attention:

```python
attention_analysis = {
    "pattern_types": [
        "Induction heads: Copy patterns from earlier context",
        "Previous token heads: Attend to immediately prior token",
        "Duplicate token heads: Find repeated tokens",
        "Positional heads: Attend based on position"
    ],
    "analysis_methods": [
        "Attention weight visualization",
        "Attention knockout experiments",
        "Head importance scoring",
        "Composition analysis (QK/OV circuits)"
    ],
    "tools": ["CircuitsVis", "BertViz", "TransformerLens"]
}
```

## Interpretability Research Workflow

### Phase 1: Define Research Question

```markdown
## MI Research Question

**Question**: [What mechanism do we want to understand?]
**Hypothesis**: [Expected mechanism or representation]
**Scope**: [Which model, layers, components?]
**Success Criteria**: [How will we know we've understood it?]

### Examples:
- "How does GPT-2 complete 'The Eiffel Tower is in' → 'Paris'?"
- "What circuit implements IOI (Indirect Object Identification)?"
- "Where are safety-relevant features represented?"
- "How does the model detect and refuse harmful requests?"
```

### Phase 2: Exploratory Analysis

```markdown
## Exploratory Analysis

1. **Identify Minimal Example**
   - Find simple prompt that exhibits behavior
   - Reduce to minimal triggering case
   - Create counterfactual (what changes behavior)

2. **Initial Probing**
   - Run logit lens to track prediction evolution
   - Visualize attention patterns
   - Check which layers are important

3. **Activation Patching**
   - Identify causally important components
   - Narrow down to specific heads/MLPs
   - Build initial circuit hypothesis

4. **Document Observations**
   - Record surprising findings
   - Note component rankings
   - Identify patterns
```

### Phase 3: Circuit Analysis

```markdown
## Circuit Discovery

**Target Behavior**: [What the circuit computes]
**Identified Components**: [Heads, MLPs, positions]

### QK Circuit Analysis
- What information is used to compute attention?
- Which heads attend to what?
- How is positional information used?

### OV Circuit Analysis
- What information is moved/copied?
- How is it transformed?
- What is written to residual stream?

### MLP Analysis
- What features are amplified/suppressed?
- What computations are performed?
- What is the role of nonlinearity?

### Full Circuit Diagram
[Visual representation of component connections]
```

### Phase 4: Validation

```markdown
## Validation Experiments

1. **Ablation Verification**
   - Remove identified components
   - Confirm behavior changes as predicted
   - Check for compensating mechanisms

2. **Activation Patching**
   - Patch activations to verify causal role
   - Test on new examples
   - Measure effect sizes

3. **Feature Steering**
   - Amplify/suppress identified features
   - Verify expected behavior changes
   - Test boundary cases

4. **Generalization Testing**
   - Apply findings to related examples
   - Test on distribution shift
   - Check for overfitting to specific examples
```

### Phase 5: Documentation

```markdown
## Circuit Documentation

**Circuit Name**: [Descriptive name]
**Model**: [Model name and version]
**Behavior**: [What it computes]
**Confidence**: [High/Medium/Low]

### Components
| Component | Type | Role | Evidence |
|-----------|------|------|----------|
| [Head] | Attention | [Role] | [How verified] |
| [MLP] | MLP | [Role] | [How verified] |

### Mechanism Description
[Step-by-step explanation of computation]

### Evidence Summary
- Activation patching: [Results]
- Ablation studies: [Results]
- Feature steering: [Results]

### Limitations
- [What we don't understand]
- [Potential alternative explanations]
- [Generalization concerns]

### Safety Implications
- [How this relates to safety]
- [Potential misuse concerns]
- [Monitoring recommendations]
```

## Tools and Libraries

### TransformerLens

Primary tool for MI research:

```python
# TransformerLens example workflow
from transformer_lens import HookedTransformer
import torch

# Load model with hooks
model = HookedTransformer.from_pretrained("gpt2")

# Cache activations
prompt = "The Eiffel Tower is in"
logits, cache = model.run_with_cache(prompt)

# Analyze attention patterns
attention = cache["attn", 0]  # Layer 0 attention

# Run activation patching
def patch_hook(activation, hook):
    # Modify activation
    return activation

# Apply hook
model.run_with_hooks(prompt, fwd_hooks=[("blocks.0.attn.hook_attn", patch_hook)])
```

### Other Essential Tools

```yaml
interpretability_toolkit:
  core_tools:
    - TransformerLens: "Main MI library for transformers"
    - nnsight: "Neural network inspection and intervention"
    - Pyvene: "Intervention-based interpretability"
    - Baukit: "Activation editing and analysis"
    
  visualization:
    - CircuitsVis: "Interactive circuit visualization"
    - BertViz: "Attention pattern visualization"
    - Ecco: "NLP model exploration"
    
  feature_analysis:
    - dictionary_learning: "Sparse autoencoder training"
    - captum: "PyTorch interpretability"
    - shap: "Feature attribution"
    
  datasets:
    - CounterFact: "Factual association editing"
    - IOI: "Indirect object identification"
    - Greater-Than: "Numerical reasoning"
```

## Safety Applications

### Finding Safety-Relevant Features

```python
safety_feature_discovery = {
    "objectives": [
        "Identify features that activate for harmful content",
        "Find features that enable/disable safety behaviors",
        "Discover deception-related representations",
        "Locate goal-relevant features"
    ],
    "methods": [
        "Train SAEs and examine feature activations on harmful/safe content",
        "Probe for safety-relevant concepts",
        "Trace circuits for refusal behavior",
        "Compare aligned vs unaligned model internals"
    ],
    "applications": [
        "Feature-based content filtering",
        "Activation steering for safety",
        "Jailbreak detection via internal monitoring",
        "Alignment verification through transparency"
    ]
}
```

### Activation Steering for Safety

```python
activation_steering_safety = {
    "concept": "Modify activations to enhance safety behaviors",
    "methods": [
        "Contrastive activation addition",
        "Representation engineering",
        "Feature amplification/suppression",
        "Activation patching for safety"
    ],
    "applications": [
        "Reduce harmful outputs without fine-tuning",
        "Enhance honesty and calibration",
        "Improve refusal behavior",
        "Mitigate bias and unfairness"
    ],
    "cautions": [
        "May reduce overall capability",
        "Could create false sense of security",
        "Needs comprehensive evaluation",
        "May not generalize to novel attacks"
    ]
}
```

## Integration with Other Skills

```
1. Use experiment-tracker:
   - Log interpretability experiments
   - Track analysis iterations
   
2. Use mechanistic-interpretability (THIS SKILL):
   - Conduct MI analysis
   - Discover circuits and features
   
3. Use safety-alignment-researcher:
   - Apply findings to safety evaluation
   - Verify alignment through transparency
   
4. Use benchmark-creator:
   - Create interpretability benchmarks
   - Track analysis accuracy
   
5. Use memory-manager:
   - Store circuit discoveries
   - Link to architectures
```

## Knowledge Graph Integration

```cypher
// Store circuit discovery
CREATE (c:Circuit {
  id: 'circuit_001',
  name: 'Indirect Object Identification',
  model: 'gpt2-small',
  behavior: 'Identifies indirect objects in sentences',
  confidence: 0.85,
  discovered_date: datetime()
})

// Link components
CREATE (h:AttentionHead {
  layer: 5,
  head: 5,
  role: 'Name Mover Head'
})
CREATE (c)-[:INCLUDES]->(h)

// Link to architecture analysis
MATCH (a:Architecture {name: 'OMEGA_ASI_v550'})
CREATE (c)-[:ANALYZED_IN]->(a)
```

## Best Practices

1. **Start Simple**: Begin with minimal examples and well-understood behaviors
2. **Validate Extensively**: Use multiple methods to verify findings
3. **Document Uncertainty**: Be clear about what you don't understand
4. **Consider Alternatives**: Look for alternative explanations
5. **Check Generalization**: Test findings on diverse examples
6. **Stay Current**: Follow latest MI research (fast-moving field)
7. **Collaborate**: Share findings and methods with community
8. **Safety First**: Consider implications for safety research

## Resources

### Key Papers
- "A Mathematical Framework for Transformer Circuits" (Elhage et al.)
- "Interpretability in the Wild" (Wang et al.)
- "Scaling Monosemanticity" (Anthropic)
- "Towards Monosemanticity" (Anthropic)
- "Mechanistic Interpretability for AI Safety: A Review"

### Communities
- Alignment Forum (Mechanistic Interpretability tag)
- MATS Program (MI stream)
- EleutherAI interpretability group
- Anthropic research blog

### Tutorials
- Neel Nanda's MI tutorials
- TransformerLens documentation
- 200 Concrete Open Problems in MI
- ARENA 3.0 MI curriculum

## Version History

- **v1.0.0** (2026-01-31): Initial release with comprehensive MI frameworks, circuit analysis protocols, and safety applications

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

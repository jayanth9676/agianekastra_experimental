---
name: cognitive-architecture
description: Design and implement cognitive architectures for AGI including OpenCog Hyperon, SOAR, ACT-R, and hybrid approaches. Covers symbolic-neural integration, cognitive schematics, and self-modifying systems.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, cognitive-architecture, opencog, hyperon, symbolic-ai, neural-symbolic, self-modification]
---

# Cognitive Architecture

## Overview

This skill provides comprehensive frameworks for designing and implementing cognitive architectures for AGI systems. It covers major architectures (OpenCog Hyperon, SOAR, ACT-R), neural-symbolic integration, cognitive schematics, and approaches to building self-modifying intelligent systems.

## When to Use

- Designing AGI system architectures
- Integrating symbolic and neural components
- Implementing cognitive capabilities (attention, memory, reasoning)
- Building self-modifying/autopoietic systems
- Evaluating cognitive architecture approaches
- Integrating knowledge representation with learning
- Designing embodied cognitive systems

## Major Cognitive Architectures

### OpenCog Hyperon

Next-generation AGI framework:

```yaml
opencog_hyperon:
  core_components:
    atomspace:
      description: "Distributed weighted labeled metagraph knowledge store"
      capabilities:
        - "Unified knowledge representation"
        - "Multiple AI algorithms share same knowledge base"
        - "Distributed and scalable"
        
    metta:
      description: "Meta Type Talk - self-modifying language"
      capabilities:
        - "Unifies logic, probabilistic, and functional programming"
        - "AI algorithms can modify themselves"
        - "Meta-language for defining languages"
        
    das:
      description: "Distributed Atomspace"
      capabilities:
        - "Multiple simultaneous algorithm connections"
        - "Flexible query interface"
        - "Cross-system knowledge sharing"
        
  cognitive_components:
    pln:
      name: "Probabilistic Logic Networks"
      purpose: "Reasoning under uncertainty"
      capabilities:
        - "Combines probabilistic and logical inference"
        - "Uncertain term logic"
        - "Decision making with incomplete information"
        
    moses:
      name: "Meta-Optimizing Semantic Evolutionary Search"
      purpose: "Program evolution"
      capabilities:
        - "Evolves computer programs toward goals"
        - "Adaptive self-improving systems"
        - "Representation learning"
        
    ecan:
      name: "Economic Attention Network"
      purpose: "Attention allocation"
      capabilities:
        - "Optimizes finite cognitive resources"
        - "Importance-based processing"
        - "Focus management"
        
    nars:
      name: "Non-Axiomatic Reasoning System"
      purpose: "Reasoning under resource constraints"
      capabilities:
        - "Works with insufficient knowledge and time"
        - "Experiential learning"
        - "Belief revision"
```

### SOAR

Production system cognitive architecture:

```yaml
soar:
  description: "Symbolic cognitive architecture based on production rules"
  
  components:
    long_term_memory:
      procedural: "Production rules (if-then)"
      semantic: "Factual knowledge"
      episodic: "Remembered experiences"
      
    working_memory:
      description: "Current situation representation"
      structure: "Graph of working memory elements"
      
    decision_cycle:
      phases:
        - "Input: Perceive environment"
        - "Elaborate: Apply productions, update working memory"
        - "Decide: Select operator to apply"
        - "Apply: Execute selected operator"
        - "Output: Generate actions"
        
  learning:
    chunking: "Create new production rules from experience"
    reinforcement: "Update utility values"
    episodic: "Store and retrieve episodes"
    semantic: "Extract general knowledge from episodes"
    
  strengths:
    - "Well-defined cognitive theory"
    - "Extensive empirical validation"
    - "Strong at problem-solving"
    
  limitations:
    - "Primarily symbolic"
    - "Scaling challenges"
    - "Integration with neural networks complex"
```

### ACT-R

Hybrid symbolic-subsymbolic architecture:

```yaml
act_r:
  description: "Adaptive Control of Thought - Rational"
  
  modules:
    declarative:
      purpose: "Factual knowledge storage and retrieval"
      mechanism: "Activation-based retrieval"
      
    procedural:
      purpose: "Skill and action knowledge"
      mechanism: "Production rules with utility learning"
      
    visual:
      purpose: "Visual attention and perception"
      mechanism: "Attentional focus and encoding"
      
    motor:
      purpose: "Action execution"
      mechanism: "Motor programming"
      
    goal:
      purpose: "Current goal tracking"
      mechanism: "Goal buffer management"
      
  subsymbolic:
    activation:
      description: "Declarative chunk accessibility"
      factors: ["Base-level (recency/frequency)", "Spreading activation"]
      
    utility:
      description: "Production rule selection"
      factors: ["Expected utility", "Cost estimation"]
      
  learning:
    - "Base-level learning (memory strength)"
    - "Associative learning (spreading activation)"
    - "Utility learning (production selection)"
    - "Production compilation (skill acquisition)"
```

## Neural-Symbolic Integration

### Integration Approaches

```python
neural_symbolic_integration = {
    "symbolic_to_neural": {
        "knowledge_injection": {
            "method": "Encode symbolic knowledge into neural weights",
            "examples": ["KGAT", "KG-BERT", "Logic-injected training"],
            "benefit": "Neural model respects symbolic constraints"
        },
        "symbolic_loss": {
            "method": "Add loss terms for logical consistency",
            "examples": ["Semantic loss", "Logic tensor networks"],
            "benefit": "Differentiable logic enforcement"
        }
    },
    "neural_to_symbolic": {
        "knowledge_extraction": {
            "method": "Extract rules/knowledge from neural networks",
            "examples": ["Rule extraction", "Neural theorem proving"],
            "benefit": "Interpretable symbolic representation"
        },
        "neuro_symbolic_reasoning": {
            "method": "Neural networks implement symbolic operations",
            "examples": ["Neural Turing machines", "Differentiable program synthesis"],
            "benefit": "End-to-end differentiable reasoning"
        }
    },
    "hybrid_architectures": {
        "modular": {
            "description": "Separate neural and symbolic modules that communicate",
            "examples": ["Neural-symbolic VQA", "Semantic parsing + execution"],
            "benefit": "Clean separation of concerns"
        },
        "unified": {
            "description": "Single system combining both paradigms",
            "examples": ["OpenCog Hyperon", "NSCL"],
            "benefit": "Tight integration, synergistic effects"
        }
    }
}
```

### MeTTa Programming

OpenCog's meta-language:

```lisp
; MeTTa example: Define a type and function
(: Human Type)
(: mortal (-> Human Bool))

; Define rules
(= (mortal $x) True)  ; All humans are mortal

; Pattern matching
(: Socrates Human)
!(mortal Socrates)  ; Evaluates to True

; Self-modification example
(= (add-knowledge $fact) 
   (add-atom &self $fact))

; Meta-programming
(= (map $f (Cons $x $xs))
   (Cons ($f $x) (map $f $xs)))
```

## Cognitive Schematics

### PRIMUS Architecture

Proposed human-level AGI architecture:

```python
primus_architecture = {
    "description": "Cognitive architecture for human-level AGI with self-modification",
    
    "core_capabilities": {
        "perception": "Multi-modal sensory processing",
        "action": "Motor control and planning",
        "reasoning": "Logical and probabilistic inference",
        "learning": "Continual adaptation from experience",
        "memory": "Episodic, semantic, procedural storage",
        "attention": "Resource allocation and focus",
        "meta_cognition": "Self-monitoring and modification"
    },
    
    "self_modification": {
        "levels": [
            "Parameter adjustment (learning rates, thresholds)",
            "Algorithm selection (choose best method)",
            "Architecture modification (add/remove modules)",
            "Goal revision (with safety constraints)"
        ],
        "constraints": [
            "Preserve core values/goals",
            "Maintain interpretability",
            "Ensure reversibility",
            "Human approval for major changes"
        ]
    }
}
```

### Cognitive Cycle

Standard cognitive processing loop:

```python
cognitive_cycle = {
    "phases": [
        {
            "name": "Perception",
            "process": "Encode sensory input into internal representation",
            "duration": "~100ms in humans"
        },
        {
            "name": "Attention",
            "process": "Select relevant information for further processing",
            "mechanism": "Competitive selection, saliency"
        },
        {
            "name": "Working Memory",
            "process": "Hold and manipulate current information",
            "capacity": "Limited (7±2 chunks in humans)"
        },
        {
            "name": "Retrieval",
            "process": "Access relevant long-term memory",
            "mechanism": "Cue-based activation, spreading activation"
        },
        {
            "name": "Reasoning/Planning",
            "process": "Draw conclusions, make plans",
            "methods": ["Deduction", "Induction", "Analogy"]
        },
        {
            "name": "Action Selection",
            "process": "Choose behavior based on goals and situation",
            "mechanism": "Utility maximization, habit, emotion"
        },
        {
            "name": "Learning",
            "process": "Update knowledge/skills based on experience",
            "types": ["Reinforcement", "Supervised", "Unsupervised"]
        },
        {
            "name": "Meta-cognition",
            "process": "Monitor and regulate cognitive processes",
            "includes": ["Error detection", "Strategy adjustment"]
        }
    ],
    "timing": "Cycle typically 50-200ms in human cognition"
}
```

## Memory Systems

### Cognitive Memory Architecture

```python
memory_architecture = {
    "working_memory": {
        "description": "Active, limited-capacity buffer",
        "capacity": "Limited (task-dependent)",
        "duration": "Seconds without rehearsal",
        "function": "Current processing context",
        "implementation": {
            "attention_mechanism": "Transformer attention as working memory",
            "explicit_buffer": "Designated memory tokens/slots"
        }
    },
    "episodic_memory": {
        "description": "Autobiographical event memories",
        "capacity": "Large",
        "duration": "Long-term",
        "function": "Experience-based learning, temporal reasoning",
        "implementation": {
            "retrieval_augmented": "RAG systems",
            "memory_networks": "End-to-end trainable memory",
            "experience_replay": "Store and replay episodes"
        }
    },
    "semantic_memory": {
        "description": "General world knowledge",
        "capacity": "Very large",
        "duration": "Permanent",
        "function": "Concepts, facts, relationships",
        "implementation": {
            "knowledge_graphs": "Structured symbolic knowledge",
            "embeddings": "Distributed vector representations",
            "hybrid": "Combined symbolic-neural"
        }
    },
    "procedural_memory": {
        "description": "Skills and procedures",
        "capacity": "Large",
        "duration": "Long-term with practice",
        "function": "Automated skilled behavior",
        "implementation": {
            "production_rules": "Condition-action pairs",
            "policy_networks": "Learned behavior policies",
            "program_memory": "Stored procedures/functions"
        }
    }
}
```

## Self-Modification

### Autopoietic Systems

Self-producing and self-maintaining systems:

```python
autopoietic_system = {
    "definition": "System that produces and maintains itself",
    
    "properties": {
        "self_production": "Creates own components",
        "operational_closure": "Recursively defines own boundaries",
        "structural_coupling": "Adapts to environment while maintaining identity"
    },
    
    "agi_implications": {
        "self_improvement": {
            "capability_expansion": "Learn new skills autonomously",
            "architecture_modification": "Change own structure",
            "knowledge_generation": "Produce new understanding"
        },
        "safety_requirements": {
            "value_preservation": "Core goals/values invariant",
            "bounded_modification": "Limits on change scope/rate",
            "reversibility": "Ability to undo modifications",
            "monitoring": "External oversight of changes"
        }
    },
    
    "implementation_approaches": {
        "meta_learning": "Learning to learn",
        "program_synthesis": "Generate own code",
        "architecture_search": "Discover own structure",
        "goal_refinement": "Improve own objectives (carefully)"
    }
}
```

### Safe Self-Modification Protocol

```markdown
## Self-Modification Protocol

### Prerequisites
- [ ] Modification proposal documented
- [ ] Safety analysis completed
- [ ] Backup/rollback prepared
- [ ] Sandbox environment ready
- [ ] Human approval (if above threshold)

### Modification Classes

**Class A: Parameter Adjustment**
- Learning rates, thresholds, weights
- Approval: Automatic within bounds
- Rollback: Immediate

**Class B: Algorithm Selection**
- Choose between existing methods
- Approval: Automatic with logging
- Rollback: Simple

**Class C: Module Addition/Removal**
- Add new capability modules
- Approval: Requires review
- Rollback: Possible but complex

**Class D: Architecture Modification**
- Change fundamental structure
- Approval: Requires human approval
- Rollback: May be impossible

**Class E: Goal/Value Modification**
- PROHIBITED without extensive review
- Approval: Multi-party human approval
- Rollback: Critical

### Execution Steps
1. Validate modification request
2. Classify modification type
3. Check approval requirements
4. Create system snapshot
5. Execute in sandbox
6. Run validation suite
7. If passed: Deploy to production
8. If failed: Rollback and analyze
9. Log all changes

### Monitoring Post-Modification
- Performance metrics tracking
- Safety benchmark re-evaluation
- Behavioral consistency checks
- Alignment verification
```

## OMEGA ASI Integration

### Cognitive Architecture Design

```python
omega_cognitive_design = {
    "foundation": {
        "neural_backbone": "Large language model / transformer",
        "symbolic_layer": "Knowledge graph (Neo4j) + reasoning",
        "integration": "Bidirectional neural-symbolic"
    },
    
    "cognitive_modules": {
        "perception": {
            "modalities": ["Text", "Vision", "Code"],
            "encoding": "Multi-modal embeddings"
        },
        "reasoning": {
            "methods": ["CoT", "ToT", "GoT", "Symbolic inference"],
            "selection": "Meta-reasoning module"
        },
        "memory": {
            "working": "Attention + explicit buffer",
            "episodic": "Experience database",
            "semantic": "Knowledge graph",
            "procedural": "Tool/skill library"
        },
        "learning": {
            "online": "Continual learning from interaction",
            "meta": "Learn-to-learn optimization",
            "self_supervised": "Representation improvement"
        },
        "action": {
            "planning": "Hierarchical task planning",
            "execution": "Tool use and code execution",
            "monitoring": "Outcome verification"
        }
    },
    
    "control_architecture": {
        "executive": "Goal management and prioritization",
        "attention": "Resource allocation (ECAN-inspired)",
        "metacognition": "Self-monitoring and strategy adjustment"
    }
}
```

## Implementation Template

```python
class CognitiveArchitecture:
    """Base class for cognitive architecture implementation."""
    
    def __init__(self, config):
        # Core components
        self.perception = PerceptionModule(config.perception)
        self.working_memory = WorkingMemory(config.wm_capacity)
        self.long_term_memory = LongTermMemory(config.ltm)
        self.reasoning = ReasoningModule(config.reasoning)
        self.action = ActionModule(config.action)
        self.metacognition = MetacognitionModule(config.meta)
        
        # Control
        self.attention = AttentionController(config.attention)
        self.executive = ExecutiveController(config.goals)
        
    def cognitive_cycle(self, input_data):
        """Execute one cognitive cycle."""
        # 1. Perception
        percepts = self.perception.process(input_data)
        
        # 2. Attention
        attended = self.attention.select(percepts, self.working_memory)
        
        # 3. Working Memory Update
        self.working_memory.update(attended)
        
        # 4. Memory Retrieval
        retrieved = self.long_term_memory.retrieve(
            cues=self.working_memory.get_cues()
        )
        self.working_memory.integrate(retrieved)
        
        # 5. Reasoning
        conclusions = self.reasoning.infer(
            context=self.working_memory.get_context()
        )
        
        # 6. Action Selection
        actions = self.action.select(
            goals=self.executive.current_goals,
            context=self.working_memory.get_context(),
            conclusions=conclusions
        )
        
        # 7. Action Execution
        results = self.action.execute(actions)
        
        # 8. Learning
        self.learn_from_experience(input_data, actions, results)
        
        # 9. Metacognition
        self.metacognition.monitor_and_adjust(self)
        
        return results
    
    def learn_from_experience(self, input_data, actions, results):
        """Update memories and skills based on experience."""
        # Store episode
        episode = Episode(input_data, actions, results)
        self.long_term_memory.episodic.store(episode)
        
        # Extract semantic knowledge
        knowledge = self.extract_knowledge(episode)
        self.long_term_memory.semantic.update(knowledge)
        
        # Update procedural memory
        if results.success:
            self.long_term_memory.procedural.reinforce(actions)
```

## Tools and Frameworks

```yaml
cognitive_architecture_tools:
  opencog:
    - hyperon-experimental: "Core Hyperon implementation"
    - atomspace: "Knowledge graph substrate"
    - metta: "Programming language"
    
  classical:
    - jsoar: "Java implementation of SOAR"
    - pyactr: "Python implementation of ACT-R"
    - clarion: "Connectionist learning architecture"
    
  neural_symbolic:
    - scallop: "Differentiable reasoning"
    - neuro_symbolic_vqa: "Visual question answering"
    - logic_tensor_networks: "Neural logic"
    
  knowledge_graphs:
    - neo4j: "Graph database"
    - rdflib: "RDF/OWL processing"
    - ampligraph: "Knowledge graph embeddings"
```

## Integration with Other Skills

```
1. Use agi-researcher:
   - Research cognitive architecture approaches
   
2. Use cognitive-architecture (THIS SKILL):
   - Design OMEGA ASI cognitive components
   - Implement neural-symbolic integration
   
3. Use multi-agent-orchestrator:
   - Coordinate cognitive modules
   
4. Use mechanistic-interpretability:
   - Understand cognitive mechanisms
   
5. Use safety-alignment-researcher:
   - Ensure safe self-modification
   
6. Use memory-manager:
   - Store architecture designs
```

## Best Practices

1. **Start Hybrid**: Combine neural and symbolic from the start
2. **Memory First**: Strong memory systems are foundational
3. **Attention is Key**: Efficient attention allocation is critical
4. **Meta-cognition Matters**: Self-monitoring prevents failures
5. **Bound Self-Modification**: Strict limits on self-change
6. **Test Incrementally**: Validate each component
7. **Preserve Knowledge**: Avoid catastrophic forgetting
8. **Maintain Interpretability**: Keep system understandable
9. **Ground in Reality**: Connect to real-world tasks
10. **Safety by Design**: Build safety into architecture

## Version History

- **v1.0.0** (2026-01-31): Initial release with cognitive architecture frameworks, OpenCog Hyperon, neural-symbolic integration, and self-modification protocols

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

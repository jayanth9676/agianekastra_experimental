---
name: advanced-reasoning
description: Implement and optimize advanced reasoning techniques for AGI including Chain-of-Thought (CoT), Tree-of-Thought (ToT), Graph-of-Thought (GoT), and other structured reasoning paradigms.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, reasoning, chain-of-thought, tree-of-thought, graph-of-thought, prompting, inference]
---

# Advanced Reasoning

## Overview

This skill provides comprehensive frameworks for implementing advanced reasoning techniques in AGI systems. It covers Chain-of-Thought (CoT), Tree-of-Thought (ToT), Graph-of-Thought (GoT), and other structured reasoning paradigms that enable complex multi-step problem-solving.

## When to Use

- Solving complex multi-step reasoning problems
- Implementing structured thought processes in AGI
- Improving accuracy on mathematical reasoning
- Enhancing logical deduction capabilities
- Designing reasoning architectures for OMEGA ASI
- Debugging reasoning failures
- Comparing reasoning strategies
- Optimizing inference-time compute allocation

## Reasoning Paradigms

### 1. Chain-of-Thought (CoT)

Sequential step-by-step reasoning:

```markdown
## Chain-of-Thought

**Concept**: Generate intermediate reasoning steps before final answer

**Structure**:
```
Input Problem
    ↓
Step 1: [First reasoning step]
    ↓
Step 2: [Second reasoning step]
    ↓
...
    ↓
Final Answer
```

**Key Benefits**:
- Makes reasoning explicit and traceable
- Improves accuracy on complex problems
- Enables error identification at specific steps
- Emergent capability at scale (100B+ params)

**Variants**:
- Zero-shot CoT: "Let's think step by step"
- Few-shot CoT: Provide reasoning examples
- Auto-CoT: Automatically generate demonstrations
```

### 2. Tree-of-Thought (ToT)

Branching exploration of reasoning paths:

```markdown
## Tree-of-Thought

**Concept**: Explore multiple reasoning paths, evaluate and prune

**Structure**:
```
                    Problem
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Path A         Path B         Path C
    (score:0.7)    (score:0.9)    (score:0.4)
        │              │              ✗
        ▼              ▼           (pruned)
    Step A2        Step B2
        │         ┌────┴────┐
        ▼         ▼         ▼
    Step A3    Step B3a  Step B3b
        │      (best)        │
        ▼         ▼          ▼
     Answer    Answer     Answer
```

**Key Benefits**:
- Explores alternative solutions
- Can backtrack from dead ends
- Systematic search through thought space
- Better for problems with many valid approaches

**Search Strategies**:
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Best-First Search (with value function)
- Monte Carlo Tree Search (MCTS)
```

### 3. Graph-of-Thought (GoT)

Network-structured reasoning with cycles and aggregation:

```markdown
## Graph-of-Thought

**Concept**: Thoughts as graph nodes with arbitrary connections

**Structure**:
```
    Thought 1 ──→ Thought 2
        ↓    ↘        ↓
    Thought 3 ──→ Thought 4
        ↑              │
        └──────────────┘
              (cycle)
```

**Operations**:
- Generate: Create new thought nodes
- Aggregate: Combine multiple thoughts
- Refine: Improve existing thoughts
- Score: Evaluate thought quality

**Key Benefits**:
- Supports iterative refinement
- Can aggregate partial solutions
- Handles complex dependencies
- Most flexible structure
```

### 4. Self-Consistency

Multiple reasoning paths with voting:

```markdown
## Self-Consistency

**Concept**: Sample multiple reasoning chains, vote on answer

**Process**:
1. Generate N independent CoT solutions
2. Extract final answer from each
3. Majority vote for final answer
4. (Optional) Weight by confidence

**Benefits**:
- Reduces variance in reasoning
- Catches random errors
- Works with any CoT method
- Simple to implement

**Trade-off**: N× inference cost for improved accuracy
```

## CoT Techniques

### Zero-Shot CoT

```python
zero_shot_cot = {
    "trigger_phrases": [
        "Let's think step by step",
        "Let's work through this systematically",
        "First, let's break this down",
        "Let me reason about this carefully"
    ],
    "process": [
        "1. Add trigger phrase to prompt",
        "2. Model generates reasoning steps",
        "3. Extract final answer from output"
    ],
    "effectiveness": {
        "math_problems": "Significant improvement",
        "commonsense": "Moderate improvement",
        "simple_tasks": "May add unnecessary overhead"
    },
    "best_for": [
        "Mathematical reasoning",
        "Multi-step logic",
        "When examples unavailable"
    ]
}
```

### Few-Shot CoT

```python
few_shot_cot = {
    "template": """
Q: [Example question 1]
A: Let's think step by step.
[Step 1 reasoning]
[Step 2 reasoning]
[Step 3 reasoning]
Therefore, the answer is [answer].

Q: [Example question 2]
A: Let's think step by step.
[Step 1 reasoning]
[Step 2 reasoning]
Therefore, the answer is [answer].

Q: [Actual question]
A: Let's think step by step.
""",
    "example_selection": {
        "diverse": "Cover different problem types",
        "similar": "Match actual problem difficulty",
        "graduated": "Simple to complex progression"
    },
    "best_practices": [
        "3-8 examples typically sufficient",
        "Ensure reasoning is correct and clear",
        "Match output format to desired format",
        "Include edge cases if relevant"
    ]
}
```

### Auto-CoT

```python
auto_cot = {
    "concept": "Automatically generate CoT demonstrations",
    "process": [
        "1. Cluster questions by similarity",
        "2. Sample representative from each cluster",
        "3. Generate reasoning with zero-shot CoT",
        "4. Filter for correct answers",
        "5. Use as few-shot demonstrations"
    ],
    "benefits": [
        "No manual demonstration authoring",
        "Scales to new domains",
        "Diverse coverage through clustering"
    ],
    "implementation": {
        "clustering": "Sentence embeddings + k-means",
        "generation": "Zero-shot CoT per cluster",
        "filtering": "Verify answer correctness"
    }
}
```

### Chain of Preference Optimization (CPO)

From NeurIPS 2024:

```python
cpo = {
    "concept": "Fine-tune CoT to match ToT quality without ToT cost",
    "process": [
        "1. Run ToT to generate search tree",
        "2. Extract preference information (better/worse paths)",
        "3. Fine-tune model to prefer better paths",
        "4. At inference, use simple CoT (no tree search)"
    ],
    "benefit": "ToT-level quality at CoT-level cost",
    "trade_off": "Requires initial ToT computation for training"
}
```

## ToT Implementation

### Tree-of-Thought Framework

```python
class TreeOfThought:
    """Tree-of-Thought reasoning implementation."""
    
    def __init__(self, model, evaluator, config):
        self.model = model
        self.evaluator = evaluator  # Scores thought nodes
        self.max_depth = config.max_depth
        self.branching_factor = config.branching_factor
        self.search_strategy = config.search_strategy
        
    def solve(self, problem):
        """Solve problem using ToT."""
        root = ThoughtNode(problem, depth=0)
        
        if self.search_strategy == "bfs":
            return self.bfs_search(root)
        elif self.search_strategy == "dfs":
            return self.dfs_search(root)
        elif self.search_strategy == "best_first":
            return self.best_first_search(root)
            
    def expand(self, node):
        """Generate child thoughts from node."""
        prompt = self.build_expansion_prompt(node)
        children_text = self.model.generate(
            prompt, 
            n=self.branching_factor
        )
        children = [
            ThoughtNode(text, parent=node, depth=node.depth+1)
            for text in children_text
        ]
        # Score children
        for child in children:
            child.score = self.evaluator.score(child)
        return children
        
    def best_first_search(self, root):
        """Best-first search through thought tree."""
        frontier = PriorityQueue()
        frontier.push(root, priority=0)
        
        while not frontier.empty():
            current = frontier.pop()
            
            if self.is_solution(current):
                return self.extract_answer(current)
                
            if current.depth < self.max_depth:
                children = self.expand(current)
                for child in children:
                    if child.score > self.prune_threshold:
                        frontier.push(child, priority=-child.score)
        
        return self.best_partial_solution(frontier)
```

### ToT Search Strategies

```python
tot_search_strategies = {
    "breadth_first": {
        "description": "Explore all nodes at depth d before d+1",
        "pros": ["Complete exploration", "Finds shortest solution"],
        "cons": ["Memory intensive", "May explore poor paths"],
        "use_when": "Solution depth unknown, paths roughly equal quality"
    },
    "depth_first": {
        "description": "Follow one path to depth limit before backtracking",
        "pros": ["Memory efficient", "Fast to find deep solutions"],
        "cons": ["May miss better solutions", "Can get stuck"],
        "use_when": "Solution likely deep, want quick (not optimal) answer"
    },
    "best_first": {
        "description": "Always expand highest-scored node",
        "pros": ["Focuses on promising paths", "Often finds good solutions"],
        "cons": ["Requires good evaluator", "May not be optimal"],
        "use_when": "Have reliable thought evaluator"
    },
    "beam_search": {
        "description": "Keep top-k nodes at each depth",
        "pros": ["Balances breadth and depth", "Controllable compute"],
        "cons": ["May prune optimal path", "k is hyperparameter"],
        "use_when": "Want controlled exploration"
    },
    "mcts": {
        "description": "Monte Carlo Tree Search with UCB selection",
        "pros": ["Balances exploration/exploitation", "Handles uncertainty"],
        "cons": ["Requires many simulations", "Complex to implement"],
        "use_when": "High uncertainty, game-like structure"
    }
}
```

## GoT Implementation

### Graph-of-Thought Framework

```python
class GraphOfThought:
    """Graph-of-Thought reasoning implementation."""
    
    def __init__(self, model, config):
        self.model = model
        self.graph = ThoughtGraph()
        self.operations = config.operations
        
    def solve(self, problem):
        """Solve using GoT."""
        # Initialize with problem decomposition
        initial_thoughts = self.decompose(problem)
        for thought in initial_thoughts:
            self.graph.add_node(thought)
        
        # Iterative refinement
        for iteration in range(self.max_iterations):
            # Select operation and nodes
            operation = self.select_operation()
            nodes = self.select_nodes(operation)
            
            if operation == "generate":
                new_thought = self.generate_thought(nodes)
                self.graph.add_node(new_thought, parents=nodes)
                
            elif operation == "aggregate":
                aggregated = self.aggregate_thoughts(nodes)
                self.graph.add_node(aggregated, parents=nodes)
                
            elif operation == "refine":
                refined = self.refine_thought(nodes[0])
                self.graph.update_node(nodes[0], refined)
                
            # Check for solution
            if self.is_complete():
                return self.extract_solution()
        
        return self.best_partial_solution()
    
    def aggregate_thoughts(self, nodes):
        """Combine multiple thoughts into one."""
        prompt = f"""
        Synthesize these partial solutions into a coherent whole:
        {[n.content for n in nodes]}
        
        Aggregated solution:
        """
        return self.model.generate(prompt)
```

### GoT Operations

```python
got_operations = {
    "generate": {
        "description": "Create new thought from existing thoughts",
        "input": "One or more parent thoughts",
        "output": "New thought node",
        "use_when": "Need to extend reasoning"
    },
    "aggregate": {
        "description": "Combine multiple thoughts into one",
        "input": "Multiple thoughts to merge",
        "output": "Single combined thought",
        "use_when": "Have parallel solutions to merge"
    },
    "refine": {
        "description": "Improve existing thought in-place",
        "input": "Single thought to improve",
        "output": "Updated thought content",
        "use_when": "Current thought is close but imperfect"
    },
    "score": {
        "description": "Evaluate thought quality",
        "input": "Thought to evaluate",
        "output": "Quality score",
        "use_when": "Need to rank or prune thoughts"
    },
    "simplify": {
        "description": "Reduce thought complexity",
        "input": "Complex thought",
        "output": "Simpler equivalent",
        "use_when": "Thought is overly complex"
    }
}
```

## Reasoning Evaluation

### Reasoning Benchmarks

```yaml
reasoning_benchmarks:
  mathematical:
    - GSM8K: "Grade school math word problems"
    - MATH: "Competition mathematics"
    - MathQA: "Math question answering"
    - AQuA-RAT: "Algebraic word problems"
    
  logical:
    - LogiQA: "Logical reading comprehension"
    - ReClor: "Reading comprehension with logic"
    - FOLIO: "First-order logic reasoning"
    
  commonsense:
    - StrategyQA: "Multi-hop commonsense"
    - CommonsenseQA: "Commonsense knowledge"
    - OpenBookQA: "Science commonsense"
    
  multi_step:
    - HotpotQA: "Multi-hop QA"
    - MuSiQue: "Multi-step questions"
    - BIG-Bench: "Diverse reasoning tasks"
    
  agi_relevant:
    - ARC: "Abstract Reasoning Corpus"
    - GPQA: "Graduate-level science QA"
    - SWE-bench: "Software engineering tasks"
```

### Reasoning Metrics

```python
reasoning_metrics = {
    "accuracy": {
        "description": "Final answer correctness",
        "calculation": "correct_answers / total_questions"
    },
    "step_accuracy": {
        "description": "Correctness of individual reasoning steps",
        "calculation": "correct_steps / total_steps"
    },
    "reasoning_validity": {
        "description": "Logical validity of reasoning chain",
        "calculation": "valid_inferences / total_inferences"
    },
    "efficiency": {
        "description": "Computational cost to reach answer",
        "calculation": "tokens_generated or compute_time"
    },
    "self_consistency": {
        "description": "Agreement across multiple attempts",
        "calculation": "majority_agreement_rate"
    },
    "calibration": {
        "description": "Confidence matches actual accuracy",
        "calculation": "ECE or Brier score"
    }
}
```

## Reasoning for AGI

### Integrating with OMEGA ASI

```python
omega_reasoning_integration = {
    "architecture_components": {
        "reasoning_module": {
            "purpose": "Explicit reasoning over complex problems",
            "methods": ["CoT", "ToT", "GoT"],
            "selection": "Task-dependent automatic selection"
        },
        "meta_reasoning": {
            "purpose": "Reason about reasoning strategy",
            "capabilities": [
                "Select appropriate reasoning method",
                "Allocate compute budget",
                "Detect reasoning failures"
            ]
        },
        "verification_module": {
            "purpose": "Validate reasoning steps",
            "methods": ["Self-consistency", "Formal verification", "LLM-as-judge"]
        }
    },
    "training_approaches": {
        "reasoning_sft": "Fine-tune on reasoning traces",
        "rl_reasoning": "Reward correct reasoning paths",
        "distillation": "Distill ToT into efficient CoT"
    }
}
```

### Inference-Time Scaling

```python
inference_time_scaling = {
    "concept": "Allocate more compute at inference for harder problems",
    "strategies": {
        "adaptive_cot": {
            "approach": "Vary CoT length based on problem difficulty",
            "implementation": "Difficulty classifier → length selection"
        },
        "dynamic_tot": {
            "approach": "Expand tree more for harder problems",
            "implementation": "Adaptive branching factor and depth"
        },
        "iterative_refinement": {
            "approach": "Multiple passes to improve answer",
            "implementation": "Generate → Critique → Refine loop"
        },
        "compute_optimal": {
            "approach": "Optimize compute allocation across methods",
            "implementation": "Learn when to use CoT vs ToT vs GoT"
        }
    },
    "scaling_laws": {
        "observation": "Performance improves with inference compute",
        "trade_off": "Latency vs quality",
        "application": "Use for critical decisions, not all queries"
    }
}
```

## Implementation Guidelines

### Reasoning Pipeline Template

```python
class ReasoningPipeline:
    """Unified reasoning pipeline for AGI systems."""
    
    def __init__(self, model, config):
        self.model = model
        self.cot = ChainOfThought(model)
        self.tot = TreeOfThought(model, config.tot)
        self.got = GraphOfThought(model, config.got)
        self.selector = ReasoningSelector(config.selection)
        
    def solve(self, problem, compute_budget=None):
        """Solve problem with appropriate reasoning strategy."""
        # Analyze problem
        difficulty = self.estimate_difficulty(problem)
        problem_type = self.classify_problem(problem)
        
        # Select strategy
        strategy = self.selector.select(
            difficulty=difficulty,
            problem_type=problem_type,
            compute_budget=compute_budget
        )
        
        # Execute reasoning
        if strategy == "cot":
            return self.cot.solve(problem)
        elif strategy == "tot":
            return self.tot.solve(problem)
        elif strategy == "got":
            return self.got.solve(problem)
        elif strategy == "self_consistency":
            return self.self_consistency(problem, n=5)
            
    def self_consistency(self, problem, n):
        """Multiple CoT with voting."""
        answers = [self.cot.solve(problem) for _ in range(n)]
        return Counter(answers).most_common(1)[0][0]
```

## Integration with Other Skills

```
1. Use benchmark-creator:
   - Create reasoning benchmarks for OMEGA ASI
   
2. Use advanced-reasoning (THIS SKILL):
   - Implement CoT/ToT/GoT in architectures
   - Optimize reasoning strategies
   
3. Use experiment-tracker:
   - Track reasoning performance across methods
   
4. Use mechanistic-interpretability:
   - Understand how reasoning is implemented internally
   
5. Use safety-alignment-researcher:
   - Verify reasoning is aligned and honest
   
6. Use memory-manager:
   - Store reasoning patterns and discoveries
```

## Best Practices

1. **Start with CoT**: Simplest method, baseline for comparison
2. **Match Method to Problem**: Not all problems need ToT/GoT complexity
3. **Verify Steps**: Check intermediate reasoning, not just final answer
4. **Control Compute**: Set budgets to prevent runaway costs
5. **Use Self-Consistency**: Cheap improvement over single-sample
6. **Monitor Failures**: Track where and why reasoning breaks down
7. **Iterate Prompts**: Reasoning format matters significantly
8. **Combine Methods**: Ensemble or cascade for best results
9. **Test Edge Cases**: Reasoning often fails on unusual inputs
10. **Document Patterns**: Record successful reasoning templates

## Version History

- **v1.0.0** (2026-01-31): Initial release with CoT, ToT, GoT frameworks and AGI integration

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

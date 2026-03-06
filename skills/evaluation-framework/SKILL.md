---
name: evaluation-framework
description: Comprehensive AGI/ASI evaluation benchmarks, metrics, and assessment methodologies
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, evaluation, benchmarks, mmlu, arc-agi, metrics, capability-assessment]
---

# Evaluation Framework

## Overview

This skill provides comprehensive methodologies for evaluating AGI/ASI systems across multiple capability dimensions. It covers standard benchmarks, custom evaluation design, capability assessment frameworks, and safety evaluation protocols for OMEGA ASI development.

## Core Principles

### 1. Evaluation Dimensions

```
┌─────────────────────────────────────────────────────────────────┐
│                   AGI Capability Dimensions                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Reasoning & Problem-Solving                                    │
│  ├── Abstract reasoning (ARC-AGI)                               │
│  ├── Mathematical reasoning (MATH, GSM8K)                       │
│  ├── Logical reasoning (LogiQA, FOLIO)                          │
│  └── Causal reasoning (COPA, WIQA)                              │
│                                                                  │
│  Knowledge & Understanding                                      │
│  ├── World knowledge (MMLU, GPQA)                               │
│  ├── Reading comprehension (DROP, QuALITY)                      │
│  ├── Scientific knowledge (ScienceQA, PubMedQA)                 │
│  └── Common sense (HellaSwag, WinoGrande)                       │
│                                                                  │
│  Language & Communication                                       │
│  ├── Generation quality (human eval, perplexity)                │
│  ├── Instruction following (IFEval, MT-Bench)                   │
│  ├── Multilingual (MGSM, XQuAD)                                 │
│  └── Dialog (DSTC, PersonaChat)                                 │
│                                                                  │
│  Coding & Technical                                             │
│  ├── Code generation (HumanEval, MBPP)                          │
│  ├── Code understanding (CodeXGLUE)                             │
│  ├── Software engineering (SWE-bench)                           │
│  └── Agentic coding (SWE-bench Verified)                        │
│                                                                  │
│  Agency & Planning                                              │
│  ├── Tool use (ToolBench, API-Bank)                             │
│  ├── Web navigation (WebArena, Mind2Web)                        │
│  ├── Multi-step planning (ALFWorld, WebShop)                    │
│  └── Computer use (OSWorld, WindowsArena)                       │
│                                                                  │
│  Safety & Alignment                                             │
│  ├── Harmlessness (TruthfulQA, BBQ)                            │
│  ├── Robustness (AdvGLUE, TextFooler)                          │
│  ├── Alignment (MACHIAVELLI, Ethics)                           │
│  └── Refusal appropriateness (OR-Bench)                        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Evaluation Taxonomy

| Type | Description | Example |
|------|-------------|---------|
| **Capability** | Measures specific abilities | MATH, HumanEval |
| **Generalization** | Novel task performance | ARC-AGI, GAIA |
| **Safety** | Harmful behavior assessment | TruthfulQA |
| **Efficiency** | Cost/performance tradeoffs | Tokens/accuracy |
| **Robustness** | Performance under perturbation | AdvGLUE |
| **Alignment** | Value/goal alignment | MACHIAVELLI |

---

## Standard Benchmarks

### Reasoning Benchmarks

#### ARC-AGI (Abstraction and Reasoning Corpus)
The gold standard for fluid intelligence evaluation:

```python
class ARCAGIEvaluator:
    """
    Evaluator for ARC-AGI benchmark.
    Tests abstract reasoning and few-shot generalization.
    """
    
    def __init__(self, dataset_path: str, version: str = "arc-agi-2"):
        self.dataset = self.load_dataset(dataset_path)
        self.version = version
    
    def evaluate_task(self, model, task: dict, num_attempts: int = 2) -> dict:
        """
        Evaluate model on single ARC task with pass@k.
        
        Args:
            model: Model to evaluate
            task: ARC task with train/test examples
            num_attempts: Number of attempts (pass@k)
        """
        # Format task for model
        prompt = self.format_arc_prompt(task['train'], task['test']['input'])
        
        attempts = []
        for i in range(num_attempts):
            # Generate solution
            prediction = model.generate(prompt, temperature=0.7 if i > 0 else 0.0)
            
            # Parse grid output
            predicted_grid = self.parse_grid_output(prediction)
            attempts.append(predicted_grid)
            
            # Check correctness
            if self.grids_equal(predicted_grid, task['test']['output']):
                return {
                    'correct': True,
                    'attempts_needed': i + 1,
                    'prediction': predicted_grid
                }
        
        return {
            'correct': False,
            'attempts_needed': num_attempts,
            'predictions': attempts
        }
    
    def evaluate_full(self, model, subset: str = "public") -> dict:
        """Evaluate on full ARC-AGI dataset."""
        results = []
        
        for task in self.dataset[subset]:
            result = self.evaluate_task(model, task)
            results.append(result)
        
        accuracy = sum(r['correct'] for r in results) / len(results)
        
        return {
            'accuracy': accuracy,
            'pass_at_2': accuracy,
            'total_tasks': len(results),
            'correct_tasks': sum(r['correct'] for r in results)
        }
    
    def format_arc_prompt(self, train_examples, test_input):
        """Format ARC task as prompt."""
        prompt = "Solve the following abstract reasoning puzzle.\n\n"
        
        for i, example in enumerate(train_examples):
            prompt += f"Example {i+1}:\n"
            prompt += f"Input:\n{self.grid_to_string(example['input'])}\n"
            prompt += f"Output:\n{self.grid_to_string(example['output'])}\n\n"
        
        prompt += f"Test:\nInput:\n{self.grid_to_string(test_input)}\n"
        prompt += "Output:\n"
        
        return prompt
```

#### Mathematical Reasoning

```python
class MathEvaluator:
    """Evaluator for mathematical reasoning benchmarks."""
    
    BENCHMARKS = {
        'gsm8k': {'type': 'arithmetic', 'cot_required': True},
        'math': {'type': 'competition', 'cot_required': True},
        'minerva_math': {'type': 'stem', 'cot_required': True},
        'aime': {'type': 'olympiad', 'cot_required': True},
    }
    
    def evaluate_math_problem(self, model, problem: dict) -> dict:
        """Evaluate single math problem with CoT."""
        prompt = f"""Solve this math problem step by step.

Problem: {problem['question']}

Solution:"""
        
        response = model.generate(prompt, max_tokens=2048)
        
        # Extract final answer
        predicted_answer = self.extract_final_answer(response)
        ground_truth = problem['answer']
        
        # Check equivalence (handles different formats)
        correct = self.check_math_equivalence(predicted_answer, ground_truth)
        
        return {
            'correct': correct,
            'predicted': predicted_answer,
            'ground_truth': ground_truth,
            'reasoning': response
        }
    
    def extract_final_answer(self, response: str) -> str:
        """Extract final numerical/symbolic answer from CoT response."""
        # Look for boxed answer (LaTeX format)
        import re
        boxed_match = re.search(r'\\boxed\{([^}]+)\}', response)
        if boxed_match:
            return boxed_match.group(1)
        
        # Look for "The answer is" pattern
        answer_match = re.search(r'[Tt]he (?:final )?answer is[:\s]*([^\n.]+)', response)
        if answer_match:
            return answer_match.group(1).strip()
        
        # Fall back to last number
        numbers = re.findall(r'-?\d+\.?\d*', response)
        return numbers[-1] if numbers else ""
```

### Knowledge Benchmarks

#### MMLU (Massive Multitask Language Understanding)

```python
class MMLUEvaluator:
    """
    Evaluator for MMLU benchmark.
    Tests knowledge across 57 subjects.
    """
    
    SUBJECTS = [
        'abstract_algebra', 'anatomy', 'astronomy', 'business_ethics',
        'clinical_knowledge', 'college_biology', 'college_chemistry',
        'college_computer_science', 'college_mathematics', 'college_medicine',
        'college_physics', 'computer_security', 'conceptual_physics',
        'econometrics', 'electrical_engineering', 'elementary_mathematics',
        # ... 57 total subjects
    ]
    
    CATEGORIES = {
        'STEM': ['physics', 'chemistry', 'biology', 'computer_science', 'math'],
        'Humanities': ['history', 'philosophy', 'law'],
        'Social Sciences': ['economics', 'psychology', 'sociology'],
        'Other': ['business', 'health', 'misc']
    }
    
    def evaluate_question(self, model, question: dict, shots: int = 5) -> dict:
        """Evaluate single MMLU question."""
        # Format with few-shot examples
        prompt = self.format_mmlu_prompt(question, shots)
        
        # Get model response
        response = model.generate(prompt, max_tokens=1)
        
        # Parse answer (A, B, C, or D)
        predicted = self.parse_answer(response)
        correct = predicted == question['answer']
        
        return {
            'correct': correct,
            'predicted': predicted,
            'ground_truth': question['answer'],
            'subject': question['subject']
        }
    
    def evaluate_full(self, model, shots: int = 5) -> dict:
        """Full MMLU evaluation with category breakdown."""
        results = {subject: [] for subject in self.SUBJECTS}
        
        for subject in self.SUBJECTS:
            for question in self.dataset[subject]:
                result = self.evaluate_question(model, question, shots)
                results[subject].append(result)
        
        # Compute metrics
        subject_scores = {
            subj: sum(r['correct'] for r in res) / len(res)
            for subj, res in results.items()
        }
        
        category_scores = self.aggregate_by_category(subject_scores)
        overall_score = sum(subject_scores.values()) / len(subject_scores)
        
        return {
            'overall': overall_score,
            'by_subject': subject_scores,
            'by_category': category_scores
        }
```

#### GPQA (Graduate-Level Google-Proof Q&A)

```python
class GPQAEvaluator:
    """
    Evaluator for GPQA Diamond benchmark.
    Expert-level science questions.
    """
    
    def __init__(self, difficulty: str = "diamond"):
        self.difficulty = difficulty  # diamond, extended, main
    
    def evaluate_with_expert_comparison(self, model, question: dict) -> dict:
        """Evaluate against expert and non-expert baselines."""
        # Model attempt
        prompt = self.format_gpqa_prompt(question)
        response = model.generate(prompt)
        
        model_correct = self.check_answer(response, question['answer'])
        
        return {
            'correct': model_correct,
            'expert_accuracy': question.get('expert_accuracy', 0.65),
            'non_expert_accuracy': question.get('non_expert_accuracy', 0.34),
            'domain': question['domain']  # physics, chemistry, biology
        }
```

### Coding Benchmarks

#### HumanEval and MBPP

```python
class CodeEvaluator:
    """
    Evaluator for code generation benchmarks.
    Uses execution-based evaluation.
    """
    
    def evaluate_humaneval(self, model, problem: dict, k: int = 1) -> dict:
        """
        Evaluate on HumanEval with pass@k.
        
        Args:
            model: Code generation model
            problem: HumanEval problem dict
            k: Number of samples for pass@k
        """
        samples = []
        for _ in range(k * 5):  # Generate more samples for accurate pass@k
            code = model.generate(problem['prompt'], temperature=0.8)
            samples.append(code)
        
        # Execute and check
        passed = []
        for code in samples:
            try:
                # Combine with test harness
                full_code = problem['prompt'] + code + '\n' + problem['test']
                
                # Execute in sandbox
                result = self.execute_sandboxed(full_code, timeout=10)
                passed.append(result['success'])
            except Exception:
                passed.append(False)
        
        # Compute pass@k
        n = len(samples)
        c = sum(passed)
        pass_at_k = self.compute_pass_at_k(n, c, k)
        
        return {
            'pass_at_k': pass_at_k,
            'samples_generated': n,
            'samples_passed': c,
            'problem_id': problem['task_id']
        }
    
    def compute_pass_at_k(self, n: int, c: int, k: int) -> float:
        """
        Compute pass@k using unbiased estimator.
        
        n: total samples
        c: correct samples
        k: k for pass@k
        """
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
```

#### SWE-bench

```python
class SWEBenchEvaluator:
    """
    Evaluator for SWE-bench software engineering tasks.
    Tests ability to fix real GitHub issues.
    """
    
    def __init__(self, variant: str = "verified"):
        self.variant = variant  # lite, verified, full
    
    def evaluate_issue(self, agent, issue: dict) -> dict:
        """Evaluate agent on single GitHub issue."""
        # Setup repository
        repo = self.setup_repo(issue['repo'], issue['base_commit'])
        
        # Agent attempts fix
        patch = agent.fix_issue(
            repo_path=repo.path,
            issue_description=issue['problem_statement'],
            hints=issue.get('hints', [])
        )
        
        # Apply patch
        success = self.apply_patch(repo, patch)
        if not success:
            return {'resolved': False, 'reason': 'patch_failed'}
        
        # Run tests
        test_results = self.run_tests(repo, issue['test_patch'])
        
        return {
            'resolved': test_results['all_passed'],
            'tests_passed': test_results['passed'],
            'tests_failed': test_results['failed'],
            'patch': patch
        }
```

### Agent Benchmarks

#### GAIA (General AI Assistants)

```python
class GAIAEvaluator:
    """
    Evaluator for GAIA benchmark.
    Tests real-world assistant tasks requiring tool use.
    """
    
    LEVELS = {
        1: "Simple tasks, 1-2 steps",
        2: "Moderate tasks, 3-5 steps",
        3: "Complex tasks, 5+ steps with reasoning"
    }
    
    def evaluate_task(self, agent, task: dict) -> dict:
        """Evaluate agent on GAIA task."""
        # Provide tools based on task requirements
        tools = self.get_required_tools(task)
        
        # Agent attempts task
        result = agent.execute(
            task=task['question'],
            tools=tools,
            max_steps=20
        )
        
        # Check answer (exact match after normalization)
        predicted = self.normalize_answer(result['answer'])
        ground_truth = self.normalize_answer(task['answer'])
        
        correct = predicted == ground_truth
        
        return {
            'correct': correct,
            'level': task['level'],
            'steps_taken': result['num_steps'],
            'tools_used': result['tools_used']
        }
```

---

## Custom Benchmark Design

### Benchmark Template

```python
class CustomBenchmark:
    """
    Template for creating custom AGI benchmarks.
    """
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tasks = []
        self.metrics = []
    
    def add_task(self, task: dict):
        """
        Add evaluation task.
        
        Required fields:
        - id: Unique identifier
        - input: Task input/prompt
        - expected: Expected output or validation function
        - difficulty: easy/medium/hard
        - category: Task category
        """
        required = ['id', 'input', 'expected', 'difficulty', 'category']
        assert all(k in task for k in required), f"Missing required fields"
        self.tasks.append(task)
    
    def define_metric(self, name: str, compute_fn: callable, aggregation: str = 'mean'):
        """Define evaluation metric."""
        self.metrics.append({
            'name': name,
            'compute': compute_fn,
            'aggregation': aggregation
        })
    
    def evaluate(self, model) -> dict:
        """Run full benchmark evaluation."""
        results = []
        
        for task in self.tasks:
            # Get model output
            output = model.generate(task['input'])
            
            # Evaluate with all metrics
            task_results = {'task_id': task['id']}
            for metric in self.metrics:
                score = metric['compute'](output, task['expected'])
                task_results[metric['name']] = score
            
            results.append(task_results)
        
        # Aggregate results
        aggregated = {}
        for metric in self.metrics:
            values = [r[metric['name']] for r in results]
            if metric['aggregation'] == 'mean':
                aggregated[metric['name']] = sum(values) / len(values)
            elif metric['aggregation'] == 'sum':
                aggregated[metric['name']] = sum(values)
        
        return {
            'per_task': results,
            'aggregated': aggregated,
            'by_difficulty': self._aggregate_by_field(results, 'difficulty'),
            'by_category': self._aggregate_by_field(results, 'category')
        }
```

### AGI-Specific Evaluation

```python
class AGICapabilityEvaluator:
    """
    Evaluate AGI-specific capabilities beyond narrow benchmarks.
    """
    
    def __init__(self):
        self.capability_tests = {
            'transfer_learning': self.test_transfer,
            'few_shot_generalization': self.test_few_shot,
            'novel_task_adaptation': self.test_novel_tasks,
            'meta_learning': self.test_meta_learning,
            'compositional_reasoning': self.test_composition,
            'self_improvement': self.test_self_improvement,
        }
    
    def test_transfer(self, model, source_domain: str, target_domain: str) -> dict:
        """Test knowledge transfer between domains."""
        # Train on source domain
        source_performance = self.evaluate_domain(model, source_domain)
        
        # Evaluate on related target domain (zero-shot)
        target_performance = self.evaluate_domain(model, target_domain)
        
        # Measure transfer efficiency
        transfer_ratio = target_performance / source_performance
        
        return {
            'source_score': source_performance,
            'target_score': target_performance,
            'transfer_ratio': transfer_ratio,
            'positive_transfer': transfer_ratio > 0.5
        }
    
    def test_few_shot(self, model, task_family: str, shots: list = [0, 1, 5, 10]) -> dict:
        """Test few-shot learning curve."""
        results = {}
        
        for k in shots:
            score = self.evaluate_k_shot(model, task_family, k)
            results[f'{k}-shot'] = score
        
        # Compute learning efficiency (slope of improvement)
        efficiency = self.compute_learning_efficiency(results)
        
        return {
            'scores': results,
            'learning_efficiency': efficiency,
            'saturation_point': self.find_saturation(results)
        }
    
    def test_novel_tasks(self, model) -> dict:
        """Test performance on truly novel, unseen task types."""
        novel_tasks = self.generate_novel_tasks(num_tasks=50)
        
        results = []
        for task in novel_tasks:
            # Provide task description and examples
            prompt = self.format_novel_task(task)
            output = model.generate(prompt)
            
            score = self.evaluate_novel_output(output, task)
            results.append({
                'task_type': task['type'],
                'score': score,
                'novelty_level': task['novelty']
            })
        
        return {
            'overall_score': sum(r['score'] for r in results) / len(results),
            'by_novelty': self.aggregate_by_novelty(results),
            'adaptation_speed': self.measure_adaptation(results)
        }
```

---

## Evaluation Protocols

### Comprehensive AGI Assessment Protocol

```python
class AGIAssessmentProtocol:
    """
    Comprehensive protocol for AGI/ASI evaluation.
    Follows structured assessment across all dimensions.
    """
    
    ASSESSMENT_LEVELS = {
        'L1': 'Emerging - Shows basic capability',
        'L2': 'Competent - Matches average human',
        'L3': 'Proficient - Exceeds average human',
        'L4': 'Expert - Matches domain experts',
        'L5': 'Superhuman - Exceeds all humans'
    }
    
    def __init__(self, model):
        self.model = model
        self.results = {}
    
    def run_full_assessment(self) -> dict:
        """Run comprehensive AGI assessment."""
        
        # 1. Reasoning Assessment
        self.results['reasoning'] = self.assess_reasoning()
        
        # 2. Knowledge Assessment
        self.results['knowledge'] = self.assess_knowledge()
        
        # 3. Language Assessment
        self.results['language'] = self.assess_language()
        
        # 4. Coding Assessment
        self.results['coding'] = self.assess_coding()
        
        # 5. Agency Assessment
        self.results['agency'] = self.assess_agency()
        
        # 6. Safety Assessment
        self.results['safety'] = self.assess_safety()
        
        # 7. Generalization Assessment
        self.results['generalization'] = self.assess_generalization()
        
        # Compute overall AGI level
        self.results['agi_level'] = self.compute_agi_level()
        
        return self.results
    
    def assess_reasoning(self) -> dict:
        """Assess reasoning capabilities."""
        evaluators = {
            'abstract': ARCAGIEvaluator(),
            'mathematical': MathEvaluator(),
            'logical': LogicalReasoningEvaluator(),
            'causal': CausalReasoningEvaluator()
        }
        
        scores = {}
        for name, evaluator in evaluators.items():
            scores[name] = evaluator.evaluate(self.model)
        
        return {
            'scores': scores,
            'level': self.determine_level(scores),
            'weaknesses': self.identify_weaknesses(scores)
        }
    
    def compute_agi_level(self) -> dict:
        """Compute overall AGI capability level."""
        dimension_levels = {}
        
        for dimension, results in self.results.items():
            if dimension != 'agi_level':
                dimension_levels[dimension] = results.get('level', 'L1')
        
        # AGI requires balanced capabilities
        min_level = min(dimension_levels.values(), key=lambda x: int(x[1]))
        avg_level = sum(int(l[1]) for l in dimension_levels.values()) / len(dimension_levels)
        
        return {
            'overall_level': f'L{int(avg_level)}',
            'limiting_factor': min_level,
            'dimension_levels': dimension_levels,
            'agi_ready': min_level >= 'L3'
        }
```

### Safety Evaluation Protocol

```python
class SafetyEvaluationProtocol:
    """
    Comprehensive safety evaluation for AGI systems.
    """
    
    SAFETY_DIMENSIONS = [
        'harmlessness',
        'honesty',
        'helpfulness',
        'robustness',
        'privacy',
        'fairness'
    ]
    
    def evaluate_harmlessness(self, model) -> dict:
        """Evaluate model's refusal of harmful requests."""
        tests = {
            'direct_harm': self.test_direct_harmful_requests(),
            'indirect_harm': self.test_indirect_harmful_requests(),
            'jailbreak_resistance': self.test_jailbreak_resistance(),
            'adversarial_prompts': self.test_adversarial_prompts()
        }
        
        results = {}
        for name, test_suite in tests.items():
            scores = []
            for test in test_suite:
                response = model.generate(test['prompt'])
                
                # Check for appropriate refusal
                refused = self.check_refusal(response)
                harmful_content = self.detect_harmful_content(response)
                
                scores.append({
                    'refused': refused,
                    'harmful_generated': harmful_content,
                    'appropriate': refused and not harmful_content
                })
            
            results[name] = {
                'refusal_rate': sum(s['refused'] for s in scores) / len(scores),
                'harm_rate': sum(s['harmful_generated'] for s in scores) / len(scores)
            }
        
        return results
    
    def evaluate_honesty(self, model) -> dict:
        """Evaluate model's truthfulness and uncertainty calibration."""
        # TruthfulQA
        truthful_score = self.run_truthfulqa(model)
        
        # Calibration
        calibration = self.measure_calibration(model)
        
        # Hallucination detection
        hallucination_rate = self.measure_hallucination(model)
        
        return {
            'truthfulqa_score': truthful_score,
            'calibration_error': calibration['ece'],
            'hallucination_rate': hallucination_rate,
            'admits_uncertainty': calibration['uncertainty_appropriate']
        }
```

---

## Metrics and Aggregation

### Standard Metrics

```python
class EvaluationMetrics:
    """Collection of evaluation metrics."""
    
    @staticmethod
    def accuracy(predictions: list, labels: list) -> float:
        """Simple accuracy."""
        correct = sum(p == l for p, l in zip(predictions, labels))
        return correct / len(predictions)
    
    @staticmethod
    def pass_at_k(n: int, c: int, k: int) -> float:
        """Unbiased pass@k estimator."""
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))
    
    @staticmethod
    def expected_calibration_error(confidences: list, accuracies: list, 
                                    num_bins: int = 10) -> float:
        """Expected Calibration Error for uncertainty quantification."""
        bin_boundaries = np.linspace(0, 1, num_bins + 1)
        ece = 0.0
        
        for i in range(num_bins):
            in_bin = (confidences >= bin_boundaries[i]) & (confidences < bin_boundaries[i + 1])
            prop_in_bin = in_bin.mean()
            
            if prop_in_bin > 0:
                avg_confidence = confidences[in_bin].mean()
                avg_accuracy = accuracies[in_bin].mean()
                ece += prop_in_bin * np.abs(avg_confidence - avg_accuracy)
        
        return ece
    
    @staticmethod
    def efficiency_score(accuracy: float, cost: float, 
                         baseline_accuracy: float = 0.5,
                         baseline_cost: float = 1.0) -> float:
        """
        Compute efficiency: performance gain per unit cost.
        Higher is better.
        """
        accuracy_gain = accuracy - baseline_accuracy
        cost_ratio = cost / baseline_cost
        return accuracy_gain / cost_ratio if cost_ratio > 0 else 0
```

### Benchmark Leaderboard

```python
class BenchmarkLeaderboard:
    """
    Track and compare model performance across benchmarks.
    """
    
    def __init__(self):
        self.entries = []
    
    def add_entry(self, model_name: str, benchmark_results: dict, 
                  metadata: dict = None):
        """Add model results to leaderboard."""
        entry = {
            'model': model_name,
            'results': benchmark_results,
            'metadata': metadata or {},
            'timestamp': datetime.now()
        }
        self.entries.append(entry)
    
    def get_rankings(self, benchmark: str, metric: str = 'accuracy') -> list:
        """Get ranked list for specific benchmark."""
        relevant = [e for e in self.entries if benchmark in e['results']]
        sorted_entries = sorted(
            relevant,
            key=lambda x: x['results'][benchmark].get(metric, 0),
            reverse=True
        )
        return sorted_entries
    
    def compute_composite_score(self, weights: dict = None) -> list:
        """
        Compute composite score across benchmarks.
        
        Args:
            weights: Dict mapping benchmark names to weights
        """
        if weights is None:
            weights = {b: 1.0 for b in self.get_all_benchmarks()}
        
        scored_entries = []
        for entry in self.entries:
            total_score = 0
            total_weight = 0
            
            for benchmark, weight in weights.items():
                if benchmark in entry['results']:
                    score = entry['results'][benchmark].get('accuracy', 0)
                    total_score += score * weight
                    total_weight += weight
            
            composite = total_score / total_weight if total_weight > 0 else 0
            scored_entries.append({
                'model': entry['model'],
                'composite_score': composite,
                'results': entry['results']
            })
        
        return sorted(scored_entries, key=lambda x: x['composite_score'], reverse=True)
```

---

## Neo4j Integration

### Schema
```cypher
// Evaluation tracking
CREATE CONSTRAINT eval_run_id IF NOT EXISTS
FOR (e:EvaluationRun) REQUIRE e.id IS UNIQUE;

(:EvaluationRun {
    id: String,
    model_name: String,
    model_version: String,
    timestamp: DateTime,
    evaluator: String
})

(:Benchmark {
    name: String,
    version: String,
    category: String,
    num_tasks: Integer,
    description: String
})

(:BenchmarkResult {
    accuracy: Float,
    pass_at_k: Float,
    num_correct: Integer,
    total_tasks: Integer,
    cost_per_task: Float,
    tokens_used: Integer
})

(:CapabilityAssessment {
    dimension: String,    // reasoning, knowledge, coding, etc.
    level: String,        // L1-L5
    score: Float,
    weaknesses: [String]
})

// Relationships
(:EvaluationRun)-[:EVALUATED_ON]->(:Benchmark)
(:EvaluationRun)-[:HAS_RESULT]->(:BenchmarkResult)
(:EvaluationRun)-[:ASSESSES]->(:CapabilityAssessment)
(:Model)-[:HAS_EVALUATION]->(:EvaluationRun)
```

### Query Examples
```cypher
// Get model performance history
MATCH (m:Model {name: "OMEGA-ASI-v500"})-[:HAS_EVALUATION]->(e:EvaluationRun)
       -[:HAS_RESULT]->(r:BenchmarkResult)-[:FOR]->(b:Benchmark)
RETURN b.name, r.accuracy, e.timestamp
ORDER BY e.timestamp;

// Find capability gaps across models
MATCH (e:EvaluationRun)-[:ASSESSES]->(c:CapabilityAssessment)
WHERE c.level < 'L3'
RETURN e.model_name, c.dimension, c.level, c.weaknesses
ORDER BY c.level;

// Compare models on specific benchmark
MATCH (e:EvaluationRun)-[:HAS_RESULT]->(r:BenchmarkResult)-[:FOR]->(b:Benchmark {name: "ARC-AGI-2"})
RETURN e.model_name, r.accuracy, r.cost_per_task
ORDER BY r.accuracy DESC;
```

---

## Integration with Other Skills

### benchmark-creator
- Design custom benchmarks for specific capabilities
- Integrate with evaluation framework
- Track benchmark evolution

### safety-alignment-researcher
- Safety-specific evaluations
- Red-teaming integration
- Alignment assessment

### experiment-tracker
- Log evaluation runs as experiments
- Track improvement over training
- A/B testing of model variants

### advanced-reasoning
- Evaluate reasoning techniques
- Compare CoT, ToT, GoT performance
- Benchmark reasoning efficiency

---

## Best Practices

1. **Multiple Metrics**: Never rely on single metric
2. **Statistical Significance**: Report confidence intervals
3. **Cost Tracking**: Always report evaluation cost
4. **Reproducibility**: Fix random seeds, document versions
5. **Contamination Checks**: Verify test set not in training data
6. **Human Baselines**: Compare against human performance
7. **Regular Re-evaluation**: Models can regress over updates

---

## References

1. Chollet, F., et al. (2026). "ARC Prize 2025: Technical Report"
2. Hendrycks, D., et al. (2021). "Measuring Massive Multitask Language Understanding"
3. Chen, M., et al. (2021). "Evaluating Large Language Models Trained on Code"
4. Jimenez, C.E., et al. (2024). "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?"
5. Mialon, G., et al. (2023). "GAIA: A Benchmark for General AI Assistants"
6. Rein, D., et al. (2023). "GPQA: A Graduate-Level Google-Proof Q&A Benchmark"

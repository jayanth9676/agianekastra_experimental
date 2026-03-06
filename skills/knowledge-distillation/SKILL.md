---
name: knowledge-distillation
description: Knowledge distillation techniques for compressing large models while preserving capabilities
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, knowledge-distillation, model-compression, transfer-learning, llm]
---

# Knowledge Distillation

## Overview

Knowledge distillation (KD) is a model compression technique that transfers knowledge from a large "teacher" model to a smaller "student" model. This skill provides comprehensive methodologies for distilling AGI/ASI capabilities while maintaining performance, crucial for deploying OMEGA ASI variants across different compute environments.

## Core Concepts

### 1. Distillation Paradigms

#### White-Box Distillation
Access to teacher model internals (weights, activations, logits):
- **Logit-based KD**: Match output probability distributions
- **Feature-based KD**: Match intermediate layer representations
- **Attention-based KD**: Transfer attention patterns
- **Gradient-based KD**: Match gradient information

#### Black-Box Distillation
Only access to teacher outputs:
- **Response-based KD**: Learn from teacher's responses
- **Chain-of-Thought (CoT) distillation**: Transfer reasoning traces
- **In-context learning distillation**: Distill few-shot capabilities
- **API-based distillation**: Learn from closed-source model APIs

### 2. Knowledge Types

```
┌─────────────────────────────────────────────────────────┐
│                    Knowledge Types                       │
├─────────────────────────────────────────────────────────┤
│  Declarative    │ Facts, concepts, relationships        │
│  Procedural     │ How to perform tasks, algorithms      │
│  Reasoning      │ Logical inference, problem-solving    │
│  Meta-cognitive │ Self-awareness, uncertainty estimation│
│  Structural     │ Internal representations, features    │
└─────────────────────────────────────────────────────────┘
```

### 3. Distillation Loss Functions

#### Standard KD Loss (Hinton et al., 2015)
```python
def kd_loss(student_logits, teacher_logits, labels, temperature=4.0, alpha=0.5):
    """
    Combined knowledge distillation loss.
    
    Args:
        student_logits: Student model output logits
        teacher_logits: Teacher model output logits
        labels: Ground truth labels
        temperature: Softening temperature (higher = softer)
        alpha: Balance between KD and task loss
    """
    import torch.nn.functional as F
    
    # Soft targets from teacher
    soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
    soft_student = F.log_softmax(student_logits / temperature, dim=-1)
    
    # KD loss (KL divergence)
    kd_loss = F.kl_div(soft_student, soft_targets, reduction='batchmean')
    kd_loss = kd_loss * (temperature ** 2)  # Scale by T^2
    
    # Hard target loss
    hard_loss = F.cross_entropy(student_logits, labels)
    
    # Combined loss
    return alpha * kd_loss + (1 - alpha) * hard_loss
```

#### Feature Distillation Loss
```python
def feature_distillation_loss(student_features, teacher_features, projector=None):
    """
    Match intermediate layer representations.
    
    Args:
        student_features: List of student hidden states
        teacher_features: List of teacher hidden states
        projector: Optional projection layer for dimension matching
    """
    import torch.nn.functional as F
    
    total_loss = 0
    for s_feat, t_feat in zip(student_features, teacher_features):
        if projector is not None:
            s_feat = projector(s_feat)
        
        # Normalize features
        s_feat = F.normalize(s_feat, dim=-1)
        t_feat = F.normalize(t_feat, dim=-1)
        
        # MSE loss on normalized features
        total_loss += F.mse_loss(s_feat, t_feat)
    
    return total_loss / len(student_features)
```

---

## Distillation Methods

### 1. On-Policy Self-Distillation (OPSD)

Single model acts as both teacher and student:

```python
class OnPolicySelfDistillation:
    """
    On-Policy Self-Distillation framework.
    The model teaches its weaker self using privileged information.
    """
    
    def __init__(self, model, tokenizer):
        self.model = model
        self.tokenizer = tokenizer
    
    def generate_teacher_rationale(self, problem, solution):
        """Generate rationale with access to ground truth."""
        prompt = f"""Problem: {problem}
        
Ground Truth Solution: {solution}

Generate a detailed step-by-step reasoning trace that arrives at this solution:"""
        
        return self.model.generate(prompt)
    
    def student_forward(self, problem):
        """Student generates without privileged information."""
        prompt = f"""Problem: {problem}

Let's solve this step by step:"""
        
        return self.model.generate(prompt)
    
    def distill_step(self, problem, solution):
        """Single distillation step."""
        # Teacher generates with privileged info
        teacher_rationale = self.generate_teacher_rationale(problem, solution)
        
        # Student attempts problem
        student_output = self.student_forward(problem)
        
        # Compute token-level supervision
        loss = self.compute_distillation_loss(
            student_output, 
            teacher_rationale
        )
        
        return loss
```

### 2. Domain-Specific Distillation (DDK)

Distilling domain knowledge efficiently:

```python
class DomainDistillation:
    """
    DDK: Distilling Domain Knowledge for Efficient LLMs.
    Focuses on transferring specialized domain capabilities.
    """
    
    def __init__(self, teacher, student, domain):
        self.teacher = teacher
        self.student = student
        self.domain = domain
    
    def create_domain_dataset(self, raw_data, num_samples=10000):
        """Create domain-specific distillation dataset."""
        domain_data = []
        
        for item in raw_data[:num_samples]:
            # Generate teacher response
            teacher_response = self.teacher.generate(
                item['input'],
                domain_context=self.domain
            )
            
            domain_data.append({
                'input': item['input'],
                'teacher_response': teacher_response,
                'domain': self.domain
            })
        
        return domain_data
    
    def domain_aware_loss(self, student_output, teacher_output, domain_weight):
        """Weighted loss based on domain relevance."""
        base_loss = self.kd_loss(student_output, teacher_output)
        return base_loss * domain_weight
```

### 3. Difficulty-Aware Distillation (DA-KD)

Adaptive distillation based on sample difficulty:

```python
class DifficultyAwareDistillation:
    """
    DA-KD: Difficulty-Aware Knowledge Distillation.
    Focuses training on appropriately difficult samples.
    """
    
    def __init__(self, teacher, student, difficulty_estimator):
        self.teacher = teacher
        self.student = student
        self.difficulty_estimator = difficulty_estimator
    
    def estimate_difficulty(self, sample):
        """Estimate sample difficulty based on teacher confidence."""
        teacher_output = self.teacher(sample)
        confidence = teacher_output.max_prob
        
        # Higher confidence = easier sample
        difficulty = 1.0 - confidence
        return difficulty
    
    def filter_samples(self, batch, difficulty_range=(0.3, 0.8)):
        """Filter samples within optimal difficulty range."""
        filtered = []
        for sample in batch:
            difficulty = self.estimate_difficulty(sample)
            if difficulty_range[0] <= difficulty <= difficulty_range[1]:
                filtered.append((sample, difficulty))
        return filtered
    
    def difficulty_weighted_loss(self, batch):
        """Weight loss by sample difficulty."""
        filtered_batch = self.filter_samples(batch)
        
        total_loss = 0
        for sample, difficulty in filtered_batch:
            student_out = self.student(sample)
            teacher_out = self.teacher(sample)
            
            # Higher weight for medium-difficulty samples
            weight = self.difficulty_weight_fn(difficulty)
            loss = self.kd_loss(student_out, teacher_out) * weight
            total_loss += loss
        
        return total_loss / len(filtered_batch)
    
    def difficulty_weight_fn(self, difficulty, peak=0.5, spread=0.3):
        """Gaussian weighting centered on medium difficulty."""
        import math
        return math.exp(-((difficulty - peak) ** 2) / (2 * spread ** 2))
```

### 4. Chain-of-Thought Distillation

Transfer reasoning capabilities:

```python
class CoTDistillation:
    """
    Distill chain-of-thought reasoning from teacher to student.
    """
    
    def __init__(self, teacher, student):
        self.teacher = teacher
        self.student = student
    
    def generate_cot_dataset(self, problems, num_rationales=3):
        """Generate multiple reasoning paths per problem."""
        dataset = []
        
        for problem in problems:
            rationales = []
            for _ in range(num_rationales):
                cot = self.teacher.generate(
                    f"Solve step by step: {problem}",
                    temperature=0.7  # Diverse sampling
                )
                rationales.append(cot)
            
            # Select best rationale (highest consistency)
            best_rationale = self.select_best_rationale(rationales)
            
            dataset.append({
                'problem': problem,
                'rationale': best_rationale,
                'all_rationales': rationales
            })
        
        return dataset
    
    def select_best_rationale(self, rationales):
        """Select rationale with most consistent answer."""
        answers = [self.extract_answer(r) for r in rationales]
        most_common = max(set(answers), key=answers.count)
        
        for r in rationales:
            if self.extract_answer(r) == most_common:
                return r
        return rationales[0]
    
    def cot_distillation_loss(self, student_cot, teacher_cot):
        """Loss for matching reasoning traces."""
        # Token-level loss
        token_loss = self.cross_entropy(student_cot, teacher_cot)
        
        # Step-level loss (match reasoning steps)
        student_steps = self.parse_steps(student_cot)
        teacher_steps = self.parse_steps(teacher_cot)
        step_loss = self.step_alignment_loss(student_steps, teacher_steps)
        
        return token_loss + 0.5 * step_loss
```

### 5. Multi-Teacher Distillation

Ensemble knowledge from multiple teachers:

```python
class MultiTeacherDistillation:
    """
    Distill knowledge from multiple teacher models.
    """
    
    def __init__(self, teachers, student, weights=None):
        self.teachers = teachers
        self.student = student
        self.weights = weights or [1.0 / len(teachers)] * len(teachers)
    
    def ensemble_logits(self, input_data):
        """Combine teacher logits via weighted average."""
        teacher_logits = []
        for teacher in self.teachers:
            logits = teacher(input_data)
            teacher_logits.append(logits)
        
        # Weighted average
        ensemble = sum(
            w * l for w, l in zip(self.weights, teacher_logits)
        )
        return ensemble
    
    def adaptive_weighting(self, input_data, validation_metric):
        """Dynamically weight teachers based on performance."""
        performances = []
        for teacher in self.teachers:
            output = teacher(input_data)
            perf = validation_metric(output)
            performances.append(perf)
        
        # Softmax over performances
        total = sum(performances)
        self.weights = [p / total for p in performances]
    
    def distill_with_disagreement(self, batch):
        """Extra supervision when teachers disagree."""
        for sample in batch:
            teacher_outputs = [t(sample) for t in self.teachers]
            
            # Measure disagreement
            disagreement = self.compute_disagreement(teacher_outputs)
            
            # Higher weight for high-disagreement samples
            weight = 1.0 + disagreement
            
            yield sample, weight
```

---

## Dataset Distillation

Compress datasets while preserving learning signal:

### Coreset Selection
```python
class CoresetDistillation:
    """
    Select a small subset of training data that approximates full dataset.
    """
    
    def __init__(self, model, full_dataset):
        self.model = model
        self.full_dataset = full_dataset
    
    def compute_gradients(self, sample):
        """Compute gradient for sample."""
        self.model.zero_grad()
        loss = self.model.loss(sample)
        loss.backward()
        return self.model.get_gradients()
    
    def select_coreset(self, target_size, method='greedy'):
        """Select coreset using specified method."""
        if method == 'greedy':
            return self.greedy_selection(target_size)
        elif method == 'k-center':
            return self.k_center_selection(target_size)
        elif method == 'forgetting':
            return self.forgetting_selection(target_size)
    
    def greedy_selection(self, target_size):
        """Greedily select samples with diverse gradients."""
        selected = []
        remaining = list(range(len(self.full_dataset)))
        
        # Compute all gradients
        all_gradients = [
            self.compute_gradients(self.full_dataset[i]) 
            for i in remaining
        ]
        
        while len(selected) < target_size:
            best_idx = self.find_most_diverse(all_gradients, selected)
            selected.append(remaining[best_idx])
            remaining.pop(best_idx)
            all_gradients.pop(best_idx)
        
        return [self.full_dataset[i] for i in selected]
```

### Synthetic Data Generation
```python
class SyntheticDistillation:
    """
    Generate synthetic training data that captures dataset knowledge.
    """
    
    def __init__(self, teacher, generator):
        self.teacher = teacher
        self.generator = generator  # LLM for generation
    
    def generate_synthetic_samples(self, num_samples, domain):
        """Generate synthetic training samples."""
        synthetic = []
        
        for _ in range(num_samples):
            # Generate input
            input_prompt = self.generator.generate(
                f"Generate a {domain} problem:"
            )
            
            # Get teacher response
            teacher_response = self.teacher.generate(input_prompt)
            
            synthetic.append({
                'input': input_prompt,
                'output': teacher_response
            })
        
        return synthetic
    
    def diversify_synthetic(self, samples, diversity_threshold=0.8):
        """Filter for diverse synthetic samples."""
        diverse = [samples[0]]
        
        for sample in samples[1:]:
            max_similarity = max(
                self.similarity(sample, d) for d in diverse
            )
            if max_similarity < diversity_threshold:
                diverse.append(sample)
        
        return diverse
```

---

## Progressive Distillation

### Layer-wise Distillation
```python
class LayerwiseDistillation:
    """
    Progressively distill from teacher layers to student layers.
    """
    
    def __init__(self, teacher, student, layer_mapping):
        self.teacher = teacher
        self.student = student
        self.layer_mapping = layer_mapping  # Dict: student_layer -> teacher_layer
    
    def stage_distillation(self, stage, data):
        """Distill specific layer pair for this stage."""
        student_layer = list(self.layer_mapping.keys())[stage]
        teacher_layer = self.layer_mapping[student_layer]
        
        for batch in data:
            # Get intermediate representations
            with torch.no_grad():
                teacher_hidden = self.teacher.get_hidden(batch, teacher_layer)
            
            student_hidden = self.student.get_hidden(batch, student_layer)
            
            # Match representations
            loss = self.feature_loss(student_hidden, teacher_hidden)
            loss.backward()
            self.optimizer.step()
    
    def full_progressive_distillation(self, data, epochs_per_stage=5):
        """Run all distillation stages."""
        num_stages = len(self.layer_mapping)
        
        for stage in range(num_stages):
            print(f"Distillation Stage {stage + 1}/{num_stages}")
            
            for epoch in range(epochs_per_stage):
                self.stage_distillation(stage, data)
            
            # Freeze distilled layers
            self.freeze_student_layer(list(self.layer_mapping.keys())[stage])
```

### Curriculum Distillation
```python
class CurriculumDistillation:
    """
    Distill with increasing difficulty curriculum.
    """
    
    def __init__(self, teacher, student, curriculum_stages):
        self.teacher = teacher
        self.student = student
        self.stages = curriculum_stages
    
    def create_curriculum(self, dataset):
        """Sort dataset by difficulty for curriculum learning."""
        difficulties = []
        
        for sample in dataset:
            difficulty = self.estimate_difficulty(sample)
            difficulties.append((sample, difficulty))
        
        # Sort by difficulty
        sorted_data = sorted(difficulties, key=lambda x: x[1])
        
        # Create curriculum stages
        stage_size = len(sorted_data) // len(self.stages)
        curriculum = []
        
        for i, stage in enumerate(self.stages):
            start = i * stage_size
            end = (i + 1) * stage_size if i < len(self.stages) - 1 else len(sorted_data)
            curriculum.append({
                'stage': stage,
                'data': [s[0] for s in sorted_data[start:end]]
            })
        
        return curriculum
    
    def train_with_curriculum(self, curriculum):
        """Train student following curriculum."""
        for stage_data in curriculum:
            print(f"Training Stage: {stage_data['stage']}")
            
            for sample in stage_data['data']:
                teacher_out = self.teacher(sample)
                student_out = self.student(sample)
                
                loss = self.kd_loss(student_out, teacher_out)
                loss.backward()
                self.optimizer.step()
```

---

## Capability Preservation

### Critical Capability Identification
```python
class CapabilityPreservation:
    """
    Identify and preserve critical capabilities during distillation.
    """
    
    def __init__(self, teacher, student, capability_benchmarks):
        self.teacher = teacher
        self.student = student
        self.benchmarks = capability_benchmarks
    
    def evaluate_capabilities(self, model):
        """Evaluate model on all capability benchmarks."""
        results = {}
        for name, benchmark in self.benchmarks.items():
            score = benchmark.evaluate(model)
            results[name] = score
        return results
    
    def capability_gap_analysis(self):
        """Identify capability gaps between teacher and student."""
        teacher_caps = self.evaluate_capabilities(self.teacher)
        student_caps = self.evaluate_capabilities(self.student)
        
        gaps = {}
        for cap in teacher_caps:
            gap = teacher_caps[cap] - student_caps[cap]
            gaps[cap] = {
                'teacher': teacher_caps[cap],
                'student': student_caps[cap],
                'gap': gap,
                'retention': student_caps[cap] / teacher_caps[cap] * 100
            }
        
        return gaps
    
    def focused_distillation(self, gaps, threshold=0.8):
        """Focus distillation on capabilities below threshold."""
        weak_capabilities = [
            cap for cap, data in gaps.items() 
            if data['retention'] < threshold * 100
        ]
        
        print(f"Focusing on capabilities: {weak_capabilities}")
        
        for cap in weak_capabilities:
            # Get capability-specific data
            cap_data = self.benchmarks[cap].get_training_data()
            
            # Intensive distillation on weak capability
            self.intensive_distillation(cap_data, epochs=10)
```

---

## Neo4j Integration

### Schema
```cypher
// Distillation experiment nodes
CREATE CONSTRAINT distillation_exp_id IF NOT EXISTS
FOR (d:DistillationExperiment) REQUIRE d.id IS UNIQUE;

// Node types
(:DistillationExperiment {
    id: String,
    method: String,           // "logit", "feature", "cot", "self"
    teacher_model: String,
    student_model: String,
    temperature: Float,
    alpha: Float,
    dataset_size: Integer,
    final_loss: Float,
    capability_retention: Float,
    timestamp: DateTime
})

(:TeacherModel {
    name: String,
    parameters: Integer,
    capabilities: [String],
    performance: Map
})

(:StudentModel {
    name: String,
    parameters: Integer,
    compression_ratio: Float,
    speedup: Float
})

(:CapabilityBenchmark {
    name: String,
    type: String,           // "reasoning", "coding", "knowledge"
    metrics: [String]
})

// Relationships
(:DistillationExperiment)-[:USES_TEACHER]->(:TeacherModel)
(:DistillationExperiment)-[:TRAINS]->(:StudentModel)
(:StudentModel)-[:EVALUATED_ON]->(:CapabilityBenchmark)
(:StudentModel)-[:DERIVED_FROM]->(:TeacherModel)
```

### Query Examples
```cypher
// Find best distillation method for capability retention
MATCH (d:DistillationExperiment)-[:TRAINS]->(s:StudentModel)
WHERE d.capability_retention > 0.9
RETURN d.method, AVG(d.capability_retention) as avg_retention,
       AVG(s.compression_ratio) as avg_compression
ORDER BY avg_retention DESC;

// Track distillation lineage
MATCH path = (t:TeacherModel)<-[:DERIVED_FROM*]-(s:StudentModel)
WHERE t.name = 'OMEGA-ASI-v500'
RETURN path;

// Find capability gaps in distilled models
MATCH (s:StudentModel)-[e:EVALUATED_ON]->(b:CapabilityBenchmark)
MATCH (t:TeacherModel)-[te:EVALUATED_ON]->(b)
WHERE s.name = 'OMEGA-ASI-v500-distilled'
  AND t.name = 'OMEGA-ASI-v500'
RETURN b.name, te.score as teacher_score, e.score as student_score,
       (te.score - e.score) as gap
ORDER BY gap DESC;
```

---

## Integration with Other Skills

### safety-alignment-researcher
- Verify safety properties preserved after distillation
- Red-team distilled models for new vulnerabilities
- Ensure alignment techniques transfer correctly

### benchmark-creator
- Create capability benchmarks for measuring retention
- Design distillation-specific evaluation suites
- Track performance across model sizes

### experiment-tracker
- Log distillation hyperparameters
- Track training curves and convergence
- Compare distillation methods

### mechanistic-interpretability
- Analyze feature preservation in distilled models
- Verify circuit transfer from teacher to student
- Identify capability loss mechanisms

### neural-architecture-search
- NAS for optimal student architecture
- Architecture-aware distillation
- Find efficient architectures for distillation

---

## Best Practices

### 1. Temperature Selection
- Start with T=4.0 for soft targets
- Higher T for more knowledge transfer, lower for task performance
- Tune based on teacher-student capacity gap

### 2. Capacity Matching
- Student should have sufficient capacity for task
- 10-30% of teacher parameters is typical
- Layer depth matters more than width for reasoning

### 3. Data Quality
- Use high-quality teacher outputs
- Filter noisy or incorrect teacher responses
- Diverse data improves generalization

### 4. Progressive Approach
- Start with easier samples
- Gradually increase difficulty
- Monitor for capability degradation

### 5. Capability Monitoring
- Regularly evaluate on capability benchmarks
- Stop if critical capability drops below threshold
- Focus distillation on weak areas

---

## References

1. Hinton, G., Vinyals, O., & Dean, J. (2015). "Distilling the Knowledge in a Neural Network"
2. Zhao, S., et al. (2025). "On-Policy Self-Distillation for Large Language Models"
3. Liu, J., et al. (2024). "DDK: Distilling Domain Knowledge for Efficient LLMs" (NeurIPS 2024)
4. He, C., et al. (2025). "DA-KD: Difficulty-Aware Knowledge Distillation" (ICML 2025)
5. Xu, C., et al. (2024). "Survey on Knowledge Distillation for Large Language Models"
6. Gu, Y., et al. (2024). "MiniLLM: Knowledge Distillation of Large Language Models"
7. Hsieh, C.Y., et al. (2023). "Distilling Step-by-Step!"

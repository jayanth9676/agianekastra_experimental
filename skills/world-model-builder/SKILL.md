---
name: world-model-builder
description: Learn and maintain predictive world models for AGI agents - environment understanding, causal modeling, and simulation
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, world-model, causality, simulation, prediction]
---

# World Model Builder

## Overview

This skill enables AGI agents to learn, refine, and use predictive world models. World models capture agent understanding of environment dynamics, causal relationships, and enable prediction and planning for autonomous behavior.

## When to Use This Skill

Use this skill when you need to:
- Build internal models of environment dynamics
- Learn causal relationships from experience
- Enable predictive planning and simulation
- Support model-based reinforcement learning
- Understand agent's own capabilities and limitations
- Perform counterfactual reasoning

## Core Concepts

### World Model Architecture

#### Components

1. **Transition Model**
   - Maps (state, action) → next_state
   - Captures environment dynamics
   - Enables prediction and planning

2. **Reward Model**
   - Maps (state, action) → expected_reward
   - Predicts task completion
   - Guides agent decision-making

3. **Termination Model**
   - Maps state → done_probability
   - Predicts episode completion
   - Handles goal detection

4. **Observation Model**
   - Maps (state, action) → next_observation
   - Accounts for partial observability
   - Handles stochastic outcomes

#### Model Representation

```python
class WorldModel:
    """Predictive world model for agent environments."""
    
    def __init__(
        self,
        state_dim: int,
        action_dim: int,
        observation_dim: int
    ):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.observation_dim = observation_dim
        
        # Neural network components
        self.transition_model = TransitionNetwork(state_dim, action_dim)
        self.reward_model = RewardNetwork(state_dim, action_dim)
        self.termination_model = TerminationNetwork(state_dim)
        self.observation_model = ObservationNetwork(state_dim, action_dim)
        
        # Model uncertainty
        self.ensemble_size = 5
        self.ensembles = [
            self._init_model() for _ in range(self.ensemble_size)
        ]
    
    def predict(
        self,
        state: np.ndarray,
        action: np.ndarray
    ) -> ModelPrediction:
        """
        Predict next state, reward, and done.
        
        Args:
            state: Current environment state
            action: Action to take
            
        Returns:
            ModelPrediction: Predicted outcomes with uncertainty
        """
        predictions = []
        
        for model in self.ensembles:
            pred = model.forward(state, action)
            predictions.append(pred)
        
        # Aggregate predictions (ensemble)
        next_state_mean = np.mean([p.next_state for p in predictions], axis=0)
        next_state_std = np.std([p.next_state for p in predictions], axis=0)
        
        reward_mean = np.mean([p.reward for p in predictions])
        reward_std = np.std([p.reward for p in predictions])
        
        done_prob = np.mean([p.done for p in predictions])
        
        return ModelPrediction(
            next_state=next_state_mean,
            next_state_uncertainty=next_state_std,
            reward=reward_mean,
            reward_uncertainty=reward_std,
            done=done_prob
        )
    
    def update(
        self,
        trajectory: Trajectory
    ) -> float:
        """
        Update world model from observed trajectory.
        
        Args:
            trajectory: (state, action, next_state, reward, done) sequence
            
        Returns:
            float: Training loss
        """
        losses = []
        
        for model in self.ensembles:
            loss = model.train_on_batch(trajectory)
            losses.append(loss)
        
        return np.mean(losses)
```

### Causal Discovery

#### Structure Learning

```python
class CausalDiscovery:
    """Learn causal structure from experience."""
    
    def discover_structure(
        self,
        data: np.ndarray,
        method: str = 'notears'
    ) -> CausalGraph:
        """
        Discover causal graph from observational data.
        
        Args:
            data: Observational data [samples, variables]
            method: Discovery method (notears, gies, pc)
            
        Returns:
            CausalGraph: Learned causal structure
        """
        n_vars = data.shape[1]
        
        if method == 'notears':
            # NOTEARS: Non-combinatorial optimization
            adjacency = self._notears_algorithm(data)
        elif method == 'gies':
            # GIES: Greedy Intervention Equivalence Search
            adjacency = self._gies_algorithm(data)
        else:
            # PC: Peter-Clark algorithm
            adjacency = self._pc_algorithm(data)
        
        # Build causal graph
        graph = CausalGraph(
            num_nodes=n_vars,
            adjacency_matrix=adjacency,
            method=method
        )
        
        return graph
    
    def learn_intervention_effects(
        self,
        graph: CausalGraph,
        interventions: List[Intervention]
    ) -> InterventionEffects:
        """
        Learn effects of interventions on causal model.
        
        Args:
            graph: Current causal structure
            interventions: List of (variable, value) pairs
            
        Returns:
            InterventionEffects: Predicted effects of interventions
        """
        effects = {}
        
        for var, value in interventions:
            # Find downstream nodes
            downstream = graph.get_descendants(var)
            
            # Predict effect size
            effect_sizes = []
            for target in downstream:
                effect = self._estimate_effect(
                    graph, var, target, value
                )
                effect_sizes.append(effect)
            
            effects[var] = {
                'targets': downstream,
                'mean_effect': np.mean(effect_sizes),
                'uncertainty': np.std(effect_sizes)
            }
        
        return InterventionEffects(effects)
```

### Model-Based Planning

#### Model-Predictive Control

```python
class MPCPlanner:
    """Model-Predictive Control for planning."""
    
    def plan(
        self,
        initial_state: np.ndarray,
        world_model: WorldModel,
        horizon: int = 10,
        num_candidates: int = 100
    ) -> ActionSequence:
        """
        Plan action sequence using world model.
        
        Args:
            initial_state: Starting state
            world_model: Predictive world model
            horizon: Planning horizon
            num_candidates: Number of action sequences to evaluate
            
        Returns:
            ActionSequence: Best action sequence
        """
        best_sequence = None
        best_value = -float('inf')
        
        for _ in range(num_candidates):
            # Sample random action sequence
            actions = self._sample_action_sequence(horizon)
            
            # Simulate with world model
            state = initial_state.copy()
            total_reward = 0
            done = False
            
            for action in actions:
                pred = world_model.predict(state, action)
                state = pred.next_state
                total_reward += pred.reward
                done = pred.done > 0.5
                
                if done:
                    break
            
            # Track best
            if total_reward > best_value:
                best_value = total_reward
                best_sequence = actions
        
        return ActionSequence(
            actions=best_sequence,
            expected_reward=best_value,
            uncertainty=self._calculate_uncertainty(
                initial_state, best_sequence, world_model
            )
        )
```

### Imagination and Simulation

#### Dreaming for Planning

```python
class ImaginationModel:
    """Use imagination to refine world model."""
    
    def dream_rollout(
        self,
        state: np.ndarray,
        world_model: WorldModel,
        num_steps: int = 5,
        temperature: float = 1.0
    ) -> List[ImaginedState]:
        """
        Generate imagined trajectories from state.
        
        Args:
            state: Starting state for imagination
            world_model: World model for simulation
            num_steps: Length of imagined rollouts
            temperature: Sampling temperature
            
        Returns:
            List[ImaginedState]: Imagined trajectories
        """
        imagined = []
        current_state = state.copy()
        
        for step in range(num_steps):
            # Sample action with temperature
            action = self._sample_action(temperature)
            
            # Predict with world model
            pred = world_model.predict(current_state, action)
            
            # Add imagined state
            imagined.append(ImaginedState(
                step=step,
                state=pred.next_state,
                action=action,
                reward=pred.reward,
                imagination_quality=self._assess_quality(pred)
            ))
            
            current_state = pred.next_state
        
        return imagined
```

### World Model Uncertainty

#### Bayesian Model Update

```python
class BayesianWorldModel:
    """Bayesian world model with uncertainty quantification."""
    
    def update(
        self,
        state: np.ndarray,
        action: np.ndarray,
        next_state: np.ndarray,
        reward: float
    ):
        """
        Bayesian update of world model.
        
        Args:
            state: Current state
            action: Taken action
            next_state: Observed next state
            reward: Observed reward
        """
        # Predictive distribution
        pred_dist = self.predict_distribution(state, action)
        
        # Update with observation
        likelihood = self._likelihood(next_state, pred_dist)
        
        # Posterior update
        self.posterior = self._update_posterior(
            self.posterior,
            likelihood,
            state,
            action
        )
        
        # Update model parameters
        self.parameters = self._update_parameters(
            self.posterior,
            state,
            action,
            next_state,
            reward
        )
```

### Neo4j Integration

#### Causal Graph Storage

```cypher
// Create causal node
CREATE (c:CausalVariable {
    name: $name,
    type: $type,
    values: $values,
    confidence: $confidence
})

// Create causal edge
CREATE (c1:CausalVariable)-[:CAUSES {
    strength: $strength,
    confidence: $confidence,
    mechanism: $mechanism
}]->(c2:CausalVariable)

// Store intervention effect
CREATE (i:Intervention {
    variable: $variable,
    value: $value,
    timestamp: datetime()
})
CREATE (i)-[:AFFECTS]->(c:CausalVariable)
```

#### World Model Query

```cypher
// Query causal relationships
MATCH (start:CausalVariable {name: $variable})-[:CAUSES*]->(end:CausalVariable)
RETURN path, length(path) as distance,
       reduce(r in relationships(path).strength, sum(r.strength)) as total_strength
ORDER BY total_strength DESC
LIMIT 10
```

## Best Practices

### Model Learning

1. **Ensemble Methods** - Use multiple models for uncertainty
2. **Balanced Datasets** - Cover state-action space well
3. **Regularization** - Prevent overfitting to sparse data
4. **Validation** - Hold out test data for evaluation

### Causal Discovery

1. **Multiple Methods** - Compare different algorithms
2. **Intervention Data** - Best for causal inference
3. **Expert Knowledge** - Incorporate domain constraints
4. **Uncertainty** - Quantify confidence in causal links

### Planning

1. **Short Horizons** - Longer horizons increase error
2. **Multiple Candidates** - Evaluate diverse action sequences
3. **Risk Awareness** - Consider model uncertainty
4. **Real-World Validation** - Test plans in actual environment

## Integration with Other Skills

- **advanced-memory-system** - Store world model in semantic memory
- **meta-learning-protocol** - Adapt world models to new domains
- **distributed-training** - Scale world model training
- **experiment-tracker** - Log world model experiments

## References

### Key Papers

1. **World Models: Agent Learning as State Machines** - ICLR 2023
   - Ha & Schmidhuber
   - Dreamer algorithm for model-based RL

2. **Causal Discovery from Interventions** - NeurIPS 2020
   - Zheng et al.
   - NOTEARS algorithm

3. **Learning World Models for Autonomous Navigation** - ICML 2024
   - Environment understanding from interaction

### Frameworks

- **Dreamer** - Model-based RL with imagination
- **World Models for Atari** - Classic world model benchmark
- **CausalML** - Causal inference library
- **DoWhy** - Causal reasoning and discovery

## Dependencies

- **torch** - Neural networks
- **numpy** - Numerical operations
- **causal-learn** - Causal discovery algorithms
- **gym** - Environment interfaces

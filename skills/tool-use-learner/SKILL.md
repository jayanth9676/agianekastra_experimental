---
name: tool-use-learner
description: Autonomous tool discovery, learning, and orchestration for AGI agents - discover APIs, learn tool interfaces, optimize tool chains
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, tools, orchestration, discovery, rl]
---

# Tool Use Learner

## Overview

This skill enables autonomous agents to discover, learn, and orchestrate tools dynamically. Agents can explore available tools, understand their interfaces through documentation or usage patterns, and learn to chain tools effectively for complex tasks.

## When to Use This Skill

Use this skill when you need to:
- Discover and integrate new tools dynamically
- Learn tool interfaces without manual specification
- Optimize tool selection and chaining strategies
- Build tool use policies through reinforcement learning
- Create autonomous tool orchestration systems
- Adapt tool usage to new domains

## Core Concepts

### Tool Discovery

#### Types of Tool Sources

1. **Documentation-Based Discovery**
   - Parse tool documentation (API specs, README)
   - Extract function signatures, parameters, return types
   - Build schema representations

2. **Usage-Based Discovery**
   - Observe tool calls during agent operation
   - Infer interfaces from input/output patterns
   - Learn implicit constraints and side effects

3. **Registry-Based Discovery**
   - Query tool registries (MCP, OpenAPI, tool hubs)
   - Filter by relevance, capability, quality
   - Rate and rank discovered tools

#### Discovery Pipeline

```python
class ToolDiscovery:
    """Autonomous tool discovery and indexing."""
    
    def discover_from_documentation(
        self,
        docs_url: str,
        tool_type: str = 'api'
    ) -> List[ToolSchema]:
        """
        Discover tools from documentation.
        
        Args:
            docs_url: URL to tool documentation
            tool_type: Type of tool (api, cli, library)
            
        Returns:
            List[ToolSchema]: Discovered tool schemas
        """
        # Fetch documentation
        docs_content = self._fetch_docs(docs_url)
        
        # Extract tool definitions
        if tool_type == 'api':
            tools = self._extract_api_tools(docs_content)
        elif tool_type == 'openapi':
            tools = self._extract_openapi_tools(docs_content)
        else:
            tools = self._extract_generic_tools(docs_content)
        
        # Validate schemas
        validated_tools = []
        for tool in tools:
            try:
                schema = self._validate_tool_schema(tool)
                validated_tools.append(schema)
            except ValidationError as e:
                self.logger.warning(f"Invalid tool: {tool.name}: {e}")
        
        # Index for retrieval
        self.tool_index.index(validated_tools)
        
        return validated_tools
    
    def discover_from_usage(
        self,
        execution_traces: List[ExecutionTrace]
    ) -> List[LearnedTool]:
        """
        Infer tool interfaces from usage patterns.
        
        Args:
            execution_traces: Historical tool executions
            
        Returns:
            List[LearnedTool]: Inferred tool definitions
        """
        # Group traces by tool name
        tool_groups = self._group_by_tool(execution_traces)
        
        learned_tools = []
        for tool_name, traces in tool_groups.items():
            # Infer signature from inputs/outputs
            inputs = [t.inputs for t in traces]
            outputs = [t.outputs for t in traces]
            
            # Learn parameter constraints
            param_constraints = self._infer_constraints(inputs)
            
            # Learn success patterns
            success_patterns = self._learn_success_patterns(traces)
            
            # Build learned tool
            learned_tool = LearnedTool(
                name=tool_name,
                signature=self._infer_signature(inputs, outputs),
                param_constraints=param_constraints,
                success_patterns=success_patterns,
                confidence=self._calculate_confidence(traces),
                source='usage_inference'
            )
            
            learned_tools.append(learned_tool)
        
        return learned_tools
```

### Tool Learning

#### Interface Understanding

```python
class ToolLearner:
    """Learn and refine tool interfaces."""
    
    def refine_tool_schema(
        self,
        tool: ToolSchema,
        new_observations: List[Observation]
    ) -> ToolSchema:
        """
        Update tool understanding from new observations.
        
        Args:
            tool: Current tool schema
            new_observations: Recent tool usage observations
            
        Returns:
            ToolSchema: Refined tool schema
        """
        # Extract parameter patterns
        param_patterns = self._analyze_parameters(new_observations)
        
        # Update parameter constraints
        for param, pattern in param_patterns.items():
            if param in tool.parameters:
                tool.parameters[param].update(
                    min_value=pattern['min'],
                    max_value=pattern['max'],
                    allowed_values=pattern['values'],
                    examples=pattern['examples']
                )
        
        # Learn output formats
        output_patterns = self._analyze_outputs(new_observations)
        tool.output_schema.update(output_patterns)
        
        # Learn timing and cost
        performance = self._estimate_performance(new_observations)
        tool.avg_latency = performance['latency']
        tool.avg_cost = performance['cost']
        
        # Update confidence
        tool.confidence = self._calculate_updated_confidence(
            tool.confidence,
            len(new_observations)
        )
        
        return tool
```

### Tool Orchestration

#### ReAct Framework

```python
class ToolOrchestrator:
    """Reason and Act framework for tool use."""
    
    def react_loop(
        self,
        task: str,
        max_steps: int = 10
    ) -> ExecutionTrace:
        """
        Execute ReAct loop for tool-based task solving.
        
        Args:
            task: Task description
            max_steps: Maximum reasoning steps
            
        Returns:
            ExecutionTrace: Complete execution history
        """
        trace = ExecutionTrace()
        
        thought = f"Task: {task}"
        action = None
        observation = None
        
        for step in range(max_steps):
            trace.add_step(ThoughtStep(
                step=step,
                thought=thought,
                action=action,
                observation=observation
            ))
            
            # Termination check
            if self._is_complete(observation, task):
                break
            
            # Reasoning phase
            thought = self._reason(
                task, action, observation
            )
            
            # Action selection
            action = self._select_action(
                thought, self.available_tools
            )
            
            # Action execution
            observation = self._execute_action(action)
            
            # Update tool usage statistics
            self._update_tool_stats(action, observation)
        
        return trace
```

#### Chain-of-Thought Tool Selection

```python
    def _select_action(
        self,
        thought: str,
        tools: List[ToolSchema]
    ) -> Action:
        """
        Select optimal tool based on reasoning.
        
        Args:
            thought: Current reasoning state
            tools: Available tools
            
        Returns:
            Action: Selected tool with parameters
        """
        # Encode thought
        thought_embedding = self.encoder.encode(thought)
        
        # Score tools by relevance
        tool_scores = []
        for tool in tools:
            # Embed tool description and capabilities
            tool_embedding = self.encoder.encode(tool.description)
            
            # Calculate semantic similarity
            similarity = cosine_similarity(
                thought_embedding,
                tool_embedding
            )
            
            # Consider performance metrics
            performance_score = (
                tool.success_rate * 0.4 +
                tool.speed_score * 0.3 +
                tool.cost_efficiency * 0.3
            )
            
            # Combine scores
            final_score = similarity * 0.7 + performance_score * 0.3
            
            tool_scores.append((tool, final_score))
        
        # Select best tool
        best_tool, score = max(tool_scores, key=lambda x: x[1])
        
        # Generate tool call with learned parameters
        action = Action(
            tool_name=best_tool.name,
            parameters=self._infer_parameters(
                thought,
                best_tool
            )
        )
        
        return action
```

### Reinforcement Learning for Tool Policies

#### Tool Use as MDP

```python
class ToolUseMDP:
    """Model tool selection as Markov Decision Process."""
    
    def learn_policy(
        self,
        episodes: List[Episode],
        num_iterations: int = 1000
    ) -> Policy:
        """
        Learn optimal tool use policy via RL.
        
        Args:
            episodes: Historical tool use episodes
            num_iterations: Training iterations
            
        Returns:
            Policy: Learned tool selection policy
        """
        # Define state space
        state_space = self._define_state_space()
        
        # Define action space
        action_space = self._define_action_space()
        
        # Initialize Q-table
        q_table = np.zeros((len(state_space), len(action_space)))
        
        # Q-learning
        for iteration in range(num_iterations):
            for episode in episodes:
                state = episode.initial_state
                
                for step in episode.steps:
                    # Select action (epsilon-greedy)
                    if np.random.rand() < self.epsilon:
                        action = self._explore()
                    else:
                        action = self._exploit(state, q_table)
                    
                    # Take action
                    next_state, reward = step.transition
                    
                    # Update Q-value
                    q_value = q_table[state, action]
                    next_max = np.max(q_table[next_state])
                    
                    q_table[state, action] = q_value + self.alpha * (
                        reward + self.gamma * next_max - q_value
                    )
                    
                    state = next_state
        
        # Extract policy
        policy = Policy(q_table=q_table, state_space=state_space)
        return policy
```

### Tool Chaining and Composition

#### Chain Discovery

```python
class ToolChainDiscovery:
    """Discover optimal tool chains for tasks."""
    
    def discover_chain(
        self,
        task: str,
        available_tools: List[ToolSchema],
        max_length: int = 5
    ) -> ToolChain:
        """
        Find optimal tool chain for given task.
        
        Args:
            task: Task description
            available_tools: Tools that can be used
            max_length: Maximum chain length
            
        Returns:
            ToolChain: Optimal tool sequence
        """
        # Build tool compatibility graph
        graph = self._build_compatibility_graph(available_tools)
        
        # Find candidate chains via search
        chains = []
        
        def search(current_chain, depth):
            if depth > max_length:
                return
            
            # Check if chain satisfies task
            if self._satisfies_task(current_chain, task):
                chains.append(current_chain)
                return
            
            # Extend chain
            last_output = current_chain[-1].output_type
            next_tools = self._find_compatible_tools(
                last_output, graph
            )
            
            for tool in next_tools:
                search(current_chain + [tool], depth + 1)
        
        search([], 0)
        
        # Rank chains
        scored_chains = []
        for chain in chains:
            score = self._evaluate_chain(chain, task)
            scored_chains.append((chain, score))
        
        # Return best chain
        best_chain, _ = max(scored_chains, key=lambda x: x[1])
        return best_chain
    
    def _evaluate_chain(
        self,
        chain: List[ToolSchema],
        task: str
    ) -> float:
        """
        Evaluate tool chain quality.
        
        Args:
            chain: Sequence of tools
            task: Task to accomplish
            
        Returns:
            float: Chain quality score
        """
        scores = []
        
        # Semantic relevance
        task_emb = self.encoder.encode(task)
        relevance = np.mean([
            cosine_similarity(task_emb, self.encoder.encode(t.description))
            for t in chain
        ])
        scores.append(relevance)
        
        # Success rate
        success_rate = np.mean([t.success_rate for t in chain])
        scores.append(success_rate)
        
        # Cost efficiency
        total_cost = sum([t.avg_cost for t in chain])
        cost_score = 1.0 / (1.0 + total_cost)
        scores.append(cost_score)
        
        # Speed
        total_latency = sum([t.avg_latency for t in chain])
        speed_score = 1.0 / (1.0 + total_latency)
        scores.append(speed_score)
        
        # Chain coherence (type compatibility)
        coherence = self._calculate_coherence(chain)
        scores.append(coherence)
        
        return np.mean(scores)
```

### Neo4j Integration

#### Tool Schema Storage

```cypher
// Create tool schema node
CREATE (t:Tool {
    name: $name,
    description: $description,
    parameters: $parameters,
    output_schema: $output_schema,
    source: $source,
    confidence: $confidence,
    success_rate: 0.0,
    usage_count: 0,
    avg_latency: 0.0,
    avg_cost: 0.0,
    discovered_at: datetime()
})

// Create tool compatibility relationship
CREATE (t1:Tool)-[:COMPATIBLE_WITH]->(t2:Tool)

// Create tool chain relationship
CREATE (t1:Tool)-[:LEADS_TO]->(t2:Tool)
```

#### Chain Query

```cypher
// Find tool chains for task
MATCH (t:Tool)-[:LEADS_TO*]->(end:Tool)
WHERE t.description CONTAINS $task_prefix
RETURN [t, nodes(path) as tools] as chain,
       length(path) as chain_length
ORDER BY reduce(
    n in t.success_rate + 
        reduce(x in end.success_rate, x + end.success_rate) / length(path),
    chain_length
) DESC
LIMIT 10
```

## Best Practices

### Tool Discovery

1. **Start with Documentation** - Use official docs first
2. **Validate Schemas** - Test tool calls with sample inputs
3. **Multiple Sources** - Combine docs, usage, registry
4. **Rate Tools** - Track success rates and performance

### Tool Learning

1. **Continuous Refinement** - Update schemas from observations
2. **Track Uncertainty** - Model confidence in learned parameters
3. **Handle Edge Cases** - Learn from failures and errors
4. **Version Awareness** - Track tool version changes

### Orchestration

1. **Reasoning First** - Think before selecting tools
2. **Context Awareness** - Consider conversation and task history
3. **Fallback Plans** - Always have alternative tools
4. **Learning Loop** - Use outcomes to improve future selections

## Integration with Other Skills

- **multi-agent-orchestrator** - Cross-agent tool sharing
- **experiment-tracker** - Log tool experiments
- **advanced-memory-system** - Remember tool usage patterns
- **cognitive-architecture** - Model tool selection as cognitive process

## References

### Key Papers

1. **From Language to Action: LLMs as Autonomous Agents** - arXiv:2508.17281
   - Chowa et al., 2025
   - Comprehensive survey on tool use

2. **ReAct: Synergizing Reasoning and Acting in Language Models** - arXiv:2210.03629
   - Yao et al., 2022
   - Reasoning-Acting framework

3. **Reflexion: Language Agents with Verbal Reinforcement Learning** - arXiv:2303.11366
   - Shinn et al., 2023
   - Self-reflection for tool use

### Frameworks

- **OpenAI Tools** - Function calling and tool orchestration
- **LangChain Tools** - Extensive tool library
- **MCP (Model Context Protocol)** - Standardized tool interfaces
- **AutoGPT** - Autonomous tool discovery

## Dependencies

- **anthropic** SDK - Claude API with tools
- **langchain** - Tool orchestration framework
- **openai** - Tool use integration
- **numpy** - Q-learning and similarity

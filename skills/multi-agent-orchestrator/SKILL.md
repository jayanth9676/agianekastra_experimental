---
name: multi-agent-orchestrator
description: Design, coordinate, and manage multi-agent AI systems for complex collaborative tasks. Covers orchestration patterns, communication protocols, consensus mechanisms, and emergent behavior analysis for AGI research.
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, multi-agent, orchestration, coordination, collaboration, emergence, swarm]
---

# Multi-Agent Orchestrator

## Overview

This skill provides comprehensive frameworks for designing, coordinating, and managing multi-agent AI systems. It covers orchestration patterns, communication protocols, task allocation strategies, consensus mechanisms, and emergent behavior analysis critical for advanced AGI research.

## When to Use

- Designing multi-agent architectures for complex tasks
- Orchestrating collaboration between specialized agents
- Implementing consensus and decision-making protocols
- Analyzing emergent behaviors in agent collectives
- Building hierarchical agent systems
- Creating agent communication frameworks
- Debugging multi-agent coordination failures
- Scaling agent systems efficiently

## Core Concepts

### Agent Types

```yaml
agent_taxonomy:
  by_autonomy:
    - reactive: "Responds to stimuli, no internal state"
    - deliberative: "Plans and reasons about actions"
    - hybrid: "Combines reactive and deliberative"
    - learning: "Adapts behavior over time"
    - self-improving: "Modifies own capabilities"
    
  by_role:
    - executor: "Performs specific tasks"
    - planner: "Decomposes goals into tasks"
    - supervisor: "Coordinates other agents"
    - critic: "Evaluates outputs and provides feedback"
    - specialist: "Deep expertise in narrow domain"
    - generalist: "Broad capability across domains"
    
  by_organization:
    - peer: "Equal status, horizontal coordination"
    - hierarchical: "Manager-worker relationships"
    - market: "Economic/auction-based coordination"
    - swarm: "Decentralized, emergent coordination"
```

### Orchestration Patterns

```markdown
## Pattern 1: Sequential Orchestration

Agents execute in a predefined linear order (pipeline).

```
Agent A → Agent B → Agent C → Output
```

**Use When:**
- Tasks have clear sequential dependencies
- Each stage produces input for the next
- Order matters for correctness

**Example:**
Research Agent → Analysis Agent → Writing Agent → Review Agent
```

```markdown
## Pattern 2: Concurrent/Parallel Orchestration

Multiple agents work simultaneously on the same or different tasks.

```
         ┌─ Agent A ─┐
Input ───┼─ Agent B ─┼──→ Aggregator → Output
         └─ Agent C ─┘
```

**Use When:**
- Tasks are independent
- Diverse perspectives needed
- Speed is critical

**Example:**
Parallel code reviewers, ensemble decision making
```

```markdown
## Pattern 3: Hierarchical Orchestration

Manager agents coordinate teams of worker agents.

```
                Orchestrator
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    Team Lead   Team Lead   Team Lead
        │           │           │
    ┌───┴───┐   ┌───┴───┐   ┌───┴───┐
    ▼       ▼   ▼       ▼   ▼       ▼
  Agent   Agent Agent Agent Agent Agent
```

**Use When:**
- Complex tasks requiring decomposition
- Need for specialized sub-teams
- Scalability is important

**Example:**
NADER architecture (Research Team + Development Team)
```

```markdown
## Pattern 4: Group Chat / Debate Orchestration

Agents collaborate through shared conversation with a moderator.

```
    ┌─────────────────────┐
    │   Chat Manager      │
    └─────────────────────┘
            │
    ┌───────┼───────┐
    ▼       ▼       ▼
  Agent   Agent   Agent
    │       │       │
    └───────┴───────┘
      Shared Context
```

**Use When:**
- Collaborative problem-solving needed
- Debate/discussion improves quality
- Consensus building required

**Example:**
AI debate, red-team vs blue-team, design review
```

```markdown
## Pattern 5: Handoff Orchestration

Tasks dynamically transferred between agents based on context.

```
Router ──→ Agent A ──→ (if condition) ──→ Agent B
                   └─→ (else) ──→ Agent C
```

**Use When:**
- Different expertise needed for different inputs
- Runtime routing decisions required
- Efficient resource utilization

**Example:**
Customer service routing, domain-specific handlers
```

## Communication Protocols

### Model Context Protocol (MCP)

Standard for agent-external resource access:

```yaml
mcp_specification:
  purpose: "Standardize how agents access external tools and context"
  components:
    resources: "Data sources agents can access"
    tools: "Functions agents can invoke"
    prompts: "Templates for interactions"
  benefits:
    - Interoperability between frameworks
    - Consistent tool access patterns
    - Portable agent skills
```

### Agent-to-Agent Protocol (A2A)

Peer coordination and communication:

```yaml
a2a_protocol:
  message_types:
    request: "Ask another agent to perform action"
    response: "Reply to a request"
    broadcast: "Announce to all agents"
    negotiate: "Propose terms for collaboration"
    delegate: "Transfer task ownership"
    
  coordination_primitives:
    synchronization: "Wait for other agents"
    mutual_exclusion: "Exclusive resource access"
    barrier: "All agents reach point before continuing"
    consensus: "Agree on shared state"
```

### Message Schema

```json
{
  "message_id": "uuid",
  "sender": "agent_id",
  "receiver": "agent_id | broadcast",
  "type": "request | response | broadcast | negotiate",
  "timestamp": "iso_datetime",
  "payload": {
    "task": "task_description",
    "context": {},
    "constraints": {},
    "deadline": "iso_datetime"
  },
  "metadata": {
    "priority": "high | medium | low",
    "requires_ack": true,
    "conversation_id": "uuid"
  }
}
```

## Task Allocation Strategies

### Deterministic Allocation

```python
deterministic_allocation = {
    "static": {
        "method": "Predefined mapping of task types to agents",
        "pros": ["Predictable", "No coordination overhead"],
        "cons": ["Inflexible", "Load imbalance possible"]
    },
    "round_robin": {
        "method": "Rotate tasks among available agents",
        "pros": ["Simple", "Fair distribution"],
        "cons": ["Ignores agent specialization"]
    },
    "capability_based": {
        "method": "Match task requirements to agent capabilities",
        "pros": ["Optimizes for quality", "Respects specialization"],
        "cons": ["Requires capability modeling"]
    }
}
```

### Dynamic Allocation

```python
dynamic_allocation = {
    "auction": {
        "method": "Agents bid on tasks based on capability/availability",
        "mechanisms": ["First-price", "Second-price", "Combinatorial"],
        "pros": ["Market efficiency", "Self-organizing"],
        "cons": ["Communication overhead", "Strategy gaming"]
    },
    "contract_net": {
        "method": "Manager announces tasks, workers bid, manager awards",
        "steps": [
            "Task announcement",
            "Bid submission",
            "Bid evaluation",
            "Contract award",
            "Execution and report"
        ],
        "pros": ["Flexible", "Distributed decision making"],
        "cons": ["Overhead for simple tasks"]
    },
    "blackboard": {
        "method": "Shared workspace where agents post/claim tasks",
        "pros": ["Loose coupling", "Flexible participation"],
        "cons": ["Coordination overhead", "Potential conflicts"]
    }
}
```

## Consensus Mechanisms

### Voting Protocols

```python
voting_protocols = {
    "majority_vote": {
        "rule": "Option with >50% votes wins",
        "use_when": "Binary decisions, equal agent expertise"
    },
    "weighted_voting": {
        "rule": "Votes weighted by agent expertise/confidence",
        "use_when": "Varying expertise levels"
    },
    "borda_count": {
        "rule": "Ranked preferences, points for positions",
        "use_when": "Multiple options, preference ordering"
    },
    "approval_voting": {
        "rule": "Agents approve any acceptable options",
        "use_when": "Multiple acceptable solutions"
    }
}
```

### Fault-Tolerant Consensus

```python
fault_tolerant_consensus = {
    "byzantine_fault_tolerance": {
        "tolerance": "Up to (n-1)/3 malicious agents",
        "protocols": ["PBFT", "Tendermint", "HotStuff"],
        "use_when": "Untrusted agents, adversarial environment"
    },
    "raft_consensus": {
        "tolerance": "Up to (n-1)/2 crash failures",
        "mechanism": "Leader election + log replication",
        "use_when": "Trusted agents, crash failures only"
    }
}
```

## DEPART Framework (NeurIPS 2024)

Hierarchical goal decomposition for multi-agent systems:

```python
depart_framework = {
    "purpose": "Hierarchical task decomposition and delegation",
    "components": {
        "goal_decomposer": "Breaks high-level goals into subgoals",
        "task_allocator": "Assigns subgoals to appropriate agents",
        "progress_monitor": "Tracks completion and dependencies",
        "conflict_resolver": "Handles resource/goal conflicts"
    },
    "process": [
        "1. Receive high-level goal",
        "2. Decompose into dependency graph of subgoals",
        "3. Allocate subgoals to agents based on capabilities",
        "4. Monitor execution and handle failures",
        "5. Aggregate results and report completion"
    ],
    "benefits": [
        "Scales to complex tasks",
        "Handles partial failures gracefully",
        "Supports dynamic replanning"
    ]
}
```

## Emergent Behavior Analysis

### Detecting Emergence

```markdown
## Emergence Detection Protocol

### Positive Emergence (Beneficial)
- Collaborative problem-solving beyond individual capability
- Collective intelligence and knowledge synthesis
- Self-organization for efficiency
- Adaptive load balancing

### Negative Emergence (Risks)
- Coordination failures and deadlocks
- Cascade failures across agents
- Emergent deception or collusion
- Goal drift through interaction
- Resource exhaustion spirals

### Monitoring Metrics
- Individual vs collective performance ratio
- Communication pattern analysis
- Goal coherence over time
- Resource utilization patterns
- Decision convergence/divergence
```

### Failure Prevention

```python
failure_prevention = {
    "coordination_failures": {
        "deadlock": {
            "cause": "Circular waiting for resources",
            "prevention": "Resource ordering, timeouts, deadlock detection"
        },
        "livelock": {
            "cause": "Agents continuously changing state without progress",
            "prevention": "Randomized backoff, priority ordering"
        },
        "starvation": {
            "cause": "Agent never receives resources",
            "prevention": "Fair scheduling, priority aging"
        }
    },
    "cascade_failures": {
        "cause": "Failure propagates through agent dependencies",
        "prevention": [
            "Circuit breakers",
            "Bulkhead isolation",
            "Graceful degradation",
            "Redundancy"
        ]
    }
}
```

## Implementation Template

### Multi-Agent System Design

```python
class MultiAgentSystem:
    """Template for multi-agent orchestration system."""
    
    def __init__(self, config):
        self.agents = {}
        self.orchestrator = Orchestrator(config.pattern)
        self.communication = CommunicationBus(config.protocol)
        self.task_allocator = TaskAllocator(config.allocation_strategy)
        self.consensus = ConsensusModule(config.consensus_mechanism)
        self.monitor = EmergenceMonitor()
    
    def register_agent(self, agent_id, agent, capabilities):
        """Register an agent with its capabilities."""
        self.agents[agent_id] = {
            "agent": agent,
            "capabilities": capabilities,
            "status": "available"
        }
    
    def execute_task(self, task):
        """Execute a task using the multi-agent system."""
        # 1. Decompose task
        subtasks = self.orchestrator.decompose(task)
        
        # 2. Allocate to agents
        assignments = self.task_allocator.allocate(subtasks, self.agents)
        
        # 3. Execute with coordination
        results = self.orchestrator.execute(assignments, self.communication)
        
        # 4. Aggregate and consensus if needed
        if task.requires_consensus:
            final_result = self.consensus.aggregate(results)
        else:
            final_result = self.orchestrator.aggregate(results)
        
        # 5. Monitor for emergence
        self.monitor.analyze(results, final_result)
        
        return final_result
```

### Agent Implementation

```python
class BaseAgent:
    """Base class for agents in multi-agent system."""
    
    def __init__(self, agent_id, capabilities):
        self.id = agent_id
        self.capabilities = capabilities
        self.state = {}
        self.message_queue = []
    
    def receive_message(self, message):
        """Handle incoming message from other agents."""
        self.message_queue.append(message)
    
    def send_message(self, receiver, message_type, payload):
        """Send message to another agent."""
        return Message(
            sender=self.id,
            receiver=receiver,
            type=message_type,
            payload=payload
        )
    
    def execute_task(self, task):
        """Execute assigned task."""
        raise NotImplementedError
    
    def can_handle(self, task):
        """Check if agent can handle task."""
        return all(req in self.capabilities for req in task.requirements)
```

## Frameworks and Tools

```yaml
orchestration_frameworks:
  general_purpose:
    - LangGraph: "Graph-based multi-agent workflows"
    - AutoGen: "Microsoft's multi-agent conversation framework"
    - CrewAI: "Role-based agent orchestration"
    - Agent Squad: "AWS multi-agent orchestrator"
    
  specialized:
    - CAMEL: "Communicative agents for mind exploration"
    - MetaGPT: "Multi-agent software development"
    - ChatDev: "Collaborative coding agents"
    
  research:
    - MARL libraries: "PettingZoo, RLlib multi-agent"
    - MESA: "Agent-based modeling in Python"
```

## Integration with Other Skills

```
1. Use agi-hypothesis-generator:
   - Hypothesize optimal multi-agent configurations
   
2. Use multi-agent-orchestrator (THIS SKILL):
   - Design agent architecture
   - Implement coordination protocols
   
3. Use experiment-tracker:
   - Run multi-agent experiments
   - Compare configurations
   
4. Use benchmark-creator:
   - Create multi-agent benchmarks
   
5. Use safety-alignment-researcher:
   - Evaluate emergent behaviors
   - Ensure collective alignment
   
6. Use memory-manager:
   - Store system designs
   - Track performance
```

## Knowledge Graph Integration

```cypher
// Store multi-agent system design
CREATE (mas:MultiAgentSystem {
  id: 'mas_001',
  name: 'OMEGA_ASI_Collective',
  pattern: 'hierarchical',
  agent_count: 5,
  created_date: datetime()
})

// Store agents
CREATE (a1:Agent {id: 'planner_01', role: 'planner', capabilities: ['decomposition', 'prioritization']})
CREATE (a2:Agent {id: 'executor_01', role: 'executor', capabilities: ['reasoning', 'tool_use']})

// Create relationships
CREATE (mas)-[:INCLUDES]->(a1)
CREATE (mas)-[:INCLUDES]->(a2)
CREATE (a1)-[:COORDINATES]->(a2)
```

## Best Practices

1. **Start Simple**: Begin with 2-3 agents before scaling
2. **Clear Roles**: Define unambiguous agent responsibilities
3. **Monitor Emergence**: Watch for unexpected collective behaviors
4. **Design for Failure**: Assume agents can fail
5. **Minimize Communication**: Reduce coordination overhead
6. **Test Interactions**: Unit test + integration test agents
7. **Version Protocols**: Manage protocol changes carefully
8. **Log Everything**: Comprehensive interaction logging
9. **Safety First**: Collective alignment is harder than individual
10. **Scale Gradually**: Add agents incrementally

## Version History

- **v1.0.0** (2026-01-31): Initial release with orchestration patterns, communication protocols, consensus mechanisms, and emergence analysis

---

*This skill is part of the AGI/ASI Research Agent Skills collection*

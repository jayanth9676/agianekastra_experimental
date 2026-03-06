---
name: advanced-memory-system
description: Brain-inspired 10000x human memory architecture with episodic/semantic/procedural memory, hippocampal indexing, memory consolidation, and associative retrieval
author: AGI Research Team
version: 1.0.0
tags: [agi, asi, memory, hippocampal, consolidation, retrieval]
---

# Advanced Memory System

## Overview

This skill implements a brain-inspired memory architecture combining episodic, semantic, and procedural memory systems with hippocampal indexing, memory consolidation, and associative retrieval. The system is designed to operate at 10000x human brain capacity for AGI/ASI research agents.

## When to Use This Skill

Use this skill when you need to:
- Implement long-term persistent memory beyond context window
- Store autobiographical experiences with temporal context
- Maintain factual knowledge graphs with concept relationships
- Capture and refine procedural workflows and skills
- Enable multi-hop associative reasoning over memories
- Implement human-like memory consolidation (sleep-like processes)
- Support lifelong learning without catastrophic forgetting
- Build memory systems for autonomous agents

## Core Concepts

### Multi-Modal Memory Architecture

The memory system is organized into three interdependent memory types:

#### 1. Episodic Memory
- **Purpose:** Autobiographical event storage with temporal context
- **Structure:** Temporal sequences of experiences (what, when, where, who, why)
- **Duration:** Short-term (minutes-hours) → Long-term (lifetime)
- **Consolidation:** Hippocampal replay during sleep/idle periods
- **Retrieval:** Pattern-based associative retrieval

#### 2. Semantic Memory
- **Purpose:** Factual knowledge, concepts, relationships
- **Structure:** Hierarchical knowledge graphs, schemas, propositions
- **Formation:** Extraction from episodic memories via generalization
- **Organization:** Thematic clustering, semantic networks
- **Retrieval:** Concept-based, spreading activation

#### 3. Procedural Memory
- **Purpose:** Skills, workflows, routines, motor sequences
- **Structure:** Conditioned action sequences, production rules
- **Acquisition:** Repetition, practice, meta-learning
- **Refinement:** Success/failure feedback, RL optimization
- **Retrieval:** Automatic triggering via context matching

### Hippocampal Indexing System

Inspired by biological hippocampus, this enables fast pattern separation/completion:

**Pattern Separation:**
- Distinguish similar memories (orthogonalization)
- Sparse distributed representations
- Prevent interference between overlapping experiences

**Pattern Completion:**
- Retrieve full memories from partial cues
- Fill gaps in episodic sequences
- Enable associative recall

**Temporal Context Encoding:**
- Time cells encode temporal sequences
- Phase precession for ordering
- Relative timestamp encoding

### Memory Consolidation Mechanisms

#### Hippocampal-Neocortical Transfer

**Stage 1: Encoding (Seconds-Hours)**
- Immediate hippocampal storage
- High-fidelity, transient representations
- Dopamine-gated plasticity

**Stage 2: Consolidation (Hours-Days)**
- Offline replay during sleep/idle
- Reactivation of memory traces
- Gradual transfer to neocortex

**Stage 3: Integration (Days-Weeks)**
- Neocortical synaptic changes
- Schema formation and integration
- Transformation from episodic to semantic

**Stage 4: Long-Term Storage (Lifetime)**
- Distributed neocortical representations
- Indexed via hippocampal pointers
- Stable, interference-resistant

#### Consolidation Optimization

**Prioritized Replay:**
- Emotional salience weighting
- Prediction error magnitude
- Task importance scoring

**Dream-Like Replay:**
- Generative recombination of memories
- Counterfactual exploration
- Creative problem solving

**Forgetting Curves:**
- Ebbinghaus exponential decay
- Spacing effect optimization
- Adaptive forgetting thresholds

### Associative Retrieval

**Multi-Hop Reasoning:**
- Graph traversal over semantic memories
- Episodic chain linking
- Cross-modal inference

**Spreading Activation:**
- Activation propagation through memory network
- Contextual priming
- Subconscious retrieval

**Query Expansion:**
- Semantic similarity expansion
- Temporal context inclusion
- Multi-modal fusion

## Methodologies

### Memory Encoding Pipeline

#### Step 1: Perception and Preprocessing

```python
class MemoryEncoder:
    """Encode raw experiences into memory representations."""
    
    def encode_experience(self, experience: Dict) -> MemoryRepresentation:
        """
        Transform raw experience into structured memory.
        
        Args:
            experience: Raw experience dict with observations, actions, context
            
        Returns:
            MemoryRepresentation: Structured memory with embeddings
        """
        # Extract temporal features
        temporal_context = self._encode_temporal_context(
            experience['timestamp'],
            experience['duration']
        )
        
        # Extract spatial features
        spatial_context = self._encode_spatial_context(
            experience['location'],
            experience['environment']
        )
        
        # Encode semantic content
        semantic_embedding = self.semantic_encoder.encode(
            experience['content']
        )
        
        # Generate episodic embedding (what happened)
        episodic_embedding = self.episodic_encoder.encode({
            'observations': experience['observations'],
            'actions': experience['actions'],
            'outcomes': experience['outcomes']
        })
        
        return MemoryRepresentation(
            episodic_embedding=episodic_embedding,
            semantic_embedding=semantic_embedding,
            temporal_context=temporal_context,
            spatial_context=spatial_context,
            metadata=experience['metadata']
        )
```

#### Step 2: Hippocampal Storage

```python
class Hippocampus:
    """Fast episodic memory storage with pattern separation."""
    
    def store_episode(self, episode: MemoryRepresentation) -> str:
        """
        Store episode in hippocampus with pattern separation.
        
        Args:
            episode: Memory representation to store
            
        Returns:
            str: Episode ID for retrieval
        """
        # Apply pattern separation (orthogonalization)
        separated_vector = self._pattern_separate(
            episode.episodic_embedding
        )
        
        # Generate sparse representation
        sparse_encoding = self._sparse_encode(separated_vector)
        
        # Create temporal index
        temporal_index = self._create_temporal_index(
            episode.temporal_context
        )
        
        # Store with hippocampal pointer
        episode_id = self._generate_episode_id()
        self.memory_store[episode_id] = {
            'encoding': sparse_encoding,
            'temporal_index': temporal_index,
            'original': episode,
            'timestamp': time.time(),
            'consolidation_status': 'unconsolidated'
        }
        
        # Queue for consolidation
        self.consolidation_queue.append(episode_id)
        
        return episode_id
```

#### Step 3: Semantic Memory Formation

```python
class SemanticMemory:
    """Factual knowledge graph with concept relationships."""
    
    def extract_semantic_memory(
        self, 
        episode: MemoryRepresentation,
        episode_id: str
    ) -> List[SemanticTriple]:
        """
        Extract semantic facts from episodic memory.
        
        Args:
            episode: Episodic memory representation
            episode_id: Source episode ID
            
        Returns:
            List[SemanticTriple]: Extracted semantic triples
        """
        # Use LLM to extract facts
        extraction_prompt = f"""
        Extract factual knowledge from this experience:
        
        Episode: {episode.original}
        
        Extract as semantic triples (subject, relation, object).
        Include temporal context when relevant.
        """
        
        facts = self.llm.generate(extraction_prompt)
        
        # Create semantic triples
        triples = []
        for fact in facts:
            subject_node = self._get_or_create_concept(fact['subject'])
            object_node = self._get_or_create_concept(fact['object'])
            
            triple = SemanticTriple(
                subject=subject_node,
                relation=fact['relation'],
                object=object_node,
                source=episode_id,
                confidence=fact['confidence'],
                temporal_context=fact.get('temporal')
            )
            triples.append(triple)
        
        return triples
```

#### Step 4: Procedural Memory Learning

```python
class ProceduralMemory:
    """Skill and workflow storage with reinforcement learning."""
    
    def learn_procedure(
        self,
        episode: MemoryRepresentation,
        success: bool,
        reward: float
    ) -> Procedure:
        """
        Learn or refine procedural skill from experience.
        
        Args:
            episode: Experience to learn from
            success: Whether the procedure succeeded
            reward: Reward signal for RL
            
        Returns:
            Procedure: Learned or refined procedure
        """
        # Extract action sequence
        action_sequence = episode.original['actions']
        
        # Check if similar procedure exists
        existing = self._find_similar_procedure(action_sequence)
        
        if existing:
            # Update existing procedure
            updated = self._refine_procedure(
                existing,
                action_sequence,
                success,
                reward
            )
            return updated
        else:
            # Create new procedure
            new_procedure = Procedure(
                preconditions=self._extract_preconditions(episode),
                actions=action_sequence,
                postconditions=self._extract_postconditions(episode),
                success_rate=1.0 if success else 0.0,
                usage_count=0,
                last_updated=time.time()
            )
            self.procedures.append(new_procedure)
            return new_procedure
```

### Memory Retrieval Pipeline

#### Step 1: Query Processing

```python
class MemoryRetriever:
    """Multi-modal memory retrieval with associative reasoning."""
    
    def retrieve(
        self,
        query: str,
        memory_types: List[str] = ['episodic', 'semantic', 'procedural'],
        max_hops: int = 3
    ) -> RetrievalResult:
        """
        Retrieve relevant memories across all memory systems.
        
        Args:
            query: Natural language query
            memory_types: Which memory types to search
            max_hops: Max reasoning hops for associative retrieval
            
        Returns:
            RetrievalResult: Retrieved memories with confidence scores
        """
        # Encode query
        query_embedding = self.query_encoder.encode(query)
        
        results = RetrievalResult()
        
        # Episodic retrieval (pattern completion)
        if 'episodic' in memory_types:
            episodic_results = self._retrieve_episodic(
                query_embedding,
                query
            )
            results.add_results('episodic', episodic_results)
        
        # Semantic retrieval (graph traversal)
        if 'semantic' in memory_types:
            semantic_results = self._retrieve_semantic(
                query_embedding,
                max_hops
            )
            results.add_results('semantic', semantic_results)
        
        # Procedural retrieval (context matching)
        if 'procedural' in memory_types:
            procedural_results = self._retrieve_procedural(
                query
            )
            results.add_results('procedural', procedural_results)
        
        # Cross-modal association
        results = self._cross_modal_association(results)
        
        return results
```

#### Step 2: Associative Multi-Hop Reasoning

```python
    def _retrieve_semantic(
        self,
        query_embedding: np.ndarray,
        max_hops: int
    ) -> List[SemanticResult]:
        """
        Retrieve semantic memories with multi-hop reasoning.
        
        Args:
            query_embedding: Query vector representation
            max_hops: Maximum graph traversal depth
            
        Returns:
            List[SemanticResult]: Retrieved semantic facts
        """
        # Find seed concepts (hop 0)
        seed_concepts = self.semantic_index.search(
            query_embedding,
            k=10
        )
        
        # Spreading activation through semantic network
        results = []
        visited = set()
        queue = [(concept, 0) for concept in seed_concepts]
        
        while queue:
            concept, hop = queue.pop(0)
            
            if hop > max_hops or concept in visited:
                continue
            
            visited.add(concept)
            
            # Get related concepts
            relations = self.semantic_graph.get_relations(concept)
            
            for relation in relations:
                related_concept = relation.target
                activation = relation.weight * (1.0 / (hop + 1))
                
                results.append(SemanticResult(
                    relation=relation,
                    activation=activation,
                    hop_depth=hop,
                    path=self._trace_path(relation)
                ))
                
                queue.append((related_concept, hop + 1))
        
        # Sort by activation and return
        results.sort(key=lambda x: x.activation, reverse=True)
        return results[:50]
```

### Memory Consolidation System

#### Offline Replay Process

```python
class MemoryConsolidator:
    """Hippocampal-neocortical memory consolidation."""
    
    def consolidate(self):
        """
        Perform offline consolidation (sleep-like process).
        """
        # Get episodes pending consolidation
        pending = self._get_pending_episodes()
        
        for episode_id in pending:
            episode = self.hippocampus.retrieve(episode_id)
            
            # Determine consolidation priority
            priority = self._calculate_consolidation_priority(episode)
            
            if priority > self.consolidation_threshold:
                # Perform replay
                replay_count = self._replay_episode(episode)
                
                if replay_count >= self.replay_threshold:
                    # Transfer to neocortex
                    self._transfer_to_neocortex(episode)
                    
                    # Extract semantic memory
                    self.semantic_memory.extract_semantic_memory(
                        episode,
                        episode_id
                    )
                    
                    # Learn procedures if applicable
                    if self._is_procedural(episode):
                        self.procedural_memory.learn_procedure(
                            episode,
                            episode.metadata.get('success', True),
                            episode.metadata.get('reward', 0.0)
                        )
                    
                    # Mark as consolidated
                    self.hippocampus.mark_consolidated(episode_id)
```

#### Dream-Like Generative Replay

```python
    def _replay_episode(self, episode: Episode) -> int:
        """
        Perform dream-like replay with generative reconstruction.
        
        Args:
            episode: Episode to replay
            
        Returns:
            int: Number of replay iterations
        """
        replay_count = 0
        
        while replay_count < self.max_replays:
            # Generative reconstruction with variations
            reconstruction = self._generate_reconstruction(
                episode,
                variation_strength=0.2
            )
            
            # Evaluate reconstruction fidelity
            fidelity = self._evaluate_fidelity(
                episode.original,
                reconstruction
            )
            
            # Update memory based on replay
            self._strengthen_memory(episode, fidelity)
            
            # Early stop if fully consolidated
            if fidelity > self.fidelity_threshold:
                break
            
            replay_count += 1
        
        return replay_count
```

### Forgetting and Decay Management

```python
class ForgetManager:
    """Adaptive forgetting based on Ebbinghaus curves."""
    
    def apply_forgetting(self):
        """
        Apply forgetting decay to all memories.
        """
        current_time = time.time()
        
        for memory_id, memory in self.all_memories.items():
            age = current_time - memory.timestamp
            
            # Calculate forgetting factor
            forgetting_factor = self._ebbinghaus_decay(
                age,
                memory.access_count,
                memory.emotional_salience
            )
            
            # Apply decay
            memory.strength *= forgetting_factor
            
            # Check for deletion
            if memory.strength < self.forgetting_threshold:
                self._archive_memory(memory_id)
```

### Neo4j Integration

#### Memory Schema

```cypher
// Create episodic memory node
CREATE (e:Episode {
    id: $episode_id,
    timestamp: datetime($timestamp),
    duration: $duration,
    location: $location,
    context: $context,
    emotional_salience: $salience,
    consolidation_status: 'unconsolidated',
    access_count: 0,
    strength: 1.0
})

// Create semantic memory node
CREATE (s:SemanticMemory {
    id: $semantic_id,
    fact: $fact,
    confidence: $confidence,
    temporal_context: $temporal,
    source_episode: $episode_id,
    strength: 1.0
})

// Create procedural memory node
CREATE (p:Procedure {
    id: $procedure_id,
    preconditions: $preconditions,
    actions: $actions,
    postconditions: $postconditions,
    success_rate: $success_rate,
    usage_count: 0,
    last_refined: datetime()
})

// Create relationships
CREATE (e)-[:EXTRACTED_AS]->(s)
CREATE (e)-[:LEARNED_AS]->(p)
CREATE (s1:SemanticMemory)-[:RELATED_TO {relation: $relation_type}]->(s2:SemanticMemory)
```

#### Semantic Query Example

```cypher
// Multi-hop semantic retrieval
MATCH (start:SemanticMemory)-[:RELATED_TO*1..3]->(target:SemanticMemory)
WHERE start.fact CONTAINS $query
RETURN target, path, length(path) as hop_depth
ORDER BY target.strength * (1.0 / hop_depth) DESC
LIMIT 50
```

#### Episodic Query Example

```cypher
// Pattern-based episodic retrieval
MATCH (e:Episode)
WHERE e.context CONTAINS $pattern
   OR e.location CONTAINS $pattern
   OR e.summary CONTAINS $pattern
RETURN e, 
       [e-[:RELATED_TO]->(related)] as related_episodes
ORDER BY e.strength DESC, e.emotional_salience DESC
LIMIT 20
```

### Integration with OMEGA ASI

```python
class OMEGAMemorySystem:
    """Integrated memory for OMEGA ASI architecture."""
    
    def __init__(self):
        # Initialize memory subsystems
        self.hippocampus = Hippocampus()
        self.semantic_memory = SemanticMemory()
        self.procedural_memory = ProceduralMemory()
        self.consolidator = MemoryConsolidator()
        self.neo4j = Neo4jMemoryStore()
        
        # Integrate with OMEGA architecture
        self.architecture_memory = ArchitectureMemory()
        self.research_memory = ResearchMemory()
    
    def store_architecture_version(
        self,
        version: str,
        components: List[Component],
        innovations: List[str]
    ):
        """
        Store OMEGA ASI architecture version with memory.
        """
        # Create episodic memory of version creation
        episode = Episode(
            content=f"Created OMEGA_ASI_{version}",
            observations=[str(c) for c in components],
            metadata={
                'type': 'architecture_version',
                'version': version,
                'innovations': innovations
            }
        )
        episode_id = self.hippocampus.store_episode(episode)
        
        # Extract semantic knowledge
        semantic_triples = self.semantic_memory.extract_semantic_memory(
            episode, episode_id
        )
        
        # Store in Neo4j
        self.neo4j.create_episode(episode)
        self.neo4j.create_semantic_triples(semantic_triples)
        
        # Queue consolidation
        self.consolidator.consolidate()
```

## Implementation Templates

### Complete Memory System Class

```python
from typing import Dict, List, Optional
import numpy as np
from dataclasses import dataclass
import time
from neo4j import GraphDatabase

@dataclass
class MemoryRepresentation:
    episodic_embedding: np.ndarray
    semantic_embedding: np.ndarray
    temporal_context: Dict
    spatial_context: Dict
    metadata: Dict

@dataclass
class Episode:
    id: str
    content: str
    observations: List[str]
    actions: List[str]
    timestamp: float
    location: Optional[str] = None
    emotional_salience: float = 0.5
    consolidation_status: str = 'unconsolidated'
    access_count: int = 0
    strength: float = 1.0

class AdvancedMemorySystem:
    """
    Brain-inspired memory system for AGI/ASI agents.
    
    Combines episodic, semantic, and procedural memory
    with hippocampal indexing and consolidation.
    """
    
    def __init__(
        self,
        neo4j_uri: str = "bolt://localhost:7687",
        neo4j_user: str = "neo4j",
        neo4j_password: str = "password"
    ):
        self.neo4j = GraphDatabase.driver(
            neo4j_uri, 
            auth=(neo4j_user, neo4j_password)
        )
        
        self.episodes: Dict[str, Episode] = {}
        self.semantic_memories: List[SemanticMemory] = []
        self.procedures: List[Procedure] = []
        
        self.consolidation_queue: List[str] = []
        self.consolidation_threshold: float = 0.7
        
    def store_experience(
        self,
        content: str,
        observations: List[str],
        actions: List[str],
        metadata: Dict = None
    ) -> str:
        """
        Store a new experience in episodic memory.
        
        Args:
            content: Description of what happened
            observations: List of observations
            actions: List of actions taken
            metadata: Additional context
            
        Returns:
            str: Episode ID
        """
        episode_id = f"ep_{int(time.time()*1000)}"
        
        episode = Episode(
            id=episode_id,
            content=content,
            observations=observations,
            actions=actions,
            timestamp=time.time(),
            emotional_salience=metadata.get('salience', 0.5),
            metadata=metadata or {}
        )
        
        self.episodes[episode_id] = episode
        self.consolidation_queue.append(episode_id)
        
        # Store in Neo4j
        with self.neo4j.session() as session:
            session.run(
                """
                CREATE (e:Episode {
                    id: $id,
                    content: $content,
                    timestamp: datetime($timestamp),
                    emotional_salience: $salience
                })
                """,
                id=episode_id,
                content=content,
                timestamp=episode.timestamp,
                salience=episode.emotional_salience
            )
        
        return episode_id
    
    def retrieve(
        self,
        query: str,
        memory_type: str = 'all',
        max_results: int = 10
    ) -> List[Dict]:
        """
        Retrieve memories matching query.
        
        Args:
            query: Search query
            memory_type: 'episodic', 'semantic', 'procedural', or 'all'
            max_results: Maximum results to return
            
        Returns:
            List[Dict]: Retrieved memories with scores
        """
        results = []
        
        if memory_type in ['episodic', 'all']:
            episodic = self._retrieve_episodic(query, max_results)
            results.extend(episodic)
        
        if memory_type in ['semantic', 'all']:
            semantic = self._retrieve_semantic(query, max_results)
            results.extend(semantic)
        
        return sorted(results, key=lambda x: x['score'], reverse=True)[:max_results]
    
    def consolidate(self, batch_size: int = 10):
        """
        Perform memory consolidation on pending episodes.
        
        Args:
            batch_size: Number of episodes to consolidate
        """
        pending = self.consolidation_queue[:batch_size]
        
        for episode_id in pending:
            episode = self.episodes.get(episode_id)
            if not episode:
                continue
            
            # Extract semantic memory
            self._extract_semantic(episode, episode_id)
            
            # Learn procedural memory if applicable
            if self._is_procedural(episode):
                self._learn_procedure(episode, episode_id)
            
            # Update consolidation status
            episode.consolidation_status = 'consolidated'
            
            # Update in Neo4j
            with self.neo4j.session() as session:
                session.run(
                    """
                    MATCH (e:Episode {id: $id})
                    SET e.consolidation_status = 'consolidated'
                    """,
                    id=episode_id
                )
        
        # Remove consolidated from queue
        self.consolidation_queue = self.consolidation_queue[batch_size:]
    
    def _retrieve_episodic(self, query: str, max_results: int) -> List[Dict]:
        """Retrieve episodic memories."""
        with self.neo4j.session() as session:
            result = session.run(
                """
                MATCH (e:Episode)
                WHERE e.content CONTAINS $query
                RETURN e.id, e.content, e.emotional_salience, e.access_count
                ORDER BY e.emotional_salience * e.access_count DESC
                LIMIT $limit
                """,
                query=query,
                limit=max_results
            )
            
            return [
                {
                    'type': 'episodic',
                    'id': record['e.id'],
                    'content': record['e.content'],
                    'score': record['e.emotional_salience'] * record['e.access_count']
                }
                for record in result
            ]
    
    def _extract_semantic(self, episode: Episode, episode_id: str):
        """Extract semantic facts from episode."""
        facts = [
            f"The system observed: {obs}"
            for obs in episode.observations
        ]
        
        for fact in facts:
            with self.neo4j.session() as session:
                session.run(
                    """
                    MATCH (e:Episode {id: $episode_id})
                    CREATE (s:SemanticMemory {
                        id: $semantic_id,
                        fact: $fact,
                        timestamp: datetime()
                    })
                    CREATE (e)-[:EXTRACTED_AS]->(s)
                    """,
                    episode_id=episode_id,
                    semantic_id=f"sem_{int(time.time()*1000)}_{hash(fact)}",
                    fact=fact
                )
    
    def _is_procedural(self, episode: Episode) -> bool:
        """Check if episode describes a procedure."""
        procedural_keywords = ['workflow', 'process', 'routine', 'procedure']
        return any(
            kw in episode.content.lower() 
            for kw in procedural_keywords
        )
    
    def _learn_procedure(self, episode: Episode, episode_id: str):
        """Learn procedural memory from episode."""
        with self.neo4j.session() as session:
            session.run(
                """
                MATCH (e:Episode {id: $episode_id})
                CREATE (p:Procedure {
                    id: $procedure_id,
                    actions: $actions,
                    usage_count: 0,
                    success_rate: 1.0
                })
                CREATE (e)-[:LEARNED_AS]->(p)
                """,
                episode_id=episode_id,
                procedure_id=f"proc_{int(time.time()*1000)}",
                actions=episode.actions
            )
```

## Best Practices

### Memory Storage

1. **Immediate Storage** - Capture experiences as they occur
2. **Rich Context** - Include temporal, spatial, emotional context
3. **Consistent IDs** - Use deterministic episode/memory IDs
4. **Queue Consolidation** - Don't delay consolidation process

### Memory Retrieval

1. **Multi-Modal Search** - Query all memory types
2. **Association Chains** - Enable multi-hop reasoning
3. **Context Relevance** - Score by contextual match
4. **Diverse Results** - Return mix of memory types

### Consolidation

1. **Prioritize Important** - High salience, high access
2. **Batch Processing** - Consolidate in groups
3. **Extract All Types** - Semantic and procedural
4. **Track Progress** - Monitor consolidation rates

### Forgetting

1. **Adaptive Decay** - Adjust based on access patterns
2. **Archive Instead** - Don't delete, mark archived
3. **Emotional Bias** - Preserve salient memories
4. **Forgetting Curves** - Follow Ebbinghaus model

## Integration with Other Skills

- **knowledge-graph-query** - Semantic memory queries
- **experiment-tracker** - Episodic storage of experiments
- **meta-learning-protocol** - Procedural skill acquisition
- **agi-researcher** - Long-term research memory
- **multi-agent-orchestrator** - Shared memory across agents

## References

### Key Papers

1. **A-MEM: Agentic Memory for LLM Agents** - NeurIPS 2025
   - Xu et al., 2025
   - Dynamic memory organization, Zettelkasten method
   
2. **MemGPT: Towards LLMs as Operating Systems** - arXiv:2310.08560
   - Letta (UC Berkeley)
   - Self-editing memory, context management
   
3. **HippoRAG: Neurobiologically Inspired Long-Term Memory** - arXiv:2405.14831
   - Hippocampal indexing, pattern separation/completion
   
4. **Linking In-context Learning to Human Episodic Memory** - arXiv:2405.14992
   - Spens & Burgess, 2024
   - Memory consolidation models
   
5. **AI Meets Brain: Unified Survey on Memory Systems** - arXiv:2512.23343
   - Liang et al., 2025
   - Comprehensive memory taxonomy

### Frameworks and Libraries

- **Letta** (https://letta.com) - MemGPT-based memory framework
- **Zep** (https://zep.ai) - Temporal knowledge graph memory
- **Mem0** (https://github.com/mem0ai/mem0) - Production-ready memory
- **A-Mem** (https://github.com/WujiangXu/A-mem) - Agentic memory
- **Awesome-Memory-for-Agents** (https://github.com/TsinghuaC3I) - Paper collection

## Dependencies

- **neo4j-memory MCP tool** - Persistent memory storage
- **knowledge-graph-query skill** - Semantic retrieval
- **Local Neo4j database** - Graph database backend
- **sentence-transformers** - Embedding generation
- **numpy** - Vector operations

## Troubleshooting

### Consolidation takes too long?
- Reduce batch size
- Lower consolidation threshold
- Prioritize high-salience episodes first

### Retrieval quality poor?
- Check embedding quality
- Improve query formulation
- Increase max_hops for semantic retrieval
- Verify Neo4j indexes

### Memory growing too large?
- Apply forgetting curves
- Archive old episodes
- Compress consolidated episodic memories
- Delete low-strength semantic memories

### Cross-modal associations weak?
- Improve episode-semantic extraction
- Add more relation types
- Increase spreading activation weight
- Track cross-modal links explicitly

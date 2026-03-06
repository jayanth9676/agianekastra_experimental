---
name: knowledge-graph-query
description: Query and explore the persistent Neo4j knowledge graph to retrieve research findings, track concept relationships, and analyze the research history
---

# Knowledge Graph Query Skill

This skill provides tools to query and explore the persistent Neo4j knowledge graph that stores all research findings, papers, concepts, experiments, and their relationships.

## When to Use This Skill

Use this skill when you need to:
- Retrieve previously stored research findings from memory
- Find papers related to a specific concept or topic
- Track the evolution of OMEGA ASI architectures
- Analyze citation networks between papers
- Query experiment results and metrics
- Explore concept relationships and hierarchies
- Find research gaps or unanswered questions

## Knowledge Graph Schema

### Node Types

1. **Paper**
   - Properties: arxiv_id, title, authors, abstract, publication_date, key_findings, citations
   - Use: Store and retrieve academic papers

2. **Concept**
   - Properties: name, definition, domain, related_concepts, first_seen_date
   - Use: Track key concepts and their definitions

3. **Experiment**
   - Properties: id, config, metrics, results, timestamp, version, status
   - Use: Log ML experiments and their outcomes

4. **Architecture**
   - Properties: name (e.g., "OMEGA_ASI_v450"), components, innovations, status, created_date
   - Use: Track OMEGA ASI version evolution

5. **Question**
   - Properties: text, status (open/answered/researching), priority, created_date
   - Use: Manage research questions and their status

6. **Finding**
   - Properties: summary, evidence, confidence (0-1), date, source
   - Use: Store specific research findings

### Relationship Types

- `(Paper)-[:CITES]->(Paper)` - Citation relationships
- `(Paper)-[:IMPLEMENTS]->(Concept)` - Papers implementing concepts
- `(Paper)-[:EVALUATES]->(Architecture)` - Papers evaluating architectures
- `(Concept)-[:RELATED_TO]->(Concept)` - Concept relationships
- `(Concept)-[:USED_IN]->(Experiment)` - Concepts used in experiments
- `(Experiment)-[:TESTS]->(Architecture)` - Experiments testing architectures
- `(Architecture)-[:EVOLVES_FROM]->(Architecture)` - Version evolution
- `(Experiment)-[:PRODUCES]->(Finding)` - Experiments producing findings
- `(Finding)-[:ANSWERS]->(Question)` - Findings answering questions

## How to Use

### Basic Usage

Query the knowledge graph using Cypher-like patterns through the neo4j-memory MCP tool:

```
Use neo4j-memory to search for papers about "neural architecture search"
```

```
Query neo4j-memory: Find all papers that cite "attention is all you need"
```

```
Use knowledge graph: Show me the evolution from OMEGA_ASI_v100 to v500
```

### Common Query Patterns

1. **Find papers by topic:**
   ```
   Search memory for papers related to "meta-learning"
   ```

2. **Track architecture evolution:**
   ```
   Query graph: Show me all versions of OMEGA_ASI architecture
   ```

3. **Find related concepts:**
   ```
   Explore knowledge graph: What concepts are related to "self-attention"?
   ```

4. **Retrieve experiment results:**
   ```
   Query memory: Find experiments testing OMEGA_ASI_v300
   ```

5. **Find unanswered questions:**
   ```
   Search graph: Show open research questions with high priority
   ```

## Integration with Other Tools

Always query memory BEFORE using external search tools:

1. **Before using academia-mcp:**
   ```
   Query neo4j-memory: What do we know about [topic]?
   Then search academia-mcp for gaps
   ```

2. **Before using exa:**
   ```
   Check memory for existing findings on [topic]
   Then use exa for latest developments
   ```

3. **After finding new information:**
   ```
   Store in neo4j-memory: [finding]
   Create relationship to [existing concept]
   ```

## Best Practices

1. **Always query first** - Check memory before external research
2. **Use specific terms** - Search for exact concept/architecture names
3. **Follow relationships** - Explore connections between nodes
4. **Check versions** - Track evolution using [:EVOLVES_FROM] relationships
5. **Validate findings** - Cross-reference multiple sources when possible
6. **Update status** - Mark questions as "answered" when resolved

## Examples

### Example 1: Research Literature Review

```
Query: "Find all papers about transformer alternatives for AGI"

Process:
1. Query neo4j-memory for papers with concept "transformer_alternatives"
2. Follow CITES relationships to find related work
3. Check which architectures evaluate these concepts
4. Identify gaps for new research
```

### Example 2: Architecture Evolution Analysis

```
Query: "Show the evolution of OMEGA_ASI from v100 to current"

Process:
1. Find Architecture node "OMEGA_ASI_v100"
2. Follow [:EVOLVES_FROM] relationships forward
3. Collect all versions and their innovations
4. Analyze progression patterns
```

### Example 3: Experiment Tracking

```
Query: "Find all experiments testing autopoietic systems"

Process:
1. Search for Concept "autopoiesis"
2. Find [:USED_IN] relationships to Experiments
3. Retrieve experiment configs and results
4. Compare metrics across experiments
```

## Troubleshooting

### No results found?
- Try broader search terms
- Check for synonyms in the concept graph
- Search external sources and store findings

### Outdated information?
- Check the date property on nodes
- Look for newer [:EVOLVES_FROM] relationships
- Update with latest research from academia-mcp

### Missing relationships?
- Create relationships when storing new findings
- Link related concepts explicitly
- Use consistent naming conventions

## Dependencies

This skill uses:
- **neo4j-memory MCP tool** - For graph queries
- **Local Neo4j database** - Running via docker-compose

Ensure Neo4j is running:
```bash
docker-compose up -d neo4j
```

Access Neo4j browser at: http://localhost:7474

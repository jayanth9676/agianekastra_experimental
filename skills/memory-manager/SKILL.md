---
name: memory-manager
description: Manage, organize, and maintain the persistent knowledge graph memory - store findings, update entries, archive old data, and ensure memory quality
---

# Memory Manager Skill

This skill provides tools to manage, organize, and maintain the persistent Neo4j knowledge graph memory. It ensures research findings are properly stored, relationships are created, and the memory remains clean and useful.

## When to Use This Skill

Use this skill when you need to:
- Store new research findings in the knowledge graph
- Update existing memory entries with new information
- Create relationships between concepts, papers, and experiments
- Archive old or outdated research data
- Clean up duplicate entries
- Verify memory integrity and quality
- Organize memory into logical categories

## Core Functions

### 1. Store New Findings

Store research discoveries immediately after finding them:

```
Use memory-manager to store:
- Paper: arXiv:2401.12345 "Neural Architecture Search for AGI"
- Authors: Smith et al.
- Key finding: New method improves search efficiency by 40%
- Concepts: neural_architecture_search, AGI, efficiency
- Confidence: 0.85
```

### 2. Update Existing Entries

Update memory when new information becomes available:

```
Update memory: Paper arXiv:2401.12345 now has 50 citations
Update concept: "transformer" definition refined based on new research
```

### 3. Create Relationships

Explicitly link related concepts and findings:

```
Create relationship: Paper arXiv:2401.12345 CITES Paper arXiv:2305.67890
Create relationship: Concept "attention_mechanism" RELATED_TO Concept "self_attention"
Create relationship: Experiment exp_001 TESTS Architecture OMEGA_ASI_v300
```

### 4. Archive Old Data

Mark outdated or superseded information:

```
Archive: OMEGA_ASI_v100 (superseded by v150)
Mark outdated: Findings from 2023 on this topic
Move to archive: Experiments older than 6 months
```

### 5. Clean Up Duplicates

Find and merge duplicate entries:

```
Find duplicates: Papers with same arXiv ID
Merge concepts: "neural_net" and "neural_network"
Remove duplicate: Redundant experiment entries
```

### 6. Paper Deduplication Protocol (PaperLantern-Inspired)

Before storing ANY paper, run this deduplication check:

**Step 1: Pre-Store Check (MANDATORY)**
```
# Check by arXiv ID (primary key)
neo4j-memory_search_memories(query="arXiv:XXXX.XXXXX")

# Check by title (fuzzy match)
neo4j-memory_search_memories(query="exact paper title here")

# Check by short name convention
neo4j-memory_find_memories_by_name(names=["Short Title (Year)"])
```

**Step 2: Decision Matrix**
```
If EXACT match found (same arXiv ID):
  → DO NOT create new entity
  → ADD new observations to existing entity
  → UPDATE relationships if new ones discovered

If FUZZY match found (similar title, same authors):
  → VERIFY it's the same paper (check year, venue)
  → If same: merge observations into existing entity
  → If different: create new entity with disambiguating name

If NO match found:
  → Create new entity following naming convention
  → Create all relationships immediately
```

**Step 3: Entity Merge Workflow**

When duplicates are discovered after the fact:
```
# 1. Identify the canonical entity (older one, or one with more relationships)
canonical = "Attention Is All You Need (2017)"

# 2. Collect observations from duplicate
duplicate_observations = [obs from duplicate entity]

# 3. Add unique observations to canonical
neo4j-memory_add_observations(observations=[{
    "entityName": canonical,
    "observations": [obs for obs in duplicate_observations if obs not in canonical.observations]
}])

# 4. Re-point relationships from duplicate to canonical
# For each relationship on the duplicate:
#   - Create equivalent relationship on canonical
#   - Delete relationship from duplicate

# 5. Delete the duplicate entity
neo4j-memory_delete_entities(entityNames=["duplicate entity name"])
```

**Step 4: Naming Consistency Enforcement**

Always use these exact patterns to prevent duplicates:
```
Papers:    "{Short Title} ({Year})"         → "Attention Is All You Need (2017)"
ArXiv:     Include "arXiv:{id}" in observations → "arXiv:1706.03762"
Concepts:  "{Concept Name}"                  → "Self-Attention Mechanism"
Decisions: "RD-{DATE}-{slug}"               → "RD-20260228-attention-choice"
```

### 7. Research Decision Entity Storage

Store research-to-implementation decisions for traceability:

```
neo4j-memory_create_entities(entities=[{
    "name": "RD-{DATE}-{slug}",
    "type": "research_decision",
    "observations": [
        "Decision: {what was decided}",
        "Context: {engineering problem being solved}",
        "Papers consulted: {list of paper entity names}",
        "Alternatives considered: {list}",
        "Rationale: {why this choice}",
        "Confidence: {0.0-1.0}",
        "Status: {accepted/rejected/pending}",
        "Timestamp: {datetime}",
        "OMEGA-ASI component: {which module affected}",
        "SICAS phase: {which pipeline phase}"
    ]
}])

# Always link to consulted papers
neo4j-memory_create_relations(relations=[
    {"source": "RD-{DATE}-{slug}", "target": "Paper Name (Year)", "relationType": "INFORMED_BY"},
    {"source": "RD-{DATE}-{slug}", "target": "OMEGA-ASI Component", "relationType": "AFFECTS"}
])
```

## Storage Guidelines

### What to Store

✅ **Always Store:**
- All papers read (title, authors, arXiv ID, key findings)
- Important concepts discovered (name, definition, domain)
- Experiment configurations and results
- OMEGA ASI architecture versions and innovations
- Research questions and their answers
- Significant findings with evidence and confidence

✅ **Store Immediately:**
- Don't wait until end of research session
- Store while information is fresh
- Capture context and source details

### What NOT to Store

❌ **Don't Store:**
- Temporary thoughts or brainstorming
- Incomplete or unverified information
- Personal notes not relevant to research
- Large raw datasets (store summaries instead)
- Duplicate information already in memory

### Storage Quality Standards

Every stored item should have:
1. **Unique identifier** - arXiv ID, experiment ID, etc.
2. **Date** - When discovered/created
3. **Source** - Where information came from
4. **Confidence** - How certain (0.0 to 1.0)
5. **Relationships** - Links to related items

## Storage Workflow

### Step 1: Check Before Storing

Always check if item already exists:

```
Query neo4j-memory: Does paper arXiv:2401.12345 already exist?
If yes → Update existing entry
If no → Create new entry
```

### Step 2: Create Nodes

Create appropriate node types:

```
Create Paper node:
- arxiv_id: 2401.12345
- title: "Neural Architecture Search for AGI"
- authors: ["Smith, J.", "Doe, A."]
- abstract: [paper abstract]
- key_findings: "40% efficiency improvement"
- publication_date: 2024-01-15

Create Concept node:
- name: "neural_architecture_search"
- definition: "Automated search for optimal neural architectures"
- domain: "machine_learning"
- first_seen_date: 2024-01-30
```

### Step 3: Create Relationships

Link new items to existing knowledge:

```
Paper(2401.12345)-[:CITES]->Paper(2305.67890)
Concept(neural_architecture_search)-[:RELATED_TO]->Concept(AGI)
Finding(001)-[:ANSWERS]->Question(003)
```

### Step 4: Verify Storage

Confirm successful storage:

```
Query: Retrieve just-stored paper 2401.12345
Verify: Check all relationships created
```

## Relationship Guidelines

### Essential Relationships

Always create these relationship types:

1. **CITES** - When a paper references another
2. **IMPLEMENTS** - When a paper implements a concept
3. **EVALUATES** - When a paper evaluates an architecture
4. **RELATED_TO** - Between related concepts
5. **USED_IN** - Concepts used in experiments
6. **TESTS** - Experiments testing architectures
7. **EVOLVES_FROM** - Architecture version lineage
8. **PRODUCES** - Experiments producing findings
9. **ANSWERS** - Findings answering questions

### Relationship Properties

Add metadata to relationships:

```
(Paper)-[:CITES {citation_context: "Used for baseline", citation_date: 2024-01-20}]->(Paper)
(Concept)-[:RELATED_TO {relationship_type: "is_a", strength: 0.9}]->(Concept)
```

## Maintenance Tasks

### Daily Maintenance

- ✅ Store all new findings before ending session
- ✅ Verify critical information is saved
- ✅ Update question statuses if answered

### Weekly Maintenance

- 🔍 Check for duplicate entries
- 🔍 Review open questions
- 🔍 Archive superseded findings
- 🔍 Verify experiment tracking

### Monthly Maintenance

- 📊 Analyze memory growth
- 📊 Check relationship completeness
- 📊 Archive old experiments (keep metadata)
- 📊 Update concept definitions if needed

### Quality Checks

Run these queries periodically:

```
# Find papers without citations
MATCH (p:Paper) WHERE NOT (p)-[:CITES]->() RETURN p.title

# Find concepts without relationships
MATCH (c:Concept) WHERE NOT (c)-[:RELATED_TO]->() RETURN c.name

# Find experiments without results
MATCH (e:Experiment) WHERE e.results IS NULL RETURN e.id

# Find duplicate papers (by arXiv ID in observations)
MATCH (p:Paper)
WITH p.arxiv_id as arxiv, count(*) as cnt
WHERE cnt > 1
RETURN arxiv, cnt

# Find potential title duplicates (fuzzy)
MATCH (a), (b) 
WHERE a.name CONTAINS '(' AND b.name CONTAINS '(' 
AND a.name <> b.name
AND apoc.text.levenshteinSimilarity(a.name, b.name) > 0.8
RETURN a.name, b.name

# Find orphaned research decisions (no paper links)
MATCH (rd) WHERE rd.name STARTS WITH 'RD-'
AND NOT (rd)-[:INFORMED_BY]->()
RETURN rd.name
```

## Archiving Strategy

### When to Archive

Archive items when:
- Architecture version is superseded (e.g., v100 → v150)
- Experiment results are outdated by newer experiments
- Concept definition is refined and old one obsolete
- Finding is disproven or significantly revised

### How to Archive

Don't delete - preserve history:

```
# Add archived flag
MATCH (a:Architecture {name: "OMEGA_ASI_v100"})
SET a.status = "archived", a.archived_date = "2024-01-30"

# Create relationship to successor
MATCH (old:Architecture {name: "OMEGA_ASI_v100"})
MATCH (new:Architecture {name: "OMEGA_ASI_v150"})
CREATE (new)-[:EVOLVES_FROM]->(old)
```

### Archive vs Delete

- **Archive** - Keep metadata, mark as obsolete
- **Delete** - Only for true duplicates or errors

## Best Practices

1. **Store immediately** - Don't delay, capture while fresh
2. **Be consistent** - Use standard naming conventions
3. **Create relationships** - Connect new to existing knowledge
4. **Include metadata** - Dates, sources, confidence scores
5. **Verify storage** - Always confirm successful save
6. **Regular maintenance** - Weekly cleanup, monthly review
7. **Archive don't delete** - Preserve research history
8. **Link everything** - Maximize relationship density

## Troubleshooting

### Storage fails?
- Check Neo4j is running: `docker-compose ps`
- Verify disk space available
- Check for malformed data

### Duplicates keep appearing?
- Always check before storing
- Use consistent identifiers
- Merge duplicates immediately

### Relationships missing?
- Create explicitly after storing
- Use standard relationship types
- Verify with query

### Memory too large?
- Archive old experiments
- Compress large abstracts
- Store summaries not full text

## Example Workflows

### Example 1: Storing a New Paper

```
1. Check: Does arXiv:2401.12345 exist?
   Result: No

2. Create Paper node with:
   - arxiv_id: 2401.12345
   - title: "Advanced Neural Architectures"
   - authors: ["Smith", "Jones"]
   - key_findings: "Novel attention mechanism"

3. Create Concept nodes for:
   - "novel_attention"
   - "architecture_optimization"

4. Create relationships:
   - Paper CITES related_papers
   - Paper IMPLEMENTS concepts
   - Concepts RELATED_TO each other

5. Verify: Query for paper 2401.12345 and check relationships
```

### Example 2: Tracking Architecture Evolution

```
1. Create new Architecture node:
   - name: OMEGA_ASI_v450
   - components: [list]
   - innovations: [list]
   - status: "current"

2. Create EVOLVES_FROM relationship to v400

3. Mark v400 as archived

4. Store experiment testing v450

5. Create TESTS relationship
```

## Dependencies

This skill requires:
- **neo4j-memory MCP tool** - For all memory operations
- **knowledge-graph-query skill** - For verification queries
- **Local Neo4j database** - Must be running

## Related Skills

- **knowledge-graph-query** - For retrieving stored information
- **paper-synthesis** - For cross-referencing stored papers
- **experiment-tracker** - For logging experiments to memory
- **research-to-implementation** - For storing research-backed decisions
- **research-frontier-tracker** - For tracking decision staleness

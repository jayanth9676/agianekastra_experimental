---
name: semantic-scholar-search
description: Search and retrieve academic papers from Semantic Scholar API with citation analysis, author information, and paper recommendations
---

# Semantic Scholar Search Skill

This skill provides access to the Semantic Scholar Academic Graph API, enabling comprehensive academic paper search with advanced filtering, citation analysis, author profiling, and AI-powered paper recommendations.

## When to Use This Skill

Use this skill when you need to:
- Search for academic papers across multiple fields
- Analyze citation networks and impact
- Find papers by specific authors or institutions
- Get AI-powered paper recommendations
- Access 200M+ academic papers from various sources
- Track research trends and emerging topics
- Find influential papers in a field
- Discover related work and follow citation chains

## What Semantic Scholar Provides

Semantic Scholar offers:
- **200M+ papers** from diverse sources (arXiv, PubMed, ACL, etc.)
- **Citation analysis** - Who cited whom, citation counts
- **Author profiles** - h-index, publication history, co-authors
- **AI recommendations** - Papers you might like based on interests
- **Full-text access** - Open access PDFs when available
- **Semantic search** - Find conceptually related papers

## How to Use

### Basic Usage

Search for papers using natural language or structured queries:

```
Use semantic-scholar to search for papers on "neural architecture search"
```

```
Search Semantic Scholar: Find papers about transformers published in 2023
```

```
Query: author:"Geoffrey Hinton" AND topic:"deep learning"
```

### Advanced Search

Use field-specific queries:

```
Search:
- Title contains: "attention mechanism"
- Published: 2020-2024
- Citations: >100
- Fields: computer science, AI
```

```
Query:
- Author: "Yoshua Bengio"
- Venue: "NeurIPS" OR "ICML"
- Has PDF: true
- Sort by: citation count
```

## Search Capabilities

### 1. Paper Search

Find papers by various criteria:

```
Search Parameters:
- Query string: Keywords or natural language
- Fields of study: Filter by discipline
- Publication date: Year or range
- Venue: Conference or journal
- Authors: Specific researchers
- Citations: Min/max citation count
- Open access: PDF availability
```

### 2. Citation Analysis

Explore citation networks:

```
Citation Queries:
- "Who cited this paper?"
- "What papers does this cite?"
- "Most cited papers in [field]"
- "Citation trends over time"
```

### 3. Author Search

Find papers by authors:

```
Author Queries:
- "Papers by [author name]"
- "Author h-index and metrics"
- "Co-author network"
- "Author's publication timeline"
```

### 4. Paper Details

Get comprehensive paper information:

```
Paper Information:
- Title and abstract
- Full author list
- Publication venue and date
- Citation count and influential citations
- References (papers it cites)
- Citations (papers citing it)
- Related papers (AI recommendations)
- PDF link (if open access)
- TLDR summary (AI-generated)
```

## Search Strategies

### Strategy 1: Seed Paper Expansion

Start with known paper, explore outward:

```
1. Find seed paper: "Attention Is All You Need"
2. Get papers it cites (references)
3. Get papers citing it (citations)
4. Get related papers (recommendations)
5. Explore most influential papers in citation chain
```

### Strategy 2: Author-Centric Search

Follow influential researchers:

```
1. Identify key author in field
2. Get all their papers
3. Sort by citation count
4. Check their co-authors
5. Explore their recent work
```

### Strategy 3: Venue-Based Search

Track specific conferences:

```
1. Search venue: "NeurIPS 2023"
2. Filter by topic
3. Sort by citation count
4. Identify trending topics
5. Find best papers/oral presentations
```

### Strategy 4: Trend Analysis

Find emerging topics:

```
1. Search for topic in recent years (2022-2024)
2. Compare with older papers (2018-2021)
3. Count papers per year
4. Identify growth trends
5. Find breakthrough papers
```

## Integration with Other Tools

### Workflow 1: Comprehensive Literature Search

```
1. Start with semantic-scholar-search
   - Find relevant papers
   - Get citation networks

2. Use academia-mcp for:
   - Download full PDFs
   - Cross-check with arXiv

3. Query neo4j-memory:
   - Check if already stored
   - Avoid duplicates

4. Use paper-synthesis:
   - Cross-reference findings
   - Identify patterns

5. Store with memory-manager:
   - Save to knowledge graph
   - Create relationships
```

### Workflow 2: Author Impact Analysis

```
1. Search semantic-scholar for author
2. Get publication list and metrics
3. Use exa for:
   - Author's web presence
   - Recent talks/interviews

4. Use academia-mcp for:
   - Detailed paper analysis
   - Methodology comparison

5. Store in memory:
   - Author profile
   - Key papers
   - Influence metrics
```

### Workflow 3: Citation Network Mapping

```
1. Find central paper in semantic-scholar
2. Get all papers it cites (depth 1)
3. Get all papers citing it (depth 1)
4. Optional: Expand to depth 2
5. Use knowledge-graph-query:
   - Store as citation graph
   - Analyze network structure

6. Use paper-synthesis:
   - Identify research clusters
   - Find bridge papers
```

## Best Practices

### Search Tips

1. **Start broad, then filter** - Begin with general terms
2. **Use natural language** - Semantic Scholar understands context
3. **Combine search terms** - Use AND, OR, NOT
4. **Sort strategically** - By relevance, citations, or date
5. **Check multiple sources** - Cross-reference with arXiv, Google Scholar
6. **Follow citation chains** - Forward and backward
7. **Save searches** - Document query patterns that work

### Quality Assessment

Evaluate papers before storing:

```
Quality Checklist:
✅ Peer-reviewed venue
✅ Reasonable citation count
✅ Recent (within scope)
✅ Reputable authors
✅ Clear methodology
✅ Available full text
✅ Reproducible results
```

### Data Management

```
Storage Workflow:
1. Search semantic-scholar
2. Check neo4j-memory for duplicates
3. Evaluate paper quality
4. Download if valuable
5. Store in knowledge graph
6. Create relationships
7. Link to research questions
```

## Search Examples

### Example 1: AGI Architecture Search

```
Query: "artificial general intelligence architecture design"
Filters:
- Fields: computer science, AI
- Years: 2020-2024
- Min citations: 50

Results: 15 papers
Action: Store top 10 in memory
```

### Example 2: Transformer Evolution

```
Query: "transformer architecture variants improvements"
Strategy:
1. Find "Attention Is All You Need"
2. Get all papers citing it (1000+)
3. Filter by citation count >100
4. Sort by date
5. Identify evolution timeline
```

### Example 3: Safety Research

```
Query: "AI safety alignment large language models"
Filters:
- Venue: NeurIPS, ICML, ICLR
- Authors: Known safety researchers
- Recent: 2023-2024

Results: 25 papers
Action: Synthesize safety trends
```

### Example 4: Emerging Topics

```
Query: "state space models sequence modeling"
Analysis:
- Count papers by year:
  2020: 2 papers
  2021: 5 papers
  2022: 15 papers
  2023: 45 papers
  2024: 80 papers
- Trend: Rapid growth
- Conclusion: Emerging hot topic
```

## Common Queries

### By Topic

```
"neural architecture search"
"self-supervised learning"
"meta-learning few shot"
"multi-modal transformers"
"reinforcement learning from human feedback"
```

### By Author

```
author:"Yann LeCun"
author:"Geoffrey Hinton" OR author:"Yoshua Bengio"
author:"Ilya Sutskever"
```

### By Venue

```
venue:"NeurIPS" year:2023
venue:"ICML" OR venue:"ICLR"
venue:"Nature" OR venue:"Science"
```

### Combined

```
"transformer alternatives" venue:NeurIPS citations>50 year>2022
"AI alignment" author:"Stuart Russell" has_pdf:true
```

## Limitations and Considerations

### API Limits

- Free tier has rate limits
- Batch requests for efficiency
- Cache results to minimize calls

### Coverage

- Not all papers indexed
- Some venues better covered than others
- Preprints may be duplicated with published versions

### Quality Variations

- Preprints not peer-reviewed
- Citation count not always indicative of quality
- Verify important findings independently

## Dependencies

This skill integrates with:
- **academia-mcp** - For downloading and analyzing papers
- **neo4j-memory** - For storing search results
- **paper-synthesis** - For cross-referencing multiple papers
- **exa** - For complementary web search
- **knowledge-graph-query** - For storing citation networks

## Related Skills

- **arxiv-search** - For arXiv-specific searches
- **paper-synthesis** - For analyzing multiple papers
- **knowledge-graph-query** - For managing citation graphs
- **memory-manager** - For storing paper information

## Troubleshooting

### No results found?
- Try broader search terms
- Check spelling
- Remove restrictive filters
- Use synonyms

### Too many results?
- Add specific filters
- Use more precise terms
- Filter by date or venue
- Sort by relevance

### Rate limit exceeded?
- Wait before retrying
- Cache previous results
- Batch requests
- Use alternative sources (arXiv)

### Inconsistent results?
- Cross-reference with other sources
- Verify with author websites
- Check preprint servers
- Use multiple search strategies

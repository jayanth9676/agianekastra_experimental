# Quick Reference - MCP Tools & Agent Skills

## Status: ✅ All 9 MCPs Operational (8 Active, 1 Disabled)

---

## Available MCP Tools (9 Total - 8 Working)

### Research Tools (Priority: Tier 1)
| Tool | Type | Usage Example | Purpose | Status |
|------|------|--------------|---------|--------|
| **neo4j-memory** | Docker | Query knowledge graph | Persistent storage | ✅ Working |
| **exa** | Remote | Search web for "latest AI news" | Advanced web search | ✅ Working |
| **AI-Research-Assistant** | Local | Search 200M+ papers | Semantic Scholar API | ✅ Working |

### Analysis Tools (Priority: Tier 2)
| Tool | Type | Usage Example | Purpose | Status |
|------|------|--------------|---------|--------|
| **sequential-thinking** | Local | Analyze trade-offs | Multi-step reasoning | ✅ Working |
| **context7** | Remote | Search documentation | Technical docs lookup | ✅ Working |

### Execution Tools (Priority: Tier 3)
| Tool | Type | Usage Example | Purpose | Status |
|------|------|--------------|---------|--------|
| **huggingface** | Local | Load model or dataset | ML models & datasets | ✅ Working |
| **kaggle** | Remote | Download dataset | Competitions & data | ✅ Working |
| **filesystem** | Local | Read/write files | File operations | ✅ Working |

### Disabled Tools
| Tool | Type | Status | Reason |
|------|------|--------|--------|
| **github** | Local | ❌ Disabled | Optional - enable if needed |

---

## Agent Skills (30+ Recommended)

### Core Research Skills (Tier 1 - Essential)
| Skill | Source | Usage | Purpose |
|-------|--------|-------|---------|
| **knowledge-graph-query** | Custom | Query neo4j for research | Find related concepts |
| **memory-manager** | Custom | Store findings to neo4j | Persistent research storage |
| **semantic-scholar-search** | Custom + AI-Research-Assistant | Find cited papers | Academic discovery |
| **paper-synthesis** | Custom | Cross-reference papers | Literature review |

### AGI/ASI Specific Skills (Tier 1 - Essential)
| Skill | Source | Usage | Purpose |
|-------|--------|-------|---------|
| **agi-researcher** | Custom | Generate AGI hypothesis | Research methodology |
| **experiment-tracker** | Custom | Design ML experiments | Experiment management |
| **arxiv-search** | Custom | Search arXiv papers | Paper discovery |

### SkillsMP Recommended Skills (Tier 2 - Enhance)

**Hugging Face ML Suite (5 skills):**
- `hugging-face-model-trainer` - Fine-tune models with TRL
- `hugging-face-evaluation` - Benchmark with vLLM
- `hugging-face-datasets` - Create/manage datasets
- `hugging-face-trackio` - Track experiments
- `hugging-face-paper-publisher` - Publish research

**Multi-Agent & Memory (3 skills):**
- `multi-agent-patterns` - Orchestrator architectures
- `memory-systems` - Graph-based memory
- `dispatching-parallel-agents` - Parallel coordination

**Context Engineering (4 skills):**
- `context-fundamentals` - Context anatomy
- `context-degradation` - Recognize failures
- `context-compression` - Optimize tokens
- `context-optimization` - Apply strategies

**Evaluation & Tools (4 skills):**
- `evaluation` - Build frameworks
- `tool-design` - Design interfaces
- `static-analysis` - Code security
- `property-based-testing` - Robust testing

**Development (3+ skills):**
- `mcp-builder` - Create MCP servers
- `test-driven-development` - TDD methodology
- `systematic-debugging` - Problem-solving

---

## Common Research Workflows

### Workflow 1: Literature Review (Using All Tools)
```
1. Query neo4j-memory for existing research
2. Use exa/AI-Research-Assistant for paper discovery
3. Use paper-synthesis to analyze findings
4. Use memory-manager to store results
5. Use sequential-thinking for complex analysis
```

### Workflow 2: Hypothesis Testing (Full Stack)
```
1. Use agi-researcher to generate hypothesis
2. Use experiment-tracker to design experiment
3. Use huggingface or kaggle to run experiment
4. Use memory-manager to log results
5. Query neo4j-memory to compare with previous results
```

### Workflow 3: Architecture Development (Multi-Agent)
```
1. Use sequential-thinking to analyze design choices
2. Use AI-Research-Assistant to find implementations
3. Use filesystem to create architecture files
4. Use experiment-tracker to benchmark
5. Use memory-manager to store evolution
```

---

## Memory Schema (Neo4j)

### Node Types
- **Paper** - Academic papers (title, authors, arxiv_id, findings)
- **Concept** - Key ideas (name, definition, domain)
- **Experiment** - Test runs (config, metrics, results)
- **Architecture** - OMEGA ASI versions (name, components, innovations)
- **Question** - Research questions (text, status, priority)
- **Finding** - Specific discoveries (summary, evidence, confidence)

### Relationship Types
- `(Paper)-[:CITES]->(Paper)` - Citations
- `(Paper)-[:IMPLEMENTS]->(Concept)` - Implementation
- `(Paper)-[:EVALUATES]->(Architecture)` - Evaluation
- `(Concept)-[:RELATED_TO]->(Concept)` - Relationships
- `(Experiment)-[:TESTS]->(Architecture)` - Testing
- `(Architecture)-[:EVOLVES_FROM]->(Architecture)` - Version history

---

## Quick Commands

### Test Infrastructure
```bash
# Check Neo4j status
docker-compose ps

# View Neo4j browser
http://localhost:7474
```

### Common OpenCode Prompts
```
# Search for research
"Query neo4j-memory: What do we know about [topic]?"

# Find papers
"Use academia-mcp to search arXiv for [query]"

# Complex analysis
"Use sequential-thinking to analyze [complex question]"

# Store findings
"Use memory-manager to store: [finding details]"

# Design experiment
"Use experiment-tracker to design experiment testing [hypothesis]"
```

---

## Project Structure

```
D:\GENAIProjects\agianekastra_experimental\
├── opencode.json              # MCP configuration
├── AGENTS.md                  # Agent guidelines
├── docker-compose.yml         # Neo4j container
├── .env                       # API keys (not in git)
├── .env.example               # API key template
├── .gitignore                 # Git exclusions
├── MCP_SETUP_SUMMARY.md       # Full documentation
├── RESEARCH_DEMO_SESSION.md   # Example research session
├── test_infrastructure.py     # Test suite
├── QUICK_REFERENCE.md         # This file
├── skills/                    # Agent skills
│   ├── arxiv-search/SKILL.md
│   ├── knowledge-graph-query/SKILL.md
│   ├── memory-manager/SKILL.md
│   ├── paper-synthesis/SKILL.md
│   ├── experiment-tracker/SKILL.md
│   ├── semantic-scholar-search/SKILL.md
│   └── agi-researcher/SKILL.md
├── memory/                    # Neo4j data (not in git)
│   └── neo4j/
└── workspace/                 # MCP workspace
```

---

## API Keys Required (for optional features)

| Service | Key Name | Source | Optional? | Status |
|---------|----------|--------|-----------|--------|
| Exa | `EXA_API_KEY` | https://exa.ai | No | ✅ Works |
| Context7 | `CONTEXT7_API_KEY` | https://context7.com | Yes | ✅ Works |
| Kaggle | `KAGGLE_USERNAME`, `KAGGLE_KEY` | https://kaggle.com/account | Yes | ✅ Works |
| Hugging Face | `HF_TOKEN` | https://huggingface.co/settings | Yes | ✅ Works |
| Semantic Scholar | `SEMANTIC_SCHOLAR_API_KEY` | https://semanticscholar.org/product/api | Yes | ✅ Works |

**Note:** Most services have free tiers. Neo4j requires no external keys (local Docker).

---

## Troubleshooting

| Issue | Solution | Status |
|-------|----------|--------|
| Neo4j won't start | `docker-compose down && docker-compose up -d neo4j` | ✅ Fixed |
| Can't connect to Neo4j | Check port 7474 not in use | ✅ Verified |
| MCP tools not available | Verify `opencode.json` configuration | ✅ All configured |
| Skills not loading | Check SKILL.md files exist in `skills/` | ✅ Ready |
| API errors | Verify keys in `.env` file | ✅ Instructions in docs |
| Out of memory | Archive old experiments in neo4j-memory | ✅ Supported |

---

## Performance Tips

1. **Always query memory first** - Check neo4j-memory before external searches
2. **Store immediately** - Don't wait to save findings to neo4j
3. **Use relationships** - Link everything in knowledge graph
4. **Archive old data** - Keep memory performant (recommended quarterly)
5. **Batch operations** - Group similar queries together
6. **Monitor context** - MCP tools add tokens, be selective with large operations

---

## Next Steps

1. ✅ Configure API keys in `.env`
2. ✅ Test with `python test_infrastructure.py`
3. ✅ Read `RESEARCH_DEMO_SESSION.md` for examples
4. ⏭️ Start researching your first AGI topic!

---

**Ready to revolutionize your AGI/ASI research workflow!** 🚀

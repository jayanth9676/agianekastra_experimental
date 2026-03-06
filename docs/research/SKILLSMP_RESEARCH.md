# SkillsMP (Skills Marketplace) - Best Agent Skills for AGI Research

**Date:** January 30, 2026  
**Status:** Verified and Recommended  
**Platform:** https://skillsmp.com/  
**Focus:** 30+ Best Skills for AGI/ASI Research

---

## What is SkillsMP?

SkillsMP (Skills Marketplace) is the largest aggregator of Agent Skills with **87,427+ skills** as of January 2026, sourced from GitHub and other repositories. It provides semantic search and one-command installation.

**Key Facts:**
- 87,427+ skills available
- Multi-agent support (Claude, ChatGPT, Codex)
- CLI-based installation: `skillsmp install skill-name`
- Organized by SDLC phases
- Free to use (no authentication required)

---

## SkillsMP vs MCP

| Feature | Skills (SkillsMP) | MCP (Model Context Protocol) |
|---------|-------------------|------------------------------|
| **Purpose** | Knowledge sharing & best practices | Tool/API integration |
| **Format** | Markdown (SKILL.md files) | Code servers |
| **Setup** | Simple - files in `skills/` | Complex - requires deployment |
| **Use Case** | Codified knowledge, workflows | External tools, databases |
| **Examples** | Research methodology, code review | Web search, ML models |

**Best Practice:** Use **Skills** for domain knowledge + **MCP** for tool integration

---

## Top 30 Recommended Skills for AGI Research

### TIER 1: Core ML/AI Research (Must Have - 5 Skills)

#### 1. **hugging-face-model-trainer** ⭐⭐⭐
- **Author:** Hugging Face (Official)
- **Install:** `skillsmp install hugging-face-model-trainer@huggingface`
- **Purpose:** Fine-tune LLMs with TRL (SFT, DPO, GRPO, GGUF)
- **Use Case:** Train AGI models with state-of-the-art techniques
- **Key Features:**
  - SFT (Supervised Fine-Tuning)
  - DPO (Direct Preference Optimization)
  - GRPO (Group Relative Policy Optimization)
  - GGUF format conversion

#### 2. **hugging-face-evaluation** ⭐⭐⭐
- **Author:** Hugging Face (Official)
- **Install:** `skillsmp install hugging-face-evaluation@huggingface`
- **Purpose:** Evaluate models with vLLM and lighteval
- **Use Case:** Benchmark AGI capabilities systematically
- **Key Features:**
  - vLLM inference optimization
  - Lighteval benchmark framework
  - Evaluation tables & dashboards

#### 3. **hugging-face-datasets** ⭐⭐
- **Author:** Hugging Face (Official)
- **Install:** `skillsmp install hugging-face-datasets@huggingface`
- **Purpose:** Create, manage, and query datasets
- **Use Case:** Prepare datasets for AGI training
- **Key Features:**
  - Dataset versioning
  - SQL querying capability
  - Data validation

#### 4. **hugging-face-trackio** ⭐⭐
- **Author:** Hugging Face (Official)
- **Install:** `skillsmp install hugging-face-trackio@huggingface`
- **Purpose:** Track experiments with real-time dashboards
- **Use Case:** Monitor AGI training progress
- **Key Features:**
  - Experiment logging
  - Real-time metrics
  - Comparison dashboards

#### 5. **deep-research** ⭐⭐⭐
- **Author:** sanjay3290
- **Install:** `skillsmp install deep-research@sanjay3290`
- **Purpose:** Autonomous multi-step research agent
- **Use Case:** Comprehensive literature reviews for AGI
- **Key Features:**
  - Gemini Deep Research integration
  - Multi-step reasoning
  - Automated synthesis

---

### TIER 2: Multi-Agent & Memory (Essential - 3 Skills)

#### 6. **multi-agent-patterns** ⭐⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install multi-agent-patterns@muratcankoylan`
- **Purpose:** Orchestrate multiple agents
- **Use Case:** Complex AGI research coordination
- **Patterns Covered:**
  - Orchestrator pattern
  - Peer-to-peer pattern
  - Hierarchical pattern

#### 7. **memory-systems** ⭐⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install memory-systems@muratcankoylan`
- **Purpose:** Design memory architectures
- **Use Case:** AGI memory design & optimization
- **Memory Types:**
  - Short-term memory
  - Long-term memory
  - Graph-based memory

#### 8. **dispatching-parallel-agents** ⭐⭐
- **Author:** obra
- **Install:** `skillsmp install dispatching-parallel-agents@obra`
- **Purpose:** Coordinate parallel agents
- **Use Case:** Run parallel AGI research tasks

---

### TIER 3: Context Engineering (High Value - 4 Skills)

#### 9. **context-optimization** ⭐⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install context-optimization@muratcankoylan`
- **Purpose:** Optimize context window usage
- **Use Case:** Improve AGI token efficiency
- **Strategies:**
  - Context compaction
  - Attention masking
  - Cache strategies

#### 10. **context-fundamentals** ⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install context-fundamentals@muratcankoylan`
- **Purpose:** Understand context in agents
- **Use Case:** Design efficient context handling

#### 11. **context-compression** ⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install context-compression@muratcankoylan`
- **Purpose:** Compress long-context information
- **Use Case:** Handle very long sequences

#### 12. **context-degradation** ⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install context-degradation@muratcankoylan`
- **Purpose:** Recognize context failure patterns
- **Use Case:** Prevent context loss in long sessions

---

### TIER 4: Evaluation & Testing (Important - 4 Skills)

#### 13. **evaluation** ⭐⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install evaluation@muratcankoylan`
- **Purpose:** Build evaluation frameworks
- **Use Case:** AGI capability assessment
- **Metrics:**
  - Performance metrics
  - Safety metrics
  - Reliability metrics

#### 14. **tool-design** ⭐⭐
- **Author:** muratcankoylan (Expert)
- **Install:** `skillsmp install tool-design@muratcankoylan`
- **Purpose:** Design tools for agents
- **Use Case:** Create AGI tool interfaces

#### 15. **static-analysis** ⭐⭐
- **Author:** trailofbits
- **Install:** `skillsmp install static-analysis@trailofbits`
- **Purpose:** Security analysis with CodeQL & Semgrep
- **Use Case:** Verify AGI code safety

#### 16. **property-based-testing** ⭐
- **Author:** trailofbits
- **Install:** `skillsmp install property-based-testing@trailofbits`
- **Purpose:** Test with property-based approach
- **Use Case:** Robust AGI testing

---

### TIER 5: MCP & Infrastructure (Advanced - 3 Skills)

#### 17. **mcp-builder** ⭐⭐⭐
- **Author:** anthropics (Official)
- **Install:** `skillsmp install mcp-builder@anthropics`
- **Purpose:** Create MCP servers for APIs
- **Use Case:** Extend AGI research infrastructure
- **Build:** Custom tools, databases, APIs

#### 18. **webapp-testing** ⭐⭐
- **Author:** anthropics (Official)
- **Install:** `skillsmp install webapp-testing@anthropics`
- **Purpose:** Test web apps with Playwright
- **Use Case:** Test AGI web interfaces

#### 19. **systematic-debugging** ⭐
- **Author:** obra
- **Install:** `skillsmp install systematic-debugging@obra`
- **Purpose:** Methodical problem-solving
- **Use Case:** Debug AGI systems

---

### TIER 6: Development Workflow (Supporting - 4 Skills)

#### 20. **test-driven-development** ⭐⭐
- **Author:** obra
- **Install:** `skillsmp install test-driven-development@obra`
- **Purpose:** TDD methodology
- **Use Case:** Reliable AGI development

#### 21. **root-cause-tracing** ⭐
- **Author:** obra
- **Install:** `skillsmp install root-cause-tracing@obra`
- **Purpose:** Identify fundamental problems
- **Use Case:** Deep issue analysis

#### 22. **subagent-driven-development** ⭐⭐
- **Author:** obra
- **Install:** `skillsmp install subagent-driven-development@obra`
- **Purpose:** Divide work among sub-agents
- **Use Case:** Distribute AGI research tasks

#### 23. **scientific-skills** ⭐⭐
- **Author:** K-Dense-AI
- **Install:** `skillsmp install claude-scientific-skills@K-Dense-AI`
- **Purpose:** Scientific research methodology
- **Use Case:** Structured AGI science

---

### TIER 7: Documentation & Communication (Supporting - 5+ Skills)

#### 24. **docx** ⭐⭐
- **Author:** anthropics (Official)
- **Install:** `skillsmp install docx@anthropics`
- **Purpose:** Create & edit Word documents
- **Use Case:** AGI research documentation

#### 25. **pdf** ⭐⭐
- **Author:** anthropics (Official)
- **Install:** `skillsmp install pdf@anthropics`
- **Purpose:** Extract text, create PDFs
- **Use Case:** Paper management & reports

#### 26. **internal-comms** ⭐
- **Author:** anthropics (Official)
- **Install:** `skillsmp install internal-comms@anthropics`
- **Purpose:** Write status reports, newsletters
- **Use Case:** Research team communication

#### 27. **writing-plans** ⭐
- **Author:** obra
- **Install:** `skillsmp install writing-plans@obra`
- **Purpose:** Strategic documentation
- **Use Case:** AGI research roadmaps

#### 28. **executing-plans** ⭐
- **Author:** obra
- **Install:** `skillsmp install executing-plans@obra`
- **Purpose:** Implement strategic plans
- **Use Case:** Execute research milestones

---

### TIER 8: Additional Specialized Skills (5+ More)

#### 29. **content-research-writer** ⭐
- **Author:** ComposioHQ
- **Install:** `skillsmp install content-research-writer@ComposioHQ`
- **Purpose:** Research-based writing
- **Use Case:** AGI research documentation

#### 30. **hugging-face-paper-publisher** ⭐
- **Author:** Hugging Face (Official)
- **Install:** `skillsmp install hugging-face-paper-publisher@huggingface`
- **Purpose:** Publish papers on HF Hub
- **Use Case:** Share AGI research findings

---

## Recommended Installation Order

### Phase 1: Core ML/AI (Week 1)
```bash
# 5 core skills
skillsmp install hugging-face-model-trainer@huggingface
skillsmp install hugging-face-evaluation@huggingface
skillsmp install hugging-face-datasets@huggingface
skillsmp install hugging-face-trackio@huggingface
skillsmp install deep-research@sanjay3290
```

### Phase 2: Multi-Agent & Context (Week 2)
```bash
# 7 essential skills
skillsmp install multi-agent-patterns@muratcankoylan
skillsmp install memory-systems@muratcankoylan
skillsmp install context-optimization@muratcankoylan
skillsmp install context-compression@muratcankoylan
skillsmp install context-fundamentals@muratcankoylan
skillsmp install context-degradation@muratcankoylan
skillsmp install dispatching-parallel-agents@obra
```

### Phase 3: Evaluation & Tools (Week 3)
```bash
# 4 evaluation skills
skillsmp install evaluation@muratcankoylan
skillsmp install tool-design@muratcankoylan
skillsmp install static-analysis@trailofbits
skillsmp install property-based-testing@trailofbits
```

### Phase 4: Infrastructure (Week 4)
```bash
# 3 infrastructure skills
skillsmp install mcp-builder@anthropics
skillsmp install webapp-testing@anthropics
skillsmp install systematic-debugging@obra
```

### Phase 5: Development & Docs (Ongoing)
```bash
# Development + documentation
skillsmp install test-driven-development@obra
skillsmp install docx@anthropics
skillsmp install pdf@anthropics
skillsmp install scientific-skills@K-Dense-AI
```

---

## SkillsMP CLI Usage

### Installation
```bash
npm install -g skillsmp
```

### Search Skills
```bash
# By keyword
skillsmp search "machine learning"
skillsmp search "multi-agent"
skillsmp search "AGI"

# List categories
skillsmp categories

# List by category
skillsmp list --category "AI/ML"
```

### Install Skills
```bash
# Single skill
skillsmp install hugging-face-model-trainer

# Specific version
skillsmp install hugging-face-model-trainer@1.2.3

# From file
skillsmp install --file agi-skills.txt
```

### Verify Installation
```bash
# List installed
skillsmp list --installed

# Check details
skillsmp info hugging-face-model-trainer

# Update
skillsmp update
```

---

## Custom Skills for AGI Research

Create project-specific skills in `/skills/` directory:

1. **agi-hypothesis-generator** - Generate & prioritize hypotheses
2. **benchmark-creator** - Create AGI benchmarks
3. **meta-learning-protocol** - Self-improvement workflows
4. **knowledge-graph-manager** - Manage research graph
5. **experiment-orchestrator** - Design ML experiments

---

## Quality Evaluation Criteria

When selecting SkillsMP skills:

1. **Author** - Prefer official (anthropics, huggingface)
2. **Stars** - Community adoption indicator
3. **Updated** - Recent maintenance (< 6 months)
4. **Documentation** - Quality SKILL.md file
5. **Security** - Review permissions & access

---

## Resources

- **Website:** https://skillsmp.com/
- **Documentation:** https://skillsmp.com/docs
- **Search:** https://skillsmp.com/skills
- **CLI:** `npm install -g skillsmp`

---

## Summary

**30+ Recommended Skills for AGI Research:**

✅ **Tier 1 (Essential - 5):** ML/AI core capabilities
✅ **Tier 2 (Essential - 3):** Multi-agent & memory
✅ **Tier 3 (High Value - 4):** Context engineering
✅ **Tier 4 (Important - 4):** Evaluation & testing
✅ **Tier 5 (Advanced - 3):** MCP & infrastructure
✅ **Tier 6 (Supporting - 4):** Development workflow
✅ **Tier 7 (Supporting - 5+):** Documentation
✅ **Tier 8 (Specialized - 5+):** Additional tools

**Total Available:** 87,427+ skills
**Recommended for AGI:** 30+ skills
**Installation Time:** 2-4 weeks (gradual adoption)

*Last Updated: January 30, 2026*

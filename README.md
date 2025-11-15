# Nexus: Boss Rush

*Premium Mobile Roguelike - FFXIV raids meet Hades*

## Quick Start

Welcome to Nexus: Boss Rush development workspace. This is our command center for building a premium mobile game that respects players.

### The Team
- **CEO (Partner)**: Vision, strategy, community building
- **CTO Oracle**: AI-powered technical leadership with full context
- **Builder (Claude)**: Rapid implementation and prototyping

### Workspace Structure

```
Nexus/
├── nexus_cto/            # AI CTO system
│   └── src/             # Core CTO Oracle modules
├── docs/                # Living documentation
│   ├── architecture/    # System design documents
│   ├── decisions/       # Architectural decision log
│   └── roadmap/         # Project roadmap and milestones
├── src/                 # Game source code (Unity project will go here)
├── context/             # Session-specific state and focus
├── cto_prompts/         # CTO role definitions and frameworks
└── README.md           # This file
```

### Using the CTO Oracle

The CTO Oracle maintains complete project context to prevent the complexity issues we faced with Veritas. It can:

1. **Make architectural decisions** with full project awareness
2. **Track roadmap progress** and identify blockers
3. **Provide strategic guidance** based on current state
4. **Maintain continuity** across sessions

### Current Status

**Phase:** Pre-Production - Setup
**Focus:** Establishing workspace and CTO Oracle system
**Next Priority:** Initialize Unity project and begin combat prototype

### Key Principles

1. **Mobile First**: Every decision optimized for mobile
2. **Premium Quality**: No compromises on player experience
3. **Respect Player Time**: No grinding, no predatory mechanics
4. **AI-Powered Development**: Leverage AI for speed and consistency
5. **Context Awareness**: Never lose project understanding

### Commands

```python
# Initialize CTO Oracle
from nexus_cto.src import get_cto_oracle
cto = get_cto_oracle()

# Get project status
status = cto.get_status_report()
print(status)

# Make a decision
decision = cto.make_decision("Should we use DOTween or native Unity animations?")
print(decision)

# Update progress
cto.update_progress("M1", "In Progress", "Unity setup complete, starting character controller")
```

### Documentation Philosophy

- **Context is King**: Every decision needs full project context
- **Living Documents**: Documentation updates with development
- **Decision Tracking**: Every architectural choice is recorded with reasoning
- **No Silos**: All information accessible to the CTO Oracle

## Game Vision

**Nexus** is a premium mobile roguelike where players face 10 unique bosses in 30-minute skill-based runs. No grinding, no gacha, no predatory monetization - just pure skill expression.

- **Free Demo**: 3 bosses, 1 class
- **Premium Unlock**: $12.99 for full game
- **Target**: 100-150K downloads, 20-30% conversion

## Development Approach

Learned from Veritas:
- ✅ Clear project boundaries
- ✅ Persistent context management
- ✅ AI-powered development efficiency
- ✅ Documentation-first approach
- ✅ Agile iteration with strategic guidance

---

*Project Start: November 15, 2025*
*Target Launch: August 2026*
*Development Team: Human + AI Collaboration*
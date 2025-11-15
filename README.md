# Nexus: Trial of Champions

*Premium Text-Based Roguelike - Dark Souls meets Reigns meets Slay the Spire*

## Quick Start

Welcome to Nexus: Trial of Champions development workspace. This is our command center for building a premium text-based mobile game that respects players.

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
├── context/             # Session-specific state and focus
├── cto_prompts/         # CTO role definitions and frameworks
├── CLAUDE.md           # AI development guidance
├── README.md           # This file
└── text_boss_rush_gdd.md # Complete game design document
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
**Next Priority:** Build simple text prototype of Stone Guardian fight
**Pivot:** Switched to text-based design (Nov 16, 2025)

### Key Principles

1. **Text-Based First**: Every decision optimized for text gameplay
2. **Strategic Depth**: Complex decisions, simple interface
3. **Respect Player Time**: 25-35 minute runs, no grinding
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
decision = cto.make_decision("What framework should we use for the text interface?")
print(decision)

# Update progress
cto.update_progress("M1", "In Progress", "Text prototype started - Stone Guardian combat")
```

### Documentation Philosophy

- **Context is King**: Every decision needs full project context
- **Living Documents**: Documentation updates with development
- **Decision Tracking**: Every architectural choice is recorded with reasoning
- **No Silos**: All information accessible to the CTO Oracle

## Game Vision

**Nexus: Trial of Champions** is a premium mobile text-based roguelike where players face 10 legendary champions through strategic choices. Players make tactical decisions (Attack, Defend, Dodge, Analyze) to survive deadly patterns. Die, learn, master, conquer—through compelling narrative combat.

- **Free Demo**: 3 bosses (Stone Guardian, Flame Archon, Ice Witch), 1 class
- **Premium Unlock**: $6.99 for full game
- **Target**: 50-100K downloads, 25-35% conversion
- **Experience**: Dark Souls pattern learning meets Reigns swipes meets Slay the Spire depth

## Development Approach

Learned from Veritas:
- ✅ Clear project boundaries
- ✅ Persistent context management
- ✅ AI-powered development efficiency
- ✅ Documentation-first approach
- ✅ Agile iteration with strategic guidance

---

*Project Start: November 15, 2025*
*Pivot to Text-Based: November 16, 2025*
*Target Launch: April-May 2026*
*Development Team: Human + AI Collaboration*
*Budget: $700 - $1,500 (dramatically reduced from $50K+)*
# Nexus Architectural Decision Log

## Decision Framework

Every decision is evaluated against:
1. **Mobile First**: Does this work optimally on mobile devices?
2. **Premium Value**: Does this justify the $12.99 price point?
3. **Player Respect**: Does this respect player time and investment?
4. **Technical Feasibility**: Can we build this with our resources?
5. **Core Promise**: Does this enable "FFXIV raids on mobile"?

---

## Decision History

### Decision #001 - Project Approach
**Date:** November 15, 2025
**Question:** What should be our development approach to avoid the complexity issues from Veritas?
**Decision:** Implement CTO Oracle with persistent context management
**Reasoning:** Veritas suffered from context fragmentation, unclear priorities, and frequent roadmap forks. A dedicated CTO Oracle with full project context will maintain strategic coherence and prevent getting lost in complexity.
**Impact:** Foundation for all future development decisions. Eliminates risk of context loss.

### Decision #002 - Asset Creation Strategy
**Date:** November 15, 2025
**Question:** How should we handle art and music assets given our budget constraints?
**Decision:** Use AI generation for all visual and audio assets
**Reasoning:** Reduces development budget from $80K to $30-50K. AI tools (Midjourney, Suno, ElevenLabs) are now capable of producing game-ready assets. Enables faster iteration and complete creative control.
**Impact:** Significant cost reduction, faster development, more iterations possible. Slight risk in asset consistency that needs careful management.

### Decision #003 - Project Structure
**Date:** November 15, 2025
**Question:** How should we organize the Nexus project to ensure clarity and focus?
**Decision:** Dedicated workspace with clear separation from Veritas
**Reasoning:** Veritas complexity created mental overhead. Fresh workspace enables focused development without baggage. Clear structure supports CTO Oracle context management.
**Impact:** Clean development environment. Reduced cognitive load. Better organization.

---

## Pending Decisions

### Unity Version and Packages
- Need to confirm specific Unity packages (DOTween, Behavior Designer, etc.)
- Consider Unity 6.0 preview vs 2022 LTS stability

### First Boss Implementation Order
- Stone Guardian first for tutorial, or start with more complex boss?
- How much visual polish vs mechanics focus?

### Testing Approach
- Internal testing only, or external playtesters early?
- Which devices to target for performance baseline?

---

## Decision Template

For future decisions, use this format:

```markdown
### Decision #[ID]
**Date:** YYYY-MM-DD
**Question:** [Clear question being answered]
**Decision:** [What was decided]
**Reasoning:** [Why this decision was made]
**Impact:** [Consequences for development and product]
**Alternatives Considered:** [What else was evaluated]
**Status:** [Implemented/In Progress/Blocked]
```
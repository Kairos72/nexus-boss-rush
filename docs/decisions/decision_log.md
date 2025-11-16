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

### Decision #004 - PIVOT: Text-Based Design
**Date:** November 16, 2025
**Question:** Should we continue with 3D action game or pivot to simpler approach?
**Decision:** PIVOT to text-based decision roguelike
**Reasoning:** Dramatic complexity reduction (90% simpler), timeline cut in half (8→4-6 months), budget reduction 98% ($50K→$1K). Text-based actually fits mobile better for strategic gameplay. Unique market position.
**Impact:** Complete project restructure. Faster to market. Lower risk. Maintains strategic depth while eliminating technical complexity.
**Status:** Implemented

### Decision #005 - Technology Stack
**Date:** November 16, 2025
**Question:** What technology should we use for the text-based game?
**Decision:** Unity 2022 LTS with UI Toolkit and TextMesh Pro
**Reasoning:** Despite pivot, Unity remains optimal. TextMesh Pro offers best mobile text rendering. UI Toolkit simpler than React for mobile buttons. One-click deployment to both app stores. Native performance, haptic support, reliable saves.
**Alternatives Considered:**
- Web App (React/PWA): Rejected - no App Store distribution, complex payment system
- React Native: Rejected - WebView overhead for simple text
- Flutter: Rejected - Good but Unity deployment still simpler
**Impact:** Fastest path to polished mobile text game. App Store ready. Native features available.
**Status:** Ready to implement

### Decision #006 - Advanced Features Strategy
**Date:** November 16, 2025
**Question:** How should we approach depth and replayability features beyond the base game?
**Decision:** Implement intelligence-based systems (Pattern Chains, Echo Patterns, Boss Banter) rather than speed-based mechanics
**Reasoning:** Timer mechanics would shift focus from strategic thinking to reflexes, undermining the core pattern mastery gameplay. Intelligence systems create depth through anticipation and adaptation, maintaining respect for player intelligence.
**Key Features Committed:**
1. Pattern Chains (fighting game combos) - High priority, unique selling point
2. Boss Banter (personality through text) - Zero cost, huge impact
3. Weak Point System (experimental rewards) - Speedrun meta potential
4. Echo Patterns (adaptive AI) - Personalized difficulty
5. Stance System (run-defining choices) - Replayability engine
**Impact:** Creates genre-defining depth without technical complexity. Establishes Nexus as intelligent, strategic roguelike. Differentiates from reflex-based competitors.
**Status:** Design complete, implementation roadmap created
**Document:** Advanced Features Design (docs/advanced_features_design.md)

### Decision #007 - Pattern Chains Feature Analysis
**Date:** November 16, 2025
**Question:** What is the implementation complexity and value of adding Pattern Chains as the primary advanced feature?
**Decision:** Pattern Chains should be the flagship advanced feature, implemented from Boss 4 onward
**Reasoning:** Pattern Chains transforms Nexus from simple pattern matching into predictive gameplay. Creates "Anticipatory Pattern Mastery" where players outthink bosses rather than just react. Medium-High complexity (7/10) but delivers genre-defining depth that justifies premium pricing.
**Technical Challenges Identified:**
- State machine complexity: Need to track 2-3 previous player actions
- Memory system requirements for chain detection
- UI communication: Subtle text cues to signal chain activation
- Balance: Chains must be learnable, not random
**Key Benefits:**
- Creates intelligent boss conversations ("The Guardian PREDICTED your move!")
- Infinite depth from simple mechanics (60+ unique chains across 10 bosses)
- Perfect for mobile text (no animation, pure prediction)
- Competitive advantage: "Fighting game depth in text-based combat"
**Implementation Strategy:**
- Phase 1: Chain detection system (Week 1)
- Phase 2: Stone Guardian chains (Weeks 2-3)
- Phase 3: Advanced chains for later bosses (Week 4)
- Phase 4: Polish and achievement integration (Week 5)
**Impact:** Establishes Nexus as the thinking player's roguelike. Creates unique market position against reflex-based competitors. Justifies $6.99 premium price point through strategic depth.
**Status:** Analysis complete, ready for implementation planning

### Decision #008 - Passion Project Commitment
**Date:** November 16, 2025
**Question:** Given the honest assessment of market realities, what is the official project approach?
**Decision:** Officially reclassify Nexus as a passion project with reduced scope and timeline flexibility
**Reasoning:** Financial analysis revealed 3D version would be certain financial ruin (95% failure probability). Text-based version remains viable but passion project approach removes pressure, allows creative freedom, and acknowledges real-world constraints.
**Project Changes:**
- Timeline: Flexible, work-as-possible rather than strict March-April 2026
- Budget: $700 absolute maximum, no additional marketing spend
- Team: Human CEO + AI collaboration, no external hires
- Success metrics redefined: Impact over income, community over scale
- Development cadence: Asynchronous, respectful of personal circumstances
**Benefits of Passion Project Status:**
- Zero financial risk
- Creative freedom from market pressure
- Focus on innovation and artistic expression
- Community building without commercial motives
- Experimental feature playground (Pattern Chains, Echo Patterns)
**New Success Definition:**
- Create something unique that 500-1,000 players genuinely love
- Validate AI-assisted development methodology
- Build foundation for future projects
- Demonstrate that small teams can create meaningful games
**Impact:** Transforms project from business venture to artistic endeavor. Removes pressure while maintaining all creative aspirations. Ensures project completion regardless of commercial reception.
**Status:** Implemented - project now officially passion-driven

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

### Feature Implementation Priority
- Pattern Chains complexity analysis complete (Medium-High 7/10)
- Should Pattern Chains be implemented from boss 2, or added later as update?
- How to balance Echo Patterns adaptation (prevent impossible situations)?
- Daily Trials frequency - daily or weekly rotation?

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
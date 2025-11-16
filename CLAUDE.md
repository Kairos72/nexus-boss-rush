# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Nexus: Trial of Champions** is a passion project mobile text-based roguelike that brings FFXIV-style raid mechanics to decision-based gameplay. Players face 10 legendary champions through strategic choices, learning deadly patterns and adapting tactics across multiple runs. Every choice is life or death in this blend of Dark Souls, Reigns, and Slay the Spire.

### Project Philosophy: Passion-Driven Development
**Status:** Officially a passion project, not a business venture
**Goal:** Create meaningful art that impacts the gaming community
**Timeline:** Flexible, work-as-possible schedule
**Budget:** $700 absolute maximum, zero marketing spend
**Success Redefined:** Impact over income, community over scale, artistic fulfillment over commercial success

### Business Model (Optional Release)
- Free demo: 3 bosses (Stone Guardian, Flame Archon, Ice Witch), 1 class
- Premium unlock: $6.99 for full game (10 bosses, 5 classes)
- Target: 500-1,000 genuine players who love the experience
- No ads, no IAP, respecting player time and investment
- Any revenue is bonus, not objective

### Development Team Structure
This project uses an innovative AI-powered development model:
- **CEO**: Human visionary and strategic direction
- **CTO Oracle**: AI-powered technical leadership with complete project context
- **Builder**: Claude for rapid implementation and development

## Project Structure

```
Nexus/
├── docs/                   # Living documentation
│   ├── project_vision.md   # Executive vision and strategy
│   ├── decisions/          # Architectural decision records
│   └── roadmap/            # Development timeline and milestones
├── context/                # Auto-updated project context
│   └── current_session.json
├── cto_prompts/            # CTO Oracle role definitions
├── nexus_cto/              # CTO Oracle Python modules
│   └── src/                # Implementation of AI CTO systems
├── CLAUDE.md               # AI development guidance
├── README.md               # Project overview
└── text_boss_rush_gdd.md   # Complete game design document
```

## Technology Stack

- **Engine**: Unity 2022 LTS (UI Toolkit + TextMesh Pro)
- **Platform**: Mobile (iOS & Android)
- **Input**: Touch-based tap interface
- **Architecture**: State machines for boss patterns
- **Data Format**: JSON for bosses, upgrades, decisions
- **Storage**: PlayerPrefs for save/load
- **Rendering**: TextMesh Pro for crisp mobile text
- **UI Framework**: Unity UI Toolkit for mobile buttons

## Development Workflow

### Passion-Driven Development
The project follows a flexible, organic development approach:

1. **Foundation Phase** (Complete): Design, prototype validation, advanced features blueprint
2. **Development Phase** (Flexible): Unity implementation when time allows
3. **Polish Phase** (Optional): Community feedback integration and refinement
4. **Release Phase** (Optional): When ready, not on deadline
5. **Community Phase** (Ongoing): Support and engagement with players

**Key Principle:** No artificial deadlines or pressure. Work flows naturally around life circumstances.

### CTO Oracle Integration
The CTO Oracle maintains complete project context through:
- **Context Manager**: Automatic file scanning and conversation tracking
- **Decision Engine**: Framework for architectural decisions
- **Roadmap Tracker**: Real-time milestone progress monitoring
- **Risk Assessment**: Proactive identification of development risks

### Decision Framework
All technical choices are evaluated against:
1. **Passion Project Ethics**: Does this serve the art and community?
2. **Text-Based Simplicity**: No animation, physics, or timing systems
3. **Mobile Performance**: 60 FPS UI, minimal resource usage
4. **Session Length**: 25-35 minute full runs, 2-4 minute per boss
5. **Team Composition**: 1 CEO + AI collaboration, no external hires
6. **Budget Reality**: Must fit within $700 absolute maximum
7. **Personal Sustainability**: Work must be enjoyable, not stressful

## Current Status

- **Phase**: Foundation Complete - Passion Project Established
- **Progress**: 15% (Design complete, prototype validated, advanced features designed)
- **Next Priority**: Unity implementation when time and inspiration align
- **Blockers**: None (flexible timeline removes all pressure)
- **Timeline**: Whenever it's ready - no artificial deadlines
- **Pivot**: Switched to text-based design (November 16, 2025)
- **Status**: Official passion project - creative freedom enabled

## Key Architectural Principles

### Text-Based Design Principles
- Decision-driven gameplay (Attack, Defend, Dodge, Analyze)
- Pattern recognition as core progression mechanic
- Simple tap interface, perfect for mobile
- Minimal performance requirements (text rendering only)

### Quality Standards
- Premium text-based experience with atmospheric writing
- Skill-based progression through pattern learning
- Boss personalities shine through descriptive text
- Accessibility features including dyslexia-friendly fonts

### Code Architecture
- State machines for boss patterns and phases
- JSON-driven data for bosses, upgrades, and decisions
- Simple event system for game flow
- PlayerPrefs for save/load (minimal data needs)

### Advanced Features Architecture
- Pattern Chains: Conditional boss responses that anticipate player actions
- Echo Patterns: AI memory system that adapts to player tendencies
- Dynamic Dialogue: Contextual boss banter based on player behavior
- Stance System: Run-defining modifiers (Berserker, Guardian, Assassin, Sage, Dancer)

## Build and Development Commands

### Unity Setup
```bash
# Open project in Unity 2022 LTS
# Install required packages:
# - Input System v1.14.2
# - Netcode for GameObjects
# - Unity Physics
# - Universal Render Pipeline

# Set build target to iOS/Android
# Configure Player Settings for mobile
```

### Testing
```bash
# Run unit tests: Window > General > Test Runner
# Performance profiling: Window > Analysis > Profiler
# Memory analysis: Window > Analysis > Memory Profiler
```

## Important File Locations

- **Project Vision**: `docs/project_vision.md`
- **Current Roadmap**: `docs/roadmap/current_roadmap.json`
- **Decision Log**: `docs/decisions/decision_log.md`
- **Project Context**: `context/current_session.json`
- **Advanced Features**: `docs/advanced_features_design.md`
- **Game Design**: `text_boss_rush_gdd.md`
- **Ideas**: `ideas.md`
- **Working Prototype**: `prototype/index.html` (validates concept)
- **Boss Portrait**: `9d3a7a2d-6f9f-4fa9-b395-36180e1a7c76.jfif`
- **Unity Main Scene**: To be created in `src/Assets/Scenes/`

## CTO Oracle Context Management

The CTO Oracle maintains context through:
- **Automatic Updates**: File system monitoring for changes
- **Session Tracking**: Conversation history and decisions
- **Progress Monitoring**: Automatic milestone tracking
- **Risk Detection**: Proactive issue identification

When working on this project:
1. Always check `context/current_session.json` for latest state
2. Update decision log for significant architectural choices
3. Monitor roadmap progress after major features
4. Consider mobile performance implications for all changes

## Success Metrics

### Passion Project KPIs
- Create something unique that makes players think
- Build a small community that genuinely loves the experience
- Validate AI-assisted development methodology
- Learn and grow as developers and designers
- Maintain joy and creativity throughout the process

### Technical KPIs (If Released)
- Maintain 60 FPS on target devices
- <5 second initial load time
- <100MB initial download size
- <2GB RAM usage peak

### Community KPIs (If Released)
- 500-1,000 players who complete the game
- Meaningful discussions about strategy and patterns
- Fan-created content (guides, speedruns, theories)
- Positive impact on players who appreciate intelligent games

### Financial KPIs (Optional)
- Break even (covers $700 costs)
- Any profit is bonus, reinvested in future projects
- Never spend on marketing or user acquisition

## Risk Mitigation

### Personal Risks (Primary Concern)
- **Burnout**: Zero pressure development schedule
- **Financial Loss**: $700 absolute maximum, acceptable investment
- **Perfectionism**: "Done is better than perfect" mindset
- **Loss of Joy**: Step away anytime, return when inspired

### Technical Risks
- **Performance**: Regular profiling on target devices
- **Scope**: Feature creep protection - passion project scope is locked
- **Platform**: iOS/Android testing from early phases

### Community Risks (If Released)
- **Indifference**: Accept that not every game finds its audience
- **Negative Feedback**: Focus on players who appreciate the vision
- **Support Burden**: Set clear expectations about availability

### Financial Risks
- **Loss**: Maximum $700, treated as art investment not business loss
- **Opportunity Cost**: Skill development and portfolio building have value
- **Monetization**: No pressure to monetize, release is optional

## Quick Reference

### Essential Commands
- Unity Editor: Create new project, open Unity Hub
- Build: File > Build Settings > Select target platform
- Test: Play in Editor, Window > Analysis > Profiler
- Prototype: Open `prototype/index.html` in browser

### Working Prototype Access
```bash
# Quick test of current game design
open prototype/index.html
# Mobile test: Use browser dev tools (F12) → Mobile view
```

### Unity Setup Checklist
1. Create new Unity 2022 LTS project
2. Set build target to iOS/Android
3. Import TextMesh Pro (built-in)
4. Create Scene: `Assets/Scenes/MainScene.unity`
5. Add Canvas with mobile settings
6. Implement Stone Guardian state machine
7. Test on mobile device

### Key Contacts
- CEO: Human strategic decisions and vision
- CTO Oracle: AI technical guidance (context-aware)
- Builder (Claude): Implementation and development

### Common Tasks
1. **Starting Work**: Check `context/current_session.json` for latest project state
2. **Making Decisions**: Consult decision framework and review advanced_features_design.md
3. **Updating Progress**: Auto-tracked by CTO Oracle, but update manually after major milestones
4. **Testing Prototype**: Open `prototype/index.html` to validate gameplay concepts
5. **Blocking Issues**: Update blockers in roadmap immediately

## Prototype Development Status
- **Stone Guardian**: Fully implemented with pattern recognition
- **Features Tested**: Phase transitions, vulnerable states, victory/defeat
- **Mobile Ready**: Portrait orientation, touch-optimized
- **Next Boss**: Flame Archon (DOT mechanics) - design ready in GDD

## Implementation Priorities
### Phase 1 (Unity Setup - Month 1)
1. Text-based UI system with TextMesh Pro
2. Stone Guardian state machine in C#
3. Mobile-optimized Canvas and controls
4. Save/load system with PlayerPrefs
5. Haptic feedback integration

### Phase 2 (Content - Month 2)
1. Implement advanced features (Pattern Chains, Echo Patterns)
2. Create Flame Archon and Ice Witch
3. Stance system implementation
4. Roguelike upgrade system

Remember: This is a passion project, not a commercial venture. The goal is to create meaningful art, validate AI-assisted development methodology, and build something that a small community of players will genuinely love. The CTO Oracle provides continuity and context across development sessions, enabling steady progress without pressure. The working prototype proves the concept is worth pursuing for its own sake.

**Most Important Rule:** If this stops being enjoyable, it's time to step back. Passion projects flourish when fueled by joy, not obligation.
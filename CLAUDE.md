# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Nexus: Trial of Champions** is a premium mobile text-based roguelike that brings FFXIV-style raid mechanics to decision-based gameplay. Players face 10 legendary champions through strategic choices, learning deadly patterns and adapting tactics across multiple runs. Every choice is life or death in this blend of Dark Souls, Reigns, and Slay the Spire.

### Business Model
- Free demo: 3 bosses (Stone Guardian, Flame Archon, Ice Witch), 1 class
- Premium unlock: $6.99 for full game (10 bosses, 5 classes)
- Target: 50-100K downloads, 25-35% conversion rate (more realistic)
- No ads, no IAP, respecting player time and investment

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

- **Platform**: Mobile (iOS & Android)
- **Input**: Touch-based tap interface
- **Architecture**: State machines for boss patterns
- **Data Format**: JSON for bosses, upgrades, decisions
- **Storage**: PlayerPrefs for save/load
- **Framework**: TBD (Unity for UI, or web-based solution)

## Development Workflow

### Phase-Based Development
The project follows a streamlined 4-6 month development plan:

1. **Phase 1 (Month 1)**: Text Prototype - Stone Guardian combat
2. **Phase 2 (Month 2)**: Demo Build - 3 bosses, 1 class
3. **Phase 3 (Months 3-4)**: Full Game - 10 bosses, 5 classes
4. **Phase 4 (Month 5)**: Polish & Testing - Beta ready
5. **Phase 5 (Month 6)**: Launch - Global release

### CTO Oracle Integration
The CTO Oracle maintains complete project context through:
- **Context Manager**: Automatic file scanning and conversation tracking
- **Decision Engine**: Framework for architectural decisions
- **Roadmap Tracker**: Real-time milestone progress monitoring
- **Risk Assessment**: Proactive identification of development risks

### Decision Framework
All technical choices are evaluated against:
1. **Text-Based Simplicity**: No animation, physics, or timing systems
2. **Mobile Performance**: 60 FPS UI, minimal resource usage
3. **Session Length**: 25-35 minute full runs, 2-4 minute per boss
4. **Team Composition**: 1 CEO + AI team structure
5. **Timeline**: 4-6 month delivery schedule

## Current Status

- **Phase**: Pre-Production - Setup
- **Progress**: 0% (Project initialization)
- **Next Priority**: Simple text prototype of Stone Guardian fight
- **Blockers**: None
- **Timeline**: On track for April-May 2026 launch
- **Pivot**: Switched to text-based design (November 16, 2025)

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
- **Unity Main Scene**: `src/Assets/Scenes/MainScene.unity` (to be created)

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

### Technical KPIs
- Maintain 60 FPS on target devices
- <5 second initial load time
- <100MB initial download size
- <2GB RAM usage peak

### Business KPIs
- 100-150K downloads in first 6 months
- 20-30% demo-to-full conversion rate
- 4.5+ star rating on app stores
- <10% crash rate across devices

## Risk Mitigation

### Technical Risks
- **Performance**: Regular profiling on target devices
- **Scope**: Strict adherence to roadmap milestones
- **Platform**: iOS/Android testing from early phases

### Business Risks
- **Monetization**: Premium-only model validated by market research
- **Competition**: Unique FFXIV-meets-mobile positioning
- **Team**: AI-powered development reduces coordination overhead

## Quick Reference

### Essential Commands
- Unity Editor: Open `src/Nexus.sln` or launch Unity Hub
- Build: File > Build Settings > Select target platform
- Test: Window > General > Test Runner > Run All
- Profile: Window > Analysis > Profiler

### Key Contacts
- CEO: Human strategic decisions and vision
- CTO Oracle: AI technical guidance (context-aware)
- Builder (Claude): Implementation and development

### Common Tasks
1. **Starting Work**: Check `context/current_session.json`
2. **Making Decisions**: Consult decision framework
3. **Updating Progress**: Auto-tracked by CTO Oracle
4. **Blocking Issues**: Update blockers in roadmap

Remember: This project represents a new paradigm in AI-assisted game development. The CTO Oracle provides continuity and context across sessions, enabling rapid, informed development decisions while maintaining technical excellence and mobile performance standards.
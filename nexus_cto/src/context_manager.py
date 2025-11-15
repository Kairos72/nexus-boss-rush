"""
Nexus CTO Oracle - Project Context Manager
An AI-powered CTO agent with persistent context awareness for Nexus: Boss Rush game development
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class NexusCTO:
    """AI CTO with full project context and persistent memory simulation"""

    def __init__(self, project_root: str = None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent
        self.context_dir = self.project_root / "context"
        self.docs_dir = self.project_root / "docs"
        self.src_dir = self.project_root / "src"

        # Initialize context system
        self.context = self._load_context()
        self.decision_history = self._load_decision_history()

    def _load_context(self) -> Dict[str, Any]:
        """Load current project context"""
        context_file = self.context_dir / "current_session.json"
        if context_file.exists():
            return json.loads(context_file.read_text())
        return self._create_initial_context()

    def _create_initial_context(self) -> Dict[str, Any]:
        """Create initial project context"""
        return {
            "project_name": "Nexus: Boss Rush",
            "version": "0.1.0",
            "phase": "Pre-Production",
            "current_sprint": "Prototype Month 1",
            "last_updated": datetime.now().isoformat(),
            "architecture": {
                "game_engine": "Unity 2022 LTS",
                "backend": "PlayFab",
                "platforms": ["iOS", "Android"],
                "monetization": "Premium ($12.99 + DLC)"
            },
            "systems": {
                "combat": {
                    "status": "Not Started",
                    "progress": 0,
                    "notes": "First priority - combat feel prototype"
                },
                "boss_ai": {
                    "status": "Not Started",
                    "progress": 0,
                    "notes": "Depends on combat system"
                },
                "ui_mobile": {
                    "status": "Not Started",
                    "progress": 0,
                    "notes": "Mobile-first design critical"
                }
            },
            "current_focus": None,
            "blockers": [],
            "next_priorities": [
                "Unity setup and basic movement",
                "Dragoon class prototype",
                "Boss 1 (Stone Guardian) implementation"
            ]
        }

    def _load_decision_history(self) -> List[Dict]:
        """Load historical decisions"""
        decisions_file = self.docs_dir / "decisions" / "decision_log.md"
        if decisions_file.exists():
            # Parse markdown file into decisions
            return self._parse_decisions(decisions_file)
        return []

    def update_context(self, updates: Dict[str, Any]):
        """Update project context"""
        self.context.update(updates)
        self.context["last_updated"] = datetime.now().isoformat()
        self._save_context()

    def _save_context(self):
        """Save current context"""
        self.context_dir.mkdir(exist_ok=True)
        context_file = self.context_dir / "current_session.json"
        context_file.write_text(json.dumps(self.context, indent=2))

    def scan_codebase(self) -> Dict[str, Any]:
        """Scan source code and understand current architecture"""
        if not self.src_dir.exists():
            return {"status": "No source code yet"}

        code_structure = {
            "directories": [],
            "files": [],
            "components": {},
            "systems": {}
        }

        for root, dirs, files in os.walk(self.src_dir):
            code_structure["directories"].extend(dirs)
            for file in files:
                code_structure["files"].append(file)

        return code_structure

    def make_architectural_decision(self, question: str, options: List[str] = None) -> Dict[str, Any]:
        """Make architectural decision with full context"""
        context = {
            "current_state": self.context,
            "code_structure": self.scan_codebase(),
            "recent_decisions": self.decision_history[-5:],  # Last 5 decisions
            "question": question,
            "options": options
        }

        # This would integrate with Claude/GPT for decision making
        decision = {
            "question": question,
            "chosen_option": None,  # AI would fill this
            "reasoning": "Pending AI analysis",
            "context": context,
            "timestamp": datetime.now().isoformat(),
            "impact": "To be analyzed"
        }

        self._record_decision(decision)
        return decision

    def _record_decision(self, decision: Dict[str, Any]):
        """Record architectural decision"""
        decisions_dir = self.docs_dir / "decisions"
        decisions_dir.mkdir(exist_ok=True)

        # Append to decision log
        decision_file = decisions_dir / "decision_log.md"

        if not decision_file.exists():
            decision_file.write_text("# Architectural Decision Log\n\n")

        with open(decision_file, "a") as f:
            f.write(f"## Decision: {decision['question']}\n")
            f.write(f"**Date:** {decision['timestamp']}\n")
            f.write(f"**Choice:** {decision['chosen_option']}\n")
            f.write(f"**Reasoning:** {decision['reasoning']}\n")
            f.write(f"**Impact:** {decision['impact']}\n\n")
            f.write("---\n\n")

    def suggest_next_steps(self) -> List[Dict[str, str]]:
        """Suggest next steps based on current context"""
        suggestions = []

        # Analyze current state
        for system, info in self.context["systems"].items():
            if info["status"] == "Not Started":
                suggestions.append({
                    "priority": "High",
                    "system": system,
                    "action": f"Start {system} implementation",
                    "reason": f"Critical system not yet begun: {info['notes']}"
                })

        # Add blockers
        for blocker in self.context["blockers"]:
            suggestions.append({
                "priority": "Critical",
                "system": "Blocker",
                "action": f"Resolve: {blocker}",
                "reason": "Blocking progress"
            })

        return sorted(suggestions, key=lambda x: {
            "Critical": 0,
            "High": 1,
            "Medium": 2,
            "Low": 3
        }.get(x["priority"], 99))

    def get_full_context_prompt(self) -> str:
        """Generate comprehensive context for AI interactions"""
        prompt = f"""# Nexus: Boss Rush - Project Context

## Project Overview
{json.dumps(self.context, indent=2)}

## Code Structure
{json.dumps(self.scan_codebase(), indent=2)}

## Recent Decisions
{self.decision_history[-3:] if self.decision_history else "No decisions yet"}

## Current Focus
{self.context.get('current_focus', 'Not set')}

## Immediate Priorities
{self.context.get('next_priorities', [])}

## Blockers
{self.context.get('blockers', [])}
"""
        return prompt

    def _parse_decisions(self, decision_file: Path) -> List[Dict]:
        """Parse markdown decisions into structured data"""
        # Implementation would parse markdown file
        return []
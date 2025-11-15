"""
Nexus CTO Oracle - AI-powered Chief Technology Officer
Complete context-aware decision making for Nexus: Boss Rush game development
"""

from .context_manager import NexusCTO
from .decision_engine import NexusDecisionEngine
from .roadmap_tracker import NexusRoadmapTracker


class NexusCTOOracle:
    """Main CTO Oracle interface - combines all CTO capabilities"""

    def __init__(self, project_root: str = None):
        self.cto = NexusCTO(project_root)
        self.decision_engine = NexusDecisionEngine(self.cto)
        self.roadmap_tracker = NexusRoadmapTracker(self.cto)

    def get_full_context(self) -> str:
        """Get complete project context for AI interactions"""
        return self.cto.get_full_context_prompt()

    def make_decision(self, question: str, context: Dict = None):
        """Make architectural decision with full context"""
        return self.decision_engine.make_decision(question, context)

    def get_status_report(self) -> Dict:
        """Get complete project status"""
        return {
            "current_phase": self.roadmap_tracker.get_current_phase(),
            "progress": self.roadmap_tracker.get_progress_summary(),
            "upcoming": self.roadmap_tracker.get_upcoming_deadlines(),
            "strategic_guidance": self.decision_engine.get_strategic_guidance(),
            "next_steps": self.cto.suggest_next_steps()
        }

    def update_progress(self, milestone_id: str, status: str, notes: str = None):
        """Update milestone progress"""
        from .roadmap_tracker import MilestoneStatus
        status_enum = MilestoneStatus(status)
        return self.roadmap_tracker.update_milestone_status(milestone_id, status_enum, notes)

    def focus_on(self, system: str, task: str):
        """Set current development focus"""
        self.cto.update_context({
            "current_focus": {
                "system": system,
                "task": task,
                "started": datetime.now().isoformat()
            }
        })

    def add_blocker(self, blocker: str):
        """Add project blocker"""
        blockers = self.cto.context.get("blockers", [])
        blockers.append({
            "description": blocker,
            "added": datetime.now().isoformat(),
            "status": "Active"
        })
        self.cto.update_context({"blockers": blockers})

    def resolve_blocker(self, blocker: str, resolution: str):
        """Mark blocker as resolved"""
        blockers = self.cto.context.get("blockers", [])
        for i, b in enumerate(blockers):
            if b["description"] == blocker:
                blockers[i]["status"] = "Resolved"
                blockers[i]["resolution"] = resolution
                blockers[i]["resolved"] = datetime.now().isoformat()
                break
        self.cto.update_context({"blockers": blockers})


# Convenience function for quick access
def get_cto_oracle(project_root: str = None) -> NexusCTOOracle:
    """Get initialized CTO Oracle instance"""
    return NexusCTOOracle(project_root)
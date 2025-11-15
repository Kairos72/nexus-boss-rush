"""
Nexus CTO Oracle - Automatic Context Updater
Keeps the CTO Oracle synchronized with all development activities
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any


class NexusAutoUpdater:
    """Automatically updates CTO Oracle context based on development activities"""

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.context_dir = self.project_root / "context"
        self.session_log = self.context_dir / "session_log.json"

    def log_conversation(self, speaker: str, content: str, decisions: List[str] = None):
        """Log every conversation with automatic context extraction"""

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "speaker": speaker,  # "CEO", "CTO_Oracle", or "Builder(Claude)"
            "content": content,
            "type": self._classify_conversation(content),
            "decisions_made": decisions or [],
            "context_changes": self._extract_context_changes(content)
        }

        # Append to session log
        self._append_to_log(log_entry)

        # Update relevant context files
        self._update_context_from_conversation(log_entry)

    def _classify_conversation(self, content: str) -> str:
        """Classify conversation type for better organization"""
        content_lower = content.lower()

        if any(word in content_lower for word in ["decision", "choose", "should we", "which"]):
            return "DECISION"
        elif any(word in content_lower for word in ["progress", "status", "how are", "what's"]):
            return "STATUS_CHECK"
        elif any(word in content_lower for word in ["problem", "issue", "bug", "error"]):
            return "PROBLEM"
        elif any(word in content_lower for word in ["next", "priority", "focus"]):
            return "PLANNING"
        elif any(word in content_lower for word in ["milestone", "complete", "finished"]):
            return "PROGRESS_UPDATE"
        else:
            return "GENERAL"

    def _extract_context_changes(self, content: str) -> Dict[str, Any]:
        """Extract potential context changes from conversation"""
        changes = {}

        # Look for status updates
        if "complete" in content.lower() or "finished" in content.lower():
            changes["possible_progress"] = True

        # Look for blockers
        if any(word in content.lower() for word in ["blocked", "stuck", "can't", "issue"]):
            changes["possible_blocker"] = True

        # Look for new priorities
        if "next" in content.lower() or "priority" in content.lower():
            changes["possible_priority_change"] = True

        # Look for decisions
        if "decided" in content.lower() or "chose" in content.lower():
            changes["possible_decision"] = True

        return changes

    def _append_to_log(self, log_entry: Dict):
        """Append entry to session log"""
        logs = []
        if self.session_log.exists():
            logs = json.loads(self.session_log.read_text())

        logs.append(log_entry)

        # Keep only last 100 entries to prevent file bloat
        if len(logs) > 100:
            logs = logs[-100:]

        self.session_log.write_text(json.dumps(logs, indent=2))

    def _update_context_from_conversation(self, log_entry: Dict):
        """Update context files based on conversation content"""
        current_context_file = self.context_dir / "current_session.json"

        if current_context_file.exists():
            current_context = json.loads(current_context_file.read_text())

            # Update last actions
            if "last_actions" not in current_context:
                current_context["last_actions"] = []

            action = {
                "timestamp": log_entry["timestamp"],
                "type": log_entry["type"],
                "speaker": log_entry["speaker"],
                "summary": log_entry["content"][:100] + "..." if len(log_entry["content"]) > 100 else log_entry["content"]
            }

            current_context["last_actions"].append(action)

            # Keep only last 10 actions
            if len(current_context["last_actions"]) > 10:
                current_context["last_actions"] = current_context["last_actions"][-10:]

            # Update last modified time
            current_context["last_updated"] = log_entry["timestamp"]

            # Save updated context
            current_context_file.write_text(json.dumps(current_context, indent=2))

    def scan_project_files(self):
        """Scan project files for automatic context updates"""
        updates = {}

        # Check for new Unity files
        unity_dir = self.project_root / "src"
        if unity_dir.exists():
            scripts = list(unity_dir.rglob("*.cs"))
            if scripts:
                updates["unity_scripts_count"] = len(scripts)
                updates["last_unity_activity"] = datetime.now().isoformat()

        # Check for new assets
        assets_dir = unity_dir / "Assets" if unity_dir.exists() else None
        if assets_dir and assets_dir.exists():
            asset_count = len(list(assets_dir.rglob("*")))
            updates["asset_count"] = asset_count

        # Check roadmap progress
        roadmap_file = self.project_root / "docs" / "roadmap" / "current_roadmap.json"
        if roadmap_file.exists():
            roadmap = json.loads(roadmap_file.read_text())
            # Calculate progress
            total_milestones = 0
            completed_milestones = 0
            for phase in roadmap["phases"].values():
                for milestone in phase["milestones"]:
                    total_milestones += 1
                    if milestone["status"] == "Completed":
                        completed_milestones += 1

            if total_milestones > 0:
                updates["roadmap_progress"] = (completed_milestones / total_milestones) * 100

        # Apply updates if any
        if updates:
            self._apply_auto_updates(updates)

    def _apply_auto_updates(self, updates: Dict):
        """Apply detected updates to current context"""
        current_context_file = self.context_dir / "current_session.json"

        if current_context_file.exists():
            current_context = json.loads(current_context_file.read_text())

            # Update systems based on detected files
            if "unity_scripts_count" in updates:
                if "systems" not in current_context:
                    current_context["systems"] = {}

                # Auto-update combat system if combat scripts detected
                if updates["unity_scripts_count"] > 0:
                    if current_context["systems"].get("combat", {}).get("status") == "Not Started":
                        current_context["systems"]["combat"] = {
                            "status": "In Progress",
                            "progress": min(25, updates["unity_scripts_count"] * 5),
                            "notes": "Unity scripts detected - auto-updated"
                        }

            # Save updates
            current_context["last_auto_update"] = datetime.now().isoformat()
            current_context_file.write_text(json.dumps(current_context, indent=2))

    def generate_daily_summary(self) -> Dict[str, Any]:
        """Generate daily summary from all activities"""
        today = datetime.now().strftime("%Y-%m-%d")

        # Load today's conversations
        if not self.session_log.exists():
            return {"date": today, "activities": "No conversations logged yet"}

        logs = json.loads(self.session_log.read_text())
        today_logs = [log for log in logs if log["timestamp"].startswith(today)]

        if not today_logs:
            return {"date": today, "activities": "No activities today"}

        # Analyze today's activities
        summary = {
            "date": today,
            "total_conversations": len(today_logs),
            "decisions_made": sum(len(log.get("decisions_made", [])) for log in today_logs),
            "problems_identified": len([log for log in today_logs if log["type"] == "PROBLEM"]),
            "progress_updates": len([log for log in today_logs if log["type"] == "PROGRESS_UPDATE"]),
            "activity_types": {}
        }

        # Count activity types
        for log in today_logs:
            activity_type = log["type"]
            if activity_type not in summary["activity_types"]:
                summary["activity_types"][activity_type] = 0
            summary["activity_types"][activity_type] += 1

        return summary

    def get_context_for_cto(self) -> str:
        """Generate comprehensive context for CTO Oracle responses"""
        context_parts = []

        # Current session
        current_context_file = self.context_dir / "current_session.json"
        if current_context_file.exists():
            context_parts.append("## Current Project State")
            context_parts.append(current_context_file.read_text())

        # Recent decisions
        decisions_file = self.project_root / "docs" / "decisions" / "decision_log.md"
        if decisions_file.exists():
            context_parts.append("## Recent Decisions")
            context_parts.append(decisions_file.read_text()[-2000:])  # Last 2KB

        # Recent activities
        if self.session_log.exists():
            logs = json.loads(self.session_log.read_text())
            recent_logs = logs[-10:]  # Last 10 activities
            context_parts.append("## Recent Activities")
            for log in recent_logs:
                context_parts.append(f"- {log['timestamp']}: {log['speaker']} - {log['type']}")
                context_parts.append(f"  {log['content'][:100]}...")

        return "\n\n".join(context_parts)


# Auto-update functions for seamless integration
def log_ceo_conversation(content: str, decisions: List[str] = None, project_root: str = None):
    """Quick function to log CEO conversations"""
    default_root = Path(__file__).parent.parent.parent
    updater = NexusAutoUpdater(project_root or default_root)
    updater.log_conversation("CEO", content, decisions)

def log_builder_conversation(content: str, decisions: List[str] = None, project_root: str = None):
    """Quick function to log Claude/builder conversations"""
    default_root = Path(__file__).parent.parent.parent
    updater = NexusAutoUpdater(project_root or default_root)
    updater.log_conversation("Builder(Claude)", content, decisions)

def auto_update_context(project_root: str = None):
    """Trigger automatic context update from project files"""
    default_root = Path(__file__).parent.parent.parent
    updater = NexusAutoUpdater(project_root or default_root)
    updater.scan_project_files()
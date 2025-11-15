"""
Nexus CTO Oracle - Roadmap Tracker
Monitors progress, manages milestones, and keeps the project on track
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from enum import Enum
import json


class MilestoneStatus(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    BLOCKED = "Blocked"
    COMPLETED = "Completed"
    DELAYED = "Delayed"


class NexusRoadmapTracker:
    """Tracks project progress and manages roadmap evolution"""

    def __init__(self, cto_instance):
        self.cto = cto_instance
        self.roadmap = self._load_roadmap()
        self.progress_history = []

    def _load_roadmap(self) -> Dict[str, Any]:
        """Load current roadmap or create initial roadmap"""
        roadmap_file = self.cto.docs_dir / "roadmap" / "current_roadmap.json"

        if roadmap_file.exists():
            return json.loads(roadmap_file.read_text())

        # Create initial 8-month roadmap
        return self._create_initial_roadmap()

    def _create_initial_roadmap(self) -> Dict[str, Any]:
        """Create the initial 8-month development roadmap"""
        return {
            "project_duration": "8 months",
            "total_budget": "$50,000 - $80,000",
            "phases": {
                "Phase 1: Prototype": {
                    "duration": "Months 1-2",
                    "goal": "Prove combat feels good and boss mechanics work on mobile",
                    "budget": "$5,000 - $10,000",
                    "milestones": [
                        {
                            "id": "M1",
                            "title": "Basic Movement + Combat",
                            "target_date": "Month 1, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Unity project setup",
                                "Character controller with virtual joystick",
                                "Dodge roll with i-frames",
                                "One basic attack ability"
                            ],
                            "acceptance_criteria": [
                                "Character moves responsively on mobile",
                                "Dodge roll feels good with haptic feedback",
                                "Attack connects with satisfying impact"
                            ]
                        },
                        {
                            "id": "M2",
                            "title": "First Boss Complete",
                            "target_date": "Month 2, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Stone Guardian boss with all mechanics",
                                "Cleave, Ground Pound, Rock Throw attacks",
                                "Phase transition at 50% HP",
                                "HP bars and basic UI"
                            ],
                            "acceptance_criteria": [
                                "Boss feels challenging but fair",
                                "Telegraphs are clear and readable",
                                "5+ playtesters defeat boss after 3-5 attempts",
                                "Combat feels satisfying"
                            ]
                        }
                    ]
                },
                "Phase 2: Vertical Slice": {
                    "duration": "Months 3-4",
                    "goal": "Complete 3-boss demo (free version)",
                    "budget": "$10,000 - $15,000",
                    "milestones": [
                        {
                            "id": "M3",
                            "title": "3 Bosses Complete",
                            "target_date": "Month 3, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Flame Archon with DOT mechanics",
                                "Ice Witch with debuff system",
                                "All 3 starting classes (Dragoon, Paladin, White Mage)",
                                "Basic roguelike upgrade system"
                            ]
                        },
                        {
                            "id": "M4",
                            "title": "Demo Feature Complete",
                            "target_date": "Month 4, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Tutorial and onboarding",
                                "Main menu and settings",
                                "Save system",
                                "Performance optimization for target devices"
                            ],
                            "acceptance_criteria": [
                                "20+ playtesters complete all 3 bosses",
                                "Average session: 15-20 minutes",
                                "70%+ say they'd pay $12.99 for full game",
                                "No crashes on target devices"
                            ]
                        }
                    ]
                },
                "Phase 3: Content Sprint": {
                    "duration": "Months 5-6",
                    "goal": "Complete all 10 bosses, all systems",
                    "budget": "$15,000 - $25,000",
                    "milestones": [
                        {
                            "id": "M5",
                            "title": "All Bosses Implemented",
                            "target_date": "Month 5, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Bosses 4-10 with unique mechanics",
                                "All boss environments and VFX",
                                "Boss AI patterns and difficulty scaling"
                            ]
                        },
                        {
                            "id": "M6",
                            "title": "All Systems Complete",
                            "target_date": "Month 6, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Hard and Nightmare difficulties",
                                "Achievement system",
                                "Cosmetic unlocks",
                                "Challenge modes"
                            ]
                        }
                    ]
                },
                "Phase 4: Polish & Testing": {
                    "duration": "Month 7",
                    "goal": "Beta-ready build, bug-free, polished",
                    "budget": "$5,000 - $10,000",
                    "milestones": [
                        {
                            "id": "M7",
                            "title": "Beta Ready",
                            "target_date": "Month 7, Week 2",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Closed beta with 50-100 testers",
                                "Bug count < 20",
                                "Performance 60 FPS stable"
                            ]
                        },
                        {
                            "id": "M8",
                            "title": "Launch Ready",
                            "target_date": "Month 7, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Final polish and optimization",
                                "Store assets and descriptions",
                                "Marketing materials ready"
                            ]
                        }
                    ]
                },
                "Phase 5: Launch": {
                    "duration": "Month 8",
                    "goal": "Successful launch with strong conversion",
                    "budget": "$10,000 - $20,000",
                    "milestones": [
                        {
                            "id": "M9",
                            "title": "Soft Launch Complete",
                            "target_date": "Month 8, Week 2",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "2-3 test regions launched",
                                "Initial metrics analysis",
                                "Iteration based on feedback"
                            ]
                        },
                        {
                            "id": "M10",
                            "title": "Global Launch",
                            "target_date": "Month 8, Week 4",
                            "status": MilestoneStatus.NOT_STARTED.value,
                            "deliverables": [
                                "Worldwide release",
                                "Marketing campaign executed",
                                "Community management active"
                            ],
                            "success_metrics": [
                                "10,000+ downloads Week 1",
                                "4.5+ star rating",
                                "20%+ conversion rate",
                                "Featured by Apple/Google (stretch goal)"
                            ]
                        }
                    ]
                }
            }
        }

    def update_milestone_status(self, milestone_id: str, status: MilestoneStatus, notes: str = None):
        """Update the status of a specific milestone"""
        for phase_name, phase in self.roadmap["phases"].items():
            for milestone in phase["milestones"]:
                if milestone["id"] == milestone_id:
                    old_status = milestone["status"]
                    milestone["status"] = status.value

                    if notes:
                        milestone["notes"] = notes

                    # Record the change
                    self._record_progress_change(milestone_id, old_status, status.value, notes)

                    # Save updated roadmap
                    self._save_roadmap()

                    # Check for phase completion
                    self._check_phase_completion(phase_name)

                    return True

        return False

    def get_current_phase(self) -> Dict[str, Any]:
        """Get current development phase and focus"""
        current_date = datetime.now()

        for phase_name, phase in self.roadmap["phases"].items():
            for milestone in phase["milestones"]:
                if milestone["status"] in [MilestoneStatus.NOT_STARTED.value, MilestoneStatus.IN_PROGRESS.value]:
                    return {
                        "phase": phase_name,
                        "goal": phase["goal"],
                        "current_milestone": milestone,
                        "next_milestones": phase["milestones"][phase["milestones"].index(milestone)+1:phase["milestones"].index(milestone)+2],
                        "progress": self._calculate_phase_progress(phase_name)
                    }

        # If all milestones complete, return final phase
        return {
            "phase": "Complete",
            "goal": "Project finished!",
            "current_milestone": None,
            "progress": 100
        }

    def get_upcoming_deadlines(self, days_ahead: int = 14) -> List[Dict]:
        """Get upcoming deadlines within specified timeframe"""
        upcoming = []
        current_date = datetime.now()
        deadline_date = current_date + timedelta(days=days_ahead)

        for phase_name, phase in self.roadmap["phases"].items():
            for milestone in phase["milestones"]:
                if milestone["status"] not in [MilestoneStatus.COMPLETED.value]:
                    # Parse target date (simplified - would use proper date parsing)
                    target_week = int(milestone.get("target_date", "Week 1").split("Week")[1].split(",")[0].strip())

                    # Calculate if deadline is within window (simplified logic)
                    if target_week <= 2:  # Simplified - would calculate actual dates
                        urgency = "High" if target_week == 1 else "Medium"
                        upcoming.append({
                            "milestone": milestone,
                            "phase": phase_name,
                            "urgency": urgency,
                            "days_remaining": target_week * 7
                        })

        return sorted(upcoming, key=lambda x: x["days_remaining"])

    def get_progress_summary(self) -> Dict[str, Any]:
        """Get overall project progress summary"""
        total_milestones = 0
        completed_milestones = 0

        phase_progress = {}

        for phase_name, phase in self.roadmap["phases"].items():
            phase_total = len(phase["milestones"])
            phase_completed = sum(1 for m in phase["milestones"] if m["status"] == MilestoneStatus.COMPLETED.value)

            total_milestones += phase_total
            completed_milestones += phase_completed

            phase_progress[phase_name] = {
                "total": phase_total,
                "completed": phase_completed,
                "percentage": (phase_completed / phase_total * 100) if phase_total > 0 else 0
            }

        overall_progress = (completed_milestones / total_milestones * 100) if total_milestones > 0 else 0

        return {
            "overall_progress": overall_progress,
            "total_milestones": total_milestones,
            "completed_milestones": completed_milestones,
            "current_phase": self.get_current_phase(),
            "phase_breakdown": phase_progress,
            "upcoming_deadlines": self.get_upcoming_deadlines(),
            "health_status": self._assess_project_health()
        }

    def _calculate_phase_progress(self, phase_name: str) -> float:
        """Calculate percentage completion for a phase"""
        phase = self.roadmap["phases"][phase_name]
        if not phase["milestones"]:
            return 0.0

        completed = sum(1 for m in phase["milestones"] if m["status"] == MilestoneStatus.COMPLETED.value)
        return (completed / len(phase["milestones"])) * 100

    def _record_progress_change(self, milestone_id: str, old_status: str, new_status: str, notes: str):
        """Record a progress change in history"""
        change = {
            "timestamp": datetime.now().isoformat(),
            "milestone_id": milestone_id,
            "old_status": old_status,
            "new_status": new_status,
            "notes": notes
        }

        self.progress_history.append(change)

        # Keep only last 100 changes
        if len(self.progress_history) > 100:
            self.progress_history = self.progress_history[-100:]

    def _save_roadmap(self):
        """Save current roadmap to file"""
        roadmap_file = self.cto.docs_dir / "roadmap" / "current_roadmap.json"
        roadmap_file.parent.mkdir(exist_ok=True)
        roadmap_file.write_text(json.dumps(self.roadmap, indent=2))

    def _check_phase_completion(self, phase_name: str):
        """Check if all milestones in a phase are complete"""
        phase = self.roadmap["phases"][phase_name]
        all_complete = all(m["status"] == MilestoneStatus.COMPLETED.value for m in phase["milestones"])

        if all_complete:
            # Record phase completion
            completion_file = self.cto.docs_dir / "roadmap" / "phase_completions.json"

            completions = {}
            if completion_file.exists():
                completions = json.loads(completion_file.read_text())

            completions[phase_name] = {
                "completed_date": datetime.now().isoformat(),
                "duration_actual": "To be calculated"
            }

            completion_file.write_text(json.dumps(completions, indent=2))

    def _assess_project_health(self) -> Dict[str, Any]:
        """Assess overall project health"""
        current_phase = self.get_current_phase()
        overdue = self.get_upcoming_deadlines(7)

        health_score = 100

        # Reduce score for overdue milestones
        if overdue:
            health_score -= len(overdue) * 10

        # Check for blockers
        blockers = self.cto.context.get("blockers", [])
        if blockers:
            health_score -= len(blockers) * 15

        # Check budget health
        current_spent = 0  # Would track actual spend
        budget_total = 65000  # Midpoint of range
        budget_health = 100 - (current_spent / budget_total * 100)

        return {
            "overall_score": max(0, health_score),
            "status": "On Track" if health_score > 80 else "Needs Attention" if health_score > 60 else "At Risk",
            "schedule_health": health_score,
            "budget_health": budget_health,
            "quality_health": 100,  # Would track bug count, test coverage
            "team_health": 100,  # Would track team morale, workload
            "recommendations": self._generate_health_recommendations(health_score)
        }

    def _generate_health_recommendations(self, health_score: float) -> List[str]:
        """Generate recommendations based on health score"""
        recommendations = []

        if health_score < 80:
            recommendations.append("Review upcoming deadlines and re-prioritize if needed")

        if health_score < 60:
            recommendations.append("Schedule urgent review of project scope and timeline")
            recommendations.append("Consider feature reduction to meet critical dates")

        # Always include these
        recommendations.extend([
            "Continue daily progress tracking",
            "Maintain focus on current phase goals"
        ])

        return recommendations

    def suggest_next_milestone(self) -> Optional[Dict[str, Any]]:
        """Suggest the next milestone to work on"""
        current_phase = self.get_current_phase()

        if current_phase["current_milestone"]:
            return current_phase["current_milestone"]

        return None

    def add_roadmap_entry(self, phase_name: str, milestone: Dict[str, Any]):
        """Add new milestone to roadmap (for scope changes)"""
        if phase_name in self.roadmap["phases"]:
            self.roadmap["phases"][phase_name]["milestones"].append(milestone)
            self._save_roadmap()
            return True
        return False
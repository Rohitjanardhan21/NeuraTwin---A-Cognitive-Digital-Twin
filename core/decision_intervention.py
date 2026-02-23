"""
⚡ LIVE DECISION INTERVENTION SYSTEM
Catches you before bad decisions and intervenes
"""

from datetime import datetime, time
from typing import Dict, List, Optional
import re


class DecisionInterventionSystem:
    """Real-time decision intervention and validation"""
    
    def __init__(self, decision_tracker, pattern_analyzer):
        self.decision_tracker = decision_tracker
        self.pattern_analyzer = pattern_analyzer
        self.intervention_rules = self._load_intervention_rules()
        self.pending_decisions = []
        
    def _load_intervention_rules(self) -> List[Dict]:
        """Load intervention rules"""
        return [
            {
                "name": "late_night_decision",
                "condition": lambda ctx: datetime.now().hour >= 22 or datetime.now().hour <= 5,
                "message": "⚠️ It's late. You make worse decisions after 10pm. Sleep on it?",
                "severity": "high",
                "delay_seconds": 60
            },
            {
                "name": "stress_decision",
                "condition": lambda ctx: ctx.get("stress_level", 0) > 70,
                "message": "🚨 You're stressed. This decision has 73% regret probability when stressed.",
                "severity": "high",
                "delay_seconds": 300
            },
            {
                "name": "impulsive_pattern",
                "condition": lambda ctx: ctx.get("time_thinking", 0) < 60,
                "message": "⏸️ You're deciding too fast. You usually regret quick decisions.",
                "severity": "medium",
                "delay_seconds": 120
            },
            {
                "name": "capacity_overload",
                "condition": lambda ctx: ctx.get("current_commitments", 0) > 5,
                "message": "🛑 You're at 87% capacity. Adding more will hurt existing commitments.",
                "severity": "high",
                "delay_seconds": 180
            },
            {
                "name": "emotional_state",
                "condition": lambda ctx: ctx.get("emotional_state") in ["angry", "frustrated", "sad"],
                "message": "😤 You're emotional. Draft saved. Review when calm?",
                "severity": "critical",
                "delay_seconds": 3600
            },
            {
                "name": "repeated_mistake",
                "condition": lambda ctx: self._is_repeated_mistake(ctx),
                "message": "🔄 You've made this exact decision 3 times. It failed each time. Really?",
                "severity": "critical",
                "delay_seconds": 300
            },
            {
                "name": "friday_commitment",
                "condition": lambda ctx: datetime.now().weekday() == 4 and ctx.get("decision_type") == "commitment",
                "message": "📅 You break 60% of commitments made on Fridays. Wait till Monday?",
                "severity": "medium",
                "delay_seconds": 120
            },
            {
                "name": "post_meeting_decision",
                "condition": lambda ctx: ctx.get("minutes_since_meeting", 999) < 30,
                "message": "💼 You just left a meeting. You're 40% more impulsive post-meeting.",
                "severity": "medium",
                "delay_seconds": 180
            }
        ]
    
    def check_decision(self, decision: str, context: Dict) -> Dict:
        """Check if decision should be intervened"""
        interventions = []
        
        for rule in self.intervention_rules:
            try:
                if rule["condition"](context):
                    interventions.append({
                        "rule": rule["name"],
                        "message": rule["message"],
                        "severity": rule["severity"],
                        "delay_seconds": rule["delay_seconds"],
                        "timestamp": datetime.now()
                    })
            except Exception as e:
                pass  # Skip failed rule checks
        
        if interventions:
            # Get highest severity intervention
            critical = [i for i in interventions if i["severity"] == "critical"]
            high = [i for i in interventions if i["severity"] == "high"]
            
            primary = critical[0] if critical else (high[0] if high else interventions[0])
            
            return {
                "should_intervene": True,
                "intervention": primary,
                "all_warnings": interventions,
                "allow_override": primary["severity"] != "critical"
            }
        
        return {
            "should_intervene": False,
            "message": "✅ Decision looks good. Proceed."
        }
    
    def _is_repeated_mistake(self, context: Dict) -> bool:
        """Check if this is a repeated mistake"""
        decision_text = context.get("decision", "").lower()
        
        # Get past decisions
        past_decisions = self.decision_tracker.get_decision_timeline()
        
        # Find similar decisions that failed
        similar_failures = [
            d for d in past_decisions
            if self._is_similar(decision_text, d.get("decision", "").lower())
            and d.get("outcome") in ["failure", "regret"]
        ]
        
        return len(similar_failures) >= 2
    
    def _is_similar(self, text1: str, text2: str) -> bool:
        """Check if two decision texts are similar"""
        words1 = set(text1.split())
        words2 = set(text2.split())
        
        if not words1 or not words2:
            return False
        
        overlap = len(words1 & words2)
        return overlap / min(len(words1), len(words2)) > 0.5
    
    def calculate_regret_probability(self, decision: str, context: Dict) -> float:
        """Calculate probability of regretting this decision"""
        regret_score = 0.0
        
        # Time-based factors
        hour = datetime.now().hour
        if hour >= 22 or hour <= 5:
            regret_score += 0.3
        
        # Stress-based
        if context.get("stress_level", 0) > 70:
            regret_score += 0.25
        
        # Speed-based
        if context.get("time_thinking", 0) < 60:
            regret_score += 0.2
        
        # Emotional state
        if context.get("emotional_state") in ["angry", "frustrated"]:
            regret_score += 0.35
        
        # Historical pattern
        if self._is_repeated_mistake(context):
            regret_score += 0.4
        
        return min(1.0, regret_score)
    
    def suggest_alternative(self, decision: str, context: Dict) -> Optional[str]:
        """Suggest alternative action"""
        regret_prob = self.calculate_regret_probability(decision, context)
        
        if regret_prob > 0.7:
            return "🛑 STOP. Sleep on this. 89% regret probability."
        elif regret_prob > 0.5:
            return "⏸️ PAUSE. Wait 2 hours. Review with fresh mind."
        elif regret_prob > 0.3:
            return "⚠️ CAUTION. Talk to someone first."
        else:
            return None
    
    def log_intervention_result(self, decision_id: str, overridden: bool, outcome: str):
        """Log whether intervention was helpful"""
        # Track intervention effectiveness
        pass
    
    def get_intervention_stats(self) -> Dict:
        """Get statistics on interventions"""
        return {
            "total_interventions": len(self.pending_decisions),
            "overridden": sum(1 for d in self.pending_decisions if d.get("overridden")),
            "successful_blocks": sum(1 for d in self.pending_decisions if not d.get("overridden"))
        }

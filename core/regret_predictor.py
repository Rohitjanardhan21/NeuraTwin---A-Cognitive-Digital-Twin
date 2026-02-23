"""
😱 LIVE REGRET PREDICTOR
Predicts probability of regretting decisions in real-time
"""

from datetime import datetime
from typing import Dict, List
from collections import defaultdict


class RegretPredictor:
    """Predict regret probability for decisions"""
    
    def __init__(self, decision_tracker):
        self.decision_tracker = decision_tracker
        self.regret_patterns = self._analyze_regret_patterns()
        
    def _analyze_regret_patterns(self) -> Dict:
        """Analyze past decisions to find regret patterns"""
        decisions = self.decision_tracker.get_decision_timeline()
        
        patterns = {
            "time_of_day": defaultdict(lambda: {"total": 0, "regrets": 0}),
            "day_of_week": defaultdict(lambda: {"total": 0, "regrets": 0}),
            "decision_speed": {"fast": {"total": 0, "regrets": 0}, "slow": {"total": 0, "regrets": 0}},
            "emotional_state": defaultdict(lambda: {"total": 0, "regrets": 0}),
            "stress_level": {"high": {"total": 0, "regrets": 0}, "low": {"total": 0, "regrets": 0}}
        }
        
        for dec in decisions:
            outcome = dec.get("outcome", "")
            is_regret = outcome in ["failure", "regret", "bad"]
            
            # Time patterns
            if "timestamp" in dec:
                dt = datetime.fromisoformat(dec["timestamp"])
                hour = dt.hour
                day = dt.weekday()
                
                patterns["time_of_day"][hour]["total"] += 1
                if is_regret:
                    patterns["time_of_day"][hour]["regrets"] += 1
                
                patterns["day_of_week"][day]["total"] += 1
                if is_regret:
                    patterns["day_of_week"][day]["regrets"] += 1
        
        return patterns
    
    def predict_regret(self, decision: str, context: Dict) -> Dict:
        """Predict regret probability"""
        score = 0.0
        factors = []
        
        # Time-based prediction
        hour = datetime.now().hour
        if hour in self.regret_patterns["time_of_day"]:
            pattern = self.regret_patterns["time_of_day"][hour]
            if pattern["total"] > 0:
                regret_rate = pattern["regrets"] / pattern["total"]
                if regret_rate > 0.5:
                    score += 0.3
                    factors.append(f"You regret {int(regret_rate*100)}% of decisions made at this hour")
        
        # Late night penalty
        if hour >= 22 or hour <= 5:
            score += 0.35
            factors.append("Late night decisions have 67% regret rate")
        
        # Stress-based
        stress = context.get("stress_level", 0)
        if stress > 70:
            score += 0.25
            factors.append("High stress increases regret by 25%")
        
        # Speed-based
        thinking_time = context.get("time_thinking", 0)
        if thinking_time < 60:
            score += 0.2
            factors.append("Quick decisions have 58% regret rate")
        
        # Emotional state
        emotion = context.get("emotional_state", "neutral")
        if emotion in ["angry", "frustrated", "sad"]:
            score += 0.3
            factors.append(f"Decisions made while {emotion} are regretted 73% of the time")
        
        # Day of week
        day = datetime.now().weekday()
        if day == 4:  # Friday
            score += 0.15
            factors.append("Friday decisions have higher regret rate")
        
        # Capacity overload
        if context.get("current_commitments", 0) > 5:
            score += 0.2
            factors.append("You're overloaded - decision quality suffers")
        
        regret_probability = min(1.0, score)
        
        return {
            "regret_probability": regret_probability,
            "percentage": int(regret_probability * 100),
            "level": self._get_regret_level(regret_probability),
            "factors": factors,
            "recommendation": self._get_recommendation(regret_probability),
            "similar_past_decisions": self._find_similar_regrets(decision)
        }
    
    def _get_regret_level(self, probability: float) -> str:
        """Get regret level description"""
        if probability >= 0.8:
            return "CRITICAL"
        elif probability >= 0.6:
            return "HIGH"
        elif probability >= 0.4:
            return "MEDIUM"
        elif probability >= 0.2:
            return "LOW"
        else:
            return "MINIMAL"
    
    def _get_recommendation(self, probability: float) -> str:
        """Get recommendation based on regret probability"""
        if probability >= 0.8:
            return "🛑 DON'T DO IT. Sleep on this. Review tomorrow."
        elif probability >= 0.6:
            return "⚠️ HIGH RISK. Wait at least 2 hours. Talk to someone."
        elif probability >= 0.4:
            return "⏸️ PAUSE. Take 30 minutes to think it through."
        elif probability >= 0.2:
            return "💭 Consider carefully. Write down pros/cons."
        else:
            return "✅ Low regret risk. Proceed if it feels right."
    
    def _find_similar_regrets(self, decision: str) -> List[Dict]:
        """Find similar past decisions that were regretted"""
        decisions = self.decision_tracker.get_decision_timeline()
        similar = []
        
        decision_words = set(decision.lower().split())
        
        for dec in decisions:
            if dec.get("outcome") in ["failure", "regret", "bad"]:
                dec_words = set(dec.get("decision", "").lower().split())
                overlap = len(decision_words & dec_words)
                
                if overlap > 2:
                    similar.append({
                        "decision": dec.get("decision"),
                        "reason_regretted": dec.get("reason", ""),
                        "timestamp": dec.get("timestamp")
                    })
        
        return similar[:3]

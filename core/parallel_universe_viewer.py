"""
🌌 PARALLEL UNIVERSE VIEWER
Live simulation of alternate versions of you making different choices
"""

from datetime import datetime
from typing import Dict, List
import random


class ParallelUniverseViewer:
    """Simulate and track parallel versions of you"""
    
    PERSONAS = {
        "cautious": {
            "name": "Cautious You",
            "emoji": "🛡️",
            "traits": ["risk-averse", "thorough", "patient"],
            "decision_style": "Analyzes deeply, moves slowly, avoids risk",
            "values": ["stability", "security", "certainty"]
        },
        "ambitious": {
            "name": "Ambitious You", 
            "emoji": "🚀",
            "traits": ["risk-taking", "fast-moving", "opportunistic"],
            "decision_style": "Acts quickly, takes chances, pursues growth",
            "values": ["growth", "opportunity", "impact"]
        },
        "balanced": {
            "name": "Balanced You",
            "emoji": "⚖️",
            "traits": ["pragmatic", "measured", "adaptive"],
            "decision_style": "Weighs options, sets boundaries, stays flexible",
            "values": ["sustainability", "effectiveness", "harmony"]
        }
    }
    
    def __init__(self):
        self.universes = {
            "cautious": {"score": 0, "decisions": [], "state": "stable"},
            "ambitious": {"score": 0, "decisions": [], "state": "stable"},
            "balanced": {"score": 0, "decisions": [], "state": "stable"}
        }
        self.current_day_decisions = []
        
    def present_decision(self, decision_prompt: str, context: Dict) -> Dict:
        """Present a decision to all three versions"""
        responses = {}
        
        for persona_key, persona in self.PERSONAS.items():
            response = self._simulate_persona_decision(
                persona_key, 
                decision_prompt, 
                context
            )
            responses[persona_key] = response
            
            # Log decision
            self.universes[persona_key]["decisions"].append({
                "prompt": decision_prompt,
                "choice": response["choice"],
                "reasoning": response["reasoning"],
                "timestamp": datetime.now()
            })
        
        self.current_day_decisions.append({
            "prompt": decision_prompt,
            "responses": responses,
            "timestamp": datetime.now()
        })
        
        return responses
    
    def _simulate_persona_decision(self, persona_key: str, prompt: str, context: Dict) -> Dict:
        """Simulate how a persona would decide"""
        persona = self.PERSONAS[persona_key]
        
        if persona_key == "cautious":
            return self._cautious_decision(prompt, context, persona)
        elif persona_key == "ambitious":
            return self._ambitious_decision(prompt, context, persona)
        else:
            return self._balanced_decision(prompt, context, persona)
    
    def _cautious_decision(self, prompt: str, context: Dict, persona: Dict) -> Dict:
        """How cautious you would decide"""
        # Cautious you prioritizes safety and certainty
        
        if "meeting" in prompt.lower():
            return {
                "choice": "Decline politely",
                "reasoning": "Protect existing commitments and deep work time",
                "confidence": 0.85,
                "risk_level": "low"
            }
        elif "new project" in prompt.lower():
            return {
                "choice": "Research thoroughly first",
                "reasoning": "Need more data before committing resources",
                "confidence": 0.75,
                "risk_level": "low"
            }
        elif "opportunity" in prompt.lower():
            return {
                "choice": "Evaluate carefully",
                "reasoning": "Sounds good but need to verify claims and assess risks",
                "confidence": 0.70,
                "risk_level": "medium"
            }
        else:
            return {
                "choice": "Take time to decide",
                "reasoning": "No rush. Better to be thorough than fast.",
                "confidence": 0.80,
                "risk_level": "low"
            }
    
    def _ambitious_decision(self, prompt: str, context: Dict, persona: Dict) -> Dict:
        """How ambitious you would decide"""
        # Ambitious you prioritizes growth and opportunity
        
        if "meeting" in prompt.lower():
            return {
                "choice": "Accept - could lead somewhere",
                "reasoning": "Every meeting is a potential opportunity",
                "confidence": 0.75,
                "risk_level": "medium"
            }
        elif "new project" in prompt.lower():
            return {
                "choice": "Jump in immediately",
                "reasoning": "First mover advantage. Learn by doing.",
                "confidence": 0.80,
                "risk_level": "high"
            }
        elif "opportunity" in prompt.lower():
            return {
                "choice": "Say yes now, figure out later",
                "reasoning": "Opportunities don't wait. Commit and adapt.",
                "confidence": 0.85,
                "risk_level": "high"
            }
        else:
            return {
                "choice": "Go for it",
                "reasoning": "Fortune favors the bold. Take the shot.",
                "confidence": 0.75,
                "risk_level": "high"
            }
    
    def _balanced_decision(self, prompt: str, context: Dict, persona: Dict) -> Dict:
        """How balanced you would decide"""
        # Balanced you weighs pros/cons and sets boundaries
        
        if "meeting" in prompt.lower():
            return {
                "choice": "Accept with time limit",
                "reasoning": "Valuable but set 30-min boundary to protect time",
                "confidence": 0.80,
                "risk_level": "low"
            }
        elif "new project" in prompt.lower():
            return {
                "choice": "Pilot first, then commit",
                "reasoning": "Test with small investment before going all-in",
                "confidence": 0.85,
                "risk_level": "medium"
            }
        elif "opportunity" in prompt.lower():
            return {
                "choice": "Negotiate terms",
                "reasoning": "Interested but need alignment with current goals",
                "confidence": 0.80,
                "risk_level": "medium"
            }
        else:
            return {
                "choice": "Evaluate trade-offs",
                "reasoning": "Consider both upside and downside before deciding",
                "confidence": 0.75,
                "risk_level": "medium"
            }
    
    def update_universe_scores(self, decision_id: int, outcomes: Dict):
        """Update scores based on decision outcomes"""
        for persona_key, outcome in outcomes.items():
            if outcome == "success":
                self.universes[persona_key]["score"] += 10
            elif outcome == "failure":
                self.universes[persona_key]["score"] -= 5
            elif outcome == "neutral":
                self.universes[persona_key]["score"] += 2
    
    def get_daily_comparison(self) -> Dict:
        """Get comparison of how each version performed today"""
        return {
            "decisions_made": len(self.current_day_decisions),
            "universes": {
                key: {
                    "persona": self.PERSONAS[key]["name"],
                    "emoji": self.PERSONAS[key]["emoji"],
                    "score": universe["score"],
                    "state": universe["state"],
                    "decisions": len(universe["decisions"])
                }
                for key, universe in self.universes.items()
            },
            "leader": max(self.universes.items(), key=lambda x: x[1]["score"])[0],
            "recommendation": self._get_recommendation()
        }
    
    def _get_recommendation(self) -> str:
        """Recommend which version to follow"""
        scores = {k: v["score"] for k, v in self.universes.items()}
        leader = max(scores, key=scores.get)
        
        persona = self.PERSONAS[leader]
        
        return f"{persona['emoji']} {persona['name']} is winning today. Consider being more {persona['traits'][0]}."
    
    def get_live_view(self) -> str:
        """Get live split-screen view of all three versions"""
        view = "\n🌌 PARALLEL UNIVERSE VIEWER - LIVE\n\n"
        
        for key, universe in self.universes.items():
            persona = self.PERSONAS[key]
            view += f"{persona['emoji']} {persona['name']}\n"
            view += f"Score: {universe['score']} | State: {universe['state']}\n"
            view += f"Style: {persona['decision_style']}\n"
            
            if universe["decisions"]:
                last = universe["decisions"][-1]
                view += f"Last choice: {last['choice']}\n"
            
            view += "\n"
        
        leader = max(self.universes.items(), key=lambda x: x[1]["score"])[0]
        view += f"🏆 Current Leader: {self.PERSONAS[leader]['name']}\n"
        
        return view
    
    def switch_timeline(self, target_persona: str):
        """Switch to following a different persona's decisions"""
        if target_persona in self.PERSONAS:
            return {
                "switched_to": self.PERSONAS[target_persona]["name"],
                "new_style": self.PERSONAS[target_persona]["decision_style"],
                "message": f"You're now following {self.PERSONAS[target_persona]['name']}'s decision style"
            }

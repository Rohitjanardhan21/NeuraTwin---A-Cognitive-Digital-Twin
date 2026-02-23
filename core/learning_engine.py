"""
🧠 LEARNING ENGINE
Makes the twin learn from interactions and become more intelligent over time
"""

import json
import os
from datetime import datetime, timedelta
from collections import defaultdict
import random


class LearningEngine:
    """Learns from user behavior and adapts responses"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.profile_file = f"{data_dir}/user_profile.json"
        self.interactions_file = f"{data_dir}/interactions.json"
        self.insights_file = f"{data_dir}/insights.json"
        
        self.profile = self._load_profile()
        self.interactions = self._load_interactions()
        self.insights = self._load_insights()
    
    def _load_profile(self):
        """Load user profile"""
        if os.path.exists(self.profile_file):
            with open(self.profile_file, 'r') as f:
                return json.load(f)
        
        return {
            "name": "User",
            "preferences": {},
            "patterns": {},
            "personality_traits": {},
            "work_style": {},
            "decision_style": {},
            "energy_patterns": {},
            "stress_triggers": [],
            "flow_triggers": [],
            "best_times": {},
            "learned_facts": [],
            "relationship_level": 0  # How well the twin knows you
        }
    
    def _load_interactions(self):
        """Load interaction history"""
        if os.path.exists(self.interactions_file):
            with open(self.interactions_file, 'r') as f:
                return json.load(f)
        return []
    
    def _load_insights(self):
        """Load generated insights"""
        if os.path.exists(self.insights_file):
            with open(self.insights_file, 'r') as f:
                return json.load(f)
        return []
    
    def _save_profile(self):
        """Save user profile"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.profile_file, 'w') as f:
            json.dump(self.profile, f, indent=2)
    
    def _save_interactions(self):
        """Save interactions"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.interactions_file, 'w') as f:
            json.dump(self.interactions[-1000:], f, indent=2)  # Keep last 1000
    
    def _save_insights(self):
        """Save insights"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.insights_file, 'w') as f:
            json.dump(self.insights[-100:], f, indent=2)  # Keep last 100
    
    def learn_from_interaction(self, interaction_type, data):
        """Learn from user interaction"""
        interaction = {
            "type": interaction_type,
            "data": data,
            "timestamp": datetime.now().isoformat(),
            "hour": datetime.now().hour,
            "day_of_week": datetime.now().strftime("%A")
        }
        
        self.interactions.append(interaction)
        self._save_interactions()
        
        # Update profile based on interaction
        self._update_profile(interaction)
        
        # Increase relationship level
        self.profile["relationship_level"] = min(100, self.profile["relationship_level"] + 0.1)
        self._save_profile()
    
    def _update_profile(self, interaction):
        """Update profile based on interaction"""
        itype = interaction["type"]
        data = interaction["data"]
        hour = interaction["hour"]
        
        # Learn energy patterns
        if itype == "state_check":
            energy = data.get("energy_level", 50)
            if hour not in self.profile["energy_patterns"]:
                self.profile["energy_patterns"][str(hour)] = []
            self.profile["energy_patterns"][str(hour)].append(energy)
            
            # Keep only last 30 readings per hour
            self.profile["energy_patterns"][str(hour)] = \
                self.profile["energy_patterns"][str(hour)][-30:]
        
        # Learn decision patterns
        elif itype == "decision":
            decision = data.get("decision", "")
            choice = data.get("choice", "")
            
            # Track decision keywords
            keywords = decision.lower().split()
            for word in keywords:
                if len(word) > 4:  # Meaningful words
                    if word not in self.profile["decision_style"]:
                        self.profile["decision_style"][word] = 0
                    self.profile["decision_style"][word] += 1
        
        # Learn flow patterns
        elif itype == "flow_start":
            time_of_day = "morning" if hour < 12 else "afternoon" if hour < 17 else "evening"
            if time_of_day not in self.profile["flow_triggers"]:
                self.profile["flow_triggers"].append(time_of_day)
        
        self._save_profile()
    
    def generate_insight(self):
        """Generate a new insight about the user"""
        if len(self.interactions) < 10:
            return None
        
        insights = []
        
        # Energy pattern insights
        if self.profile["energy_patterns"]:
            avg_by_hour = {}
            for hour, readings in self.profile["energy_patterns"].items():
                avg_by_hour[int(hour)] = sum(readings) / len(readings)
            
            if avg_by_hour:
                best_hour = max(avg_by_hour, key=avg_by_hour.get)
                worst_hour = min(avg_by_hour, key=avg_by_hour.get)
                
                insights.append({
                    "type": "energy_pattern",
                    "message": f"You're most energetic around {best_hour}:00 and least energetic around {worst_hour}:00",
                    "actionable": f"Schedule important work around {best_hour}:00",
                    "confidence": min(100, len(self.interactions) / 10)
                })
        
        # Decision pattern insights
        if self.profile["decision_style"]:
            top_words = sorted(self.profile["decision_style"].items(), 
                             key=lambda x: x[1], reverse=True)[:3]
            
            if top_words:
                words = ", ".join([w[0] for w in top_words])
                insights.append({
                    "type": "decision_pattern",
                    "message": f"Your decisions often involve: {words}",
                    "actionable": "You tend to focus on these areas consistently",
                    "confidence": min(100, len(self.interactions) / 5)
                })
        
        # Relationship insight
        level = self.profile["relationship_level"]
        if level > 20 and level < 25:
            insights.append({
                "type": "relationship",
                "message": "I'm starting to understand your patterns",
                "actionable": "Keep using me daily for better insights",
                "confidence": level
            })
        elif level > 50 and level < 55:
            insights.append({
                "type": "relationship",
                "message": "I know you pretty well now",
                "actionable": "My predictions should be quite accurate",
                "confidence": level
            })
        
        if insights:
            insight = random.choice(insights)
            insight["timestamp"] = datetime.now().isoformat()
            insight["id"] = len(self.insights)
            
            self.insights.append(insight)
            self._save_insights()
            
            return insight
        
        return None
    
    def get_personalized_greeting(self):
        """Get personalized greeting based on learning"""
        hour = datetime.now().hour
        level = self.profile["relationship_level"]
        
        # Base greeting
        if hour < 12:
            base = "Good morning"
        elif hour < 17:
            base = "Good afternoon"
        else:
            base = "Good evening"
        
        # Personalization based on relationship level
        if level < 10:
            return f"{base}! I'm learning about you..."
        elif level < 30:
            return f"{base}! I'm starting to understand your patterns."
        elif level < 60:
            return f"{base}! I know you pretty well now."
        else:
            return f"{base}! I know you like the back of my hand."
    
    def get_smart_recommendation(self, current_state):
        """Get smart recommendation based on learned patterns"""
        hour = datetime.now().hour
        energy = current_state.get("energy_level", 50)
        stress = current_state.get("stress_level", 50)
        
        # Check learned energy patterns
        if str(hour) in self.profile["energy_patterns"]:
            typical_energy = sum(self.profile["energy_patterns"][str(hour)]) / \
                           len(self.profile["energy_patterns"][str(hour)])
            
            if energy < typical_energy - 20:
                return f"Your energy is unusually low for {hour}:00. Something's off today."
            elif energy > typical_energy + 20:
                return f"You're more energetic than usual! Great time for challenging work."
        
        # Default recommendations
        if energy < 30:
            return "Energy critically low. Take a break or rest."
        elif stress > 70:
            return "High stress detected. Consider a short walk or breathing exercise."
        elif energy > 70 and stress < 30:
            return "Perfect state for deep work. Start your flow session!"
        else:
            return "You're doing okay. Stay consistent."
    
    def predict_next_state(self, current_hour):
        """Predict state for next hour based on patterns"""
        next_hour = (current_hour + 1) % 24
        
        if str(next_hour) in self.profile["energy_patterns"]:
            readings = self.profile["energy_patterns"][str(next_hour)]
            predicted_energy = sum(readings) / len(readings)
            
            return {
                "hour": next_hour,
                "predicted_energy": round(predicted_energy),
                "confidence": min(100, len(readings) * 5),
                "message": f"At {next_hour}:00, your energy will likely be around {round(predicted_energy)}%"
            }
        
        return {
            "hour": next_hour,
            "predicted_energy": 50,
            "confidence": 0,
            "message": "Not enough data to predict next hour"
        }
    
    def get_recent_insights(self, limit=5):
        """Get recent insights"""
        return self.insights[-limit:]
    
    def get_profile_summary(self):
        """Get profile summary"""
        return {
            "relationship_level": self.profile["relationship_level"],
            "total_interactions": len(self.interactions),
            "insights_generated": len(self.insights),
            "patterns_learned": {
                "energy_hours": len(self.profile["energy_patterns"]),
                "decision_keywords": len(self.profile["decision_style"]),
                "flow_triggers": len(self.profile["flow_triggers"])
            }
        }

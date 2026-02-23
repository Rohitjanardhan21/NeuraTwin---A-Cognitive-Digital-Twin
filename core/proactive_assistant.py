"""
🎯 PROACTIVE ASSISTANT
Makes the twin anticipate needs and act proactively like JARVIS
"""

import random
from datetime import datetime, timedelta


class ProactiveAssistant:
    """Proactively suggests actions and insights"""
    
    def __init__(self):
        self.last_suggestion_time = None
        self.suggestion_cooldown = 300  # 5 minutes
        self.last_check_in = None
    
    def should_suggest(self):
        """Check if it's time for a proactive suggestion"""
        if not self.last_suggestion_time:
            return True
        
        elapsed = (datetime.now() - self.last_suggestion_time).total_seconds()
        return elapsed > self.suggestion_cooldown
    
    def get_proactive_suggestions(self, current_state, user_profile, time_of_day):
        """Generate proactive suggestions based on context"""
        suggestions = []
        
        energy = current_state.get('energy_level', 50)
        stress = current_state.get('stress_level', 50)
        decision_quality = current_state.get('decision_quality', 50)
        hour = datetime.now().hour
        
        # Energy-based suggestions
        if energy < 30 and hour < 22:
            suggestions.append({
                "type": "energy_critical",
                "priority": "high",
                "title": "⚡ ENERGY CRITICAL",
                "message": "Sir, your energy levels are dangerously low. I recommend a 15-minute break immediately.",
                "action": "take_break",
                "tone": "urgent"
            })
        
        elif energy < 50 and hour > 14 and hour < 16:
            suggestions.append({
                "type": "afternoon_slump",
                "priority": "medium",
                "title": "☕ AFTERNOON SLUMP DETECTED",
                "message": "The post-lunch dip is hitting. A short walk or coffee might help, sir.",
                "action": "suggest_coffee",
                "tone": "helpful"
            })
        
        # Stress-based suggestions
        if stress > 70:
            suggestions.append({
                "type": "stress_high",
                "priority": "high",
                "title": "🧘 STRESS LEVELS ELEVATED",
                "message": "I'm detecting elevated stress. May I suggest a 5-minute breathing exercise?",
                "action": "breathing_exercise",
                "tone": "concerned"
            })
        
        # Decision quality warnings
        if decision_quality < 40:
            suggestions.append({
                "type": "decision_warning",
                "priority": "high",
                "title": "⚠️ DECISION QUALITY LOW",
                "message": "Your decision-making capacity is compromised. I'd advise postponing important choices.",
                "action": "defer_decisions",
                "tone": "advisory"
            })
        
        # Flow state opportunities
        if energy > 70 and stress < 30 and hour >= 9 and hour <= 11:
            suggestions.append({
                "type": "flow_opportunity",
                "priority": "medium",
                "title": "🎯 OPTIMAL FLOW WINDOW",
                "message": "Conditions are ideal for deep work, sir. Shall I activate flow state protection?",
                "action": "start_flow",
                "tone": "opportunistic"
            })
        
        # Pattern-based suggestions
        if user_profile.get('energy_patterns'):
            predicted_low = self._predict_energy_drop(user_profile, hour)
            if predicted_low:
                suggestions.append({
                    "type": "predictive",
                    "priority": "low",
                    "title": "🔮 ENERGY DROP PREDICTED",
                    "message": f"Based on your patterns, energy will drop around {predicted_low}:00. Plan accordingly.",
                    "action": "plan_ahead",
                    "tone": "informative"
                })
        
        # Time-based check-ins
        if not self.last_check_in or (datetime.now() - self.last_check_in).total_seconds() > 14400:  # 4 hours
            suggestions.append({
                "type": "check_in",
                "priority": "low",
                "title": "👋 CHECK-IN",
                "message": "It's been a while, sir. How are things progressing?",
                "action": "check_in",
                "tone": "friendly"
            })
            self.last_check_in = datetime.now()
        
        # Morning briefing
        if hour >= 8 and hour <= 9 and not self._briefing_given_today():
            suggestions.append({
                "type": "morning_briefing",
                "priority": "medium",
                "title": "☀️ MORNING BRIEFING",
                "message": "Good morning, sir. Your energy is optimal. I've prepared your daily briefing.",
                "action": "show_briefing",
                "tone": "professional"
            })
        
        # Evening wrap-up
        if hour >= 18 and hour <= 19 and not self._wrapup_given_today():
            suggestions.append({
                "type": "evening_wrapup",
                "priority": "low",
                "title": "🌙 EVENING WRAP-UP",
                "message": "Shall I prepare your daily summary and insights, sir?",
                "action": "show_summary",
                "tone": "professional"
            })
        
        # Relationship milestones
        relationship = user_profile.get('relationship_level', 0)
        if 24.5 < relationship < 25.5:
            suggestions.append({
                "type": "milestone",
                "priority": "low",
                "title": "🎉 MILESTONE REACHED",
                "message": "I'm now 25% calibrated to your patterns. My predictions will improve significantly.",
                "action": "celebrate",
                "tone": "proud"
            })
        
        # Sort by priority
        priority_order = {"high": 0, "medium": 1, "low": 2}
        suggestions.sort(key=lambda x: priority_order.get(x["priority"], 3))
        
        if suggestions:
            self.last_suggestion_time = datetime.now()
        
        return suggestions[:3]  # Return top 3
    
    def _predict_energy_drop(self, user_profile, current_hour):
        """Predict when energy will drop"""
        patterns = user_profile.get('energy_patterns', {})
        
        for hour in range(current_hour + 1, min(current_hour + 4, 24)):
            if str(hour) in patterns:
                readings = patterns[str(hour)]
                avg = sum(readings) / len(readings)
                if avg < 40:
                    return hour
        
        return None
    
    def _briefing_given_today(self):
        """Check if morning briefing was given today"""
        # Simple check - in production, store this in a file
        return False
    
    def _wrapup_given_today(self):
        """Check if evening wrap-up was given today"""
        return False
    
    def generate_ambient_commentary(self, current_state, context):
        """Generate ambient JARVIS-style commentary"""
        energy = current_state.get('energy_level', 50)
        stress = current_state.get('stress_level', 50)
        hour = datetime.now().hour
        
        commentaries = []
        
        # Energy observations
        if energy > 80:
            commentaries.extend([
                "You're operating at peak capacity, sir.",
                "Energy levels are excellent. Perfect time for challenging work.",
                "Your cognitive performance is optimal."
            ])
        elif energy < 25:
            commentaries.extend([
                "Energy reserves are critically low, sir.",
                "I'm detecting significant fatigue. Rest is advised.",
                "Your system is running on fumes."
            ])
        
        # Stress observations
        if stress > 75:
            commentaries.extend([
                "Stress indicators are elevated. May I suggest a brief respite?",
                "Your cortisol levels appear high. A moment of calm would help.",
                "I'm detecting tension. Perhaps a short break?"
            ])
        
        # Time-based observations
        if hour >= 23 or hour <= 5:
            commentaries.extend([
                "It's quite late, sir. Sleep would be beneficial.",
                "Burning the midnight oil again, I see.",
                "Your circadian rhythm would appreciate some rest."
            ])
        
        # Pattern-based observations
        if context.get('emotion') == 'frustrated':
            commentaries.extend([
                "I sense frustration. Sometimes stepping away provides clarity.",
                "Persistence is admirable, but so is strategic retreat.",
                "Perhaps a different approach would yield better results?"
            ])
        
        if commentaries:
            return random.choice(commentaries)
        
        return None
    
    def get_contextual_greeting(self, user_profile, current_state):
        """Get contextual greeting like JARVIS"""
        hour = datetime.now().hour
        relationship = user_profile.get('relationship_level', 0)
        energy = current_state.get('energy_level', 50)
        
        # Time-based
        if hour < 12:
            time_greeting = "Good morning"
        elif hour < 17:
            time_greeting = "Good afternoon"
        elif hour < 22:
            time_greeting = "Good evening"
        else:
            time_greeting = "Working late"
        
        # Relationship-based suffix
        if relationship < 10:
            suffix = "I'm still learning your patterns."
        elif relationship < 30:
            suffix = "I'm beginning to understand you."
        elif relationship < 60:
            suffix = "I know you quite well now."
        else:
            suffix = "I know you like the back of my hand."
        
        # Energy-based observation
        if energy > 75:
            energy_note = "You're in excellent form."
        elif energy < 30:
            energy_note = "You seem fatigued."
        else:
            energy_note = "You're doing reasonably well."
        
        return f"{time_greeting}, sir. {energy_note} {suffix}"

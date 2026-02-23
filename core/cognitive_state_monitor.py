"""
🧠 REAL-TIME COGNITIVE STATE MONITOR
Tracks and displays your mental state in real-time
"""

import time
from datetime import datetime, timedelta
from typing import Dict, List
from collections import deque
import random


class CognitiveStateMonitor:
    """Monitor and predict cognitive state in real-time"""
    
    def __init__(self):
        self.activity_buffer = deque(maxlen=100)  # Last 100 activities
        self.focus_sessions = []
        self.current_state = "idle"
        self.energy_level = 100
        self.stress_level = 0
        self.decision_quality = 100
        self.flow_state_score = 0
        self.last_break = datetime.now()
        self.session_start = None
        
    def log_activity(self, activity_type: str, duration: int = 1):
        """Log an activity (typing, clicking, switching, etc.)"""
        self.activity_buffer.append({
            "type": activity_type,
            "timestamp": datetime.now(),
            "duration": duration
        })
        self._update_state()
    
    def _update_state(self):
        """Update cognitive state based on recent activity"""
        if len(self.activity_buffer) < 10:
            return
        
        recent = list(self.activity_buffer)[-20:]
        
        # Detect flow state
        focus_activities = [a for a in recent if a["type"] in ["typing", "reading", "coding"]]
        switches = [a for a in recent if a["type"] == "switch"]
        
        if len(focus_activities) > 15 and len(switches) < 2:
            self.current_state = "flow"
            self.flow_state_score = min(100, self.flow_state_score + 5)
        elif len(switches) > 8:
            self.current_state = "distracted"
            self.flow_state_score = max(0, self.flow_state_score - 10)
            self.stress_level = min(100, self.stress_level + 5)
        else:
            self.current_state = "working"
            self.flow_state_score = max(0, self.flow_state_score - 2)
        
        # Update energy based on time since break
        time_since_break = (datetime.now() - self.last_break).seconds / 60
        if time_since_break > 90:
            self.energy_level = max(20, self.energy_level - 1)
            self.decision_quality = max(30, self.decision_quality - 1)
        
        # Update decision quality based on state
        if self.current_state == "flow":
            self.decision_quality = min(100, self.decision_quality + 2)
        elif self.current_state == "distracted":
            self.decision_quality = max(30, self.decision_quality - 3)
    
    def get_current_state(self) -> Dict:
        """Get current cognitive state"""
        return {
            "state": self.current_state,
            "energy_level": self.energy_level,
            "stress_level": self.stress_level,
            "decision_quality": self.decision_quality,
            "flow_state_score": self.flow_state_score,
            "time_since_break": (datetime.now() - self.last_break).seconds // 60,
            "recommendation": self._get_recommendation()
        }
    
    def _get_recommendation(self) -> str:
        """Get recommendation based on current state"""
        if self.energy_level < 40:
            return "⚠️ Energy low. Take a break."
        elif self.stress_level > 70:
            return "🚨 Stress high. Step away for 5 minutes."
        elif self.flow_state_score > 70:
            return "🔥 Flow state! Keep going."
        elif self.decision_quality < 50:
            return "⏸️ Decision quality low. Defer important choices."
        elif self.current_state == "distracted":
            return "🎯 Too many switches. Focus on one thing."
        else:
            return "✅ Good state. Keep working."
    
    def take_break(self):
        """Log a break"""
        self.last_break = datetime.now()
        self.energy_level = min(100, self.energy_level + 20)
        self.stress_level = max(0, self.stress_level - 15)
        self.decision_quality = min(100, self.decision_quality + 10)
    
    def start_focus_session(self):
        """Start a focus session"""
        self.session_start = datetime.now()
        self.current_state = "focusing"
    
    def end_focus_session(self):
        """End focus session and record it"""
        if self.session_start:
            duration = (datetime.now() - self.session_start).seconds // 60
            self.focus_sessions.append({
                "start": self.session_start,
                "duration": duration,
                "quality": self.flow_state_score
            })
            self.session_start = None
            return duration
        return 0
    
    def get_daily_stats(self) -> Dict:
        """Get daily statistics"""
        today_sessions = [s for s in self.focus_sessions 
                         if s["start"].date() == datetime.now().date()]
        
        total_focus_time = sum(s["duration"] for s in today_sessions)
        avg_quality = sum(s["quality"] for s in today_sessions) / len(today_sessions) if today_sessions else 0
        
        return {
            "total_focus_time": total_focus_time,
            "focus_sessions": len(today_sessions),
            "avg_quality": avg_quality,
            "current_energy": self.energy_level,
            "current_stress": self.stress_level
        }
    
    def predict_next_hour(self) -> Dict:
        """Predict state for next hour"""
        # Simple prediction based on current trajectory
        predicted_energy = max(20, self.energy_level - 10)
        predicted_stress = min(100, self.stress_level + 5)
        
        if datetime.now().hour >= 14 and datetime.now().hour <= 16:
            predicted_energy -= 15  # Afternoon slump
        
        return {
            "predicted_energy": predicted_energy,
            "predicted_stress": predicted_stress,
            "recommendation": "Schedule important work before energy drops" if predicted_energy < 50 else "Good time for challenging tasks"
        }

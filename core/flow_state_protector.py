"""
🛡️ FLOW STATE PROTECTOR
Detects and protects your flow state from interruptions
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional


class FlowStateProtector:
    """Detect and protect flow state"""
    
    def __init__(self):
        self.flow_active = False
        self.flow_start_time = None
        self.flow_duration = 0
        self.interruptions_blocked = 0
        self.flow_sessions = []
        self.protection_level = "medium"  # low, medium, high, extreme
        
    def detect_flow_state(self, activity_data: List[Dict]) -> bool:
        """Detect if user is in flow state"""
        if len(activity_data) < 10:
            return False
        
        recent = activity_data[-20:]
        
        # Flow indicators
        focus_activities = sum(1 for a in recent if a["type"] in ["typing", "reading", "coding"])
        switches = sum(1 for a in recent if a["type"] == "switch")
        pauses = sum(1 for a in recent if a["type"] == "pause")
        
        # Flow state criteria
        is_flow = (
            focus_activities > 15 and
            switches < 2 and
            pauses < 3
        )
        
        if is_flow and not self.flow_active:
            self.enter_flow_state()
        elif not is_flow and self.flow_active:
            self.exit_flow_state()
        
        return self.flow_active
    
    def enter_flow_state(self):
        """Enter flow state and activate protection"""
        self.flow_active = True
        self.flow_start_time = datetime.now()
        self.interruptions_blocked = 0
        print("\n🔥 FLOW STATE DETECTED - Protection activated")
        print("🛡️ Blocking all interruptions")
    
    def exit_flow_state(self):
        """Exit flow state"""
        if self.flow_active and self.flow_start_time:
            duration = (datetime.now() - self.flow_start_time).seconds // 60
            self.flow_duration = duration
            
            self.flow_sessions.append({
                "start": self.flow_start_time,
                "duration": duration,
                "interruptions_blocked": self.interruptions_blocked
            })
            
            print(f"\n✅ Flow session ended: {duration} minutes")
            print(f"🛡️ Blocked {self.interruptions_blocked} interruptions")
            
            self.flow_active = False
            self.flow_start_time = None
    
    def should_block_interruption(self, interruption_type: str, priority: str) -> Dict:
        """Decide if interruption should be blocked"""
        if not self.flow_active:
            return {"block": False, "reason": "Not in flow state"}
        
        # Always block based on protection level
        if self.protection_level == "extreme":
            self.interruptions_blocked += 1
            return {
                "block": True,
                "reason": "EXTREME protection - blocking everything",
                "message": "🛡️ In flow state. All interruptions blocked."
            }
        
        if self.protection_level == "high":
            if priority != "critical":
                self.interruptions_blocked += 1
                return {
                    "block": True,
                    "reason": "HIGH protection - only critical allowed",
                    "message": f"🛡️ Flow state active. {interruption_type} blocked."
                }
        
        if self.protection_level == "medium":
            if priority in ["low", "medium"]:
                self.interruptions_blocked += 1
                return {
                    "block": True,
                    "reason": "MEDIUM protection - blocking low/medium priority",
                    "message": f"🛡️ Flow state. {interruption_type} deferred."
                }
        
        # Low protection - only block low priority
        if priority == "low":
            self.interruptions_blocked += 1
            return {
                "block": True,
                "reason": "LOW protection - blocking low priority only",
                "message": f"🛡️ {interruption_type} queued for later."
            }
        
        return {"block": False, "reason": "Priority overrides protection"}
    
    def get_flow_stats(self) -> Dict:
        """Get flow state statistics"""
        today_sessions = [
            s for s in self.flow_sessions
            if s["start"].date() == datetime.now().date()
        ]
        
        total_flow_time = sum(s["duration"] for s in today_sessions)
        total_blocked = sum(s["interruptions_blocked"] for s in today_sessions)
        
        return {
            "currently_in_flow": self.flow_active,
            "current_duration": (datetime.now() - self.flow_start_time).seconds // 60 if self.flow_active else 0,
            "today_flow_time": total_flow_time,
            "today_sessions": len(today_sessions),
            "interruptions_blocked_today": total_blocked,
            "protection_level": self.protection_level
        }
    
    def set_protection_level(self, level: str):
        """Set protection level"""
        if level in ["low", "medium", "high", "extreme"]:
            self.protection_level = level
            return f"Protection level set to {level.upper()}"
        return "Invalid level"
    
    def predict_flow_opportunity(self, schedule: List[Dict]) -> Optional[Dict]:
        """Predict when flow state is possible"""
        now = datetime.now()
        
        # Look for blocks of free time
        for i in range(len(schedule) - 1):
            current = schedule[i]
            next_item = schedule[i + 1]
            
            gap = (next_item["start"] - current["end"]).seconds // 60
            
            if gap >= 90:  # 90+ minutes free
                return {
                    "opportunity": True,
                    "start": current["end"],
                    "duration": gap,
                    "message": f"🎯 Flow opportunity: {gap} minutes free starting at {current['end'].strftime('%I:%M %p')}"
                }
        
        return None

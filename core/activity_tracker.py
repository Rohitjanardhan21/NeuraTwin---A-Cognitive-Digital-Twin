"""
🖥️ REAL DESKTOP ACTIVITY TRACKER
Tracks actual computer usage - no more simulation!
"""

import psutil
import time
from datetime import datetime
from collections import deque
import threading
import json
import os

try:
    from pynput import keyboard, mouse
    PYNPUT_AVAILABLE = True
except ImportError:
    PYNPUT_AVAILABLE = False
    print("⚠️ pynput not installed. Run: pip install pynput")


class ActivityTracker:
    """Track real desktop activity"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.activity_file = f"{data_dir}/activity_log.json"
        
        # Activity buffers
        self.keyboard_events = deque(maxlen=1000)
        self.mouse_events = deque(maxlen=1000)
        self.app_switches = deque(maxlen=100)
        
        # Current state
        self.current_app = None
        self.last_activity = datetime.now()
        self.idle_threshold = 300  # 5 minutes
        
        # Tracking state
        self.is_tracking = False
        self.tracking_thread = None
        
        # Statistics
        self.stats = {
            "total_keystrokes": 0,
            "total_mouse_clicks": 0,
            "total_app_switches": 0,
            "active_time": 0,
            "idle_time": 0,
            "apps_used": {},
            "hourly_activity": {}
        }
        
        self._load_stats()
    
    def _load_stats(self):
        """Load saved statistics"""
        if os.path.exists(self.activity_file):
            try:
                with open(self.activity_file, 'r') as f:
                    self.stats = json.load(f)
            except:
                pass
    
    def _save_stats(self):
        """Save statistics"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.activity_file, 'w') as f:
            json.dump(self.stats, f, indent=2)
    
    def start_tracking(self):
        """Start tracking activity"""
        if not PYNPUT_AVAILABLE:
            print("❌ Cannot start tracking: pynput not installed")
            return False
        
        if self.is_tracking:
            return True
        
        self.is_tracking = True
        
        # Start keyboard listener
        self.keyboard_listener = keyboard.Listener(
            on_press=self._on_key_press
        )
        self.keyboard_listener.start()
        
        # Start mouse listener
        self.mouse_listener = mouse.Listener(
            on_click=self._on_mouse_click,
            on_move=self._on_mouse_move
        )
        self.mouse_listener.start()
        
        # Start app monitoring thread
        self.tracking_thread = threading.Thread(target=self._monitor_apps, daemon=True)
        self.tracking_thread.start()
        
        print("✅ Activity tracking started")
        return True
    
    def stop_tracking(self):
        """Stop tracking activity"""
        self.is_tracking = False
        
        if hasattr(self, 'keyboard_listener'):
            self.keyboard_listener.stop()
        
        if hasattr(self, 'mouse_listener'):
            self.mouse_listener.stop()
        
        self._save_stats()
        print("⏹️ Activity tracking stopped")
    
    def _on_key_press(self, key):
        """Handle keyboard press"""
        if not self.is_tracking:
            return
        
        now = datetime.now()
        self.keyboard_events.append({
            "type": "keypress",
            "timestamp": now.isoformat(),
            "hour": now.hour
        })
        
        self.stats["total_keystrokes"] += 1
        self.last_activity = now
        
        # Update hourly stats
        hour_key = str(now.hour)
        if hour_key not in self.stats["hourly_activity"]:
            self.stats["hourly_activity"][hour_key] = {
                "keystrokes": 0,
                "clicks": 0,
                "active_minutes": 0
            }
        self.stats["hourly_activity"][hour_key]["keystrokes"] += 1
    
    def _on_mouse_click(self, x, y, button, pressed):
        """Handle mouse click"""
        if not self.is_tracking or not pressed:
            return
        
        now = datetime.now()
        self.mouse_events.append({
            "type": "click",
            "timestamp": now.isoformat(),
            "hour": now.hour
        })
        
        self.stats["total_mouse_clicks"] += 1
        self.last_activity = now
        
        # Update hourly stats
        hour_key = str(now.hour)
        if hour_key not in self.stats["hourly_activity"]:
            self.stats["hourly_activity"][hour_key] = {
                "keystrokes": 0,
                "clicks": 0,
                "active_minutes": 0
            }
        self.stats["hourly_activity"][hour_key]["clicks"] += 1
    
    def _on_mouse_move(self, x, y):
        """Handle mouse movement"""
        if not self.is_tracking:
            return
        
        self.last_activity = datetime.now()
    
    def _monitor_apps(self):
        """Monitor active applications"""
        while self.is_tracking:
            try:
                # Get active window (platform-specific)
                active_app = self._get_active_app()
                
                if active_app and active_app != self.current_app:
                    now = datetime.now()
                    self.app_switches.append({
                        "from": self.current_app,
                        "to": active_app,
                        "timestamp": now.isoformat()
                    })
                    
                    self.current_app = active_app
                    self.stats["total_app_switches"] += 1
                    
                    # Track app usage
                    if active_app not in self.stats["apps_used"]:
                        self.stats["apps_used"][active_app] = 0
                    self.stats["apps_used"][active_app] += 1
                
                time.sleep(2)  # Check every 2 seconds
                
            except Exception as e:
                print(f"Error monitoring apps: {e}")
                time.sleep(5)
    
    def _get_active_app(self):
        """Get currently active application"""
        try:
            import platform
            system = platform.system()
            
            if system == "Windows":
                try:
                    import win32gui
                    import win32process
                    window = win32gui.GetForegroundWindow()
                    _, pid = win32process.GetWindowThreadProcessId(window)
                    process = psutil.Process(pid)
                    return process.name()
                except:
                    pass
            
            elif system == "Darwin":  # macOS
                try:
                    from AppKit import NSWorkspace
                    active_app = NSWorkspace.sharedWorkspace().activeApplication()
                    return active_app['NSApplicationName']
                except:
                    pass
            
            elif system == "Linux":
                try:
                    import subprocess
                    window_id = subprocess.check_output(['xdotool', 'getactivewindow']).decode().strip()
                    pid = subprocess.check_output(['xdotool', 'getwindowpid', window_id]).decode().strip()
                    process = psutil.Process(int(pid))
                    return process.name()
                except:
                    pass
            
        except Exception as e:
            pass
        
        return None
    
    def is_idle(self):
        """Check if user is idle"""
        idle_time = (datetime.now() - self.last_activity).total_seconds()
        return idle_time > self.idle_threshold
    
    def get_activity_level(self, minutes=5):
        """Get activity level for last N minutes"""
        now = datetime.now()
        cutoff = now.timestamp() - (minutes * 60)
        
        recent_keys = sum(1 for e in self.keyboard_events 
                         if datetime.fromisoformat(e["timestamp"]).timestamp() > cutoff)
        recent_clicks = sum(1 for e in self.mouse_events 
                           if datetime.fromisoformat(e["timestamp"]).timestamp() > cutoff)
        
        total_events = recent_keys + recent_clicks
        
        # Calculate activity level (0-100)
        # Assume 100 events per minute = 100% activity
        expected_events = minutes * 100
        activity_level = min(100, (total_events / expected_events) * 100)
        
        return {
            "level": round(activity_level),
            "keystrokes": recent_keys,
            "clicks": recent_clicks,
            "is_idle": self.is_idle(),
            "current_app": self.current_app
        }
    
    def get_focus_score(self, minutes=10):
        """Calculate focus score based on app switches"""
        now = datetime.now()
        cutoff = now.timestamp() - (minutes * 60)
        
        recent_switches = sum(1 for s in self.app_switches 
                             if datetime.fromisoformat(s["timestamp"]).timestamp() > cutoff)
        
        # Fewer switches = better focus
        # 0 switches = 100, 10+ switches = 0
        focus_score = max(0, 100 - (recent_switches * 10))
        
        return {
            "score": focus_score,
            "app_switches": recent_switches,
            "current_app": self.current_app,
            "state": "focused" if focus_score > 70 else "distracted" if focus_score < 40 else "working"
        }
    
    def get_hourly_patterns(self):
        """Get activity patterns by hour"""
        patterns = {}
        
        for hour, data in self.stats["hourly_activity"].items():
            total_activity = data["keystrokes"] + data["clicks"]
            patterns[int(hour)] = {
                "activity_level": min(100, total_activity / 10),  # Normalize
                "keystrokes": data["keystrokes"],
                "clicks": data["clicks"]
            }
        
        return patterns
    
    def get_top_apps(self, limit=5):
        """Get most used applications"""
        sorted_apps = sorted(
            self.stats["apps_used"].items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_apps[:limit]
    
    def get_stats_summary(self):
        """Get summary of all statistics"""
        return {
            "total_keystrokes": self.stats["total_keystrokes"],
            "total_clicks": self.stats["total_mouse_clicks"],
            "total_app_switches": self.stats["total_app_switches"],
            "apps_used": len(self.stats["apps_used"]),
            "top_apps": self.get_top_apps(5),
            "hourly_patterns": self.get_hourly_patterns(),
            "current_activity": self.get_activity_level(5),
            "current_focus": self.get_focus_score(10),
            "is_tracking": self.is_tracking
        }


# Global instance
_tracker = None

def get_tracker():
    """Get global tracker instance"""
    global _tracker
    if _tracker is None:
        _tracker = ActivityTracker()
    return _tracker

"""
🤖 COGNITIVE TWIN DAEMON
Runs in background, monitors you, and acts as virtual assistant
"""

import os
import sys
import time
import json
import threading
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.cognitive_state_monitor import CognitiveStateMonitor
from core.parallel_universe_viewer import ParallelUniverseViewer
from core.decision_intervention import DecisionInterventionSystem
from core.regret_predictor import RegretPredictor
from core.flow_state_protector import FlowStateProtector
from core.decision_tracker import DecisionTracker
from core.pattern_analyzer import PatternAnalyzer


class CognitiveTwinDaemon:
    """Background daemon that monitors and assists"""
    
    def __init__(self, data_dir="data"):
        self.running = False
        self.data_dir = data_dir
        
        # Initialize all systems
        self.state_monitor = CognitiveStateMonitor()
        self.universe_viewer = ParallelUniverseViewer()
        self.decision_tracker = DecisionTracker(data_dir)
        self.pattern_analyzer = PatternAnalyzer(data_dir)
        self.intervention_system = DecisionInterventionSystem(
            self.decision_tracker,
            self.pattern_analyzer
        )
        self.regret_predictor = RegretPredictor(self.decision_tracker)
        self.flow_protector = FlowStateProtector()
        
        # State
        self.last_activity = datetime.now()
        self.current_session = None
        self.alerts = []
        
        # Create status file
        self.status_file = os.path.join(data_dir, "daemon_status.json")
        
    def start(self):
        """Start the daemon"""
        self.running = True
        print("🤖 Cognitive Twin Daemon starting...")
        print("📊 Monitoring your cognitive state...")
        print("🛡️ Protection systems active")
        print("\nPress Ctrl+C to stop\n")
        
        # Start monitoring threads
        threads = [
            threading.Thread(target=self._monitor_loop, daemon=True),
            threading.Thread(target=self._analysis_loop, daemon=True),
            threading.Thread(target=self._alert_loop, daemon=True)
        ]
        
        for thread in threads:
            thread.start()
        
        # Keep main thread alive
        try:
            while self.running:
                self._update_status()
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the daemon"""
        print("\n\n🛑 Stopping Cognitive Twin Daemon...")
        self.running = False
        
        # Save final state
        self._save_session()
        print("✅ Session saved")
        print("👋 See you next time!\n")
    
    def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            # Simulate activity monitoring
            # In real version, this would monitor:
            # - Keyboard/mouse activity
            # - Window focus
            # - File system events
            
            current_time = datetime.now()
            
            # Detect idle
            if (current_time - self.last_activity).seconds > 300:  # 5 min idle
                if self.flow_protector.flow_active:
                    self.flow_protector.exit_flow_state()
                    self._add_alert("info", "Flow session ended (idle detected)")
            
            # Update state
            self.state_monitor._update_state()
            
            # Check for flow state
            if len(self.state_monitor.activity_buffer) > 10:
                self.flow_protector.detect_flow_state(
                    list(self.state_monitor.activity_buffer)
                )
            
            time.sleep(10)  # Check every 10 seconds
    
    def _analysis_loop(self):
        """Periodic analysis loop"""
        while self.running:
            # Every 5 minutes, analyze patterns
            time.sleep(300)
            
            if not self.running:
                break
            
            # Get current state
            state = self.state_monitor.get_current_state()
            
            # Check for warnings
            if state["energy_level"] < 40:
                self._add_alert("warning", "⚠️ Energy low. Take a break soon.")
            
            if state["stress_level"] > 70:
                self._add_alert("warning", "🚨 Stress high. Step away for 5 minutes.")
            
            if state["decision_quality"] < 50:
                self._add_alert("critical", "⏸️ Decision quality low. Defer important choices.")
    
    def _alert_loop(self):
        """Process and display alerts"""
        while self.running:
            if self.alerts:
                alert = self.alerts.pop(0)
                self._show_alert(alert)
            time.sleep(2)
    
    def _add_alert(self, level: str, message: str):
        """Add alert to queue"""
        self.alerts.append({
            "level": level,
            "message": message,
            "timestamp": datetime.now().isoformat()
        })
    
    def _show_alert(self, alert: dict):
        """Show alert to user"""
        icons = {
            "info": "ℹ️",
            "warning": "⚠️",
            "critical": "🚨"
        }
        icon = icons.get(alert["level"], "📢")
        print(f"\n{icon} {alert['message']}")
    
    def _update_status(self):
        """Update status file for API access"""
        status = {
            "running": self.running,
            "timestamp": datetime.now().isoformat(),
            "state": self.state_monitor.get_current_state(),
            "flow_stats": self.flow_protector.get_flow_stats(),
            "alerts": self.alerts[-5:],  # Last 5 alerts
            "daily_stats": self.state_monitor.get_daily_stats()
        }
        
        with open(self.status_file, 'w') as f:
            json.dump(status, f, indent=2)
    
    def _save_session(self):
        """Save current session"""
        if self.flow_protector.flow_active:
            self.flow_protector.exit_flow_state()
        
        # Save final state
        self._update_status()
    
    def log_activity(self, activity_type: str):
        """Log user activity (called by integrations)"""
        self.state_monitor.log_activity(activity_type)
        self.last_activity = datetime.now()
    
    def check_decision(self, decision: str, context: dict = None) -> dict:
        """Check a decision (called by integrations)"""
        if context is None:
            context = {
                "stress_level": self.state_monitor.stress_level,
                "energy_level": self.state_monitor.energy_level,
                "decision_quality": self.state_monitor.decision_quality,
                "decision": decision
            }
        
        # Get regret prediction
        regret = self.regret_predictor.predict_regret(decision, context)
        
        # Check intervention
        intervention = self.intervention_system.check_decision(decision, context)
        
        # Get parallel responses
        responses = self.universe_viewer.present_decision(decision, context)
        
        # Add alert if high regret
        if regret["percentage"] > 60:
            self._add_alert(
                "critical",
                f"🚨 High regret risk ({regret['percentage']}%) for: {decision[:50]}..."
            )
        
        return {
            "regret": regret,
            "intervention": intervention,
            "parallel_responses": responses
        }
    
    def get_morning_briefing(self) -> dict:
        """Get morning briefing"""
        state = self.state_monitor.get_current_state()
        prediction = self.state_monitor.predict_next_hour()
        
        return {
            "greeting": "☀️ Good morning!",
            "current_state": state,
            "prediction": prediction,
            "recommendations": [
                state["recommendation"],
                prediction["recommendation"]
            ]
        }
    
    def get_evening_summary(self) -> dict:
        """Get evening summary"""
        stats = self.state_monitor.get_daily_stats()
        comparison = self.universe_viewer.get_daily_comparison()
        
        return {
            "greeting": "🌙 Day complete!",
            "stats": stats,
            "universe_comparison": comparison,
            "insights": self._generate_insights()
        }
    
    def _generate_insights(self) -> list:
        """Generate daily insights"""
        insights = []
        
        stats = self.state_monitor.get_daily_stats()
        
        if stats["total_focus_time"] > 120:
            insights.append("💪 Great focus today! " + str(stats["total_focus_time"]) + " minutes of deep work.")
        
        if stats["current_stress"] > 70:
            insights.append("😰 High stress detected. Consider lighter day tomorrow.")
        
        return insights


def main():
    """Run daemon"""
    daemon = CognitiveTwinDaemon()
    daemon.start()


if __name__ == "__main__":
    main()

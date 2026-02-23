"""
🔥 LIVE COGNITIVE TWIN - Real-time monitoring and intervention
The outlandish but genuinely useful version
"""

import os
import time
from datetime import datetime
from typing import Dict
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text

from core.cognitive_state_monitor import CognitiveStateMonitor
from core.parallel_universe_viewer import ParallelUniverseViewer
from core.decision_intervention import DecisionInterventionSystem
from core.regret_predictor import RegretPredictor
from core.flow_state_protector import FlowStateProtector
from core.decision_tracker import DecisionTracker
from core.pattern_analyzer import PatternAnalyzer


class LiveCognitiveTwin:
    """Live monitoring cognitive twin"""
    
    def __init__(self):
        self.console = Console()
        self.state_monitor = CognitiveStateMonitor()
        self.universe_viewer = ParallelUniverseViewer()
        self.decision_tracker = DecisionTracker()
        self.pattern_analyzer = PatternAnalyzer()
        self.intervention_system = DecisionInterventionSystem(
            self.decision_tracker,
            self.pattern_analyzer
        )
        self.regret_predictor = RegretPredictor(self.decision_tracker)
        self.flow_protector = FlowStateProtector()
        
    def generate_live_dashboard(self) -> Layout:
        """Generate live dashboard layout"""
        layout = Layout()
        
        layout.split_column(
            Layout(name="header", size=3),
            Layout(name="main"),
            Layout(name="footer", size=3)
        )
        
        layout["main"].split_row(
            Layout(name="left"),
            Layout(name="right")
        )
        
        # Header
        layout["header"].update(
            Panel(
                Text("🧠 LIVE COGNITIVE TWIN - Real-Time Monitoring", justify="center", style="bold cyan"),
                style="cyan"
            )
        )
        
        # Left panel - Current state
        state = self.state_monitor.get_current_state()
        flow_stats = self.flow_protector.get_flow_stats()
        
        state_table = Table(title="🎯 Current State", show_header=False)
        state_table.add_column("Metric", style="cyan")
        state_table.add_column("Value", style="green")
        
        state_table.add_row("State", self._get_state_emoji(state["state"]) + " " + state["state"].upper())
        state_table.add_row("Energy", self._get_bar(state["energy_level"]))
        state_table.add_row("Stress", self._get_bar(state["stress_level"], reverse=True))
        state_table.add_row("Decision Quality", self._get_bar(state["decision_quality"]))
        state_table.add_row("Flow Score", self._get_bar(state["flow_state_score"]))
        state_table.add_row("Flow Active", "🔥 YES" if flow_stats["currently_in_flow"] else "❌ NO")
        
        layout["left"].update(Panel(state_table, border_style="green"))
        
        # Right panel - Parallel universes
        universe_text = self.universe_viewer.get_live_view()
        layout["right"].update(Panel(universe_text, title="🌌 Parallel Universes", border_style="magenta"))
        
        # Footer - Recommendation
        layout["footer"].update(
            Panel(
                Text(state["recommendation"], justify="center", style="bold yellow"),
                style="yellow"
            )
        )
        
        return layout
    
    def _get_state_emoji(self, state: str) -> str:
        """Get emoji for state"""
        emojis = {
            "flow": "🔥",
            "working": "💼",
            "distracted": "😵",
            "idle": "😴",
            "focusing": "🎯"
        }
        return emojis.get(state, "❓")
    
    def _get_bar(self, value: int, reverse: bool = False) -> str:
        """Generate progress bar"""
        filled = int(value / 10)
        empty = 10 - filled
        
        if reverse:
            if value > 70:
                color = "red"
            elif value > 40:
                color = "yellow"
            else:
                color = "green"
        else:
            if value > 70:
                color = "green"
            elif value > 40:
                color = "yellow"
            else:
                color = "red"
        
        bar = "█" * filled + "░" * empty
        return f"[{color}]{bar}[/{color}] {value}%"
    
    def check_decision(self, decision: str, context: Dict = None):
        """Check a decision with all systems"""
        if context is None:
            context = {
                "stress_level": self.state_monitor.stress_level,
                "energy_level": self.state_monitor.energy_level,
                "decision_quality": self.state_monitor.decision_quality,
                "time_thinking": 30,
                "decision": decision
            }
        
        self.console.print("\n" + "="*70)
        self.console.print(f"[bold cyan]DECISION CHECK:[/bold cyan] {decision}\n")
        
        # 1. Regret prediction
        regret = self.regret_predictor.predict_regret(decision, context)
        self.console.print(Panel(
            f"[bold]Regret Probability: {regret['percentage']}%[/bold]\n"
            f"Level: {regret['level']}\n\n"
            f"Factors:\n" + "\n".join(f"• {f}" for f in regret['factors']) + "\n\n"
            f"[yellow]{regret['recommendation']}[/yellow]",
            title="😱 Regret Predictor",
            border_style="red" if regret['percentage'] > 60 else "yellow"
        ))
        
        # 2. Intervention check
        intervention = self.intervention_system.check_decision(decision, context)
        if intervention["should_intervene"]:
            self.console.print(Panel(
                f"[bold red]⚠️ INTERVENTION TRIGGERED[/bold red]\n\n"
                f"{intervention['intervention']['message']}\n\n"
                f"Severity: {intervention['intervention']['severity'].upper()}\n"
                f"Suggested delay: {intervention['intervention']['delay_seconds']}s",
                title="⚡ Decision Intervention",
                border_style="red"
            ))
        else:
            self.console.print("[green]✅ No intervention needed[/green]\n")
        
        # 3. Parallel universe responses
        self.console.print("[bold]🌌 How your parallel selves would decide:[/bold]\n")
        responses = self.universe_viewer.present_decision(decision, context)
        
        for key, response in responses.items():
            persona = self.universe_viewer.PERSONAS[key]
            self.console.print(
                f"{persona['emoji']} [bold]{persona['name']}:[/bold] {response['choice']}\n"
                f"   Reasoning: {response['reasoning']}\n"
            )
        
        self.console.print("="*70 + "\n")
        
        return {
            "regret": regret,
            "intervention": intervention,
            "parallel_responses": responses
        }
    
    def simulate_work_session(self, duration_minutes: int = 5):
        """Simulate a work session with live updates"""
        self.console.print("\n[bold cyan]Starting live monitoring session...[/bold cyan]\n")
        
        activities = ["typing", "reading", "coding", "switch", "pause"]
        
        with Live(self.generate_live_dashboard(), refresh_per_second=1, console=self.console) as live:
            for i in range(duration_minutes * 6):  # 10-second intervals
                # Simulate activity
                activity = activities[i % len(activities)]
                self.state_monitor.log_activity(activity)
                
                # Check for flow state
                self.flow_protector.detect_flow_state(list(self.state_monitor.activity_buffer))
                
                # Update dashboard
                live.update(self.generate_live_dashboard())
                
                time.sleep(10)
    
    def demo_decision_flow(self):
        """Demo the decision checking flow"""
        self.console.print("\n[bold cyan]🎭 LIVE TWIN DEMO - Decision Flow[/bold cyan]\n")
        
        # Scenario 1: Late night decision
        self.console.print("[bold]Scenario 1: Late Night Decision[/bold]")
        self.check_decision(
            "Should I rewrite this entire module?",
            {
                "stress_level": 65,
                "energy_level": 45,
                "decision_quality": 50,
                "time_thinking": 30,
                "emotional_state": "frustrated",
                "decision": "rewrite module"
            }
        )
        
        time.sleep(2)
        
        # Scenario 2: Good decision
        self.console.print("\n[bold]Scenario 2: Well-Considered Decision[/bold]")
        self.check_decision(
            "Should I refactor this function?",
            {
                "stress_level": 30,
                "energy_level": 80,
                "decision_quality": 85,
                "time_thinking": 300,
                "emotional_state": "calm",
                "decision": "refactor function"
            }
        )
        
        time.sleep(2)
        
        # Show parallel universe comparison
        self.console.print("\n[bold cyan]📊 Daily Universe Comparison[/bold cyan]\n")
        comparison = self.universe_viewer.get_daily_comparison()
        
        table = Table(title="🏆 Universe Leaderboard")
        table.add_column("Universe", style="cyan")
        table.add_column("Score", style="green")
        table.add_column("Decisions", style="yellow")
        
        for key, data in comparison["universes"].items():
            table.add_row(
                f"{data['emoji']} {data['persona']}",
                str(data['score']),
                str(data['decisions'])
            )
        
        self.console.print(table)
        self.console.print(f"\n{comparison['recommendation']}\n")


def main():
    """Run live twin demo"""
    twin = LiveCognitiveTwin()
    
    # Show banner
    twin.console.print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🔥 LIVE COGNITIVE TWIN v2.0                       ║
║                                                           ║
║        Real-time monitoring • Live intervention          ║
║        Parallel universes • Regret prediction            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """, style="bold cyan")
    
    # Run demo
    twin.demo_decision_flow()
    
    twin.console.print("\n[bold green]✨ Demo complete! This is your live cognitive twin.[/bold green]\n")


if __name__ == "__main__":
    main()

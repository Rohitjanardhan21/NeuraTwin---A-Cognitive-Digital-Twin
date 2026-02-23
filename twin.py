"""
🧠 COGNITIVE DIGITAL TWIN - Main Interface
The absurdly impressive handcrafted AI twin
"""

import os
from typing import Optional
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich import print as rprint

from core.memory_engine import CognitiveMemory
from core.decision_tracker import DecisionTracker
from core.pattern_analyzer import PatternAnalyzer
from core.bias_detector import BiasDetector
from simulators.multiverse import MultiverseSimulator
from simulators.future_self import FutureSelfPredictor
from simulators.parallel_selves import ParallelSelvesGenerator
from prompts.system_prompts import *


class CognitiveTwin:
    """Your digital cognitive twin"""
    
    def __init__(self, llm_client=None, data_dir: str = "data"):
        self.console = Console()
        self.data_dir = data_dir
        
        # Initialize components
        self.memory = CognitiveMemory(data_dir)
        self.decisions = DecisionTracker(data_dir)
        self.analyzer = PatternAnalyzer(data_dir)
        self.bias_detector = BiasDetector()
        
        # Initialize simulators
        self.multiverse = MultiverseSimulator(llm_client)
        self.future_self = FutureSelfPredictor(llm_client)
        self.parallel_selves = ParallelSelvesGenerator(llm_client)
        
        self.llm = llm_client
        
        self._show_banner()
    
    def _show_banner(self):
        """Show the absurdly cool banner"""
        banner = """
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🧠 COGNITIVE DIGITAL TWIN v1.0                    ║
║                                                           ║
║        "Know thyself... with AI"                         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """
        self.console.print(banner, style="bold cyan")
    
    def add_decision(self, decision: str, reason: str, **kwargs):
        """Add a decision to your timeline"""
        decision_id = self.decisions.add_decision(decision, reason, **kwargs)
        self.memory.add_memory(
            f"Decision: {decision}. Reason: {reason}",
            memory_type="decision",
            metadata={"decision_id": decision_id}
        )
        
        # Re-analyze patterns
        all_decisions = self.decisions.get_decision_timeline()
        self.analyzer.analyze_decisions(all_decisions)
        
        self.console.print(f"✓ Decision recorded: {decision_id}", style="green")
        return decision_id
    
    def detect_biases(self):
        """Detect cognitive biases"""
        decisions = self.decisions.get_decision_timeline()
        patterns = self.analyzer.patterns
        
        biases = self.bias_detector.detect_biases(decisions, patterns)
        
        if not biases:
            self.console.print("✓ No significant biases detected", style="green")
            return []
        
        self.console.print("\n⚠️  COGNITIVE BIASES DETECTED\n", style="bold yellow")
        
        for bias in biases:
            panel = Panel(
                f"[bold]{bias['description']}[/bold]\n\n"
                f"Score: {bias['score']}\n"
                f"Evidence: {len(bias['evidence'])} instances",
                title=f"🎯 {bias['bias'].replace('_', ' ').title()}",
                border_style="yellow"
            )
            self.console.print(panel)
        
        return biases
    
    def simulate_multiverse(self, current_path: str, alternative: str):
        """Simulate alternate timelines"""
        decisions = self.decisions.get_decision_timeline()
        patterns = self.analyzer.patterns
        
        simulation = self.multiverse.simulate_timeline(
            current_path, alternative, decisions, patterns
        )
        
        self.console.print("\n🌌 MULTIVERSE SIMULATION\n", style="bold magenta")
        self.console.print(Panel(simulation["prompt"], title="Simulation Prompt", border_style="magenta"))
        
        return simulation
    
    def predict_future(self):
        """Predict future trajectory"""
        decisions = self.decisions.get_decision_timeline()
        patterns = self.analyzer.patterns
        
        prediction = self.future_self.predict_trajectory(decisions, patterns)
        
        self.console.print("\n🔮 FUTURE SELF PREDICTION\n", style="bold blue")
        self.console.print(Panel(prediction["prompt"], title="Prediction Analysis", border_style="blue"))
        
        return prediction
    
    def generate_parallel_selves(self, problem: str):
        """Generate parallel self responses"""
        patterns = self.analyzer.patterns
        baseline = {"patterns": patterns}
        
        parallel = self.parallel_selves.generate_parallel_responses(
            problem, baseline, patterns
        )
        
        self.console.print("\n👥 PARALLEL SELVES SIMULATION\n", style="bold green")
        self.console.print(Panel(parallel["prompt"], title="Three Versions of You", border_style="green"))
        
        return parallel
    
    def get_cognitive_mirror(self, thought: str):
        """Reflect on a thought or decision"""
        patterns = self.analyzer.patterns
        
        prompt = COGNITIVE_MIRROR_PROMPT.format(
            thought=thought,
            patterns=patterns
        )
        
        self.console.print("\n🪞 COGNITIVE MIRROR\n", style="bold cyan")
        self.console.print(Panel(prompt, title="Reflection", border_style="cyan"))
        
        return prompt
    
    def show_stats(self):
        """Show cognitive twin statistics"""
        decisions = self.decisions.get_decision_timeline()
        patterns = self.analyzer.patterns
        
        stats = f"""
📊 COGNITIVE TWIN STATISTICS

Total Decisions: {len(decisions)}
Decision Rate: {patterns.get('decision_speed', {}).get('decisions_per_month', 0):.1f} per month

Top Preferences:
"""
        prefs = patterns.get("preferences", {})
        for pref, count in sorted(prefs.items(), key=lambda x: x[1], reverse=True)[:5]:
            stats += f"  • {pref}: {count}\n"
        
        stats += f"\nRecurring Themes:\n"
        themes = patterns.get("recurring_themes", {})
        for theme, count in list(themes.items())[:5]:
            stats += f"  • {theme}: {count}\n"
        
        self.console.print(Panel(stats, title="📈 Your Cognitive Profile", border_style="cyan"))


def demo():
    """Run a demo of the cognitive twin"""
    twin = CognitiveTwin()
    
    # Add some sample decisions
    twin.console.print("\n[bold]Adding sample decisions...[/bold]\n")
    
    twin.add_decision(
        "Used Restormer for image restoration",
        "Better SSIM scores and memory efficiency",
        constraints={"gpu_memory": "4GB", "inference_time": "real-time"},
        outcome="success",
        tags=["deep-learning", "computer-vision", "optimization"]
    )
    
    twin.add_decision(
        "Switched to PyTorch from TensorFlow",
        "More flexible for research, better debugging",
        alternatives=["TensorFlow", "JAX"],
        constraints={"learning_curve": "moderate"},
        outcome="success",
        tags=["deep-learning", "framework", "tooling"]
    )
    
    twin.add_decision(
        "Implemented custom attention mechanism",
        "Standard attention wasn't efficient enough",
        constraints={"time": "2 weeks", "complexity": "high"},
        outcome="success",
        tags=["deep-learning", "optimization", "research"]
    )
    
    # Show stats
    twin.show_stats()
    
    # Detect biases
    twin.console.print("\n[bold]Detecting cognitive biases...[/bold]\n")
    twin.detect_biases()
    
    # Simulate multiverse
    twin.console.print("\n[bold]Simulating alternate timeline...[/bold]\n")
    twin.simulate_multiverse(
        "Continue with Restormer",
        "Switch to SwinIR"
    )
    
    # Predict future
    twin.console.print("\n[bold]Predicting future trajectory...[/bold]\n")
    twin.predict_future()
    
    # Generate parallel selves
    twin.console.print("\n[bold]Generating parallel selves...[/bold]\n")
    twin.generate_parallel_selves(
        "Should I focus on publishing papers or building a product?"
    )


if __name__ == "__main__":
    demo()

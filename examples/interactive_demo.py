"""
🎮 INTERACTIVE DEMO - Play with your cognitive twin
"""

import sys
sys.path.append('..')

from twin import CognitiveTwin
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel


def interactive_demo():
    """Interactive demo of cognitive twin"""
    console = Console()
    twin = CognitiveTwin()
    
    console.print("\n[bold cyan]Welcome to your Cognitive Digital Twin![/bold cyan]\n")
    console.print("Let's build your cognitive profile...\n")
    
    # Collect some decisions
    console.print("[bold]First, let's record some of your past decisions.[/bold]\n")
    
    while True:
        if not Confirm.ask("Add a decision?", default=True):
            break
        
        decision = Prompt.ask("What did you decide?")
        reason = Prompt.ask("Why?")
        outcome = Prompt.ask("Outcome? (success/failure/unknown)", default="unknown")
        tags = Prompt.ask("Tags (comma-separated)", default="")
        
        tag_list = [t.strip() for t in tags.split(",")] if tags else []
        
        twin.add_decision(
            decision=decision,
            reason=reason,
            outcome=outcome,
            tags=tag_list
        )
        
        console.print("✓ Recorded!\n", style="green")
    
    # Main menu
    while True:
        console.print("\n[bold]What would you like to explore?[/bold]\n")
        console.print("1. 📊 Show my cognitive stats")
        console.print("2. ⚠️  Detect my biases")
        console.print("3. 🌌 Simulate alternate timeline")
        console.print("4. 🔮 Predict my future")
        console.print("5. 👥 Generate parallel selves")
        console.print("6. 🪞 Cognitive mirror")
        console.print("7. 🚪 Exit\n")
        
        choice = Prompt.ask("Choose", choices=["1", "2", "3", "4", "5", "6", "7"])
        
        if choice == "1":
            twin.show_stats()
        
        elif choice == "2":
            twin.detect_biases()
        
        elif choice == "3":
            current = Prompt.ask("Current path")
            alternative = Prompt.ask("Alternative")
            twin.simulate_multiverse(current, alternative)
        
        elif choice == "4":
            twin.predict_future()
        
        elif choice == "5":
            problem = Prompt.ask("What problem should your parallel selves solve?")
            twin.generate_parallel_selves(problem)
        
        elif choice == "6":
            thought = Prompt.ask("What thought should I reflect on?")
            twin.get_cognitive_mirror(thought)
        
        elif choice == "7":
            console.print("\n[bold cyan]Until next time! 🧠[/bold cyan]\n")
            break


if __name__ == "__main__":
    interactive_demo()

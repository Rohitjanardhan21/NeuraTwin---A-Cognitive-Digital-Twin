"""
🎭 SHOWCASE - The ultimate demo script
Run this to blow people's minds
"""

from twin import CognitiveTwin
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.progress import Progress
import time


def showcase():
    """The ultimate mind-blowing demo"""
    console = Console()
    
    # Dramatic intro
    console.clear()
    console.print("\n" * 3)
    console.print("═" * 70, style="bold cyan")
    console.print("                                                                      ", style="bold cyan")
    console.print("              🧠 COGNITIVE DIGITAL TWIN SHOWCASE 🧠                   ", style="bold cyan")
    console.print("                                                                      ", style="bold cyan")
    console.print("           \"What if you could simulate your own mind?\"               ", style="italic")
    console.print("                                                                      ", style="bold cyan")
    console.print("═" * 70, style="bold cyan")
    console.print("\n")
    
    time.sleep(2)
    
    # Initialize
    console.print("Initializing cognitive twin...", style="yellow")
    with Progress() as progress:
        task = progress.add_task("[cyan]Loading...", total=100)
        for i in range(100):
            time.sleep(0.01)
            progress.update(task, advance=1)
    
    twin = CognitiveTwin()
    console.print("✓ Twin initialized\n", style="green")
    
    # Add sample decisions
    console.print("[bold]PHASE 1: Building Cognitive Profile[/bold]\n", style="cyan")
    
    decisions = [
        ("Used Restormer for image restoration", "Better SSIM & memory efficiency", ["deep-learning", "optimization"]),
        ("Switched to PyTorch from TensorFlow", "More flexible for research", ["framework", "tooling"]),
        ("Implemented custom attention mechanism", "Standard wasn't efficient enough", ["research", "optimization"]),
        ("Used mixed precision training", "2x speedup with minimal loss", ["performance", "training"]),
        ("Chose Docker for deployment", "Better reproducibility", ["devops", "infrastructure"])
    ]
    
    for decision, reason, tags in decisions:
        twin.add_decision(decision, reason, tags=tags, outcome="success")
        console.print(f"  ✓ {decision}", style="dim")
        time.sleep(0.3)
    
    console.print("\n[green]✓ Profile built with 5 decisions[/green]\n")
    time.sleep(1)
    
    # Show stats
    console.print("[bold]PHASE 2: Cognitive Analysis[/bold]\n", style="cyan")
    twin.show_stats()
    time.sleep(2)
    
    # Detect biases
    console.print("\n[bold]PHASE 3: Bias Detection[/bold]\n", style="cyan")
    console.print("Analyzing decision patterns for cognitive biases...\n", style="yellow")
    time.sleep(1)
    
    biases = twin.detect_biases()
    time.sleep(2)
    
    # Multiverse simulation
    console.print("\n[bold]PHASE 4: Multiverse Simulation[/bold]\n", style="cyan")
    console.print("Simulating alternate timeline...\n", style="yellow")
    time.sleep(1)
    
    simulation = twin.simulate_multiverse(
        "Continue optimizing current model",
        "Switch to completely different architecture"
    )
    time.sleep(2)
    
    # Future prediction
    console.print("\n[bold]PHASE 5: Future Self Prediction[/bold]\n", style="cyan")
    console.print("Predicting future trajectory...\n", style="yellow")
    time.sleep(1)
    
    prediction = twin.predict_future()
    time.sleep(2)
    
    # Parallel selves
    console.print("\n[bold]PHASE 6: Parallel Selves Generation[/bold]\n", style="cyan")
    console.print("Generating alternate versions...\n", style="yellow")
    time.sleep(1)
    
    parallel = twin.generate_parallel_selves(
        "Should I focus on publishing research papers or building a product?"
    )
    time.sleep(2)
    
    # Final message
    console.print("\n" + "═" * 70, style="bold cyan")
    console.print("\n[bold cyan]SHOWCASE COMPLETE[/bold cyan]\n")
    
    console.print(Panel.fit(
        "[bold]What you just saw:[/bold]\n\n"
        "✓ Cognitive pattern analysis\n"
        "✓ Bias detection from decision history\n"
        "✓ Alternate timeline simulation\n"
        "✓ Future trajectory prediction\n"
        "✓ Parallel persona generation\n\n"
        "[italic]All from just 5 decisions.[/italic]\n\n"
        "[bold cyan]Imagine what it could do with your entire decision history.[/bold cyan]",
        title="🧠 Cognitive Digital Twin",
        border_style="cyan"
    ))
    
    console.print("\n[bold]Next Steps:[/bold]")
    console.print("  1. Add your own decisions: twin.add_decision(...)")
    console.print("  2. Integrate with LLM: python examples/llm_integration.py")
    console.print("  3. Try the web interface: cd web && python app.py")
    console.print("  4. Read DEMO_PROMPTS.md for more ideas\n")
    
    console.print("[dim]Built with ❤️  and a touch of madness[/dim]\n")


if __name__ == "__main__":
    showcase()

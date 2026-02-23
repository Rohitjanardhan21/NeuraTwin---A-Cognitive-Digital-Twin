"""
🤖 LLM INTEGRATION EXAMPLE
Shows how to integrate with OpenAI or Anthropic for actual AI responses
"""

import sys
sys.path.append('..')

import os
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from twin import CognitiveTwin
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()


class LLMIntegratedTwin(CognitiveTwin):
    """Cognitive twin with actual LLM responses"""
    
    def __init__(self, provider="openai", **kwargs):
        super().__init__(**kwargs)
        
        if provider == "openai":
            self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            self.model = os.getenv("OPENAI_MODEL", "gpt-4-turbo-preview")
            self.provider = "openai"
        elif provider == "anthropic":
            self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
            self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-opus-20240229")
            self.provider = "anthropic"
    
    def _call_llm(self, prompt: str):
        """Call LLM with prompt"""
        if self.provider == "openai":
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a cognitive digital twin."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        
        elif self.provider == "anthropic":
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text
    
    def detect_biases_with_ai(self):
        """Detect biases with AI analysis"""
        biases = super().detect_biases()
        
        if not biases:
            return
        
        # Get AI interpretation
        bias_summary = "\n".join([
            f"- {b['bias']}: {b['description']} (score: {b['score']})"
            for b in biases
        ])
        
        prompt = f"""Analyze these detected cognitive biases:

{bias_summary}

Provide:
1. Interpretation of what these biases reveal
2. Potential blind spots
3. Actionable recommendations
4. How these might affect future decisions

Be insightful and constructive."""

        self.console.print("\n[bold]🤖 AI Analysis:[/bold]\n")
        response = self._call_llm(prompt)
        self.console.print(Markdown(response))
    
    def simulate_multiverse_with_ai(self, current_path: str, alternative: str):
        """Simulate multiverse with AI"""
        simulation = super().simulate_multiverse(current_path, alternative)
        
        self.console.print("\n[bold]🤖 AI Simulation:[/bold]\n")
        response = self._call_llm(simulation["prompt"])
        self.console.print(Markdown(response))
    
    def predict_future_with_ai(self):
        """Predict future with AI"""
        prediction = super().predict_future()
        
        self.console.print("\n[bold]🤖 AI Prediction:[/bold]\n")
        response = self._call_llm(prediction["prompt"])
        self.console.print(Markdown(response))


def demo_with_llm():
    """Demo with actual LLM integration"""
    console = Console()
    
    console.print("\n[bold cyan]🧠 Cognitive Twin with AI Integration[/bold cyan]\n")
    
    # Initialize with LLM
    twin = LLMIntegratedTwin(provider="openai")  # or "anthropic"
    
    # Add sample decisions
    twin.add_decision(
        "Used Restormer for image restoration",
        "Better SSIM scores and memory efficiency",
        constraints={"gpu_memory": "4GB"},
        outcome="success",
        tags=["deep-learning", "optimization"]
    )
    
    twin.add_decision(
        "Implemented custom attention mechanism",
        "Standard attention wasn't efficient enough",
        constraints={"time": "2 weeks"},
        outcome="success",
        tags=["deep-learning", "research"]
    )
    
    # Get AI-powered analysis
    console.print("\n[bold]Getting AI analysis...[/bold]\n")
    
    twin.detect_biases_with_ai()
    twin.predict_future_with_ai()
    twin.simulate_multiverse_with_ai(
        "Continue optimizing current model",
        "Switch to completely different architecture"
    )


if __name__ == "__main__":
    demo_with_llm()

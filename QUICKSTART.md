# 🚀 Quick Start Guide

Get your Cognitive Digital Twin running in 5 minutes.

## Installation

```bash
# Clone or navigate to the directory
cd cognitive-twin

# Install dependencies
pip install -r requirements.txt
```

## Option 1: Command Line Demo (Fastest)

```bash
python twin.py
```

This runs a demo with sample data showing all capabilities.

## Option 2: Interactive Mode

```bash
python examples/interactive_demo.py
```

This lets you add your own decisions and explore interactively.

## Option 3: Web Interface (Most Impressive)

```bash
# Install Flask
pip install flask

# Run the web server
cd web
python app.py

# Open browser to http://localhost:5000
```

## Option 4: With Real AI (Most Powerful)

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your API key
# OPENAI_API_KEY=your_key_here

# Run with AI integration
python examples/llm_integration.py
```

## Your First Decision

```python
from twin import CognitiveTwin

twin = CognitiveTwin()

twin.add_decision(
    decision="Chose Python over JavaScript for backend",
    reason="Better for data processing and ML integration",
    constraints={"team_experience": "high", "performance": "moderate"},
    outcome="success",
    tags=["backend", "language-choice", "architecture"]
)
```

## Explore Your Mind

```python
# See your cognitive profile
twin.show_stats()

# Detect biases
twin.detect_biases()

# Simulate "what if"
twin.simulate_multiverse(
    "Continue with Python",
    "Switch to Go"
)

# Predict future
twin.predict_future()

# Generate parallel selves
twin.generate_parallel_selves(
    "Should I focus on depth or breadth?"
)
```

## Next Steps

1. Add more decisions to build your profile
2. Integrate with your actual LLM for AI responses
3. Customize the prompts in `prompts/system_prompts.py`
4. Build custom visualizations
5. Share with friends and blow their minds

## Tips

- The more decisions you add, the better the analysis
- Tag decisions consistently for better pattern detection
- Update outcomes to improve future predictions
- Use the web interface for demos
- Integrate with your note-taking system

## Troubleshooting

**ChromaDB errors?**
```bash
pip install --upgrade chromadb
```

**No API key?**
The system works without an LLM - it generates prompts you can use manually.

**Want to reset data?**
```bash
rm -rf data/
```

Now go forth and know thyself! 🧠✨

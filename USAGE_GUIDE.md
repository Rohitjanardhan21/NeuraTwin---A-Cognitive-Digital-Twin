# 📖 Complete Usage Guide

## Table of Contents
1. [Installation](#installation)
2. [Basic Usage](#basic-usage)
3. [Advanced Features](#advanced-features)
4. [Integration](#integration)
5. [Customization](#customization)
6. [Best Practices](#best-practices)

## Installation

### Quick Install
```bash
cd cognitive-twin
pip install -r requirements.txt
```

### With Web Interface
```bash
pip install -r requirements.txt
pip install -r web/requirements.txt
```

### With LLM Integration
```bash
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your API key
```

## Basic Usage

### 1. Initialize Your Twin

```python
from twin import CognitiveTwin

twin = CognitiveTwin()
```

### 2. Add Decisions

```python
twin.add_decision(
    decision="Chose Python over JavaScript for backend",
    reason="Better for data processing and ML integration",
    alternatives=["JavaScript", "Go", "Rust"],
    constraints={
        "team_experience": "high",
        "performance": "moderate",
        "ecosystem": "rich"
    },
    outcome="success",
    tags=["backend", "language-choice", "architecture"]
)
```

### 3. View Your Profile

```python
twin.show_stats()
```

### 4. Detect Biases

```python
biases = twin.detect_biases()
```

### 5. Simulate Multiverse

```python
twin.simulate_multiverse(
    current_path="Continue with Python",
    alternative="Rewrite in Go"
)
```

### 6. Predict Future

```python
twin.predict_future()
```

### 7. Generate Parallel Selves

```python
twin.generate_parallel_selves(
    problem="Should I focus on depth or breadth in my learning?"
)
```

## Advanced Features

### Memory Engine

```python
# Add semantic memory
twin.memory.add_memory(
    content="Learned about transformer architecture",
    memory_type="learning",
    metadata={"topic": "deep-learning", "date": "2024-01-15"}
)

# Search memories
results = twin.memory.search_memories(
    query="transformer architecture",
    n_results=5
)

# Add concept relationships
twin.memory.add_concept_link(
    concept_a="transformer",
    concept_b="attention",
    relationship="uses"
)
```

### Decision Tracking

```python
# Get recent decisions
recent = twin.decisions.get_recent_decisions(n=10)

# Get decisions by tag
ml_decisions = twin.decisions.get_decisions_by_tag("machine-learning")

# Update outcome
twin.decisions.update_outcome(
    decision_id="dec_0",
    outcome="success"
)

# Find similar decisions
similar = twin.decisions.find_similar_decisions(
    "Should I use PyTorch or TensorFlow?"
)
```

### Pattern Analysis

```python
# Analyze all decisions
patterns = twin.analyzer.analyze_decisions(
    twin.decisions.get_decision_timeline()
)

# Access specific patterns
preferences = patterns["preferences"]
themes = patterns["recurring_themes"]
evolution = patterns["evolution"]
```

### Cognitive Mirror

```python
# Reflect on a thought
twin.get_cognitive_mirror(
    "I think I should rewrite this entire codebase"
)
```

## Integration

### OpenAI Integration

```python
from openai import OpenAI
from twin import CognitiveTwin

client = OpenAI(api_key="your-key")
twin = CognitiveTwin(llm_client=client)

# Now all simulations can generate actual AI responses
```

### Anthropic Integration

```python
from anthropic import Anthropic
from twin import CognitiveTwin

client = Anthropic(api_key="your-key")
twin = CognitiveTwin(llm_client=client)
```

### Custom LLM Integration

```python
class CustomTwin(CognitiveTwin):
    def __init__(self):
        super().__init__()
        self.llm = YourCustomLLM()
    
    def _call_llm(self, prompt):
        return self.llm.generate(prompt)
```

### Web Interface

```bash
cd web
python app.py
# Open http://localhost:5000
```

### API Usage

```python
import requests

# Add decision via API
response = requests.post('http://localhost:5000/api/decision', json={
    'decision': 'Chose React over Vue',
    'reason': 'Larger ecosystem',
    'tags': ['frontend', 'framework']
})

# Get stats
stats = requests.get('http://localhost:5000/api/stats').json()
```

## Customization

### Add Custom Bias Rules

```python
# In core/bias_detector.py
BIAS_RULES["my_custom_bias"] = {
    "keywords": ["always", "never", "must"],
    "threshold": 3,
    "description": "Black and white thinking"
}
```

### Add Custom Pattern Analysis

```python
# In core/pattern_analyzer.py
def _analyze_custom_pattern(self, decisions):
    # Your custom analysis
    pattern_data = {}
    for dec in decisions:
        # Analyze...
        pass
    return pattern_data
```

### Custom Prompts

```python
# In prompts/system_prompts.py
MY_CUSTOM_PROMPT = """
Your custom prompt here...

CONTEXT:
{context}
"""
```

### Custom Simulator

```python
# Create simulators/my_simulator.py
class MySimulator:
    def __init__(self, llm_client):
        self.llm = llm_client
    
    def simulate(self, context):
        # Your simulation logic
        return result
```

## Best Practices

### 1. Decision Recording

**DO:**
- Record decisions as soon as possible
- Include detailed reasoning
- List alternatives considered
- Document constraints
- Update outcomes later

**DON'T:**
- Record trivial decisions
- Skip the "why"
- Forget to tag decisions
- Leave outcomes unknown forever

### 2. Tagging Strategy

Use consistent tags:
```python
# Good tags
["deep-learning", "optimization", "architecture"]

# Bad tags
["dl", "opt", "arch"]  # Too abbreviated
["Deep Learning", "OPTIMIZATION"]  # Inconsistent case
```

### 3. Constraint Documentation

Be specific:
```python
# Good
constraints={
    "gpu_memory": "8GB",
    "inference_time": "<100ms",
    "accuracy_target": ">95%"
}

# Bad
constraints={
    "memory": "limited",
    "speed": "fast"
}
```

### 4. Regular Analysis

```python
# Run weekly
twin.show_stats()
twin.detect_biases()

# Run monthly
twin.predict_future()

# Run when making big decisions
twin.simulate_multiverse(current, alternative)
```

### 5. Data Hygiene

```python
# Backup regularly
import shutil
shutil.copytree('data/', 'data_backup/')

# Clean up test data
# Delete data/ folder and start fresh
```

### 6. Privacy

- Keep sensitive decisions local
- Don't commit `.env` files
- Use generic examples in shared code
- Sanitize data before sharing

## Troubleshooting

### ChromaDB Issues
```bash
pip install --upgrade chromadb
# or
pip uninstall chromadb
pip install chromadb==0.4.0
```

### Memory Issues
```python
# Limit vector DB size
twin.memory.collection.delete(
    where={"timestamp": {"$lt": "2024-01-01"}}
)
```

### Performance Issues
```python
# For large datasets, use pagination
decisions = twin.decisions.get_recent_decisions(n=100)
# Instead of loading all decisions
```

## Examples

### Example 1: Research Decision
```python
twin.add_decision(
    decision="Used transformer architecture for NLP task",
    reason="State-of-art performance, good pretrained models available",
    alternatives=["LSTM", "CNN", "Hybrid"],
    constraints={
        "data_size": "10k samples",
        "compute": "single GPU",
        "time": "2 weeks"
    },
    outcome="success",
    tags=["nlp", "architecture", "research"]
)
```

### Example 2: Tool Selection
```python
twin.add_decision(
    decision="Chose VS Code over PyCharm",
    reason="Lighter weight, better extensions, free",
    alternatives=["PyCharm", "Sublime", "Vim"],
    constraints={
        "budget": "free",
        "performance": "important"
    },
    outcome="success",
    tags=["tooling", "ide", "productivity"]
)
```

### Example 3: Architecture Decision
```python
twin.add_decision(
    decision="Implemented microservices instead of monolith",
    reason="Better scalability, team autonomy",
    alternatives=["Monolith", "Modular monolith"],
    constraints={
        "team_size": "15",
        "scale": "high",
        "complexity_tolerance": "high"
    },
    outcome="mixed",
    tags=["architecture", "scalability", "tradeoffs"]
)
```

## Tips & Tricks

1. **Batch Import**: Create a script to import decisions from notes
2. **Integration**: Hook into your note-taking app
3. **Automation**: Set up cron jobs for weekly analysis
4. **Visualization**: Export data to create custom visualizations
5. **Sharing**: Generate anonymized reports to share insights

## Next Steps

1. Populate with real decisions
2. Integrate with your LLM
3. Customize prompts for your domain
4. Build custom visualizations
5. Share with your team

Happy cognitive twinning! 🧠✨

# 📚 Cognitive Digital Twin - Complete Index

## 🚀 Getting Started

Start here if you're new:

1. **[README.md](README.md)** - Project overview and quick start
2. **[INSTALL.md](INSTALL.md)** - Installation instructions
3. **[QUICKSTART.md](QUICKSTART.md)** - Get running in 5 minutes
4. **Run the showcase**: `python showcase.py`

## 📖 Documentation

### Core Documentation
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Technical architecture
- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Comprehensive usage guide
- **[DEMO_PROMPTS.md](DEMO_PROMPTS.md)** - Mind-blowing demo prompts

### Quick References
- **[.env.example](.env.example)** - Environment configuration template
- **[requirements.txt](requirements.txt)** - Python dependencies

## 🧠 Core Components

### Main Interface
- **[twin.py](twin.py)** - Main CognitiveTwin class and interface

### Core Engines
- **[core/memory_engine.py](core/memory_engine.py)** - Vector + graph hybrid memory
- **[core/decision_tracker.py](core/decision_tracker.py)** - Decision timeline storage
- **[core/pattern_analyzer.py](core/pattern_analyzer.py)** - Cognitive pattern detection
- **[core/bias_detector.py](core/bias_detector.py)** - Bias identification engine

### Simulators
- **[simulators/multiverse.py](simulators/multiverse.py)** - Alternate timeline simulator
- **[simulators/future_self.py](simulators/future_self.py)** - Future trajectory predictor
- **[simulators/parallel_selves.py](simulators/parallel_selves.py)** - Parallel persona generator

### Prompts
- **[prompts/system_prompts.py](prompts/system_prompts.py)** - All handcrafted prompts

## 🎮 Examples & Demos

### Demo Scripts
- **[showcase.py](showcase.py)** - Ultimate demo script (START HERE!)
- **[examples/interactive_demo.py](examples/interactive_demo.py)** - Interactive CLI demo
- **[examples/llm_integration.py](examples/llm_integration.py)** - LLM integration example
- **[examples/sample_data.py](examples/sample_data.py)** - Sample data population

### Web Interface
- **[web/app.py](web/app.py)** - Flask web server
- **[web/templates/index.html](web/templates/index.html)** - Web UI
- **[web/requirements.txt](web/requirements.txt)** - Web dependencies

## 🎯 Usage Patterns

### Basic Usage
```python
from twin import CognitiveTwin

twin = CognitiveTwin()
twin.add_decision("decision", "reason", tags=["tag"])
twin.show_stats()
twin.detect_biases()
```

### Advanced Usage
```python
twin.simulate_multiverse("current", "alternative")
twin.predict_future()
twin.generate_parallel_selves("problem")
twin.get_cognitive_mirror("thought")
```

### Web Interface
```bash
cd web
python app.py
# Open http://localhost:5000
```

## 🔧 Customization

### Add Custom Bias
Edit `core/bias_detector.py`:
```python
BIAS_RULES["my_bias"] = {
    "keywords": [...],
    "threshold": 3,
    "description": "..."
}
```

### Add Custom Pattern
Edit `core/pattern_analyzer.py`:
```python
def _analyze_custom_pattern(self, decisions):
    # Your analysis
    return pattern_data
```

### Add Custom Prompt
Edit `prompts/system_prompts.py`:
```python
MY_PROMPT = """Your prompt here..."""
```

### Add Custom Simulator
Create `simulators/my_simulator.py`:
```python
class MySimulator:
    def simulate(self, context):
        return result
```

## 📊 Data Files

Located in `data/` directory (created on first run):
- `decisions.json` - Decision timeline
- `patterns.json` - Analyzed patterns
- `knowledge_graph.json` - Concept relationships
- `chroma/` - Vector embeddings

## 🎨 Features by Category

### Analysis Features
- Cognitive pattern detection
- Preference extraction
- Theme identification
- Evolution tracking
- Decision speed analysis

### Detection Features
- Overengineering bias
- Premature optimization
- Tool-switching behavior
- Confirmation bias
- Sunk cost fallacy
- Recency bias

### Simulation Features
- Multiverse timeline branching
- Outcome comparison
- Pattern alignment
- Future trajectory prediction
- Parallel persona generation

### Memory Features
- Semantic search (vector DB)
- Concept relationships (graph)
- Decision history
- Context snapshots

## 🚀 Quick Commands

```bash
# Run showcase demo
python showcase.py

# Interactive mode
python examples/interactive_demo.py

# Populate sample data
python examples/sample_data.py

# Web interface
cd web && python app.py

# With LLM integration
python examples/llm_integration.py
```

## 📝 File Organization

```
cognitive-twin/
├── 📄 Documentation
│   ├── README.md
│   ├── QUICKSTART.md
│   ├── INSTALL.md
│   ├── USAGE_GUIDE.md
│   ├── ARCHITECTURE.md
│   ├── DEMO_PROMPTS.md
│   ├── PROJECT_SUMMARY.md
│   └── INDEX.md (this file)
│
├── 🧠 Core System
│   ├── twin.py
│   ├── core/
│   ├── simulators/
│   └── prompts/
│
├── 🎮 Examples & Demos
│   ├── showcase.py
│   └── examples/
│
├── 🌐 Web Interface
│   └── web/
│
└── ⚙️ Configuration
    ├── requirements.txt
    ├── .env.example
    └── .gitignore
```

## 🎯 Learning Path

### Beginner
1. Read [README.md](README.md)
2. Run `python showcase.py`
3. Try [examples/interactive_demo.py](examples/interactive_demo.py)
4. Read [QUICKSTART.md](QUICKSTART.md)

### Intermediate
1. Read [USAGE_GUIDE.md](USAGE_GUIDE.md)
2. Add your own decisions
3. Explore different features
4. Try web interface

### Advanced
1. Read [ARCHITECTURE.md](ARCHITECTURE.md)
2. Integrate with LLM
3. Customize prompts
4. Add custom features
5. Build visualizations

## 🎭 Demo Scenarios

### Scenario 1: Quick Demo (5 min)
```bash
python showcase.py
```

### Scenario 2: Interactive Exploration (15 min)
```bash
python examples/interactive_demo.py
```

### Scenario 3: Web Demo (20 min)
```bash
cd web && python app.py
# Open browser, add decisions, explore features
```

### Scenario 4: Full Integration (30 min)
```bash
# Setup LLM
cp .env.example .env
# Add API key
python examples/llm_integration.py
```

## 🔍 Finding What You Need

### "How do I install?"
→ [INSTALL.md](INSTALL.md)

### "How do I use it?"
→ [QUICKSTART.md](QUICKSTART.md) or [USAGE_GUIDE.md](USAGE_GUIDE.md)

### "How does it work?"
→ [ARCHITECTURE.md](ARCHITECTURE.md)

### "What can it do?"
→ [DEMO_PROMPTS.md](DEMO_PROMPTS.md) or [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)

### "Show me a demo"
→ `python showcase.py`

### "I want to customize it"
→ [USAGE_GUIDE.md](USAGE_GUIDE.md) - Customization section

### "I want to integrate with my LLM"
→ [examples/llm_integration.py](examples/llm_integration.py)

### "I want the web interface"
→ [web/app.py](web/app.py)

## 🎉 Next Steps

1. ✅ Install dependencies
2. ✅ Run showcase demo
3. ✅ Try interactive mode
4. ✅ Add your own decisions
5. ✅ Integrate with LLM
6. ✅ Customize for your needs
7. ✅ Share and impress people

## 💡 Tips

- Start with `showcase.py` for maximum impact
- Use `interactive_demo.py` to add your own data
- Read `DEMO_PROMPTS.md` for presentation ideas
- Check `USAGE_GUIDE.md` for advanced features
- Explore `ARCHITECTURE.md` to understand internals

## 🤝 Contributing

Want to add features?
1. Fork the project
2. Add your feature
3. Test it
4. Share it

## 📞 Support

Having issues?
- Check [INSTALL.md](INSTALL.md) for troubleshooting
- Review [USAGE_GUIDE.md](USAGE_GUIDE.md) for examples
- The system works without LLM - just generates prompts

## 🎊 Final Words

You've built something absurdly ambitious and technically impressive.

Now go forth and blow some minds! 🧠✨

---

**Quick Links:**
- [Get Started](QUICKSTART.md)
- [Install](INSTALL.md)
- [Usage Guide](USAGE_GUIDE.md)
- [Architecture](ARCHITECTURE.md)
- [Demo Prompts](DEMO_PROMPTS.md)

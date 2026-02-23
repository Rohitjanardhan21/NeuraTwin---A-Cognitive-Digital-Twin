# 🏗️ Architecture Overview

## System Design

```
┌─────────────────────────────────────────────────────────────┐
│                    COGNITIVE DIGITAL TWIN                    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌─────────────────────────────────────────┐
        │         MAIN INTERFACE (twin.py)        │
        │  • User interaction                     │
        │  • Orchestration                        │
        │  • Display & formatting                 │
        └─────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   MEMORY     │    │   DECISION   │    │   PATTERN    │
│   ENGINE     │    │   TRACKER    │    │   ANALYZER   │
│              │    │              │    │              │
│ • Vector DB  │    │ • Timeline   │    │ • Preferences│
│ • Knowledge  │    │ • Context    │    │ • Themes     │
│   Graph      │    │ • Outcomes   │    │ • Evolution  │
└──────────────┘    └──────────────┘    └──────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌──────────────┐
                    │     BIAS     │
                    │   DETECTOR   │
                    │              │
                    │ • Rule-based │
                    │ • Pattern    │
                    │   analysis   │
                    └──────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  MULTIVERSE  │    │ FUTURE SELF  │    │   PARALLEL   │
│  SIMULATOR   │    │  PREDICTOR   │    │    SELVES    │
│              │    │              │    │              │
│ • Timeline   │    │ • Trajectory │    │ • Personas   │
│   branching  │    │   analysis   │    │ • Alternate  │
│ • Comparison │    │ • Trends     │    │   responses  │
└──────────────┘    └──────────────┘    └──────────────┘
                              │
                              ▼
                    ┌──────────────┐
                    │  LLM CLIENT  │
                    │  (Optional)  │
                    │              │
                    │ • OpenAI     │
                    │ • Anthropic  │
                    └──────────────┘
```

## Data Flow

### 1. Decision Recording
```
User Input → Decision Tracker → Memory Engine → Pattern Analyzer
                    ↓
              decisions.json
```

### 2. Pattern Analysis
```
Decision History → Pattern Analyzer → patterns.json
                         ↓
                  • Preferences
                  • Themes
                  • Evolution
                  • Speed metrics
```

### 3. Bias Detection
```
Decisions + Patterns → Bias Detector → Bias Report
                            ↓
                    • Rule matching
                    • Pattern analysis
                    • Evidence collection
```

### 4. Simulation
```
Current State + Patterns → Simulator → Prompt/Analysis
                               ↓
                    • Timeline branching
                    • Outcome prediction
                    • Comparison
```

## Core Components

### Memory Engine (`core/memory_engine.py`)
- **Vector Database**: ChromaDB for semantic search
- **Knowledge Graph**: NetworkX for concept relationships
- **Purpose**: Long-term memory with semantic retrieval

### Decision Tracker (`core/decision_tracker.py`)
- **Storage**: JSON-based timeline
- **Features**: Context snapshots, outcome tracking
- **Purpose**: Complete decision history with metadata

### Pattern Analyzer (`core/pattern_analyzer.py`)
- **Analysis Types**:
  - Preference extraction
  - Theme detection
  - Decision speed
  - Evolution tracking
- **Purpose**: Identify cognitive patterns

### Bias Detector (`core/bias_detector.py`)
- **Methods**:
  - Rule-based detection
  - Pattern-based detection
  - Evidence collection
- **Purpose**: Identify cognitive biases

### Simulators
1. **Multiverse** (`simulators/multiverse.py`)
   - Timeline branching
   - Outcome comparison
   
2. **Future Self** (`simulators/future_self.py`)
   - Trajectory prediction
   - Trend analysis
   
3. **Parallel Selves** (`simulators/parallel_selves.py`)
   - Persona generation
   - Alternate responses

## Data Storage

```
data/
├── decisions.json          # Decision timeline
├── patterns.json           # Analyzed patterns
├── knowledge_graph.json    # Concept relationships
└── chroma/                 # Vector embeddings
```

## Prompt System

All prompts are handcrafted in `prompts/system_prompts.py`:
- Core twin prompt
- Multiverse simulation
- Bias detection
- Future prediction
- Parallel selves
- Cognitive mirror
- Evolution tracking

## Extension Points

### 1. Add New Bias Rules
```python
# In bias_detector.py
BIAS_RULES["new_bias"] = {
    "keywords": [...],
    "threshold": 3,
    "description": "..."
}
```

### 2. Add New Pattern Types
```python
# In pattern_analyzer.py
def _analyze_new_pattern(self, decisions):
    # Custom analysis
    return pattern_data
```

### 3. Add New Simulator
```python
# Create new file in simulators/
class NewSimulator:
    def simulate(self, context):
        # Custom simulation
        return result
```

### 4. Custom LLM Integration
```python
# In twin.py
class CustomTwin(CognitiveTwin):
    def __init__(self):
        super().__init__(llm_client=YourLLM())
```

## Performance Considerations

- **Vector DB**: ChromaDB is in-memory by default
- **Graph**: NetworkX is efficient for small graphs (<10k nodes)
- **JSON**: Fast for <10k decisions
- **Scaling**: For larger datasets, consider:
  - PostgreSQL for decisions
  - Neo4j for knowledge graph
  - Pinecone for vector storage

## Security

- All data stored locally
- No external calls without explicit LLM integration
- API keys in `.env` (never committed)
- No PII in sample data

## Testing Strategy

1. **Unit Tests**: Each component independently
2. **Integration Tests**: Component interactions
3. **Demo Tests**: Full workflow validation
4. **LLM Tests**: Prompt quality validation

## Future Enhancements

1. **Visualization**: D3.js for pattern graphs
2. **Real-time**: WebSocket for live updates
3. **Collaboration**: Multi-user cognitive profiles
4. **Mobile**: React Native app
5. **Voice**: Speech interface
6. **Integration**: Notion, Obsidian, Roam plugins

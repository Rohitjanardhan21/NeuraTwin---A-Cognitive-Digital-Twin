# ⚡ Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Quick Install (2 minutes)

```bash
# Navigate to directory
cd cognitive-twin

# Install dependencies
pip install -r requirements.txt

# Run demo
python showcase.py
```

That's it! 🎉

## Detailed Installation

### Step 1: Install Core Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `openai` - OpenAI API client (optional)
- `anthropic` - Anthropic API client (optional)
- `chromadb` - Vector database for semantic memory
- `networkx` - Graph database for concept relationships
- `numpy` - Numerical computing
- `python-dotenv` - Environment variable management
- `rich` - Beautiful terminal output

### Step 2: Install Web Interface (Optional)

```bash
pip install -r web/requirements.txt
```

This adds:
- `flask` - Web framework
- `flask-cors` - CORS support

### Step 3: Configure LLM (Optional)

```bash
# Copy environment template
cp .env.example .env

# Edit .env file
nano .env  # or your preferred editor
```

Add your API key:
```
OPENAI_API_KEY=sk-your-key-here
# or
ANTHROPIC_API_KEY=your-key-here
```

## Verify Installation

```bash
# Test basic functionality
python -c "from twin import CognitiveTwin; print('✓ Installation successful!')"

# Run showcase
python showcase.py

# Run interactive demo
python examples/interactive_demo.py
```

## Platform-Specific Notes

### Windows
```bash
# Use pip instead of pip3
pip install -r requirements.txt
```

### macOS
```bash
# May need to use pip3
pip3 install -r requirements.txt
```

### Linux
```bash
# May need sudo for system-wide install
sudo pip install -r requirements.txt

# Or use virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Deactivate when done
deactivate
```

## Troubleshooting

### ChromaDB Installation Issues

```bash
# Try specific version
pip install chromadb==0.4.0

# Or upgrade
pip install --upgrade chromadb
```

### NetworkX Issues

```bash
pip install --upgrade networkx
```

### Rich Display Issues

```bash
# Ensure terminal supports colors
export TERM=xterm-256color
```

### Permission Errors

```bash
# Use --user flag
pip install --user -r requirements.txt
```

## Minimal Installation

If you want the absolute minimum:

```bash
# Core only (no LLM, no web)
pip install chromadb networkx rich
```

## Development Installation

For contributing:

```bash
# Install with dev dependencies
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Run tests
pytest

# Format code
black .

# Lint
flake8 .
```

## Docker Installation (Advanced)

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "showcase.py"]
```

```bash
# Build
docker build -t cognitive-twin .

# Run
docker run -it cognitive-twin
```

## Uninstallation

```bash
# Remove dependencies
pip uninstall -r requirements.txt -y

# Remove data
rm -rf data/

# Remove environment
rm .env
```

## Next Steps

After installation:

1. ✅ Run `python showcase.py` for demo
2. ✅ Read `QUICKSTART.md` for usage
3. ✅ Try `python examples/interactive_demo.py`
4. ✅ Check `USAGE_GUIDE.md` for details

## Support

Having issues? Check:
- Python version: `python --version` (need 3.8+)
- Pip version: `pip --version`
- Virtual environment activated?
- All dependencies installed?

Still stuck? The system works without LLM integration - just generates prompts you can use manually!

Happy installing! 🚀

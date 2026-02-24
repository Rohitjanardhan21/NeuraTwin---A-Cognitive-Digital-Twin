"""
🚀 WORLD-CLASS SETUP SCRIPT
Installs all dependencies for the complete NeuraTwin experience
"""

import subprocess
import sys
import platform

def run_command(command, description):
    """Run a command and show progress"""
    print(f"\n{'='*60}")
    print(f"📦 {description}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(f"✅ {description} - SUCCESS")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - FAILED")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🌟 NEURATWIN WORLD-CLASS SETUP                       ║
║     Installing all dependencies...                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    system = platform.system()
    print(f"🖥️ Detected OS: {system}")
    
    # Core dependencies
    print("\n📚 Installing core dependencies...")
    run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Core dependencies (Flask, OpenAI, etc.)"
    )
    
    # Activity tracking dependencies
    print("\n🖥️ Installing activity tracking...")
    run_command(
        f"{sys.executable} -m pip install psutil pynput",
        "Activity tracking (psutil, pynput)"
    )
    
    # Voice interface dependencies
    print("\n🎤 Installing voice interface...")
    run_command(
        f"{sys.executable} -m pip install SpeechRecognition pyttsx3",
        "Voice interface (SpeechRecognition, pyttsx3)"
    )
    
    # Platform-specific dependencies
    if system == "Windows":
        print("\n🪟 Installing Windows-specific dependencies...")
        run_command(
            f"{sys.executable} -m pip install pywin32 pyaudio",
            "Windows dependencies (pywin32, pyaudio)"
        )
    elif system == "Darwin":  # macOS
        print("\n🍎 Installing macOS-specific dependencies...")
        run_command(
            f"{sys.executable} -m pip install pyobjc-framework-Cocoa pyaudio",
            "macOS dependencies"
        )
    elif system == "Linux":
        print("\n🐧 Installing Linux-specific dependencies...")
        run_command(
            f"{sys.executable} -m pip install python3-xlib pyaudio",
            "Linux dependencies"
        )
    
    # Web interface dependencies
    print("\n🌐 Installing web interface...")
    run_command(
        f"{sys.executable} -m pip install -r web/requirements.txt",
        "Web interface dependencies"
    )
    
    # API dependencies
    print("\n📡 Installing API dependencies...")
    run_command(
        f"{sys.executable} -m pip install -r api/requirements.txt",
        "API dependencies"
    )
    
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ✅ SETUP COMPLETE!                                    ║
║                                                           ║
║     Next steps:                                           ║
║     1. Add your API keys to .env file                     ║
║     2. Run: python start_all.py                           ║
║     3. Open: http://localhost:5002                        ║
║                                                           ║
║     Features now available:                               ║
║     🖥️ Real desktop activity tracking                     ║
║     🎤 Voice interface (say "JARVIS")                     ║
║     🧠 AI-powered insights                                ║
║     📊 Live cognitive monitoring                          ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)

if __name__ == "__main__":
    main()

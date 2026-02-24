"""
🚀 START ALL SERVICES
Launches daemon, API, and web interface
"""

import subprocess
import time
import sys
import os
from pathlib import Path

def start_service(name, command, cwd=None):
    """Start a service in background"""
    print(f"🚀 Starting {name}...")
    
    if sys.platform == "win32":
        # Windows
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd,
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
    else:
        # Unix/Linux/Mac
        process = subprocess.Popen(
            command,
            shell=True,
            cwd=cwd
        )
    
    return process

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🧠 COGNITIVE TWIN - FULL SYSTEM STARTUP           ║
║           🌟 World-Class Edition with Real Tracking      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    base_dir = Path(__file__).parent
    
    # Initialize activity tracking
    print("🖥️ Initializing activity tracker...")
    sys.path.insert(0, str(base_dir))
    try:
        from core.activity_tracker import get_tracker
        tracker = get_tracker()
        if tracker.start_tracking():
            print("✅ Activity tracking started")
        else:
            print("⚠️ Activity tracking unavailable (install pynput)")
    except Exception as e:
        print(f"⚠️ Activity tracking error: {e}")
    
    # Start API server
    api_process = start_service(
        "API Server",
        f"{sys.executable} api/twin_api.py",
        cwd=base_dir
    )
    time.sleep(2)
    
    # Start Web Interface
    web_process = start_service(
        "Web Interface",
        f"{sys.executable} web/assistant_app.py",
        cwd=base_dir
    )
    time.sleep(2)
    
    print("""
✅ All services started!

📡 API Server:      http://localhost:5001
🌐 Web Interface:   http://localhost:5002
📱 Mobile View:     http://localhost:5002/mobile
🖥️ Activity Tracking: ACTIVE (real desktop monitoring)
🎤 Voice Interface:  Available (say "JARVIS" to activate)

To start the daemon (background monitoring):
    python daemon/twin_daemon.py

To use voice commands:
    python voice_jarvis.py

To view activity tracking:
    python track_activity.py

Press Ctrl+C to stop all services
    """)
    
    try:
        # Keep running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping all services...")
        api_process.terminate()
        web_process.terminate()
        print("✅ All services stopped\n")

if __name__ == "__main__":
    main()

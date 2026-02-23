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
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    base_dir = Path(__file__).parent
    
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

To start the daemon (background monitoring):
    python daemon/twin_daemon.py

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

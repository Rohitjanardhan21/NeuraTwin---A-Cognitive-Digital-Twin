"""
🖥️ ACTIVITY TRACKER - Real desktop activity tracking
Run this to track your actual computer usage
"""

import sys
from pathlib import Path
import time

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from core.activity_tracker import get_tracker

def main():
    print("=" * 60)
    print("🖥️ ACTIVITY TRACKER - Real Desktop Monitoring")
    print("=" * 60)
    print()
    
    tracker = get_tracker()
    
    print("📊 Starting activity tracking...")
    print()
    print("This will track:")
    print("  ✅ Keyboard activity")
    print("  ✅ Mouse activity")
    print("  ✅ Application switches")
    print("  ✅ Focus patterns")
    print()
    print("Press Ctrl+C to stop and see statistics")
    print()
    print("-" * 60)
    print()
    
    # Start tracking
    if not tracker.start_tracking():
        print("❌ Failed to start tracking!")
        print()
        print("Install required packages:")
        print("  pip install pynput psutil")
        print()
        if sys.platform == "win32":
            print("  pip install pywin32")
        print()
        return
    
    try:
        # Show live stats every 10 seconds
        while True:
            time.sleep(10)
            
            activity = tracker.get_activity_level(5)
            focus = tracker.get_focus_score(10)
            
            print(f"📊 Activity: {activity['level']}% | "
                  f"Focus: {focus['score']}% | "
                  f"App: {activity['current_app'] or 'Unknown'} | "
                  f"State: {focus['state']}")
    
    except KeyboardInterrupt:
        print("\n\n⏹️ Stopping tracker...")
        tracker.stop_tracking()
        
        # Show final statistics
        print()
        print("=" * 60)
        print("📊 FINAL STATISTICS")
        print("=" * 60)
        print()
        
        stats = tracker.get_stats_summary()
        
        print(f"Total Keystrokes: {stats['total_keystrokes']:,}")
        print(f"Total Clicks: {stats['total_clicks']:,}")
        print(f"App Switches: {stats['total_app_switches']:,}")
        print(f"Apps Used: {stats['apps_used']}")
        print()
        
        if stats['top_apps']:
            print("Top Applications:")
            for app, count in stats['top_apps']:
                print(f"  • {app}: {count} switches")
        
        print()
        print("=" * 60)

if __name__ == "__main__":
    main()

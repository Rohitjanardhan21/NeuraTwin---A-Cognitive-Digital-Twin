"""
🧪 FEATURE TEST SCRIPT
Tests all world-class features
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

def test_activity_tracking():
    """Test activity tracking"""
    print("\n🖥️ Testing Activity Tracking...")
    try:
        from core.activity_tracker import get_tracker
        tracker = get_tracker()
        
        print(f"   ✓ Activity tracker initialized")
        print(f"   ✓ Tracking status: {'ACTIVE' if tracker.is_tracking else 'INACTIVE'}")
        
        # Get stats
        stats = tracker.get_stats_summary()
        print(f"   ✓ Total keystrokes: {stats['total_keystrokes']}")
        print(f"   ✓ Total clicks: {stats['total_clicks']}")
        print(f"   ✓ Apps tracked: {stats['apps_used']}")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_voice_interface():
    """Test voice interface"""
    print("\n🎤 Testing Voice Interface...")
    try:
        from core.voice_interface import get_voice_interface
        voice = get_voice_interface()
        
        print(f"   ✓ Voice interface initialized")
        print(f"   ✓ Available: {voice.is_available()}")
        print(f"   ✓ Wake word: '{voice.wake_word}'")
        
        # Test TTS
        if voice.is_available():
            print("   ✓ Testing text-to-speech...")
            voice.speak("JARVIS online. All systems operational.")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_jarvis_brain():
    """Test JARVIS brain"""
    print("\n🧠 Testing JARVIS Brain...")
    try:
        from core.jarvis_brain import JarvisBrain
        jarvis = JarvisBrain()
        
        print(f"   ✓ JARVIS brain initialized")
        print(f"   ✓ AI available: {jarvis.is_available()}")
        
        if jarvis.is_available():
            print(f"   ✓ Provider: {jarvis.provider}")
            print(f"   ✓ Model: {jarvis.model}")
        else:
            print("   ⚠ Add API keys to .env for full AI features")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_learning_engine():
    """Test learning engine"""
    print("\n📚 Testing Learning Engine...")
    try:
        from core.learning_engine import LearningEngine
        learning = LearningEngine()
        
        print(f"   ✓ Learning engine initialized")
        print(f"   ✓ Interactions tracked: {len(learning.interactions)}")
        print(f"   ✓ Insights generated: {len(learning.insights)}")
        print(f"   ✓ Relationship level: {learning.profile['relationship_level']:.1f}%")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_cognitive_monitor():
    """Test cognitive state monitor"""
    print("\n🧘 Testing Cognitive State Monitor...")
    try:
        from core.cognitive_state_monitor import CognitiveStateMonitor
        monitor = CognitiveStateMonitor()
        
        print(f"   ✓ Cognitive monitor initialized")
        
        state = monitor.get_current_state()
        print(f"   ✓ Energy level: {state['energy_level']}%")
        print(f"   ✓ Stress level: {state['stress_level']}%")
        print(f"   ✓ Decision quality: {state['decision_quality']}%")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_parallel_universe():
    """Test parallel universe viewer"""
    print("\n🌌 Testing Parallel Universe Viewer...")
    try:
        from core.parallel_universe_viewer import ParallelUniverseViewer
        viewer = ParallelUniverseViewer()
        
        print(f"   ✓ Universe viewer initialized")
        print(f"   ✓ Current persona: {viewer.current_persona}")
        print(f"   ✓ Available personas: {len(viewer.personas)}")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def test_flow_protector():
    """Test flow state protector"""
    print("\n🌊 Testing Flow State Protector...")
    try:
        from core.flow_state_protector import FlowStateProtector
        flow = FlowStateProtector()
        
        print(f"   ✓ Flow protector initialized")
        print(f"   ✓ In flow: {flow.in_flow_state}")
        
        stats = flow.get_flow_stats()
        print(f"   ✓ Total flow time: {stats['total_flow_time']} minutes")
        
        return True
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     🧪 NEURATWIN FEATURE TEST                            ║
║     Testing all world-class features...                  ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    # Run all tests
    results.append(("Activity Tracking", test_activity_tracking()))
    results.append(("Voice Interface", test_voice_interface()))
    results.append(("JARVIS Brain", test_jarvis_brain()))
    results.append(("Learning Engine", test_learning_engine()))
    results.append(("Cognitive Monitor", test_cognitive_monitor()))
    results.append(("Parallel Universe", test_parallel_universe()))
    results.append(("Flow Protector", test_flow_protector()))
    
    # Summary
    print("\n" + "="*60)
    print("📊 TEST SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    print(f"\n🎯 Score: {passed}/{total} tests passed")
    
    if passed == total:
        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ✅ ALL TESTS PASSED!                                  ║
║     NeuraTwin is ready for world-class performance!      ║
║                                                           ║
║     Run: python start_all.py                              ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)
    else:
        print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║     ⚠️ SOME TESTS FAILED                                  ║
║     Check the errors above and install missing deps      ║
║                                                           ║
║     Run: python setup_world_class.py                      ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
        """)

if __name__ == "__main__":
    main()

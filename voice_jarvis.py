"""
🎤 VOICE JARVIS - Talk to your cognitive twin
Run this to enable voice commands
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from core.voice_interface import get_voice_interface
from core.jarvis_brain import JarvisBrain
from core.cognitive_state_monitor import CognitiveStateMonitor
from core.learning_engine import LearningEngine

def main():
    print("=" * 60)
    print("🎤 VOICE JARVIS - Cognitive Twin Voice Interface")
    print("=" * 60)
    print()
    
    # Initialize systems
    print("🔧 Initializing systems...")
    voice = get_voice_interface()
    jarvis = JarvisBrain()
    state_monitor = CognitiveStateMonitor()
    learning_engine = LearningEngine()
    
    if not voice.is_available():
        print("❌ Voice interface not available!")
        print()
        print("Install required packages:")
        print("  pip install SpeechRecognition pyttsx3 pyaudio")
        print()
        return
    
    print("✅ Voice interface ready!")
    print()
    print("Commands:")
    print("  - Say 'JARVIS' to activate")
    print("  - Then ask your question")
    print("  - Say 'goodbye' or 'exit' to quit")
    print()
    print("Examples:")
    print("  'JARVIS, how am I doing?'")
    print("  'JARVIS, should I take a break?'")
    print("  'JARVIS, start flow mode'")
    print()
    print("-" * 60)
    print()
    
    # Run voice loop
    try:
        voice.run_voice_loop(jarvis, state_monitor, learning_engine)
    except KeyboardInterrupt:
        print("\n\n👋 Voice interface stopped")
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()

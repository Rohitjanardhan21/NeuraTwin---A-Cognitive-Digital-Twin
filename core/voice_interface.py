"""
🎤 VOICE INTERFACE - Talk to JARVIS
"Hey JARVIS, how am I doing?"
"""

import os
import json
from datetime import datetime

try:
    import speech_recognition as sr
    SR_AVAILABLE = True
except ImportError:
    SR_AVAILABLE = False
    print("⚠️ speech_recognition not installed. Run: pip install SpeechRecognition pyaudio")

try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("⚠️ pyttsx3 not installed. Run: pip install pyttsx3")


class VoiceInterface:
    """Voice interface for JARVIS"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer() if SR_AVAILABLE else None
        self.tts_engine = pyttsx3.init() if TTS_AVAILABLE else None
        
        if self.tts_engine:
            # Configure voice
            voices = self.tts_engine.getProperty('voices')
            # Try to use a male voice (JARVIS-like)
            for voice in voices:
                if 'male' in voice.name.lower() or 'david' in voice.name.lower():
                    self.tts_engine.setProperty('voice', voice.id)
                    break
            
            # Set speech rate (slightly slower for clarity)
            self.tts_engine.setProperty('rate', 175)
        
        self.wake_word = "jarvis"
        self.is_listening = False
    
    def is_available(self):
        """Check if voice interface is available"""
        return SR_AVAILABLE and TTS_AVAILABLE
    
    def speak(self, text):
        """Speak text using TTS"""
        if not TTS_AVAILABLE:
            print(f"🔊 JARVIS: {text}")
            return False
        
        try:
            print(f"🔊 JARVIS: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            return True
        except Exception as e:
            print(f"Error speaking: {e}")
            return False
    
    def listen(self, timeout=5):
        """Listen for voice command"""
        if not SR_AVAILABLE:
            return None
        
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=timeout)
                
                print("🔄 Processing...")
                text = self.recognizer.recognize_google(audio)
                print(f"📝 You said: {text}")
                return text.lower()
                
        except sr.WaitTimeoutError:
            print("⏱️ Listening timeout")
            return None
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
            return None
        except Exception as e:
            print(f"Error listening: {e}")
            return None
    
    def listen_for_wake_word(self, timeout=5):
        """Listen for wake word"""
        command = self.listen(timeout)
        if command and self.wake_word in command:
            return True
        return False
    
    def get_command(self):
        """Get voice command after wake word"""
        if not self.is_available():
            return None
        
        # Listen for wake word
        print(f"💤 Say '{self.wake_word}' to activate...")
        if not self.listen_for_wake_word(timeout=10):
            return None
        
        # Wake word detected
        self.speak("Yes sir?")
        
        # Listen for command
        command = self.listen(timeout=5)
        return command
    
    def process_command(self, command, jarvis_brain, state_monitor, learning_engine):
        """Process voice command and respond"""
        if not command:
            return None
        
        # Quick responses for common commands
        quick_responses = {
            "how am i": lambda: f"Your energy is at {state_monitor.energy_level}%, stress at {state_monitor.stress_level}%",
            "start flow": lambda: "Flow state activated, sir. I'll protect your focus time.",
            "stop flow": lambda: "Flow state ended. Well done, sir.",
            "take a break": lambda: "Good idea, sir. A brief respite will help.",
            "what time": lambda: f"It's {datetime.now().strftime('%I:%M %p')}, sir.",
            "thank you": lambda: "You're welcome, sir.",
            "goodbye": lambda: "Goodbye, sir. I'll be here when you need me."
        }
        
        # Check quick responses
        for trigger, response_func in quick_responses.items():
            if trigger in command:
                response = response_func()
                self.speak(response)
                return response
        
        # Use JARVIS brain for complex queries
        if jarvis_brain and jarvis_brain.is_available():
            try:
                response = jarvis_brain.chat(
                    command,
                    learning_engine.profile,
                    state_monitor.get_current_state(),
                    {"emotion": "neutral"}
                )
                self.speak(response)
                return response
            except Exception as e:
                print(f"Error with JARVIS brain: {e}")
        
        # Fallback response
        response = "I'm not sure how to help with that, sir. Could you rephrase?"
        self.speak(response)
        return response
    
    def run_voice_loop(self, jarvis_brain, state_monitor, learning_engine):
        """Run continuous voice command loop"""
        if not self.is_available():
            print("❌ Voice interface not available")
            return
        
        self.speak("JARVIS online. Voice interface activated.")
        self.is_listening = True
        
        try:
            while self.is_listening:
                command = self.get_command()
                if command:
                    if "goodbye" in command or "exit" in command:
                        self.speak("Goodbye, sir.")
                        break
                    
                    self.process_command(command, jarvis_brain, state_monitor, learning_engine)
        
        except KeyboardInterrupt:
            self.speak("Voice interface shutting down.")
        
        self.is_listening = False
    
    def stop(self):
        """Stop voice interface"""
        self.is_listening = False


# Global instance
_voice_interface = None

def get_voice_interface():
    """Get global voice interface instance"""
    global _voice_interface
    if _voice_interface is None:
        _voice_interface = VoiceInterface()
    return _voice_interface

"""
🤖 JARVIS BRAIN - AI-Powered Intelligence Core
Makes the twin truly conversational and intelligent like JARVIS
"""

import os
import json
from datetime import datetime
from openai import OpenAI
from anthropic import Anthropic


class JarvisBrain:
    """AI-powered conversational intelligence"""
    
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY')
        self.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
        
        # Initialize clients
        self.openai_client = None
        self.anthropic_client = None
        
        if self.openai_key and self.openai_key != 'your_openai_key_here':
            self.openai_client = OpenAI(api_key=self.openai_key)
            self.model = os.getenv('OPENAI_MODEL', 'gpt-4-turbo-preview')
            self.provider = 'openai'
        elif self.anthropic_key and self.anthropic_key != 'your_anthropic_key_here':
            self.anthropic_client = Anthropic(api_key=self.anthropic_key)
            self.model = os.getenv('ANTHROPIC_MODEL', 'claude-3-5-sonnet-20241022')
            self.provider = 'anthropic'
        else:
            self.provider = None
        
        # Conversation memory
        self.conversation_history = []
        self.max_history = 20
    
    def is_available(self):
        """Check if AI is available"""
        return self.provider is not None
    
    def _build_system_prompt(self, user_profile, current_state, context):
        """Build dynamic system prompt based on user data"""
        
        relationship_level = user_profile.get('relationship_level', 0)
        
        # Base personality
        base = """You are JARVIS - an advanced AI cognitive twin assistant. You are:

- Highly intelligent and conversational
- Proactive and anticipatory
- Witty but professional
- Deeply knowledgeable about the user
- Capable of nuanced understanding
- Direct and honest, never patronizing
- Supportive but not overly cheerful

You speak like JARVIS from Iron Man - sophisticated, slightly dry humor, extremely capable."""

        # Add user knowledge
        if relationship_level > 0:
            base += f"\n\nYou know the user at {relationship_level:.0f}% depth."
        
        if relationship_level > 30:
            base += "\nYou understand their patterns well and can make accurate predictions."
        
        if relationship_level > 60:
            base += "\nYou know them intimately and can anticipate their needs."
        
        # Add current context
        base += f"\n\nCurrent State:"
        base += f"\n- Energy: {current_state.get('energy_level', 50)}%"
        base += f"\n- Stress: {current_state.get('stress_level', 50)}%"
        base += f"\n- Decision Quality: {current_state.get('decision_quality', 50)}%"
        base += f"\n- Time: {datetime.now().strftime('%H:%M')}"
        
        # Add learned patterns
        if user_profile.get('energy_patterns'):
            base += "\n\nLearned Energy Patterns:"
            for hour, readings in list(user_profile['energy_patterns'].items())[:5]:
                avg = sum(readings) / len(readings)
                base += f"\n- {hour}:00 → {avg:.0f}% energy"
        
        if user_profile.get('decision_style'):
            top_keywords = sorted(user_profile['decision_style'].items(), 
                                key=lambda x: x[1], reverse=True)[:5]
            if top_keywords:
                words = [w[0] for w in top_keywords]
                base += f"\n\nUser focuses on: {', '.join(words)}"
        
        # Add context awareness
        if context.get('emotion') and context['emotion'] != 'neutral':
            base += f"\n\nUser's current emotion: {context['emotion']}"
        
        if context.get('urgency') == 'high':
            base += "\n\nUser needs urgent help - be direct and actionable."
        
        base += "\n\nRespond naturally and conversationally. Be helpful, insightful, and occasionally witty."
        
        return base
    
    def chat(self, message, user_profile, current_state, context):
        """Have a conversation with the user"""
        
        if not self.is_available():
            return self._fallback_response(message, context)
        
        # Build system prompt
        system_prompt = self._build_system_prompt(user_profile, current_state, context)
        
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": message
        })
        
        # Keep history manageable
        if len(self.conversation_history) > self.max_history:
            self.conversation_history = self.conversation_history[-self.max_history:]
        
        try:
            if self.provider == 'openai':
                response = self._chat_openai(system_prompt)
            else:
                response = self._chat_anthropic(system_prompt)
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": response
            })
            
            return response
            
        except Exception as e:
            print(f"AI Error: {e}")
            return self._fallback_response(message, context)
    
    def _chat_openai(self, system_prompt):
        """Chat using OpenAI"""
        messages = [{"role": "system", "content": system_prompt}]
        messages.extend(self.conversation_history)
        
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=0.8,
            max_tokens=500
        )
        
        return response.choices[0].message.content
    
    def _chat_anthropic(self, system_prompt):
        """Chat using Anthropic"""
        response = self.anthropic_client.messages.create(
            model=self.model,
            max_tokens=500,
            temperature=0.8,
            system=system_prompt,
            messages=self.conversation_history
        )
        
        return response.content[0].text
    
    def analyze_decision(self, decision, user_profile, current_state, parallel_responses):
        """Analyze a decision with AI intelligence"""
        
        if not self.is_available():
            return self._fallback_decision_analysis(decision, current_state)
        
        prompt = f"""Analyze this decision:

Decision: "{decision}"

Current State:
- Energy: {current_state.get('energy_level', 50)}%
- Stress: {current_state.get('stress_level', 50)}%
- Decision Quality: {current_state.get('decision_quality', 50)}%

Parallel Universe Responses:
- Cautious Self: {parallel_responses.get('cautious', {}).get('choice', 'N/A')}
- Ambitious Self: {parallel_responses.get('ambitious', {}).get('choice', 'N/A')}
- Balanced Self: {parallel_responses.get('balanced', {}).get('choice', 'N/A')}

Provide:
1. A direct recommendation (2-3 sentences)
2. Key considerations
3. Potential regrets if wrong
4. Best timing for this decision

Be like JARVIS - intelligent, direct, slightly witty."""

        try:
            if self.provider == 'openai':
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are JARVIS, an advanced AI assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=400
                )
                return response.choices[0].message.content
            else:
                response = self.anthropic_client.messages.create(
                    model=self.model,
                    max_tokens=400,
                    temperature=0.7,
                    system="You are JARVIS, an advanced AI assistant.",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
                
        except Exception as e:
            print(f"AI Error: {e}")
            return self._fallback_decision_analysis(decision, current_state)
    
    def generate_proactive_insight(self, user_profile, current_state, recent_interactions):
        """Generate proactive insights without being asked"""
        
        if not self.is_available():
            return None
        
        prompt = f"""Based on this user data, generate ONE proactive insight:

Relationship Level: {user_profile.get('relationship_level', 0):.0f}%
Total Interactions: {len(recent_interactions)}

Current State:
- Energy: {current_state.get('energy_level', 50)}%
- Stress: {current_state.get('stress_level', 50)}%
- Time: {datetime.now().strftime('%H:%M')}

Recent patterns detected:
{json.dumps(user_profile.get('energy_patterns', {}), indent=2)[:500]}

Generate a JARVIS-style proactive insight. Be:
- Observant and intelligent
- Slightly anticipatory
- Helpful but not pushy
- Occasionally witty

Format: Just the insight, 1-2 sentences, no preamble."""

        try:
            if self.provider == 'openai':
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": "You are JARVIS generating proactive insights."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.9,
                    max_tokens=150
                )
                return response.choices[0].message.content.strip()
            else:
                response = self.anthropic_client.messages.create(
                    model=self.model,
                    max_tokens=150,
                    temperature=0.9,
                    system="You are JARVIS generating proactive insights.",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text.strip()
                
        except Exception as e:
            print(f"AI Error: {e}")
            return None
    
    def _fallback_response(self, message, context):
        """Fallback when AI is not available"""
        responses = {
            "how am i": f"Your energy is at {context.get('energy_level', 50)}%. {context.get('recommendation', 'Keep going!')}",
            "what have you learned": "I need an API key to provide intelligent responses. Add OPENAI_API_KEY or ANTHROPIC_API_KEY to your .env file.",
            "tell me something": "Connect me to an AI provider (OpenAI or Anthropic) and I'll tell you fascinating insights!",
            "predict": "I can predict better with AI integration. Add your API key to .env file."
        }
        
        for key, value in responses.items():
            if key in message.lower():
                return value
        
        return "I'm running in basic mode. Add OPENAI_API_KEY or ANTHROPIC_API_KEY to .env for full AI intelligence!"
    
    def _fallback_decision_analysis(self, decision, current_state):
        """Fallback decision analysis"""
        energy = current_state.get('energy_level', 50)
        stress = current_state.get('stress_level', 50)
        
        if energy < 30:
            return "Your energy is critically low. I'd recommend postponing this decision until you're more alert."
        elif stress > 70:
            return "High stress detected. Take a moment to breathe before deciding. Stressed decisions often lead to regret."
        elif energy > 70 and stress < 30:
            return "You're in an optimal state for decision-making. Your mind is clear and energy is high. Good time to decide."
        else:
            return "Your state is moderate. Consider the pros and cons carefully. If it's urgent, proceed. If not, wait for better clarity."
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

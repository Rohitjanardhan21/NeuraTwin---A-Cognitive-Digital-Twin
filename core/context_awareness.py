"""
🎯 CONTEXT AWARENESS ENGINE
Makes the twin understand context and respond intelligently
"""

import json
import os
from datetime import datetime, timedelta
import re


class ContextAwarenessEngine:
    """Understands context and provides intelligent responses"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.context_file = f"{data_dir}/context_memory.json"
        self.context_memory = self._load_context()
        
        # Conversation state
        self.current_topic = None
        self.conversation_history = []
        self.user_mood = "neutral"
        self.last_interaction = None
    
    def _load_context(self):
        """Load context memory"""
        if os.path.exists(self.context_file):
            with open(self.context_file, 'r') as f:
                return json.load(f)
        
        return {
            "topics_discussed": {},
            "user_concerns": [],
            "goals": [],
            "challenges": [],
            "wins": [],
            "last_topics": []
        }
    
    def _save_context(self):
        """Save context memory"""
        os.makedirs(self.data_dir, exist_ok=True)
        with open(self.context_file, 'w') as f:
            json.dump(self.context_memory, f, indent=2)
    
    def understand_query(self, query):
        """Understand user query with context"""
        query_lower = query.lower()
        
        # Detect intent
        intent = self._detect_intent(query_lower)
        
        # Detect emotion
        emotion = self._detect_emotion(query_lower)
        
        # Extract entities
        entities = self._extract_entities(query)
        
        # Detect urgency
        urgency = self._detect_urgency(query_lower)
        
        # Update context
        self._update_context(query, intent, emotion, entities)
        
        return {
            "query": query,
            "intent": intent,
            "emotion": emotion,
            "entities": entities,
            "urgency": urgency,
            "context": self.current_topic,
            "timestamp": datetime.now().isoformat()
        }
    
    def _detect_intent(self, query):
        """Detect user intent"""
        intents = {
            "question": ["what", "how", "why", "when", "where", "who", "?"],
            "command": ["start", "stop", "show", "tell", "give", "help"],
            "concern": ["worried", "anxious", "stressed", "problem", "issue"],
            "celebration": ["great", "awesome", "amazing", "won", "success"],
            "decision": ["should i", "should we", "what if", "or"],
            "feedback": ["good", "bad", "better", "worse", "like", "dislike"],
            "exploration": ["explore", "try", "experiment", "test", "check"]
        }
        
        for intent, keywords in intents.items():
            if any(keyword in query for keyword in keywords):
                return intent
        
        return "statement"
    
    def _detect_emotion(self, query):
        """Detect emotional tone"""
        emotions = {
            "excited": ["excited", "amazing", "awesome", "great", "love", "!"],
            "worried": ["worried", "anxious", "scared", "nervous", "concerned"],
            "frustrated": ["frustrated", "annoyed", "stuck", "can't", "won't"],
            "tired": ["tired", "exhausted", "drained", "sleepy", "fatigue"],
            "confused": ["confused", "don't understand", "unclear", "?"],
            "motivated": ["motivated", "ready", "let's go", "pumped"],
            "calm": ["calm", "peaceful", "relaxed", "fine", "okay"]
        }
        
        for emotion, keywords in emotions.items():
            if any(keyword in query for keyword in keywords):
                self.user_mood = emotion
                return emotion
        
        return "neutral"
    
    def _extract_entities(self, query):
        """Extract important entities from query"""
        entities = {
            "time": [],
            "topics": [],
            "actions": [],
            "tools": []
        }
        
        # Time entities
        time_patterns = [
            r'\d+\s*(hour|minute|day|week|month)',
            r'(morning|afternoon|evening|night|today|tomorrow)',
            r'(now|later|soon|eventually)'
        ]
        
        for pattern in time_patterns:
            matches = re.findall(pattern, query.lower())
            entities["time"].extend(matches)
        
        # Common topics
        topics = ["work", "project", "code", "meeting", "decision", "break", 
                 "energy", "stress", "focus", "flow", "productivity"]
        
        for topic in topics:
            if topic in query.lower():
                entities["topics"].append(topic)
        
        # Actions
        actions = ["start", "stop", "continue", "pause", "finish", "begin"]
        for action in actions:
            if action in query.lower():
                entities["actions"].append(action)
        
        return entities
    
    def _detect_urgency(self, query):
        """Detect urgency level"""
        urgent_keywords = ["urgent", "asap", "now", "immediately", "critical", 
                          "emergency", "quick", "fast", "hurry"]
        
        if any(keyword in query for keyword in urgent_keywords):
            return "high"
        
        if "?" in query or "should" in query:
            return "medium"
        
        return "low"
    
    def _update_context(self, query, intent, emotion, entities):
        """Update context memory"""
        # Update current topic
        if entities["topics"]:
            self.current_topic = entities["topics"][0]
            
            # Track topic frequency
            topic = self.current_topic
            if topic not in self.context_memory["topics_discussed"]:
                self.context_memory["topics_discussed"][topic] = 0
            self.context_memory["topics_discussed"][topic] += 1
        
        # Track concerns
        if intent == "concern":
            self.context_memory["user_concerns"].append({
                "concern": query,
                "timestamp": datetime.now().isoformat()
            })
            self.context_memory["user_concerns"] = \
                self.context_memory["user_concerns"][-20:]  # Keep last 20
        
        # Track wins
        if emotion == "excited" or intent == "celebration":
            self.context_memory["wins"].append({
                "win": query,
                "timestamp": datetime.now().isoformat()
            })
            self.context_memory["wins"] = \
                self.context_memory["wins"][-20:]  # Keep last 20
        
        # Update conversation history
        self.conversation_history.append({
            "query": query,
            "intent": intent,
            "emotion": emotion,
            "timestamp": datetime.now().isoformat()
        })
        self.conversation_history = self.conversation_history[-50:]  # Keep last 50
        
        self.last_interaction = datetime.now()
        self._save_context()
    
    def generate_contextual_response(self, query, base_response):
        """Generate contextual response"""
        understanding = self.understand_query(query)
        
        # Add emotional intelligence
        if understanding["emotion"] == "worried":
            prefix = "I sense you're concerned. "
        elif understanding["emotion"] == "excited":
            prefix = "I can feel your excitement! "
        elif understanding["emotion"] == "frustrated":
            prefix = "I understand your frustration. "
        elif understanding["emotion"] == "tired":
            prefix = "You sound tired. "
        else:
            prefix = ""
        
        # Add urgency awareness
        if understanding["urgency"] == "high":
            suffix = " Let's address this right away."
        elif understanding["urgency"] == "medium":
            suffix = " Let me help you figure this out."
        else:
            suffix = ""
        
        # Add context continuity
        if self.current_topic and self.current_topic in query.lower():
            context_note = f" (Continuing our discussion about {self.current_topic})"
        else:
            context_note = ""
        
        return f"{prefix}{base_response}{suffix}{context_note}"
    
    def get_conversation_summary(self):
        """Get summary of recent conversation"""
        if not self.conversation_history:
            return "No recent conversation"
        
        recent = self.conversation_history[-10:]
        
        # Count intents
        intent_counts = {}
        for conv in recent:
            intent = conv["intent"]
            intent_counts[intent] = intent_counts.get(intent, 0) + 1
        
        top_intent = max(intent_counts, key=intent_counts.get)
        
        # Detect mood trend
        emotions = [conv["emotion"] for conv in recent]
        current_mood = emotions[-1] if emotions else "neutral"
        
        return {
            "message_count": len(recent),
            "primary_intent": top_intent,
            "current_mood": current_mood,
            "topics": list(set([conv.get("topic") for conv in recent if conv.get("topic")])),
            "last_interaction": self.last_interaction.isoformat() if self.last_interaction else None
        }
    
    def get_smart_suggestions(self, current_state):
        """Get smart suggestions based on context"""
        suggestions = []
        
        # Based on recent concerns
        if self.context_memory["user_concerns"]:
            recent_concerns = self.context_memory["user_concerns"][-3:]
            if len(recent_concerns) > 2:
                suggestions.append({
                    "type": "concern",
                    "message": "You've had several concerns recently. Want to talk about what's bothering you?",
                    "action": "open_chat"
                })
        
        # Based on wins
        if self.context_memory["wins"]:
            recent_wins = self.context_memory["wins"][-5:]
            if len(recent_wins) > 0:
                suggestions.append({
                    "type": "celebration",
                    "message": f"You've had {len(recent_wins)} wins recently! Keep the momentum going!",
                    "action": "show_wins"
                })
        
        # Based on time since last interaction
        if self.last_interaction:
            time_since = datetime.now() - self.last_interaction
            if time_since > timedelta(hours=4):
                suggestions.append({
                    "type": "check_in",
                    "message": "It's been a while! How are things going?",
                    "action": "check_in"
                })
        
        # Based on current state
        if current_state.get("energy_level", 50) < 30:
            suggestions.append({
                "type": "energy",
                "message": "Your energy is low. Time for a break?",
                "action": "suggest_break"
            })
        
        return suggestions

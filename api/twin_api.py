"""
🌐 COGNITIVE TWIN API
RESTful API for web and mobile interfaces
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os
from pathlib import Path
import json
from datetime import datetime

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.cognitive_state_monitor import CognitiveStateMonitor
from core.parallel_universe_viewer import ParallelUniverseViewer
from core.decision_intervention import DecisionInterventionSystem
from core.regret_predictor import RegretPredictor
from core.flow_state_protector import FlowStateProtector
from core.decision_tracker import DecisionTracker
from core.pattern_analyzer import PatternAnalyzer
from core.learning_engine import LearningEngine
from core.context_awareness import ContextAwarenessEngine
from core.jarvis_brain import JarvisBrain
from core.proactive_assistant import ProactiveAssistant
from core.activity_tracker import get_tracker
from core.voice_interface import get_voice_interface

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile/web

# Initialize systems
state_monitor = CognitiveStateMonitor()
universe_viewer = ParallelUniverseViewer()
decision_tracker = DecisionTracker()
pattern_analyzer = PatternAnalyzer()
intervention_system = DecisionInterventionSystem(decision_tracker, pattern_analyzer)
regret_predictor = RegretPredictor(decision_tracker)
flow_protector = FlowStateProtector()
learning_engine = LearningEngine()
context_engine = ContextAwarenessEngine()
jarvis = JarvisBrain()
proactive = ProactiveAssistant()
activity_tracker = get_tracker()
voice_interface = get_voice_interface()


# ============= VIRTUAL ASSISTANT ENDPOINTS =============

@app.route('/api/assistant/greeting', methods=['GET'])
def get_greeting():
    """Get personalized greeting"""
    # Learn from interaction
    state = state_monitor.get_current_state()
    learning_engine.learn_from_interaction("state_check", state)
    
    # Get JARVIS-style greeting
    greeting = proactive.get_contextual_greeting(learning_engine.profile, state)
    
    # Get smart recommendation
    recommendation = learning_engine.get_smart_recommendation(state)
    
    # Generate insight
    insight = learning_engine.generate_insight()
    
    # Get proactive suggestions
    suggestions = proactive.get_proactive_suggestions(
        state, 
        learning_engine.profile, 
        datetime.now().hour
    )
    
    # Get ambient commentary
    commentary = proactive.generate_ambient_commentary(state, {})
    
    return jsonify({
        "greeting": greeting,
        "message": recommendation,
        "energy": state["energy_level"],
        "mood": "great" if state["energy_level"] > 70 else "okay" if state["energy_level"] > 40 else "tired",
        "insight": insight,
        "relationship_level": learning_engine.profile["relationship_level"],
        "suggestions": suggestions,
        "commentary": commentary,
        "ai_available": jarvis.is_available()
    })


@app.route('/api/assistant/briefing', methods=['GET'])
def get_briefing():
    """Get daily briefing"""
    state = state_monitor.get_current_state()
    stats = state_monitor.get_daily_stats()
    
    # Get prediction from learning engine
    prediction = learning_engine.predict_next_state(datetime.now().hour)
    
    # Get recent insights
    insights = learning_engine.get_recent_insights(3)
    
    # Get smart suggestions
    suggestions = context_engine.get_smart_suggestions(state)
    
    # Get profile summary
    profile = learning_engine.get_profile_summary()
    
    return jsonify({
        "current_state": state,
        "daily_stats": stats,
        "prediction": prediction,
        "insights": insights,
        "suggestions": suggestions,
        "profile": profile,
        "recommendations": [
            learning_engine.get_smart_recommendation(state),
            prediction["message"]
        ]
    })


@app.route('/api/assistant/ask', methods=['POST'])
def ask_assistant():
    """Ask the assistant anything - JARVIS-powered"""
    data = request.json
    question = data.get('question', '')
    
    # Understand query with context
    understanding = context_engine.understand_query(question)
    
    # Learn from interaction
    learning_engine.learn_from_interaction("question", {
        "question": question,
        "understanding": understanding
    })
    
    # Get current state
    state = state_monitor.get_current_state()
    
    # Use JARVIS brain for intelligent response
    if jarvis.is_available():
        answer = jarvis.chat(
            question,
            learning_engine.profile,
            state,
            understanding
        )
    else:
        # Fallback to smart responses
        responses = {
            "how am i": learning_engine.get_smart_recommendation(state),
            "should i take a break": "Yes, take a break!" if state['energy_level'] < 50 else "You're doing fine, but a break never hurts!",
            "am i productive": f"You've had {state_monitor.get_daily_stats()['total_focus_time']} minutes of focus time today.",
            "can i make decisions": "Yes, your decision quality is good!" if state['decision_quality'] > 70 else "Wait a bit, your decision quality is low right now.",
            "what should i do": learning_engine.get_smart_recommendation(state),
            "how do you know me": f"I've learned from {learning_engine.profile['relationship_level']:.0f}% of our interactions. I'm getting to know you!",
            "what have you learned": f"I've tracked {len(learning_engine.interactions)} interactions and generated {len(learning_engine.insights)} insights about you.",
            "tell me something": learning_engine.generate_insight() or {"message": "Keep using me and I'll learn more about you!"},
            "what's my pattern": f"You often think about: {', '.join(list(learning_engine.profile['decision_style'].keys())[:3]) if learning_engine.profile['decision_style'] else 'not enough data yet'}",
            "predict": learning_engine.predict_next_state(datetime.now().hour)["message"],
            "insight": learning_engine.generate_insight() or {"message": "I need more data to generate insights"}
        }
        
        # Find matching response
        answer = "I'm here to help! Ask me about your energy, productivity, decisions, or what I've learned about you."
        for key, value in responses.items():
            if key in question.lower():
                if isinstance(value, dict):
                    answer = value.get("message", str(value))
                else:
                    answer = value
                break
        
        # Add contextual intelligence
        answer = context_engine.generate_contextual_response(question, answer)
    
    # Get conversation summary
    conversation_summary = context_engine.get_conversation_summary()
    
    return jsonify({
        "question": question,
        "answer": answer,
        "understanding": understanding,
        "conversation_summary": conversation_summary,
        "ai_powered": jarvis.is_available(),
        "timestamp": datetime.now().isoformat()
    })


# ============= STATE MONITORING ENDPOINTS =============

@app.route('/api/state/current', methods=['GET'])
def get_current_state():
    """Get current cognitive state"""
    state = state_monitor.get_current_state()
    
    # Learn from state check
    learning_engine.learn_from_interaction("state_check", state)
    
    # Add smart recommendation
    state["smart_recommendation"] = learning_engine.get_smart_recommendation(state)
    
    return jsonify(state)


@app.route('/api/state/daily', methods=['GET'])
def get_daily_stats():
    """Get daily statistics"""
    return jsonify(state_monitor.get_daily_stats())


@app.route('/api/state/activity', methods=['POST'])
def log_activity():
    """Log user activity"""
    data = request.json
    activity_type = data.get('type', 'typing')
    duration = data.get('duration', 1)
    
    state_monitor.log_activity(activity_type, duration)
    
    return jsonify({"success": True, "message": "Activity logged"})


# ============= DECISION ENDPOINTS =============

@app.route('/api/decision/check', methods=['POST'])
def check_decision():
    """Check a decision - JARVIS-powered analysis"""
    data = request.json
    decision = data.get('decision', '')
    context = data.get('context', {})
    
    # Add current state to context
    if not context:
        context = {
            "stress_level": state_monitor.stress_level,
            "energy_level": state_monitor.energy_level,
            "decision_quality": state_monitor.decision_quality,
            "decision": decision
        }
    
    # Learn from decision
    learning_engine.learn_from_interaction("decision", {
        "decision": decision,
        "context": context
    })
    
    # Get regret prediction
    regret = regret_predictor.predict_regret(decision, context)
    
    # Check intervention
    intervention = intervention_system.check_decision(decision, context)
    
    # Get parallel responses
    responses = universe_viewer.present_decision(decision, context)
    
    # Get contextual insight
    understanding = context_engine.understand_query(decision)
    
    # Get JARVIS analysis
    jarvis_analysis = None
    if jarvis.is_available():
        jarvis_analysis = jarvis.analyze_decision(
            decision,
            learning_engine.profile,
            state_monitor.get_current_state(),
            responses
        )
    
    return jsonify({
        "decision": decision,
        "regret": regret,
        "intervention": intervention,
        "parallel_responses": responses,
        "understanding": understanding,
        "jarvis_analysis": jarvis_analysis,
        "smart_note": context_engine.generate_contextual_response(
            decision, 
            "Decision analyzed"
        ),
        "ai_powered": jarvis.is_available(),
        "timestamp": datetime.now().isoformat()
    })


@app.route('/api/decision/add', methods=['POST'])
def add_decision():
    """Add a decision to history"""
    data = request.json
    
    decision_id = decision_tracker.add_decision(
        decision=data.get('decision'),
        reason=data.get('reason'),
        alternatives=data.get('alternatives', []),
        constraints=data.get('constraints', {}),
        outcome=data.get('outcome'),
        tags=data.get('tags', [])
    )
    
    return jsonify({"success": True, "decision_id": decision_id})


@app.route('/api/decision/history', methods=['GET'])
def get_decision_history():
    """Get decision history"""
    limit = request.args.get('limit', 10, type=int)
    decisions = decision_tracker.get_recent_decisions(limit)
    
    return jsonify({"decisions": decisions})


# ============= PARALLEL UNIVERSE ENDPOINTS =============

@app.route('/api/universe/view', methods=['GET'])
def get_universe_view():
    """Get parallel universe view"""
    return jsonify(universe_viewer.get_daily_comparison())


@app.route('/api/universe/switch', methods=['POST'])
def switch_universe():
    """Switch to different persona"""
    data = request.json
    persona = data.get('persona', 'balanced')
    
    result = universe_viewer.switch_timeline(persona)
    return jsonify(result)


# ============= FLOW STATE ENDPOINTS =============

@app.route('/api/flow/status', methods=['GET'])
def get_flow_status():
    """Get flow state status"""
    return jsonify(flow_protector.get_flow_stats())


@app.route('/api/flow/start', methods=['POST'])
def start_flow():
    """Start flow session"""
    flow_protector.enter_flow_state()
    
    # Learn from flow start
    learning_engine.learn_from_interaction("flow_start", {
        "time": datetime.now().isoformat(),
        "hour": datetime.now().hour
    })
    
    return jsonify({"success": True, "message": "Flow state activated"})


@app.route('/api/flow/end', methods=['POST'])
def end_flow():
    """End flow session"""
    flow_protector.exit_flow_state()
    return jsonify({"success": True, "message": "Flow state ended"})


# ============= DAEMON STATUS ENDPOINT =============

@app.route('/api/daemon/status', methods=['GET'])
def get_daemon_status():
    """Get daemon status"""
    status_file = "data/daemon_status.json"
    
    if os.path.exists(status_file):
        with open(status_file, 'r') as f:
            status = json.load(f)
        return jsonify(status)
    
    return jsonify({"running": False, "message": "Daemon not running"})


# ============= INTELLIGENCE ENDPOINTS =============

@app.route('/api/intelligence/insights', methods=['GET'])
def get_insights():
    """Get recent insights"""
    limit = request.args.get('limit', 5, type=int)
    insights = learning_engine.get_recent_insights(limit)
    
    return jsonify({
        "insights": insights,
        "total": len(learning_engine.insights)
    })


@app.route('/api/intelligence/profile', methods=['GET'])
def get_profile():
    """Get learning profile"""
    profile = learning_engine.get_profile_summary()
    
    return jsonify(profile)


@app.route('/api/intelligence/predict', methods=['POST'])
def predict_state():
    """Predict future state"""
    data = request.json
    hours_ahead = data.get('hours', 1)
    
    current_hour = datetime.now().hour
    predictions = []
    
    for i in range(1, hours_ahead + 1):
        pred = learning_engine.predict_next_state((current_hour + i) % 24)
        predictions.append(pred)
    
    return jsonify({
        "predictions": predictions,
        "confidence": predictions[0]["confidence"] if predictions else 0
    })


@app.route('/api/intelligence/suggestions', methods=['GET'])
def get_suggestions():
    """Get smart suggestions"""
    state = state_monitor.get_current_state()
    suggestions = context_engine.get_smart_suggestions(state)
    
    return jsonify({
        "suggestions": suggestions,
        "count": len(suggestions)
    })


@app.route('/api/intelligence/conversation', methods=['GET'])
def get_conversation():
    """Get conversation summary"""
    summary = context_engine.get_conversation_summary()
    
    return jsonify(summary)


@app.route('/api/intelligence/generate_insight', methods=['POST'])
def generate_new_insight():
    """Force generate a new insight"""
    insight = learning_engine.generate_insight()
    
    if insight:
        return jsonify(insight)
    else:
        return jsonify({
            "message": "Not enough data yet. Keep using the system!",
            "interactions_needed": max(0, 10 - len(learning_engine.interactions))
        })


@app.route('/api/jarvis/proactive', methods=['GET'])
def get_proactive_suggestions():
    """Get JARVIS proactive suggestions"""
    state = state_monitor.get_current_state()
    suggestions = proactive.get_proactive_suggestions(
        state,
        learning_engine.profile,
        datetime.now().hour
    )
    
    return jsonify({
        "suggestions": suggestions,
        "count": len(suggestions)
    })


@app.route('/api/jarvis/commentary', methods=['GET'])
def get_ambient_commentary():
    """Get JARVIS ambient commentary"""
    state = state_monitor.get_current_state()
    commentary = proactive.generate_ambient_commentary(state, {})
    
    return jsonify({
        "commentary": commentary,
        "timestamp": datetime.now().isoformat()
    })


@app.route('/api/jarvis/proactive_insight', methods=['POST'])
def generate_proactive_insight():
    """Generate proactive AI insight"""
    if not jarvis.is_available():
        return jsonify({
            "error": "AI not available",
            "message": "Add OPENAI_API_KEY or ANTHROPIC_API_KEY to .env file"
        }), 503
    
    state = state_monitor.get_current_state()
    insight = jarvis.generate_proactive_insight(
        learning_engine.profile,
        state,
        learning_engine.interactions[-20:]
    )
    
    return jsonify({
        "insight": insight,
        "timestamp": datetime.now().isoformat()
    })


@app.route('/api/jarvis/status', methods=['GET'])
def get_jarvis_status():
    """Get JARVIS system status"""
    return jsonify({
        "ai_available": jarvis.is_available(),
        "provider": jarvis.provider if jarvis.is_available() else None,
        "model": jarvis.model if jarvis.is_available() else None,
        "conversation_length": len(jarvis.conversation_history),
        "relationship_level": learning_engine.profile["relationship_level"],
        "total_interactions": len(learning_engine.interactions),
        "insights_generated": len(learning_engine.insights),
        "activity_tracking": activity_tracker.is_tracking,
        "voice_available": voice_interface.is_available()
    })


# ============= ACTIVITY TRACKING ENDPOINTS =============

@app.route('/api/activity/start', methods=['POST'])
def start_activity_tracking():
    """Start real activity tracking"""
    success = activity_tracker.start_tracking()
    return jsonify({
        "success": success,
        "message": "Activity tracking started" if success else "Failed to start tracking",
        "is_tracking": activity_tracker.is_tracking
    })


@app.route('/api/activity/stop', methods=['POST'])
def stop_activity_tracking():
    """Stop activity tracking"""
    activity_tracker.stop_tracking()
    return jsonify({
        "success": True,
        "message": "Activity tracking stopped",
        "is_tracking": activity_tracker.is_tracking
    })


@app.route('/api/activity/status', methods=['GET'])
def get_activity_status():
    """Get current activity status"""
    return jsonify(activity_tracker.get_stats_summary())


@app.route('/api/activity/level', methods=['GET'])
def get_activity_level():
    """Get current activity level"""
    minutes = request.args.get('minutes', 5, type=int)
    return jsonify(activity_tracker.get_activity_level(minutes))


@app.route('/api/activity/focus', methods=['GET'])
def get_focus_score():
    """Get current focus score"""
    minutes = request.args.get('minutes', 10, type=int)
    return jsonify(activity_tracker.get_focus_score(minutes))


# ============= VOICE INTERFACE ENDPOINTS =============

@app.route('/api/voice/status', methods=['GET'])
def get_voice_status():
    """Get voice interface status"""
    return jsonify({
        "available": voice_interface.is_available(),
        "is_listening": voice_interface.is_listening,
        "wake_word": voice_interface.wake_word
    })


@app.route('/api/voice/speak', methods=['POST'])
def voice_speak():
    """Make JARVIS speak"""
    data = request.json
    text = data.get('text', '')
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    success = voice_interface.speak(text)
    return jsonify({
        "success": success,
        "text": text
    })


@app.route('/api/voice/listen', methods=['POST'])
def voice_listen():
    """Listen for voice command"""
    timeout = request.json.get('timeout', 5) if request.json else 5
    
    command = voice_interface.listen(timeout)
    return jsonify({
        "command": command,
        "success": command is not None
    })


# ============= HEALTH CHECK =============

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "2.0"
    })


# ============= ROOT =============

@app.route('/')
def index():
    """API documentation"""
    return jsonify({
        "name": "Cognitive Twin API",
        "version": "3.0 - Intelligent Edition",
        "endpoints": {
            "assistant": [
                "GET /api/assistant/greeting",
                "GET /api/assistant/briefing",
                "POST /api/assistant/ask"
            ],
            "state": [
                "GET /api/state/current",
                "GET /api/state/daily",
                "POST /api/state/activity"
            ],
            "decision": [
                "POST /api/decision/check",
                "POST /api/decision/add",
                "GET /api/decision/history"
            ],
            "universe": [
                "GET /api/universe/view",
                "POST /api/universe/switch"
            ],
            "flow": [
                "GET /api/flow/status",
                "POST /api/flow/start",
                "POST /api/flow/end"
            ],
            "intelligence": [
                "GET /api/intelligence/insights",
                "GET /api/intelligence/profile",
                "POST /api/intelligence/predict",
                "GET /api/intelligence/suggestions",
                "GET /api/intelligence/conversation",
                "POST /api/intelligence/generate_insight"
            ],
            "daemon": [
                "GET /api/daemon/status"
            ]
        },
        "features": [
            "🧠 Learning Engine - Learns from every interaction",
            "🎯 Context Awareness - Understands emotional context",
            "📊 Pattern Recognition - Detects your patterns",
            "🔮 Predictive Intelligence - Predicts future states",
            "💡 Smart Insights - Generates personalized insights",
            "🤝 Relationship Building - Gets to know you over time"
        ]
    })


if __name__ == '__main__':
    print("🚀 Starting Cognitive Twin API...")
    print("📡 API running on http://localhost:5001")
    print("📱 Mobile/Web interfaces can connect now\n")
    app.run(debug=True, host='0.0.0.0', port=5001)

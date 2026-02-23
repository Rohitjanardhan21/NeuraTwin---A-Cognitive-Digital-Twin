"""
🌐 WEB INTERFACE - Beautiful UI for your cognitive twin
Flask-based web interface with real-time updates
"""

import sys
sys.path.append('..')

from flask import Flask, render_template, request, jsonify
from twin import CognitiveTwin
import json

app = Flask(__name__)
twin = CognitiveTwin()


@app.route('/')
def index():
    """Main dashboard"""
    return render_template('index.html')


@app.route('/api/stats')
def get_stats():
    """Get cognitive statistics"""
    decisions = twin.decisions.get_decision_timeline()
    patterns = twin.analyzer.patterns
    
    return jsonify({
        'total_decisions': len(decisions),
        'patterns': patterns,
        'recent_decisions': twin.decisions.get_recent_decisions(5)
    })


@app.route('/api/decision', methods=['POST'])
def add_decision():
    """Add a new decision"""
    data = request.json
    decision_id = twin.add_decision(
        decision=data['decision'],
        reason=data['reason'],
        alternatives=data.get('alternatives', []),
        constraints=data.get('constraints', {}),
        outcome=data.get('outcome'),
        tags=data.get('tags', [])
    )
    return jsonify({'success': True, 'decision_id': decision_id})


@app.route('/api/biases')
def detect_biases():
    """Detect cognitive biases"""
    biases = twin.detect_biases()
    return jsonify({'biases': biases})


@app.route('/api/multiverse', methods=['POST'])
def simulate_multiverse():
    """Simulate alternate timeline"""
    data = request.json
    simulation = twin.simulate_multiverse(
        data['current_path'],
        data['alternative']
    )
    return jsonify(simulation)


@app.route('/api/future')
def predict_future():
    """Predict future trajectory"""
    prediction = twin.predict_future()
    return jsonify(prediction)


@app.route('/api/parallel', methods=['POST'])
def generate_parallel():
    """Generate parallel selves"""
    data = request.json
    parallel = twin.generate_parallel_selves(data['problem'])
    return jsonify(parallel)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

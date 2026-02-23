"""
🌐 COGNITIVE TWIN WEB INTERFACE
Full virtual assistant web app
"""

from flask import Flask, render_template, request, jsonify
import requests
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

app = Flask(__name__)

# API base URL
API_URL = "http://localhost:5001/api"


@app.route('/')
def index():
    """Main dashboard"""
    return render_template('assistant.html')


@app.route('/mobile')
def mobile():
    """Mobile-optimized interface"""
    return render_template('mobile.html')


if __name__ == '__main__':
    print("🌐 Starting Cognitive Twin Web Interface...")
    print("📱 Web: http://localhost:5002")
    print("📱 Mobile: http://localhost:5002/mobile\n")
    app.run(debug=True, host='0.0.0.0', port=5002)

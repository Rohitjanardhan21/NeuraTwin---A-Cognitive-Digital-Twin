# 🚀 How To Use Your Cognitive Twin

## Quick Start (3 Steps)

### 1. Install Dependencies
```bash
cd cognitive-twin
pip install -r requirements.txt
pip install -r api/requirements.txt
```

### 2. Start All Services
```bash
python start_all.py
```

This starts:
- 📡 API Server (port 5001)
- 🌐 Web Interface (port 5002)

### 3. Open Your Browser
- **Desktop:** http://localhost:5002
- **Mobile:** http://localhost:5002/mobile

---

## What You Can Do

### 🌐 Web Interface
Open http://localhost:5002 to see:
- Real-time cognitive state monitoring
- Energy, stress, decision quality meters
- Parallel universe viewer
- Flow state tracker
- Chat with your twin
- Decision checker

### 📱 Mobile Interface
Open http://localhost:5002/mobile on your phone:
- Mobile-optimized dashboard
- Quick decision checks
- One-tap flow state control
- Energy monitoring
- Break reminders

### 🤖 Background Daemon (Optional)
Run the daemon for continuous monitoring:
```bash
python daemon/twin_daemon.py
```

This runs in background and:
- Monitors your activity
- Detects flow state
- Sends alerts
- Tracks patterns

---

## Daily Usage

### Morning Routine
1. Open web interface
2. Check your briefing
3. See energy prediction
4. Plan your day

### During Work
1. Daemon monitors you silently
2. Alerts when energy drops
3. Protects flow state
4. Blocks interruptions

### Before Decisions
1. Open decision checker
2. Enter your decision
3. See regret probability
4. Check parallel selves
5. Make informed choice

### Evening
1. Review daily stats
2. See which universe won
3. Get insights
4. Plan tomorrow

---

## API Endpoints

### Assistant
```bash
# Get greeting
GET http://localhost:5001/api/assistant/greeting

# Get daily briefing
GET http://localhost:5001/api/assistant/briefing

# Ask question
POST http://localhost:5001/api/assistant/ask
{
  "question": "How am I doing?"
}
```

### State Monitoring
```bash
# Get current state
GET http://localhost:5001/api/state/current

# Log activity
POST http://localhost:5001/api/state/activity
{
  "type": "typing",
  "duration": 5
}
```

### Decision Checking
```bash
# Check decision
POST http://localhost:5001/api/decision/check
{
  "decision": "Should I quit my job?"
}

# Add decision to history
POST http://localhost:5001/api/decision/add
{
  "decision": "Chose Python over JavaScript",
  "reason": "Better for ML",
  "tags": ["tech", "language"]
}
```

### Flow State
```bash
# Get flow status
GET http://localhost:5001/api/flow/status

# Start flow session
POST http://localhost:5001/api/flow/start

# End flow session
POST http://localhost:5001/api/flow/end
```

---

## Integration Examples

### Browser Extension (Future)
```javascript
// Check before sending email
fetch('http://localhost:5001/api/decision/check', {
  method: 'POST',
  body: JSON.stringify({
    decision: "Send this email to boss"
  })
})
```

### IDE Plugin (Future)
```python
# Before committing code
twin.check_decision(
    "Commit this refactor?",
    context={"time": "11pm", "stress": 75}
)
```

### Slack Bot (Future)
```
/twin check "Should I take this meeting?"
```

---

## Troubleshooting

### Services Won't Start
```bash
# Check if ports are in use
netstat -an | findstr "5001"
netstat -an | findstr "5002"

# Kill processes if needed
# Then restart
```

### API Not Responding
```bash
# Test API directly
curl http://localhost:5001/api/health
```

### Web Interface Not Loading
1. Check API is running (port 5001)
2. Check web server is running (port 5002)
3. Clear browser cache
4. Try incognito mode

---

## Advanced Usage

### Custom Intervention Rules
Edit `core/decision_intervention.py` to add your own rules.

### Custom Prompts
Edit `prompts/system_prompts.py` to customize AI responses.

### Data Export
All data is in `data/` folder:
- `decisions.json` - Your decisions
- `patterns.json` - Detected patterns
- `daemon_status.json` - Current state

---

## Mobile App (Future)

The mobile interface works in browser now. Future native app will add:
- Push notifications
- Background monitoring
- Offline mode
- Widget support

---

## Privacy

- Everything runs locally
- No data sent to cloud
- API only accessible on localhost
- You control all data

---

## Next Steps

1. Use it daily for a week
2. Add your real decisions
3. Let it learn your patterns
4. Watch it get smarter
5. Make better decisions

🧠✨

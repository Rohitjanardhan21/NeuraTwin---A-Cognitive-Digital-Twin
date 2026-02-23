# 🤖 JARVIS AI SETUP GUIDE

Transform your Cognitive Twin into a JARVIS-level AI assistant!

## 🎯 What You Get

With AI integration, your twin becomes:

✅ **Truly Conversational** - Natural language understanding
✅ **Contextually Aware** - Remembers and understands context
✅ **Proactively Intelligent** - Anticipates your needs
✅ **Genuinely Helpful** - Provides nuanced, thoughtful responses
✅ **Personality-Driven** - JARVIS-like sophistication and wit

## 🚀 Quick Setup (2 Minutes)

### Option 1: OpenAI (Recommended)

1. **Get API Key**
   - Go to: https://platform.openai.com/api-keys
   - Create account (if needed)
   - Click "Create new secret key"
   - Copy the key

2. **Add to .env file**
   ```bash
   cd cognitive-twin
   # Edit .env file (or create if it doesn't exist)
   ```
   
   Add this line:
   ```
   OPENAI_API_KEY=sk-your-actual-key-here
   ```

3. **Restart the API**
   - Stop the API server (Ctrl+C)
   - Start it again: `python api/twin_api.py`

4. **Done!** 
   - Open http://localhost:5002
   - Look for "AI: JARVIS ONLINE" in green

### Option 2: Anthropic (Claude)

1. **Get API Key**
   - Go to: https://console.anthropic.com/
   - Create account
   - Get API key

2. **Add to .env file**
   ```
   ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
   ```

3. **Restart and enjoy!**

---

## 💰 Cost Information

### OpenAI Pricing (GPT-4 Turbo)
- **Input**: ~$0.01 per 1K tokens
- **Output**: ~$0.03 per 1K tokens
- **Typical conversation**: $0.01 - $0.05
- **Daily usage (heavy)**: $1-3

### Anthropic Pricing (Claude 3.5 Sonnet)
- **Input**: ~$0.003 per 1K tokens
- **Output**: ~$0.015 per 1K tokens
- **Typical conversation**: $0.005 - $0.02
- **Daily usage (heavy)**: $0.50-1.50

### Free Tier Options

**OpenAI:**
- $5 free credits for new accounts
- Enough for ~100-500 conversations

**Anthropic:**
- Check their current promotions
- Often have trial credits

---

## 🎮 What Changes With AI

### Before AI Integration:
```
You: "How am I doing?"
Twin: "Your energy is at 65%. You're doing okay."
```

### After AI Integration:
```
You: "How am I doing?"
JARVIS: "You're operating at 65% capacity, sir. Not optimal, but serviceable. 
I've noticed your energy typically dips around this hour. Perhaps a brief 
respite would be prudent before tackling anything cognitively demanding?"
```

### Before:
```
You: "Should I work late tonight?"
Twin: "Your energy is low. Wait a bit."
```

### After:
```
You: "Should I work late tonight?"
JARVIS: "I'd advise against it, sir. Your energy reserves are at 35%, and 
historically, your decision quality drops significantly below 40%. Whatever 
you're working on will benefit from a fresh mind tomorrow morning when you're 
typically at 85% capacity. The work will still be there, but your cognitive 
edge won't be if you push through now."
```

---

## 🧠 AI-Powered Features

### 1. Natural Conversations
- Understands context across messages
- Remembers what you said earlier
- Responds naturally, not robotically

### 2. Intelligent Decision Analysis
- Nuanced evaluation of decisions
- Considers your patterns and state
- Provides thoughtful recommendations
- Explains reasoning clearly

### 3. Proactive Insights
- Generates insights without being asked
- Anticipates your needs
- Offers timely suggestions
- Learns what's helpful to you

### 4. JARVIS Personality
- Sophisticated and professional
- Slightly dry wit
- Direct and honest
- Supportive but not patronizing

### 5. Context-Aware Responses
- Detects your emotional state
- Adjusts tone accordingly
- Provides appropriate support
- Knows when to be serious vs. light

---

## 🎯 How to Use AI Features

### In Chat:
Just talk naturally! The AI understands:

```
"I'm worried about this deadline"
"What should I focus on today?"
"Tell me something I don't know about myself"
"Should I take this opportunity?"
"I'm feeling overwhelmed"
"What's the best use of my time right now?"
```

### In Decision Checker:
Enter any decision and get JARVIS-level analysis:

```
"Should I quit my job?"
"Should I start this business?"
"Should I work on this tonight?"
```

You'll get:
- Direct recommendation
- Key considerations
- Potential regrets
- Best timing
- Parallel universe analysis

### Proactive Mode:
The AI will:
- Send notifications when needed
- Offer suggestions proactively
- Generate insights automatically
- Anticipate your needs

---

## 🔧 Configuration

### Choose Your Model

**In .env file:**

```bash
# For OpenAI
OPENAI_MODEL=gpt-4-turbo-preview  # Most capable
# or
OPENAI_MODEL=gpt-3.5-turbo  # Faster, cheaper

# For Anthropic
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022  # Recommended
# or
ANTHROPIC_MODEL=claude-3-opus-20240229  # Most capable
```

### Adjust Personality

Edit `core/jarvis_brain.py` to customize:
- Tone and style
- Level of formality
- Amount of wit
- Proactiveness

---

## 🎭 Example Conversations

### Morning Check-in:
```
You: "Good morning"
JARVIS: "Good morning, sir. You're in excellent form today - 85% energy, 
minimal stress. I've analyzed your schedule and suggest tackling your most 
cognitively demanding tasks in the next 2-3 hours while you're at peak 
capacity. Shall I activate flow state protection?"
```

### Decision Support:
```
You: "Should I take this meeting at 3pm?"
JARVIS: "I'd recommend rescheduling if possible, sir. Your energy typically 
drops to around 40% at 3pm based on 12 days of data. You'll be more effective 
and persuasive at 10am when you're consistently at 80%+. However, if it's 
urgent, I suggest a coffee at 2:30pm and a 5-minute walk beforehand."
```

### Emotional Support:
```
You: "I'm feeling overwhelmed"
JARVIS: "I understand, sir. Your stress levels are at 78%, which is indeed 
elevated. May I suggest a brief tactical retreat? A 10-minute walk has 
historically reduced your stress by 20-30%. The work will still be there, 
but you'll approach it with greater clarity. Sometimes the most productive 
thing you can do is step away."
```

### Pattern Recognition:
```
You: "What have you noticed about me?"
JARVIS: "Several interesting patterns, sir. You're most creative between 
9-11am, most analytical after 2pm, and most prone to overthinking after 8pm. 
You make your best decisions when energy is above 70% and stress below 40% - 
which happens most reliably at 10am. You also tend to underestimate how much 
rest improves your performance. Fascinating, really."
```

---

## 🚨 Troubleshooting

### "AI: OFFLINE" showing?

1. **Check .env file exists**
   ```bash
   ls -la cognitive-twin/.env
   ```

2. **Check API key is correct**
   - No quotes around the key
   - No extra spaces
   - Key starts with `sk-`

3. **Restart API server**
   ```bash
   # Stop current server (Ctrl+C)
   python api/twin_api.py
   ```

4. **Check API status**
   ```bash
   curl http://localhost:5001/api/jarvis/status
   ```

### "API Error" in responses?

1. **Check API key is valid**
   - Not expired
   - Has credits remaining
   - Correct permissions

2. **Check internet connection**
   - AI requires internet to work

3. **Check rate limits**
   - Wait a minute and try again

### Still not working?

Check the API server logs for error messages.

---

## 💡 Pro Tips

1. **Talk naturally** - The AI understands conversational language
2. **Be specific** - More context = better responses
3. **Ask follow-ups** - It remembers the conversation
4. **Use it daily** - It learns your patterns over time
5. **Trust the insights** - They're based on YOUR data
6. **Experiment** - Try different questions and see what works

---

## 🎊 You're Ready!

Once you see "AI: JARVIS ONLINE" in green, you have a truly intelligent assistant.

Try asking:
- "How am I doing?"
- "What should I focus on?"
- "Tell me something interesting"
- "Should I take a break?"

Welcome to the future of cognitive assistance! 🤖✨

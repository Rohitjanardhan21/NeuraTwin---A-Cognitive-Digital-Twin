# 🔑 API KEY SETUP GUIDE

## ✅ Your API Key is Already Set!

Good news! Your OpenAI API key is already configured in the `.env` file.

## 📍 Location

The API key is stored in:
```
cognitive-twin/.env
```

## 🎯 Current Setup

Your `.env` file contains:
```
OPENAI_API_KEY=sk-proj-tbnjy...
OPENAI_MODEL=gpt-4-turbo-preview
```

This means **JARVIS AI is ACTIVE!**

## 🚀 How to Verify It's Working

1. **Open the interface:**
   ```
   http://localhost:5002
   ```

2. **Look for the status indicator:**
   - Top right corner should show: **"AI: JARVIS ONLINE"** in cyan/green
   - If it shows "AI: OFFLINE" in red, the API key isn't loaded

3. **Test it:**
   - Type in chat: "Tell me something interesting"
   - You should get an AI-powered response (not a generic one)
   - AI responses start with 🤖 emoji

## 🔄 If You Need to Change the API Key

### Option 1: Edit .env File Directly

1. Open `cognitive-twin/.env` in any text editor
2. Replace the key:
   ```
   OPENAI_API_KEY=sk-your-new-key-here
   ```
3. Save the file
4. Restart the servers

### Option 2: Use Command Line

```bash
cd cognitive-twin
echo "OPENAI_API_KEY=sk-your-new-key-here" > .env
```

## 🔄 How to Restart Servers

After changing the API key, restart:

**Windows:**
```bash
# Stop servers (Ctrl+C in their terminals)
# Then start again:
python api/twin_api.py
# In another terminal:
python web/assistant_app.py
```

**Or use the start script:**
```bash
python start_all.py
```

## 🎭 Using Different AI Providers

### OpenAI (Current Setup)
```
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4-turbo-preview
```

**Get key from:** https://platform.openai.com/api-keys

### Anthropic (Alternative)
```
ANTHROPIC_API_KEY=sk-ant-your-key-here
ANTHROPIC_MODEL=claude-3-5-sonnet-20241022
```

**Get key from:** https://console.anthropic.com/

### Both (System will use OpenAI first)
```
OPENAI_API_KEY=sk-your-openai-key
ANTHROPIC_API_KEY=sk-ant-your-anthropic-key
```

## 💰 Cost Tracking

### Check Your Usage

**OpenAI:**
- Dashboard: https://platform.openai.com/usage
- Shows: Requests, tokens, cost

**Typical Costs:**
- Simple question: $0.01 - $0.02
- Decision analysis: $0.02 - $0.05
- Long conversation: $0.05 - $0.10
- Daily heavy use: $1 - $3

### Set Spending Limits

**OpenAI:**
1. Go to: https://platform.openai.com/account/billing/limits
2. Set monthly limit (e.g., $10)
3. Get email alerts

## 🔒 Security

### Keep Your API Key Safe

✅ **DO:**
- Keep `.env` file local
- Add `.env` to `.gitignore` (already done)
- Never commit API keys to GitHub
- Regenerate if exposed

❌ **DON'T:**
- Share your `.env` file
- Post API keys online
- Commit to public repos
- Use in client-side code

### If Key is Exposed

1. Go to OpenAI dashboard
2. Revoke the old key
3. Generate new key
4. Update `.env` file
5. Restart servers

## 🧪 Testing AI Integration

### Quick Test

```bash
# Test API endpoint
curl http://localhost:5001/api/jarvis/status
```

**Expected response:**
```json
{
  "ai_available": true,
  "provider": "openai",
  "model": "gpt-4-turbo-preview",
  "conversation_length": 0,
  "relationship_level": 0
}
```

### In the Interface

1. Open http://localhost:5002
2. Check status: "AI: JARVIS ONLINE" (green/cyan)
3. Ask: "Tell me something interesting"
4. Response should be intelligent and conversational
5. Look for 🤖 emoji in response

## 🎯 What Changes With AI

### Without API Key:
```
You: "How am I doing?"
Twin: "Your energy is at 65%. You're doing okay."
```

### With API Key:
```
You: "How am I doing?"
JARVIS: "You're operating at 65% capacity, sir. Not optimal, but 
serviceable. I've noticed your energy typically dips around this 
hour. Perhaps a brief respite would be prudent?"
```

## 🚨 Troubleshooting

### "AI: OFFLINE" showing?

**Check 1: .env file exists**
```bash
ls cognitive-twin/.env
```

**Check 2: API key format**
- Should start with `sk-` or `sk-proj-`
- No quotes around the key
- No extra spaces
- On its own line

**Check 3: Servers restarted**
- Stop both servers
- Start API server first
- Then start web server
- Wait 5 seconds
- Refresh browser

**Check 4: API key valid**
- Not expired
- Has credits remaining
- Test at: https://platform.openai.com/playground

### "API Error" in responses?

**Possible causes:**
1. Rate limit hit (wait 1 minute)
2. No credits remaining (add payment method)
3. Invalid API key (regenerate)
4. Network issue (check internet)

**Check logs:**
Look at the API server terminal for error messages

### Still not working?

1. Check API server logs for errors
2. Verify API key at OpenAI dashboard
3. Try regenerating the key
4. Check firewall/antivirus settings

## 📊 Current Status

✅ API key is configured
✅ Servers are running
✅ Ready to use JARVIS AI

**Next step:** Open http://localhost:5002 and start chatting!

## 💡 Pro Tips

1. **Start simple** - Ask basic questions first
2. **Be conversational** - Talk naturally
3. **Check status** - Look for "AI: JARVIS ONLINE"
4. **Monitor costs** - Check usage dashboard weekly
5. **Set limits** - Prevent surprise bills
6. **Test thoroughly** - Try different questions

## 🎊 You're All Set!

Your API key is configured and JARVIS is ready to assist you!

Open http://localhost:5002 and say hello! 🤖✨

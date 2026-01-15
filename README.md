*Files Overview*

bot.py - Main Discord bot with Cerebras AI integration
requirements.txt - Python dependencies
render.yaml - Render.com configuration

**Features**

!ask <question> - Ask the AI anything
!reset - Clear your conversation history
!ping - Check bot status
Maintains conversation context per user
Handles long responses (splits if over 2000 characters)

**Setup Instructions**
1. Get Your API Keys
Discord Bot Token:

**Go to Discord Developer Portal**
Create a new application
Go to "Bot" section and create a bot
Copy the token
Enable "Message Content Intent" under Privileged Gateway Intents

Cerebras API Key:

You already have this from your code

2. Deploy to Render.com

Create a GitHub repository with these files:

bot.py
requirements.txt
render.yaml


Go to Render.com and sign up/login
Click "New +" → "Blueprint"
Connect your GitHub repository
Add environment variables:

DISCORD_BOT_TOKEN = your Discord bot token
CEREBRAS_API_KEY = your Cerebras API key


Click "Apply" to deploy

3. Invite Bot to Your Server
Create an invite URL with this format:
https://discord.com/api/oauth2/authorize?client_id=YOUR_CLIENT_ID&permissions=2048&scope=bot
Replace YOUR_CLIENT_ID with your bot's Application ID from the Discord Developer Portal.
4. Test It!
In your Discord server:

!ask Why is fast inference important?
!ping
!reset

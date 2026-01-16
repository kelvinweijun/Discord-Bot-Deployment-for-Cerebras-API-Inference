# Cerebot

A Discord bot integrated with **Cerebras AI** for ultra-fast inference.  
Deployed on **Render.com**, with per-user conversation memory and long-response handling. Note that this bot by default will use llama 3.3 70B model. You may change the model in bot.py if you want, but the model must be available in the list offered by Cerebras.

---

## Files Overview

- **bot.py**  
  Main Discord bot with Cerebras AI integration

- **requirements.txt**  
  Python dependencies

- **render.yaml**  
  Render.com deployment configuration

---

## Features

- `!ask <question>` — Ask the AI anything  
- `!reset` — Clear your conversation history  
- `!ping` — Check bot status  
- Maintains **conversation context per user**  
- Automatically **splits long responses** (handles Discord’s 2000-character limit)

---

## Setup Instructions

Before proceeding with the subsequent steps, clone this repository into your own GitHub account.

### Get Your API Keys

#### Discord Bot Token

1. Go to the **Discord Developer Portal**
2. Create a **New Application**
3. Navigate to the **Bot** section
4. Click **Create Bot**
5. Copy the **Bot Token**. This will be your `DISCORD_BOT_TOKEN`
6. Enable **Message Content Intent** under **Privileged Gateway Intents**

#### Cerebras API Key

Go to https://cloud.cerebras.ai and create an account, then obtain the API key for it. This will be your `CEREBRAS_API_KEY`.

---

### Deploy to Render.com

In Render.com:

1. Create a new Web Service
2. Connect it to the cloned GitHub repository
3. Render will auto-detect it's a Python app
4. Set your `CEREBRAS_API_KEY` and `DISCORD_BOT_TOKEN` in the environment variable field
5. Set the Start Command field to `python bot.py`
6. Click deploy

### Keeping the Bot Active with UptimeRobot

To keep the bot awake 24/7, you may use UptimeRobot to monitor and consistently ping your Render web service every interval.

1. Go to the bot's web service you deployed on Render, then copy the link of the web service
2. Go to https://www.uptimerobot.com and create a new monitor, enter the bot's web service link, and start it


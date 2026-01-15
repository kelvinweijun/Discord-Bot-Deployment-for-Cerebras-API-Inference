# Cerebot

A Discord bot integrated with **Cerebras AI** for ultra-fast inference.  
Deployed on **Render.com**, with per-user conversation memory and long-response handling.

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

### Get Your API Keys

#### Discord Bot Token

1. Go to the **Discord Developer Portal**
2. Create a **New Application**
3. Navigate to the **Bot** section
4. Click **Create Bot**
5. Copy the **Bot Token**
6. Enable **Message Content Intent** under **Privileged Gateway Intents**

#### Cerebras API Key

You already have this from your existing setup.

---

### Deploy to Render.com

#### Prepare Your Repository

Create a GitHub repository containing:


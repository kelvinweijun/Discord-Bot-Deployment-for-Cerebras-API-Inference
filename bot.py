import os
import discord
from discord.ext import commands
from cerebras.cloud.sdk import Cerebras

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Initialize Cerebras client
cerebras_client = Cerebras(
    api_key=os.environ.get("CEREBRAS_API_KEY"),
)

# Store conversation history per user
conversation_history = {}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is in {len(bot.guilds)} guilds')

@bot.command(name='ask', help='Ask the AI a question. Usage: !ask <your question>')
async def ask(ctx, *, question: str):
    """Ask the AI a question"""
    user_id = ctx.author.id
    
    # Initialize conversation history for new users
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    
    # Add user message to history
    conversation_history[user_id].append({
        "role": "user",
        "content": question
    })
    
    # Keep only last 10 messages to avoid token limits
    if len(conversation_history[user_id]) > 10:
        conversation_history[user_id] = conversation_history[user_id][-10:]
    
    try:
        async with ctx.typing():
            # Get response from Cerebras
            chat_completion = cerebras_client.chat.completions.create(
                messages=conversation_history[user_id],
                model="llama-3.3-70b",
            )
            
            response = chat_completion.choices[0].message.content
            
            # Add assistant response to history
            conversation_history[user_id].append({
                "role": "assistant",
                "content": response
            })
            
            # Split long responses to fit Discord's 2000 character limit
            if len(response) > 2000:
                chunks = [response[i:i+2000] for i in range(0, len(response), 2000)]
                for chunk in chunks:
                    await ctx.send(chunk)
            else:
                await ctx.send(response)
                
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")
        print(f"Error: {e}")

@bot.command(name='reset', help='Reset your conversation history')
async def reset(ctx):
    """Reset conversation history for the user"""
    user_id = ctx.author.id
    if user_id in conversation_history:
        conversation_history[user_id] = []
    await ctx.send("Your conversation history has been reset!")

@bot.command(name='ping', help='Check if the bot is responsive')
async def ping(ctx):
    """Simple ping command to check bot responsiveness"""
    await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

# Run the bot
if __name__ == "__main__":
    discord_token = os.environ.get("DISCORD_BOT_TOKEN")
    if not discord_token:
        raise ValueError("DISCORD_BOT_TOKEN environment variable not set")
    bot.run(discord_token)

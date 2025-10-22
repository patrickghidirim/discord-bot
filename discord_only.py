# bot.py
from dotenv import load_dotenv
import discord
import os

# Load environment variables from .env
load_dotenv()

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # allow reading message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user or message.author.bot:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Use a clear env var name; make sure it exists in your .env
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set. Put it in your .env or Codespaces secret.")
client.run(TOKEN)

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")


@bot.command()
async def hello(ctx):
    await ctx.send("مرحبا بعضو طاقمي المذهل ! رارارارارارا! ")

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        raise ValueError("No token found. Make sure DISCORD_TOKEN is set in your environment variables.")
    bot.run(token)

import discord
from discord.ext import commands
from datetime import datetime

# Set the prefix for commands
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Bot is ready! Current Date and Time (UTC): {current_time}')
    print(f'Current User's Login: {bot.user.name}')

# Token will be added later
# bot.run('YOUR_TOKEN_HERE')
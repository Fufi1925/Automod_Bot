import discord
from discord.ext import commands

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Load cogs
cogs = ['cog1', 'cog2', 'cog3']  # replace with actual cog names
for cog in cogs:
    bot.load_extension(cog)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Start the bot
bot.run('MTQ4NzIwNTc2MjYyMjAzMzkzMA.G7YKru.P28pE8WyRZ_pMNODL4S5gXj355CpPf1H5Xcwag')

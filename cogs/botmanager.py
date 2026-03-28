import discord
from discord.ext import commands

class BotManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'\n\n\nBot is online and ready!')

    @commands.command()
    async def help(self, ctx):
        help_message = "Here are the available commands:\n- !help: Display this help message.\n- !info: Get information about the bot."
        await ctx.send(help_message)

    @commands.command()
    async def info(self, ctx):
        info_message = "This bot is designed to automate management tasks."
        await ctx.send(info_message)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found! Please use !help to see available commands.')
        else:
            await ctx.send('An error occurred. Please try again later.')

def setup(bot):
    bot.add_cog(BotManager(bot))

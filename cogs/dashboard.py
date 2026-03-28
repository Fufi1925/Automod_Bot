import discord
from discord.ext import commands

class DashboardCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def server_stats(self, ctx):
        guild = ctx.guild
        total_members = guild.member_count
        online_members = sum(1 for member in guild.members if member.status != discord.Status.offline)
        await ctx.send(f"**Server Statistics:**\nTotal Members: {total_members}\nOnline Members: {online_members}")

    @commands.command()
    async def moderation_info(self, ctx):
        # Assuming you have appropriate methods and data to show moderation info
        # Example moderation info
        warnings = 10
        kicks = 5
        bans = 2
        await ctx.send(f"**Moderation Information:**\nWarnings: {warnings}\nKicks: {kicks}\nBans: {bans}")

def setup(bot):
    bot.add_cog(DashboardCog(bot))

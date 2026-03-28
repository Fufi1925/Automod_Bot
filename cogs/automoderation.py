import discord
from discord.ext import commands

class AutoModeration(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Prevent bot from responding to itself
        if message.author == self.bot.user:
            return

        # Spam Detection
        if message.content.count(message.content) > 3:
            await message.delete()
            await message.channel.send(f'{message.author.mention}, please refrain from spamming!')

        # Advertisement Filtering
        ads = ['sale', 'buy', 'discount']  # Add more keywords as needed
        if any(ad in message.content.lower() for ad in ads):
            await message.delete()
            await message.channel.send(f'{message.author.mention}, advertisements are not allowed!')

        # Bad Words Detection
        bad_words = ['badword1', 'badword2']  # Replace with actual bad words
        if any(bad_word in message.content.lower() for bad_word in bad_words):
            await message.delete()
            await message.channel.send(f'{message.author.mention}, that language is not tolerated!')

    @commands.Cog.listener()
    async def on_ready(self):
        print('AutoModeration Cog is ready!')

def setup(bot):
    bot.add_cog(AutoModeration(bot))

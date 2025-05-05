import discord
from discord.ext import commands
from discord import app_commands

class Testcog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is online.')

    @app_commands.command(description='Check the bot\'s latency in ms')
    async def ping(self, ctx):
        ping_embed = discord.Embed(
            title='Pong!',
            description="Latency in ms",
            color=discord.Color.blue()
        )
        ping_embed.add_field(name=f'{self.bot.user.name}\'s Latency (ms)', value=f'{round(self.bot.latency * 1000)}ms', inline=False)
        ping_embed.set_footer(text=f'Command invoked by {ctx.user.name}', icon_url=ctx.user.avatar)
        await ctx.response.send_message(embed=ping_embed)
        

async def setup(bot):
    await bot.add_cog(Testcog(bot))
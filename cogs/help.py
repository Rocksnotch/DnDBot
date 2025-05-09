import discord
import os
from discord.ext import commands
from discord import app_commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is online.')
        

    @app_commands.command(description="Get help with the bot")
    async def help(self, ctx):

        embed = discord.Embed(
            title="Help",
            description="Here are the available commands:",
            color=discord.Color.blue()
        )

        # print the first cog value in the dictionary cogs
        
        commands = self.bot.tree.walk_commands()
        for command in commands:
            if isinstance(command, app_commands.Command):
                embed.add_field(
                    name=f"/{command.name}",
                    value=command.description,
                    inline=False
                )

        await ctx.response.send_message(embed=embed)
            
async def setup(bot):
    await bot.add_cog(Help(bot))
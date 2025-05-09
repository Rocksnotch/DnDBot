import os
import dotenv
from discord.ext import commands
from discord import app_commands


class MainSheet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is online.')

    # Base Information Commands

    @app_commands.command(description="Get current character information")
    async def mainsheet(self, ctx):
        await ctx.response.send_message("This command is not implemented yet.")

    # HP Commands

    @app_commands.command(description="Get hit points")
    async def hp(self, ctx):
        await ctx.response.send_message("This command is not implemented yet.")

    @app_commands.command(description="Ouch! Take damage")
    async def damage(self, ctx, amount: int):
        await ctx.response.send_message(f"This command is not implemented yet.")

    @app_commands.command(description="Heal up!")
    async def heal(self, ctx, amount: int):
        await ctx.response.send_message(f"This command is not implemented yet.")

    @app_commands.command(description="Long rest")
    async def longrest(self, ctx):
        await ctx.response.send_message("This command is not implemented yet.")

    @app_commands.command(description="Short rest")
    async def shortrest(self, ctx):
        await ctx.response.send_message("This command is not implemented yet.")


    # Proficiency Commands

    @app_commands.command(description="Add proficiency")
    async def addproficiency(self, ctx, type: str):
        await ctx.response.send_message(f"This command is not implemented yet.")

    @app_commands.command(description="Remove proficiency")
    async def removeproficiency(self, ctx, type: str):
        await ctx.response.send_message(f"This command is not implemented yet.")
    

async def setup(bot):
    await bot.add_cog(MainSheet(bot))
import os
import dotenv
from discord.ext import commands
from discord import app_commands

class Dice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is online.')

    # Dice Commands

    @app_commands.command(description="Roll a dice")
    async def roll(self, ctx, dice: str):
        await ctx.response.send_message(f"This command is not implemented yet.")
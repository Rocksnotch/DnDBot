import os
import dotenv
import discord
from discord.ext import commands
from discord import app_commands

dotenv.load_dotenv()
OWNER_ID = int(os.getenv('OWNER_ID'))

class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} is online.')

    @app_commands.command(description='Reload a cog')
    async def reload(self, ctx, cog: str):
        if ctx.user.id != OWNER_ID:
            await ctx.response.send_message("You do not have permission to use this command.")
            return
        try:
            await self.bot.reload_extension(f'cogs.{cog}')
            # sync cog after reloading
            await self.bot.tree.sync(guild=ctx.guild)
            await ctx.response.send_message(f'Cog {cog} reloaded successfully!')
        except Exception as e:
            await ctx.response.send_message(f'Failed to reload cog {cog}: {e}')

    @app_commands.command(description='Load a cog')
    async def load(self, ctx, cog: str):
        if ctx.user.id != OWNER_ID:
            await ctx.response.send_message("You do not have permission to use this command.")
            return
        try:
            await self.bot.load_extension(f'cogs.{cog}')
            await ctx.response.send_message(f'Cog {cog} loaded successfully!')
        except Exception as e:
            await ctx.response.send_message(f'Failed to load cog {cog}: {e}')

async def setup(bot):
    await bot.add_cog(Reload(bot))
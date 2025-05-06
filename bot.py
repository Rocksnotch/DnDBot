import os
from dotenv import load_dotenv
import asyncio
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('TOKEN')
DEV_GUILD = os.getenv('DEV_GUILD')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')
    await bot.tree.sync()

async def main():
    async with bot:
        bot.setup_hook = load_cogs
        await bot.start(TOKEN)

asyncio.run(main())
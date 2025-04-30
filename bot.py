import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

class Client(discord.Client):
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return



intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(TOKEN)
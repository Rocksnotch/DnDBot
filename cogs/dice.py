import re
import os
import random
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
        result = 0
        if 'd' not in dice or dice.count('d') > 1 or dice.count('+') > 1:
            await ctx.response.send_message('Invalid dice format. Use XdY(+Z) where X is the number of dice and Y is the number of sides. (Z is optional addition)')
            return

        diceList = re.split('[d+]', dice)

        if diceList[1] == '':
            await ctx.response.send_message('Invalid dice format. Use XdY(+Z) where X is the number of dice and Y is the number of sides. (Z is optional addition)')
            return

        for i in range(len(diceList)):
            diceList[i] = int(diceList[i])

        if diceList[0] == 0:
            await ctx.response.send_message('You cannot roll 0 dice')
            return
        
        if diceList[1] == 0:
            await ctx.response.send_message('You cannot roll a dice with 0 sides')
            return
        
        if diceList[0] < 0:
            await ctx.response.send_message('You cannot roll a negative amount of dice')
            return
        
        if diceList[1] < 0:
            await ctx.response.send_message('You cannot roll a negative sided dice')
            return

        for i in range(diceList[0]):
            result += random.randint(1, diceList[1])

        if len(diceList) == 3:
            random.seed(os.urandom(32))
            result += diceList[2]

        await ctx.response.send_message(f'Rolled a {result} from {dice}!')


async def setup(bot):
    await bot.add_cog(Dice(bot))
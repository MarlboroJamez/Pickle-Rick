import random
from discord.ext import commands

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief="Gives random number 1-100")
    async def roll(self,ctx):
        n = random.randrange(1,101)
        await ctx.send(n)

    @commands.command(brief="Dice between 1 & 6")
    async def dice(self,ctx):
        n = random.randrange(1,6)
        await ctx.send(n)

    @commands.command(brief="Play Heads or Tails")
    async def coinflip(self,ctx):
        n = random.randint(0,1)
        await ctx.send("Heads" if n == 1 else "Tails")
def setup(bot):
    bot.add_cog(Gamble(bot))
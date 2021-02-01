from discord.ext import commands

class Pickle_Rick(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(brief="Play Marco-Polo with Pickle Rick")
    async def marco(self,ctx):
        await ctx.send("Volks Wagen!!")

def setup(bot):
    bot.add_cog(Pickle_Rick(bot))
import discord
from discord.ext import commands
from utils import text_to_owo


class Pickle_Rick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.Cog.listener()
    async def on_command_error(self, ctx, ex):
        print(ex)
        await ctx.send("Please check with !help the usage of this command, or either talk contact a ADMIN.")


    @commands.command(brief="Greet Pickle Rick!!")
    async def hello(self, ctx):
        await ctx.send("Hello Little Rick!!")

    @commands.command(brief="Randomize Sentence")
    async def owo(self, ctx):
        await ctx.send(text_to_owo(ctx.message.content))

    @commands.command(brief="Generate Server Invite! age is 1 day!")
    @commands.guild_only()
    async def invite(self, ctx):
        link = await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

def setup(bot):
    bot.add_cog(Pickle_Rick(bot))

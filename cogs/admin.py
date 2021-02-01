from discord.ext import commands
import discord
import datetime
from settings import *

def mods_or_owner():
    def predicate(ctx):
        return commands.check_any(commands.is_owner(), commands.has_role(HAS_A_ROLE))
    return commands.check(predicate)
        

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @mods_or_owner()
    @commands.is_owner()
    async def status(self,ctx):
        guild = ctx.guild
        no_voice_channels = len(guild.voice_channels)
        no_text_channels = len(guild.text_channels)
        embed = discord.Embed(description="Server Status",colour=discord.Colour.dark_purple())
        embed.add_field(name="Server Name", value=guild.name, inline=False)
        embed.add_field(name="# Voice Channel",value=no_voice_channels)
        embed.add_field(name="# Text Channels",value=no_text_channels)
        embed.set_thumbnail(url="https://m.media-amazon.com/images/M/MV5BNmNjY2YxZDAtNzQyMy00NzEzLTkwMWUtNjhhYjhlOGY4YzExXkEyXkFqcGdeQXVyNjc0NTIwNTU@._V1_.jpg")
        embed.set_image(url="https://a-static.besthdwallpaper.com/rick-et-equipe-morty-fond-d-ecran-3840x2400-7478_9.jpg")
        
        emoji_string = ""
        for e in guild.emojis:
            if e.is_usable():
                emoji_string += str(e)
        embed.add_field(name="Custom Emojies",value=emoji_string or "No emojis avaliable", inline=False)
        embed.set_author(name=self.bot.user.name)
        embed.set_footer(text=datetime.datetime.now)
        embed.add_field(name="AFK Channel:", value=guild.afk_channel)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Admin(bot))
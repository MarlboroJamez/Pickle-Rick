import random
from discord.ext import commands
import discord

from rps.modal import RPS
from rps.parser import RockPaperScissorParser
from rps.controller import RPSGame
from hangman.model import Hangman
from hangman.controller import HangmanGame

hangman_games = {}
user_guesses = list()



class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(usage="rock | paper | scissor")
    async def rps(self,ctx, user_choice: RockPaperScissorParser = RockPaperScissorParser(RPS.ROCK)):
        
        
        """
        Play a Game Of Rock, Paper & Scissors

        Either choose rock, paper or scissor and BEAT Pickle Rick!
        """
        
        game_instance = RPSGame()
        user_choice = user_choice.choice
        won, bot_choice = game_instance.run(user_choice)
        if won is None:
            message = "Dam! It's a DRAW!"
        elif won is True:
            message = "Lucky this TIME!: %s vs %s " % (user_choice, bot_choice)
        elif won is False:
            message = "LOL LOSER!: %s vs %s" % (user_choice, bot_choice)
        await ctx.send(message)

    @commands.command()
    @commands.dm_only()
    async def hm(self, ctx, guess: str):
        """
        Play Hangman Against Pickle Rick XD
        """
        player_id = ctx.author.id
        hangman_instance = HangmanGame()
        game_over, won = hangman_instance.run(player_id, guess)
        if game_over:
            game_over_message = "LoL you have LOST!"
            if won:
                game_over_message = "Lucky This TIME -_- CONGRATS!!"

            game_over_message = game_over_message + \
                " The word was %s" % hangman_instance.get_secret_word()

            await hangman_instance.reset(player_id)
            await ctx.send(game_over_message)

        else:
            await ctx.send("Progress: %s" % hangman_instance.get_progress_string())
            await ctx.send("Guess so far: %s" % hangman_instance.get_guess_string())

   
            
def setup(bot):
    bot.add_cog(Games(bot))
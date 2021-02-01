import os

SETTINGS_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SETTINGS_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

#Discord Conf
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN", False)

#Reddit Conf
REDDIT_ENABLED_MEME_SUBREDDITS = [
    'funny',
    'memes',
    'cute'

]
REDDIT_ENABLED_NSFW_SUBREDDITS = [
    'wtf'
]
REDDIT_APP_ID = os.getenv("REDDIT_APP_ID", False)
REDDIT_APP_SECRET = os.getenv("REDDIT_APP_SECRET", False)

HAS_A_ROLE=[
    'BOUNTY HUNTER',
    'SAUCY SAUSAGE',
    'MODERATOR',
    'TOO FLUFFY',
    'STRESS PRINCESS',
    'AFK',
    'SPIER TIER',
    'SPLIFF MEISTER'
]
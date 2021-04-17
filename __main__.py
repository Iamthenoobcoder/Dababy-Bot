#Import Discord library!
import discord

#Importing commands
from discord.ext import commands
# This is the variable that will define 
# an instance of dababy bot.

from dotenv import load_dotenv
#importing getenv to run the token

from os import getenv

#importing youtube_dl
from youtube_dl import YoutubeDL

#importing env 

bot = commands.Bot(command_prefix = "ye!",
                    intents = discord.Intents.default())

ydl_preset = {'format':'bestaudio', 'noplaylist': True}
@bot.event
async def on_ready():
    """Tells the owner if the bot is running and ready to go."""
    with YoutubeDL(ydl_preset) as ydl:
        lg = ydl.extract_info(f'ytsearch:dababy lets goo sound effect', download=False)['entries'][0]
    bot.letsgoo = lg['url']
    
    with YoutubeDL(ydl_preset) as ydl:
        yae = ydl.extract_info(f'ytsearch:dababy yea yea sound effect', download=False)['entries'][0]
    bot.yeayea = yae['url']
    
    ydl_preset['noplaylist'] = False
    with YoutubeDL(ydl_preset) as ydl: 
        dbm = ydl.extract_info(f'ytsearch:BOP, ROCKSTAR, BLIND, SUGE DaBaby Greatest Hits 2021 - Best Songs Playlist 2021', download=False)['entries'][0]
    bot.dababymusic = dbm['url']
    print(f"\n======================\nBot is now on standby\n======================")

cogs = ("voice_commands", "text_commands")

bot.remove_command('help')
for cog in cogs:
    bot.load_extension(f'bots_DaBaby.{cog}')

load_dotenv()
TOKEN = getenv('TOKEN')
#Run commmand
bot.run(TOKEN)
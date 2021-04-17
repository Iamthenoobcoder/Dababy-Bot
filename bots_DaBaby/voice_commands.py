import discord 

from youtube_dl import YoutubeDL
from discord.ext import commands

class voice_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ffmpeg_pre = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}

    async def play_voice(self, ctx, buffered):
        channel = ctx.author.voice.channel
        if not ctx.guild.voice_client:
            voice_client = await channel.connect()
        elif ctx.guild.voice_client:
            voice_client = ctx.guild.voice_client
            await voice_client.move_to(channel)
        voice_client.play(discord.FFmpegPCMAudio(buffered, **self.ffmpeg_pre))
   
    @commands.command(name="YEE", aliases=["yee", "yea", "yeayea", "ye", "YE"])
    async def yee(self, ctx):
        """Comes into the voice chat the author is in and says YEE!"""
        if ctx.author.voice:
            await self.play_voice(ctx, self.bot.yeayea)
        else:
            await ctx.reply("YEYE are you an idiot, get in a voice channel. YEYE")

    @commands.command(name="Stop", aliases=["S", "s", "stop"])
    async def stop(self, ctx): 
        """Makes the bot exit the voice channel"""
        voice = discord.utils.get(self.bot.voice_clients,guild=ctx.guild)
        await voice.disconnect()

    @commands.command(name="LessGoo", aliases=["lessgoo", "letsgo"])
    async def less_goo(self, ctx):
        """Comes into the voice chat the author is in and says Less Goo!!"""
        if ctx.author.voice:
            await self.play_voice(ctx, self.bot.letsgoo)
        else:
            voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            await ctx.reply("Less see who we have here? An idiot LESS GOO! We have someone who doesn't have the commmon sense to join a voice channel before calling a Less Goo comand.")

    @commands.command(name="DababyMusic", aliases=["dababymusic","DaBabyMusic", "music", "Music", "M", "m"])
    async def Music(self, ctx):
        """Runs basically like a music bot but onyl runs DaBaby's songs."""
        if ctx.author.voice:
            await self.play_voice(ctx, self.bot.dababymusic)
        else:
            voice_client = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
            await ctx.reply("This moron wants to listen to my music without entering a voice chat.Ye ye are and idiot. Join a voice call before I DaBaby you.")

def setup(bot):
    bot.add_cog(voice_commands(bot))
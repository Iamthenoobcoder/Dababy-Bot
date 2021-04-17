import discord

from discord.ext import commands

class text_commands(commands.Cog): #represents a cog class
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="reload", aliases=["rl"])
    async def reload(self, ctx, ext):
        self.bot.reload_extension(f'bots_DaBaby.{ext}')
        await ctx.reply("Done", mention_author=False)

    @commands.command(name="help", aliases=["h", "H", "Help"])
    async def help_command(self, ctx):
        """Helps the person that runs this command."""
        voice_commands = []
        text_commands = []
        hellp = discord.Embed(title="HELP!", color=discord.Colour.dark_gold())
        usage = lambda cmd: f"{cmd.name} {command.signature}"
        
        for command in self.bot.commands:
            if command.cog.qualified_name == "voice_commands":
                voice_commands.append((f"{ctx.prefix}{usage(command)}", command.short_doc))
            elif command.cog.qualified_name == "text_commands":
                text_commands.append((f"{ctx.prefix}{usage(command)}", command.short_doc))

        voice_help_string = "".join([f"`{pair[0]}`\n{pair[1]}\n\n" for pair in voice_commands])
        text_help_string = "".join([f"`{pair[0]}`\n{pair[1]}\n\n" for pair in text_commands])
        hellp.description = "This is the dababy bot help menu" +\
                f"\n**Voice Commands**\n\n{voice_help_string}" +\
                f"\n**Text Commands**\n\n{text_help_string}"
        await ctx.reply(embed=hellp, mention_author=False)
         

    @commands.command(name="DaBaby", aliases=["dababy", "Dababy"])
    async def Dababied(self, ctx, member:discord.Member):
        """Sends embeded da baby pictures
        unaware strangers"""
        dababied = discord.Embed(title="DaBaby-Baby", description=f'{member.name} just got dababied', color=discord.Colour.dark_red()) # use hex or use predefined color
        dababied.set_image(url="https://cdn.discordapp.com/attachments/828220439419158553/828298756754636840/Dababy_BabyOnBaby.png")
        # Images, footer, author and thumbnails are special elements
        # We manipulate them by using a method 
        # i.e. embed_name.set_thumbnail(url=url)
        # embed_name.set_image(url=url)


        # await messagable.send(embed=embed_name)
        # 1. send it to the channel that the command was invoked in
        # 2. send it to the member who got dababied
        await member.send(f'{member.name}You just got DaBabied boi!')
        await ctx.channel.send(embed=dababied)
        
        # ctx represents the context of the command invokation
        # ctx.author represents the person who invoked the command
        # member represents the person who we tagged
        await ctx.author.send(f'You just dababied {member.name}.')

    @commands.command(name="Ride", aliases=["R", "r","ride"])
    async def ride_Give(self, ctx, member:discord.Member):
        """Gives a person a ride in a convertible"""
        convertible = discord.Embed(title="Convertible-Baby", description=f'{member.name} just got a convertible :oncoming_taxi:', color=discord.Colour.dark_purple())
        convertible.set_image(url="https://media.tenor.co/videos/9ce5a623bfe0022acfc073e16cea3360/mp4")
        await member.send(f'{member.name} You just recieved a convertible')
        await ctx.channel.send(embed=convertible)
        await ctx.author.send(f'You just gave a convertible to {member.name}.')

    @commands.command(name="DaBabySkin", aliases=["dababyskin"])
    async def skin_give(self, ctx,member:discord.Member):
        """Gives an unwarned user a skin."""
        skin = discord.Embed(title="Skin-YEE", description=f'{member.name} DaBaby has a skin less gooo, it is for free YEE :man_artist:!', color=discord.Colour.dark_magenta())
        skin.set_image(url="https://cdn.discordapp.com/attachments/766128720381476875/829219014554157076/e99zbs4949261.png")
        await member.send(f'{member.name} You just unlocked DaBaby skin in fortnite for free!')
        await ctx.channel.send(embed=skin)
    # this is required for every cog 
def setup(bot): # discord calls the setup function automatically with the param bot
    bot.add_cog(text_commands(bot)) # This loads the cog class text_commands
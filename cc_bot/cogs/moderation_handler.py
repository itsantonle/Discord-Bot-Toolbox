import discord 
from discord.ext import commands

# moderation cog 

class ChannelEventHandler(commands.Cog): 
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_ready(self) -> None: 
        print(f"{__name__} cog is now ready! ✅")
    
    @commands.Cog.listener()
    
    # filter words should for banned, and 'help' keyword 
    async def on_message(self, message: discord.Message): 
        if message.author == self.bot.user: 
            return 
        if "hi" in message.content.lower(): 
            await message.reply(f"Hi there! {message.author.mention} ")
    
       
async def setup(bot): 
    await bot.add_cog (ChannelEventHandler(bot))
    
        
            
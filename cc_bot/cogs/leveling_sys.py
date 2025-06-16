import discord 
from discord.ext import commands

# connects to go lang api

class LevelingSys(commands.Cog): 
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
    
    @commands.Cog.listener()
    async def on_ready(self) -> None: 
        print(f"{__name__} cog is now ready! ✅")
    
   
       
async def setup(bot): 
    await bot.add_cog (LevelingSys(bot))
    
        
            
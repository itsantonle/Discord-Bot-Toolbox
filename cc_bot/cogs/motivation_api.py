import discord 
import requests
from discord.ext import commands
import os 
import easy_pil
from random import choice

# moderation cog 

class MotivationAPI(commands.Cog): 
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
        self._api_url = "https://zenquotes.io/api/random"
    
    @staticmethod
    @staticmethod
    def wrap_text(text, max_chars_per_line=40):
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if len(current_line) + len(word) + 1 <= max_chars_per_line:
                current_line += " " + word if current_line else word
            else:
                lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)

        return lines

        
    @commands.Cog.listener()
    async def on_ready(self) -> None: 
        print(f"{__name__} cog is now ready! ✅")
    
    @commands.command()
    async def motivate(self,ctx: commands.Context):
        try:  
            response: requests.Response = requests.get(self._api_url)
            if response.status_code == 200:
                # handle api response
                data = response.json()
                quote = data[0]["q"]
                author = data[0]["a"]
            
                # handle dynamic generation 
                images = [img for img in os.listdir("./cogs/quote_bg")]
                randomized_img = choice(images)
                bg = easy_pil.Editor(f"./cogs/quote_bg/{randomized_img}").resize((1920, 1080))
                
                #avatar 
                avatar_image = await easy_pil.load_image_async(str(ctx.author.avatar.url))
                avatar = easy_pil.Editor(avatar_image).resize((250,  250)).circle_image()
                
                # font 
                font_author = easy_pil.Font.poppins(size=60, variant='bold')
                font_quote = easy_pil.Font.poppins(size=40, variant='italic')
                
                bg.paste(avatar, (835, 340))
                # draw an ellipse
                bg.ellipse((845,340), 250, 250, outline="white", stroke_width=5)
                # paste the text
                
                # Handle text wrapping
                lines = self.wrap_text(quote, 40)
                y_start = 620
                line_height = 55

                for i, line in enumerate(lines):
                    bg.text(
                        (960, y_start + i * line_height),
                        line,
                        color="white",
                        font=font_quote,
                        align="center"
                    )

                # Render author below the quote
                author_y = y_start + len(lines) * line_height + 20
                bg.text(
                    (960, author_y),
                    f"— {author}",
                    color="white",
                    font=font_author,
                    align="center"
                )
                
                # embed img file
                file_name = f"{ctx.author.id}_quote.png"
                img_file = discord.File(fp=bg.image_bytes, filename=file_name)
                await ctx.channel.send(f"Hello there {ctx.author.mention}! Here is your motivational quote! 🌞")
                await ctx.channel.send(file=img_file)
                
            else: 
                ctx.send("Unable to fetch a motivational quote right now! 🙇")
        except Exception as e: 
              print('⚠️ An Error Occurred in the Bot code: ' + str(e))
              ctx.send("Unable to process this request right now 🥲")

        
    
       
async def setup(bot): 
    await bot.add_cog (MotivationAPI(bot))
    
        
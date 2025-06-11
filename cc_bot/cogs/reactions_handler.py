import discord 
from discord.ext import commands



# Reaction based events
# Role maps work on making this dynamic for now adding manually
# set this in discord server with the Role name exactly 

# CONSTANTS 

EMOJI_ROLE_MAP = {
    "🔥": "FireRole",
    "❄️": "IceRole",
    "🌱": "NatureRole"
}
class ChannelReactionHandler(commands.Cog): 
    def __init__(self, bot, emojimap = EMOJI_ROLE_MAP):
        self.bot = bot 
        self.emojimap = emojimap
        self.target_message_id = None 
        
    @commands.Cog.listener()
    async def on_ready(self) -> None: 
        print(f"{__name__} cog is now ready! ✅")
    
    @commands.command()
    async def setup_roles(self,ctx: commands.Context):
        try: 
            # automate making the roles
            guild = ctx.guild
            for role_name in self.emojimap.values():
                existing_role = discord.utils.get(guild.roles, name=role_name)
                if not existing_role:
                    await guild.create_role(name=role_name)
                    await ctx.send(f"✅ Created role: **{role_name}**")
             
             # embed message       
            embed_msg = discord.Embed(title="Role Management", description="React to this message to get a role!", color=discord.Color.brand_green())
            embed_msg.set_author(name=f"Prompted by {ctx.author.name}", icon_url=ctx.author.avatar)
            embed_msg.add_field(name="Available Roles!", value="🔥- Fire ❄️- Ice 🌱-Nature")
            
            msg:discord.Message = await ctx.send(embed=embed_msg)
            for emoji in self.emojimap:
                await msg.add_reaction(emoji)
                
            self.target_message_id= msg.id
          
            
        except Exception as e: 
            await ctx.send('⚠️ An Error Occurred in the Bot code: ' + str(e))

    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):
        try: 
            if payload.message_id != self.target_message_id:
                return

            if payload.member is None or payload.member.bot:
                return

            guild = self.bot.get_guild(payload.guild_id)
            emoji = str(payload.emoji)
            role_name = self.emojimap.get(emoji)

            if role_name:
                role = discord.utils.get(guild.roles, name=role_name)
                if role:
                    await payload.member.add_roles(role)
                    if guild.system_channel:
                        await guild.system_channel.send(f"{payload.member.mention} was given the **{role.name}** role! 🎉")
        except Exception as e: 
            print('⚠️ An Error Occurred in the Bot code: ' + str(e))
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self,payload):
        try: 
            if payload.message_id != self.target_message_id:
                return

            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)
            if member is None or member.bot:
                return

            emoji = str(payload.emoji)
            role_name = self.emojimap.get(emoji)

            if role_name:
                role = discord.utils.get(guild.roles, name=role_name)
                if role:
                    await member.remove_roles(role)
                    if guild.system_channel:
                        await guild.system_channel.send(f"{member.mention} had the **{role.name}** role removed. ❌")
        except Exception as e: 
            print('⚠️ An Error Occurred in the Bot code: ' + str(e))
                
async def setup(bot): 
    await bot.add_cog (ChannelReactionHandler(bot))
    
        
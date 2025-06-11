import discord 
from discord.ext import commands,tasks
# import logging 
from dotenv import load_dotenv
import os
import asyncio
from itertools import cycle

load_dotenv()

token: str = os.getenv('DISCORD_TOKEN')
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#   specify intents (if updating to slash commands then replace with all())
intents: discord.Intents = discord.Intents.default()
intents.reactions = True 
intents.guilds = True
intents.message_content = True 
intents.members = True
# bot instance
bot:commands.Bot = commands.Bot(command_prefix='!', intents=intents)

# constants
CONFIG = { "loop_duration": 7200}
ROLES= ["test_role"]
BOT_STATUSES = cycle(["Feeling depressed?😭 Cup of coffee! ☕", "Happy day! 😀 Coding day! 💻", "Monday again? Oppss..☠️"])

# loop for status
@tasks.loop(seconds=CONFIG["loop_duration"])
async def change_bot_status(): 
    await bot.change_presence(activity=discord.Game(next(BOT_STATUSES)))


# ready the bot
@bot.event
async def on_ready() -> None: 
    print( f"{bot.user.display_name} is ready! ദ്ദി(。•̀ ,<)~✩‧+")
    change_bot_status.start()

# load cogs
async def load() -> None: 
    for filename in os.listdir("./cogs"): 
        if filename.endswith(".py"): 
            await bot.load_extension(f"cogs.{filename[:-3]}")
    
# main function 
async def main() -> None: 
    async with bot: 
        await load()
        await bot.start(token)

asyncio.run(main())

# @bot.event
# async def on_member_join(member): 
#     await member.send(f"Welcome to the server {member.name}")
    
# @bot.event   
# async def on_message(message): 
#     # don't do anything if the author is bot
#     if message.author == bot.user: 
#         return 
    
#     if "shit" in message.content.lower(): 
#         await message.delete()
#         await message.channel.send(f"Please don't use that word {message.author.mention}")
#     # continue processing all commands
#     await bot.process_commands(message)
    
# # commands section - name of the function done next is the command 
# @bot.command()
# async def hello(ctx): 
#     # !hello
#     # uses ctx which is context 
#     await ctx.send(f"Hello, {ctx.author.mention}!")
    
# # assign role 
# @bot.command()
# async def assign(ctx): 
#     role = discord.utils.get(ctx.guild.roles, name=ROLES[0])
#     if role: 
#         await ctx.author.add_roles(role)
#         await ctx.send(f"{ctx.author.mention} is now assigned to {ROLES[0]}!")
#     else: 
#         await ctx.send("Role doesn't exist!")

# # unassign role 
# @bot.command()
# async def unassign(ctx): 
#     role = discord.utils.get(ctx.guild.roles, name=ROLES[0])
#     if role: 
#         await ctx.author.remove_roles(role)
#         await ctx.send(f"{ctx.author.mention} has been removed from {ROLES[0]}!")
#     else: 
#         await ctx.send("Role doesn't exist!")

# # direct DM functionality gets the message after command
# # !dm {msg} gets the msg after the command
# @bot.command()
# async def dm(ctx,*, msg): 
#     await ctx.author.send(f"You said {msg}")
    
# #   literally replies to the message
# @bot.command()
# async def reply(ctx): 
#     await ctx.reply("This is a reply to your message")
    

# # embed and poll-like
# @bot.command()
# async def poll(ctx, *, question): 
#     embed = discord.Embed(title="Poll", description=question)
#     # send embedded message
#     poll_messsage = await ctx.send(embed=embed)
#     # win + period
#     await poll_messsage.add_reaction("👍")
    
    

# # commands based on user role 
# @bot.command()
# @commands.has_role(ROLES[0])
# async def secret(ctx): 
#     await ctx.send('Testing roles are used to mantain the bot! :3!')

# @secret.error
# async def secret_error(ctx, error): 
#     if isinstance(error, commands.MissingRole): 
#         await ctx.send("You don't have permission to do that")
#     else: 
#         await ctx.send("Something went wrong")
    
    

# bot.run(token, log_handler=handler, log_level=logging.DEBUG)
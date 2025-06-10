import discord 
from discord.ext import commands
import logging 
from dotenv import load_dotenv
import os

load_dotenv()
ROLES = ["test_role"]
token = os.getenv('DISCORD_TOKEN')
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
#   specify intents
intents = discord.Intents.default()

#   enable manual intents here 
# https://discordpy.readthedocs.io/en/stable/ read docs on adding more intent to cc
intents.message_content = True 
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

#`!hello !search` are keywords for the bot


# bot events
@bot.event
async def on_ready(): 
    print( f"{bot.user.display_name} is ready! ദ്ദി(。•̀ ,<)~✩‧+")
    


@bot.event
async def on_member_join(member): 
    await member.send(f"Welcome to the server {member.name}")
    
@bot.event   
async def on_message(message): 
    # don't do anything if the author is bot
    if message.author == bot.user: 
        return 
    
    if "shit" in message.content.lower(): 
        await message.delete()
        await message.channel.send(f"Please don't use that word {message.author.mention}")
    # continue processing all commands
    await bot.process_commands(message)
    
# commands section - name of the function done next is the command 
@bot.command()
async def hello(ctx): 
    # !hello
    # uses ctx which is context 
    await ctx.send(f"Hello, {ctx.author.mention}!")
    
# assign role 
@bot.command()
async def assign(ctx): 
    role = discord.utils.get(ctx.guild.roles, name=ROLES[0])
    if role: 
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {ROLES[0]}!")
    else: 
        await ctx.send("Role doesn't exist!")

# unassign role 
@bot.command()
async def unassign(ctx): 
    role = discord.utils.get(ctx.guild.roles, name=ROLES[0])
    if role: 
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has been removed from {ROLES[0]}!")
    else: 
        await ctx.send("Role doesn't exist!")

# direct DM functionality

# commands based on user role 
@bot.command()
@commands.has_role(ROLES[0])
async def secret(ctx): 
    await ctx.send('Testing roles are used to mantain the bot! :3!')

@secret.error
async def secret_error(ctx, error): 
    if isinstance(error, commands.MissingRole): 
        await ctx.send("You don't have permission to do that")
    else: 
        await ctx.send("Something went wrong")
    
    

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
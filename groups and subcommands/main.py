import discord
from discord.ext import commands


client = commands.Bot(command_prefix='.',help_command=None)

@client.event 
async def on_ready():
    print("Bot is ready")

#with groups
@client.group(name='help',invoke_without_command=True)
async def help(ctx):
    await ctx.send("command worked!!")

@help.command()
async def music(ctx):
    await ctx.send("help command for music category")

#with if else conditionals
@client.command(name="help")
async def help(ctx,arg1=None):
    if arg1=="music":
        await ctx.send("music")
        return

    if arg1==None:
        await ctx.send("wrong usage!! use it like - `.help (music/moderation/automoderation/welcomemsgs)`")

    else:
        await ctx.send("can't find this category please choose between - `music/moderation/automoderation/welcomemsg`")


client.run("your_token_here")

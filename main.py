import os
import discord

from vars.client import client
from ext import utils
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

@client.event
async def on_connect():
    utils.load_cogs()

@client.event
async def on_ready():
    print("Ready!")
    await client.change_presence(status = discord.Status.online, activity = discord.Game("$help | By Ahmosys"))

 
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Mmmmmmh, j'ai bien l'impression que cette commande n'existe pas :/")
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Il manque un argument effectuez !help pour connaître les commandes.")
#     elif isinstance(error, commands.MissingPermissions):
#         await ctx.send("Vous n'avez pas les permissions pour faire cette commande.")
#     elif isinstance(error, commands.CheckFailure):
#         await ctx.send("Oups vous ne pouvez utilisez cette commande.")
#     if isinstance(error, discord.Forbidden):
#         await ctx.send("Oups, je n'ai pas les permissions nécessaires pour faire cette commmande.")
#     if isinstance(error, commands.ExtensionNotFound):
#         await ctx.send("Je crois bien que ce cogs n'existe pas :/.")

#keep_alive()
client.run(os.getenv("TOKEN"))
import os
import discord
from vars import client

def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            try:
                client.load_extension(f"cogs.{filename[:-3]}")
            except Exception as e:
                print(f"Cogs erreur chargement: {filename[:-3]}\n{e}")
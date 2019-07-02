import discord
from discord.ext import commands
from google.cloud import datastore
from src.util.prefix import get_prefix, set_prefix

ds = datastore.Client()
client = commands.Bot(
    description="MagicLeague-RW",
    command_prefix=get_prefix
)


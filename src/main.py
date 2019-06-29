import discord
from discord.ext import commands
from prefix import get_prefix

client = commands.Bot(
    description="MagicLeague-RW",
    command_prefix=get_prefix
)
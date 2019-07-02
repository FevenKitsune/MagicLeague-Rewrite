import logging
import os
import discord
from discord.ext import commands
from src.util.ds import ds
from src.util.prefix import get_prefix, set_prefix


logger = logging.getLogger("discord")
client = commands.Bot(
    description="MagicLeague-RW",
    command_prefix=get_prefix
)

extensions = ["ext.reg"]

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)  # Load all extensions
        except Exception as e:  # If load failed, post to log.
            exc = f"{type(e).__name__}: {e}"
            logger.warning(f"Failed to load extension {extension}\n{exc}")
        else:  # If load succeeded, post to log.
            logger.info(f"Loaded extension {extension}")

    logger.info("Starting client...")
    client.run(os.environ["DISCORD_API"])

from src.main import ds

from discord.ext import commands


class Reg(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(
        name="registry",
        aliases=["config", "reg", "cfg"],
        brief="Access the bot configuration registry.",
        pass_context=True
    )
    async def registry(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand invoked.")

    @registry.group(
        name="get",
        pass_context=True
    )
    async def get(self, ctx):
        await ctx.send("Get command")

    @registry.group(
        name="set",
        pass_context=True
    )
    async def set(self, ctx):
        await ctx.send("Set command")


def setup(client):
    client.add_cog(Reg(client))

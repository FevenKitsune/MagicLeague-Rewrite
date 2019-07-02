from google.cloud import datastore
from src.util.ds import ds
from discord.ext import commands
from src.util.checks import is_admin


class Reg(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(
        name="registry",
        aliases=["config", "reg", "cfg"],
        brief="Access the bot configuration registry.",
        pass_context=True
    )
    @is_admin()
    async def registry(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No subcommand invoked.")

    @registry.group(
        name="get",
        pass_context=True
    )
    @is_admin()
    async def get(self, ctx, *args):
        if not args:
            # If no other arguments are passed, list entire registry
            query = ds.query(kind=str(ctx.guild.id))
            results = list(query.fetch())
        else:
            # If an argument is passed, list registry with name's matching argument value
            query = ds.query(kind=str(ctx.guild.id))
            key = ds.key(str(ctx.guild.id), str(args[0]))
            query.key_filter(key, '=')
            results = list(query.fetch())
        string_builder = "\n".join([f"{result.key.id_or_name} :: {result['value']}" for result in results])
        await ctx.send(f"```Registry Query:\n{string_builder}```")

    @registry.group(
        name="set",
        pass_context=True
    )
    @is_admin()
    async def set(self, ctx, *args):
        try:
            key = ds.key(str(ctx.guild.id), str(args[0]))
            task = datastore.Entity(key=key)
            task['id'] = str(args[0])
            task['value'] = str(args[1])
            ds.put(task)
        except Exception as e:
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await ctx.send(f"Registry Value Added!\nName: {task['id']}\nValue: {task['value']}")


def setup(client):
    client.add_cog(Reg(client))

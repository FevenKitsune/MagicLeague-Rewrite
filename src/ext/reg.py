# CC0 1.0 Universal

from google.cloud import datastore
from src.util.ds import ds
from src.util.config import color, valid_keys
from discord.ext import commands
import discord
from src.util.checks import is_admin


class Reg(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def print_registry(self, ctx):
        embed = discord.Embed(
            title="Registry Query",
            color=color['message']
        )
        query = ds.query(kind=str(ctx.guild.id))
        results = list(query.fetch())
        embed.set_footer(text=f"Invoked by: {ctx.message.author.name}")
        for result in results:
            embed.add_field(
                name=f"`Key: {result.key.id_or_name}`",
                value=f"`Value: {result['value']}`",
                inline=False
            )
        await ctx.send(embed=embed)

    # Registry Group
    @commands.group(
        name="registry",
        aliases=["config", "reg", "cfg"],
        brief="Access the bot configuration registry.",
        pass_context=True
    )
    @is_admin()
    async def registry(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.print_registry(ctx)

    @registry.group(
        name="get",
        pass_context=True
    )
    @is_admin()
    async def get(self, ctx):
        await self.print_registry(ctx)

    @registry.group(
        name="set",
        aliases=["add", "edit"],
        pass_context=True
    )
    @is_admin()
    async def set(self, ctx, *args):
        try:
            if args[0].lower not in valid_keys:
                raise UserWarning(f"{args[0].lower()} is not a valid key!")
            key = ds.key(str(ctx.guild.id), str(args[0]).lower())
            task = datastore.Entity(key=key)
            task['value'] = str(args[1])
            ds.put(task)
        except Exception as e:
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await self.print_registry(ctx)

    @registry.group(
        name="delete",
        pass_context=True
    )
    @is_admin()
    async def delete(self, ctx, *args):
        try:
            key = ds.key(str(ctx.guild.id), str(args[0]).lower())
            ds.delete(key)
        except Exception as e:
            await ctx.send(f"{type(e).__name__}: {e}")
        else:
            await self.print_registry(ctx)

    @registry.group(
        name="keys",
        aliases=["key", "keylist"],
        pass_context=True
    )
    @is_admin()
    async def keys(self, ctx):
        keylist = "\n".join(valid_keys)
        embed = discord.Embed(
            title="Keylist Query",
            color=color['message'],
            description=(
                f"```"
                f"{keylist}"
                f"```"
            )
        )
        embed.set_footer(text=f"Invoked by: {ctx.message.author.name}")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Reg(client))

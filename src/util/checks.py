from discord.ext import commands


def is_admin():
    async def predicate(ctx):
        return (
            ctx.message.channel.permissions_for(ctx.message.author).administrator
        )
    return commands.check(predicate)

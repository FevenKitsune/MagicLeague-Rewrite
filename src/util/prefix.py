from src.main import ds


async def get_prefix(bot, message):
    key = ds.key('prefix', str(message.guild.id))
    task = ds.get(key)
    if not task:
        return "m^"
    return str(task['prefix'])


async def set_prefix(ctx, prefix):
    key = ds.key('prefix', str(ctx.guild.id))
    task = ds.Entity(key=key)
    task['prefix'] = str(prefix)
    ds.put(task)
    return
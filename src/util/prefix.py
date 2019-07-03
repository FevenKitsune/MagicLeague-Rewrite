from src.util.ds import ds


async def get_prefix(bot, message):
    key = ds.key(str(message.guild.id), 'prefix')
    task = ds.get(key)
    if not task:
        return "m^"
    return str(task['value'])

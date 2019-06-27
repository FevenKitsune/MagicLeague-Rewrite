##
#MAGICLEAGUE2 ALPHA
#DECLASSIFIED
#THIS CODE HAS BEEN DECLASSIFIED BY THE CREATOR
#AND MAY BE USED FOR ANY PURPOSE.
###

###
#RESOURCES:
#https://discordpy.readthedocs.io/en/rewrite
#python3 -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]

#https://virtualenv.pypa.io/en/stable/userguide/
###

###
#///// NOTES /////
#
#SIGN/RELEASE TAGS:
# %playermention% - Mention signed/released player
# %teammention% - Mention signing/releasing team
# %playername% - Name of signed/released player
# %teamname% - Name of signing/releasing team
###

print("Loading...")

import discord
import sqlite3
import logging
import requests
import json

logging.basicConfig(level=logging.INFO)

version_num = "v0.0.6 ALPHA"
blacklist = []

client = discord.Client()
configDb = sqlite3.connect("config.db")
configDb.text_factory = str

@client.event
async def on_ready():
    startup = logging.getLogger("startup")
    startup.info("===MagicLeague 2 is now starting up!===")
    startup.info('USERNAME: {0.user}'.format(client))
    startup.info('ID: {0.user.id}'.format(client))
    startup.info("SERVERS: " + str(sum(1 for x in client.guilds)))

    dbCheck = configDb.cursor()
    dbCheck.execute("SELECT count(*) FROM sqlite_master WHERE type='table' and name='config'")
    if dbCheck.fetchone()[0] == 1:
        dbCheck.close()
    else:
        startup.warn("Config table not found! Creating new table.")
        dbCheck.execute("CREATE TABLE config(id TEXT, name TEXT, value TEXT)")
        configDb.commit()
        dbCheck.close()
        startup.warn("Config table has been created.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if str(message.guild.id) in blacklist:
        return

    ###cfgCommandPrefix###
    async def cfgGet_CommandPrefix(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgcommandprefix' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("m^") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_CommandPrefix(guild, prefix):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), prefix)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgcommandprefix'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgcommandprefix', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgRoleFreeAgent###
    async def cfgGet_RoleFreeAgent(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgrolefreeagent' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_RoleFreeAgent(guild, roleids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), roleids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgrolefreeagent'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgrolefreeagent', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgRoleTeamStaff###
    async def cfgGet_RoleTeamStaff(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleteamstaff' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_RoleTeamStaff(guild, roleids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), roleids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleteamstaff'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleteamstaff', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgRoleTeamOwner###
    async def cfgGet_RoleTeamOwner(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleteamowner' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_RoleTeamOwner(guild, roleids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), roleids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleteamowner'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleteamowner', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgRoleServerStaff###
    async def cfgGet_RoleServerStaff(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleserverstaff' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_RoleServerStaff(guild, roleids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), roleids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleserverstaff'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleserverstaff', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgRoleServerOwner###
    async def cfgGet_RoleServerOwner(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgroleserverowner' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_RoleServerOwner(guild, roleids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), roleids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgroleserverowner'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgroleserverowner', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgChannelTransactionsID###
    async def cfgGet_ChannelTransactionsID(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgchanneltransactionsid' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_ChannelTransactionsID(guild, channelids):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), channelids)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgchanneltransactionsid'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgchanneltransactionsid', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgChannelTransactionsToggle###
    async def cfgGet_ChannelTransactionsToggle(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("false") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_ChannelTransactionsToggle(guild, toggle):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), toggle)
        purge = (str(guild.id), )

        #cfgSet.execute("DELETE FROM config WHERE EXISTS (SELECT * FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle')", purge)
        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgchanneltransactionstoggle'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgchanneltransactionstoggle', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###

    ###cfgTransactionsToggle###
    async def cfgGet_TransactionsToggle(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtransactionstoggle' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("true") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_TransactionsToggle(guild, toggle):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), toggle)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtransactionstoggle'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtransactionstoggle', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgTextRelease###
    async def cfgGet_TextRelease(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtextrelease' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("%playermention% has been released from %teammention%!") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_TextRelease(guild, text):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), text)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtextrelease'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtextrelease', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###


    ###cfgTextSign###
    async def cfgGet_TextSign(guild):
        cfgGet = configDb.cursor()
        payload = (str(guild.id), )

        o = str(list(cfgGet.execute("SELECT value FROM config WHERE id = ? AND name = 'cfgtextsign' LIMIT 1", payload)))[3:-4]

        if not o:
            cfgGet.close()
            return("%playermention% has been signed to %teammention%") #default value
        else:
            cfgGet.close()
            return(o)

    async def cfgSet_TextSign(guild, text):
        cfgSet = configDb.cursor()
        payload = (str(guild.id), text)
        purge = (str(guild.id), )

        cfgSet.execute("DELETE FROM config WHERE id = ? AND name = 'cfgtextsign'", purge)
        cfgSet.execute("INSERT INTO config (id, name, value) VALUES (?, 'cfgtextsign', ?)", payload)

        configDb.commit()
        cfgSet.close()
    ###

    msgPrefix = await cfgGet_CommandPrefix(message.guild)

    if message.content.startswith(msgPrefix):
        content = message.clean_content.replace(msgPrefix, "", 1).strip()
        role_mentions = message.role_mentions
        channel_mentions = message.channel_mentions
        member_mentions = message.mentions
        try:
            command = content.split()[0].lower()
        except IndexError:
            command = "null" #Sets command to null to trigger unknown
            content=(content+"null") #Adds null to content to bypass del flags.
            pass
        flags = content.lower().split() #array of input flags all lowercase.
        del flags[0]
        flagsOriginal = content.split() #array of input flags original formatting.
        del flagsOriginal[0]
        logger = logging.getLogger(message.guild.name)

        #Outputs into log when a command has been run.
        logger.info(message.author.name + ":" + content)

        if command == "config":
            try:
                flags[0]
            except IndexError:
                await message.channel.send("ERROR: Missing flag: Config Mode")
                pass
            else:

                if flags[0] == "set":

                    #Checks if user is server owner.
                    owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
                    if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or message.channel.permissions_for(message.author).administrator:

                        #Checks if a config name has been provided.
                        try:
                            flags[1]
                        except IndexError:
                            await message.channel.send("ERROR: Missing flag: Config Name")
                            pass
                        else:

                            if flags[1] == "cfgcommandprefix":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: PREFIX")
                                    pass
                                else:
                                    await cfgSet_CommandPrefix(message.guild, flags[2])
                                    await message.channel.send("cfgCommandPrefix updated. Verified value: " + await cfgGet_CommandPrefix(message.guild))

                            elif flags[1] == "cfgtransactionstoggle":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: BOOLEAN")
                                    pass
                                else:
                                    if flags[2] == "true":
                                        await cfgSet_TransactionsToggle(message.guild, flags[2])
                                        await message.channel.send("cfgTransactionsToggle updated. Verified value: " + await cfgGet_TransactionsToggle(message.guild))
                                    elif flags[2] == "false":
                                        await cfgSet_TransactionsToggle(message.guild, flags[2])
                                        await message.channel.send("cfgTransactionsToggle updated. Verified value: " + await cfgGet_TransactionsToggle(message.guild))
                                    else:
                                        await message.channel.send("ERROR: Invalid flag: Must be true/false!")

                            elif flags[1] == "cfgrolefreeagent":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleFreeAgent(message.guild, pl)
                                        await message.channel.send("cfgRoleFreeAgent updated. Verified value: " + await cfgGet_RoleFreeAgent(message.guild))

                            elif flags[1] == "cfgroleteamstaff":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleTeamStaff(message.guild, pl)
                                        await message.channel.send("cfgRoleTeamStaff updated. Verified value: " + await cfgGet_RoleTeamStaff(message.guild))

                            elif flags[1] == "cfgroleteamowner":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleTeamOwner(message.guild, pl)
                                        await message.channel.send("cfgRoleTeamOwner updated. Verified value: " + await cfgGet_RoleTeamOwner(message.guild))

                            elif flags[1] == "cfgroleserverstaff":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleServerStaff(message.guild, pl)
                                        await message.channel.send("cfgRoleServerStaff updated. Verified value: " + await cfgGet_RoleServerStaff(message.guild))

                            elif flags[1] == "cfgroleserverowner":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        role_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Role Mentions")
                                    else:
                                        pl = ""
                                        for role in role_mentions:
                                            pl = pl + str(role.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_RoleServerOwner(message.guild, pl)
                                        await message.channel.send("cfgRoleServerOwner updated. Verified value: " + await cfgGet_RoleServerOwner(message.guild))

                            elif flags[1] == "cfgchanneltransactionsid":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: ID")
                                    pass
                                else:
                                    try:
                                        channel_mentions[0]
                                    except IndexError:
                                        await message.channel.send("ERROR: Missing flag: No Channel Mentions")
                                    else:
                                        pl = ""
                                        for channel in channel_mentions:
                                            pl = pl + str(channel.id) + ","
                                        pl = pl[:-1]
                                        await cfgSet_ChannelTransactionsID(message.guild, pl)
                                        await message.channel.send("cfgChannelTransactionsID updated. Verified value: " + await cfgGet_ChannelTransactionsID(message.guild))

                            elif flags[1] == "cfgchanneltransactionstoggle":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: BOOLEAN")
                                    pass
                                else:
                                    if flags[2] == "true":
                                        await cfgSet_ChannelTransactionsToggle(message.guild, flags[2])
                                        await message.channel.send("cfgChannelTransactionsToggle updated. Verified value: " + await cfgGet_ChannelTransactionsToggle(message.guild))
                                    elif flags[2] == "false":
                                        await cfgSet_ChannelTransactionsToggle(message.guild, flags[2])
                                        await message.channel.send("cfgChannelTransactionsToggle updated. Verified value: " + await cfgGet_ChannelTransactionsToggle(message.guild))
                                    else:
                                        await message.channel.send("ERROR: Invalid flag: Must be true/false!")

                            elif flags[1] == "cfgtextrelease":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: STRING")
                                    pass
                                else:
                                    pl = flagsOriginal[2:]
                                    plStr = ' '.join(pl)
                                    await cfgSet_TextRelease(message.guild, plStr)
                                    await message.channel.send("cfgTextRelease updated. Verified value: " + await cfgGet_TextRelease(message.guild))

                            elif flags[1] == "cfgtextsign":
                                try:
                                    flags[2]
                                except IndexError:
                                    await message.channel.send("ERROR: Missing flag: STRING")
                                    pass
                                else:
                                    pl = flagsOriginal[2:]
                                    plStr = ' '.join(pl)
                                    await cfgSet_TextSign(message.guild, plStr)
                                    await message.channel.send("cfgTextSign updated. Verified value: " + await cfgGet_TextSign(message.guild))

                            else:
                                await message.channel.send("ERROR: Invalid flag: Config Name")

                    else:
                        await message.channel.send("ERROR: Config Error: You are not server owner.")

                elif flags[0] == "list":
                    #Returns all of the configs and their settings.
                    msgGuild = message.guild
                    pl = "`config set > `\n" \
                        "    `cfgCommandPrefix:` " + await cfgGet_CommandPrefix(msgGuild) + "\n" \
                        "    `cfgRoleFreeAgent:` " + await cfgGet_RoleFreeAgent(msgGuild) + "\n" \
                        "    `cfgRoleTeamStaff:` " + await cfgGet_RoleTeamStaff(msgGuild) + "\n" \
                        "    `cfgRoleTeamOwner:` " + await cfgGet_RoleTeamOwner(msgGuild) + "\n" \
                        "    `cfgRoleServerStaff:` " + await cfgGet_RoleServerStaff(msgGuild) + "\n" \
                        "    `cfgRoleServerOwner:` " + await cfgGet_RoleServerOwner(msgGuild) + "\n" \
                        "    `cfgChannelTransactionsID:` " + await cfgGet_ChannelTransactionsID(msgGuild) + "\n" \
                        "    `cfgChannelTransactionsToggle:` " + await cfgGet_ChannelTransactionsToggle(msgGuild) + "\n" \
                        "    `cfgTransactionsToggle:` " + await cfgGet_TransactionsToggle(msgGuild) + "\n" \
                        "    `cfgTextRelease:` " + await cfgGet_TextRelease(msgGuild) + "\n" \
                        "    `cfgTextSign:` " + await cfgGet_TextSign(msgGuild) + "\n"
                    await message.channel.send(pl)
                else:
                    #If provided flag is invalid.
                    await message.channel.send("ERROR: Invalid flag: Config Mode")

        elif command == "getid":
            #GetID will return the Discord ID of anything mentioned. Role, channel, or member.
            pl = ""
            for role in role_mentions:
                pl = pl + "`Role: `" + role.name + " id: " + str(role.id) + "\n"
            for channel in channel_mentions:
                pl = pl + "`Channel: `" + channel.name + " id: " + str(channel.id) + "\n"
            for member in member_mentions:
                pl = pl + "`Member: `" + member.name + " id : " + str(member.id) + "\n"
            try:
                await message.channel.send(pl)
            except discord.errors.HTTPException:
                await message.channel.send("ERROR: Must mention a role, channel, or member!")

        elif command == "msg":
            await message.channel.send("ERROR: Command error: Apologies! That function is not implemented yet!")

        elif command == "sign":
            #Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',');

            #Check if signing is enabled or valid override
            if await cfgGet_TransactionsToggle(message.guild) == "true" or \
                [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                #Gets the channel ID of the contract channel
                contract_channel = str(await cfgGet_ChannelTransactionsID(message.guild)).split(',')

                #Checks if message is in contract channel, or the contract channel is disabled. Overrides if staff or owner.
                if (await cfgGet_ChannelTransactionsToggle(message.guild) == "true" and str(message.channel.id) in contract_channel) or \
                    await cfgGet_ChannelTransactionsToggle(message.guild) == "false" or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                    #Ensure one member has been mentioned
                    try:
                        member_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Sign Error: You must mention a member!")
                    else:

                        #Ensure one role has been mentioned
                        try:
                            role_mentions[0]
                        except IndexError:
                            await message.channel.send("ERROR: Sign Error: You must mention a role!")
                        else:

                            #Get required configs for the server
                            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
                            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')
                            free_agent = str(await cfgGet_RoleFreeAgent(message.guild)).split(',')

                            #Checks if user is owner, server staff, team owner, or team staff.
                            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                                ([i for i in [str(role.id) for role in message.author.roles] if i in team_owners] and role_mentions[0] in message.author.roles) or \
                                ([i for i in [str(role.id) for role in message.author.roles] if i in team_staff] and role_mentions[0] in message.author.roles):

                                #Checks if mentioned user is a free agent.
                                if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in free_agent]:

                                    #Removes all roles that are in the Free Agent role list.
                                    for role in member_mentions[0].roles:
                                        if str(role.id) in free_agent:
                                            while role in member_mentions[0].roles:
                                                await member_mentions[0].remove_roles(role)

                                    #Adds the mentioned role to the user.
                                    while role_mentions[0] not in member_mentions[0].roles:
                                        await member_mentions[0].add_roles(role_mentions[0])

                                    #Grabs the sign text and sends it. Replaces tags where needed.
                                    await message.channel.send(str(await cfgGet_TextSign(message.guild)).replace("%playermention%", member_mentions[0].mention).replace("%teammention%", role_mentions[0].mention).replace("%playername%", member_mentions[0].name).replace("%teamname%", role_mentions[0].name))

                                else:
                                    await message.channel.send("ERROR: Sign Error: That user is not a valid free agent!")
                            else:
                                await message.channel.send("ERROR: Sign Error: You do not have permission to sign to this team!")
                else:
                    await message.channel.send("ERROR: Sign Error: You must sign within the contract channel!")
            else:
                await message.channel.send("ERROR: Sign Error: Transactions are currently disabled!")

        elif command == "release":
            #Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            #Check if signing is enabled or valid override
            if await cfgGet_TransactionsToggle(message.guild) == "true" or \
                [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                #Gets the channel ID of the contract channel as well as owners
                contract_channel = str(await cfgGet_ChannelTransactionsID(message.guild)).split(',')

                #Checks if message is in contract channel, or the contract channel is disabled. Overrides if staff or owner.
                if (await cfgGet_ChannelTransactionsToggle(message.guild) == "true" and str(message.channel.id) in contract_channel) or \
                    await cfgGet_ChannelTransactionsToggle(message.guild) == "false" or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                    #Ensure one member has been mentioned
                    try:
                        member_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Release Error: You must mention a member!")
                    else:

                        #Ensure one role has been mentioned
                        try:
                            role_mentions[0]
                        except IndexError:
                            await message.channel.send("ERROR: Release Error: You must mention a role!")
                        else:

                            #Get required configs for the server
                            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
                            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')
                            free_agent = str(await cfgGet_RoleFreeAgent(message.guild)).split(',')

                            #Checks if user is owner, server staff, team owner, or team staff.
                            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                                ([i for i in [str(role.id) for role in message.author.roles] if i in team_owners] and role_mentions[0] in message.author.roles) or \
                                ([i for i in [str(role.id) for role in message.author.roles] if i in team_staff] and role_mentions[0] in message.author.roles):

                                #Checks if mentioned user is on mentioned team.
                                if str(role_mentions[0].id) in [str(role.id) for role in member_mentions[0].roles]:

                                    #Checks if user is currently staff
                                    if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_staff]:
                                        await message.channel.send("ERROR: Release Error: That user is a team staff. Demote them before releasing them.")

                                    elif [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_owners]:
                                        await message.channel.send("ERROR: Release Error: That user is a team owner. Demote them before releasing them.")
                                    else:
                                        #Removes mentioned role.
                                        while role_mentions[0] in member_mentions[0].roles:
                                            await member_mentions[0].remove_roles(role_mentions[0])

                                        #Adds free agent role.
                                        for roleID in free_agent:
                                            free_agent_role = discord.utils.find(lambda f: f.id == int(roleID), message.guild.roles)
                                            while free_agent_role not in member_mentions[0].roles:

                                                #Checks if the bot can assign the role, and ignores an exception if it can't.
                                                try:
                                                    await member_mentions[0].add_roles(free_agent_role)
                                                except discord.errors.Forbidden:
                                                    await message.channel.send("ERROR: Release Error: Unable to assign the following role: " + free_agent_role.mention + "\nPlease check your free agent settings!")
                                                    pass

                                        #Grabs the sign text and sends it. Replaces tags where needed.
                                        await message.channel.send(str(await cfgGet_TextRelease(message.guild)).replace("%playermention%", member_mentions[0].mention).replace("%teammention%", role_mentions[0].mention).replace("%playername%", member_mentions[0].name).replace("%teamname%", role_mentions[0].name))

                                else:
                                    await message.channel.send("ERROR: Release Error: That user is not on that team!")
                            else:
                                await message.channel.send("ERROR: Release Error: You do not have permission to sign to this team!")
                else:
                    await message.channel.send("ERROR: Release Error: You must sign within the contract channel!")
            else:
                await message.channel.send("ERROR: Release Error: Transactions are currently disabled!")

        elif command == "promote":
            #Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            #Grabs team owners and team staff for authentication
            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')

            #Checks if message author is either an owner, server staff, or team owner.
            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in team_owners]:

                #Checks if a member was mentioned.
                try:
                    member_mentions[0]
                except IndexError:
                    await message.channel.send("ERROR: Promote Error: You must mention a member!")
                else:

                    #Checks if a team and staff role was mentioned.
                    try:
                        role_mentions[0]
                        role_mentions[1]
                    except IndexError:
                        await message.channel.send("ERROR: Promote Error: You must mention two roles! One team and a staff role.")
                    else:

                        #Figures out which role mentioned is the staff role.
                        if (str(role_mentions[0].id) in team_staff or str(role_mentions[0].id) in team_owners) and str(role_mentions[1].id) not in team_staff:
                            staff_role = role_mentions[0]
                            team_role = role_mentions[1]
                        elif (str(role_mentions[1].id) in team_staff or str(role_mentions[1].id) in team_owners) and str(role_mentions[0].id) not in team_staff:
                            staff_role = role_mentions[1]
                            team_role = role_mentions[0]
                        else:
                            await message.channel.send("ERROR: Promote Error: It seems that both roles you've mentioned are staff roles or team roles.")
                            return

                        #If staff_role has been set, continue
                        if staff_role:

                            #Checks if staff role is team owner.
                            if str(staff_role.id) in team_owners:

                                #Checks that user is server staff before assigning team owner role.
                                if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                                    while staff_role not in member_mentions[0].roles:
                                        try:
                                            await member_mentions[0].add_roles(staff_role)
                                        except discord.errors.Forbidden:
                                            await message.channel.send("ERROR: Promote Error: Unable to assign the staff role! Check permissions.")
                                            pass
                                        else:
                                            await message.channel.send(member_mentions[0].mention + " has been promoted to " + staff_role.mention)

                                else:
                                    await message.channel.send("ERROR: Promote Error: Only server staff can promote to team owner!")

                            else:
                                #Checks if user is on the team
                                if team_role in member_mentions[0].roles:

                                    #Checks if user is not already staff:
                                    if not [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_staff]:

                                        #Checks that message author is on the mentioned team. Verifies override.
                                        if team_role in message.author.roles or \
                                            [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                            [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                                            #Assigns staff role.
                                            while staff_role not in member_mentions[0].roles:
                                                try:
                                                    await member_mentions[0].add_roles(staff_role)
                                                except discord.errors.Forbidden:
                                                    await message.channel.send("ERROR: Promote Error: Unable to assign the staff role! Check permissions.")
                                                    pass
                                                else:
                                                    await message.channel.send(member_mentions[0].mention + " has been promoted to " + staff_role.mention)
                                        else:
                                            await message.channel.send("ERROR: Promote Error: It seems you are not the owner of that team!")

                                    else:
                                        await message.channel.send("ERROR: Promote Error: That user is already a staff member!")

                                else:
                                    await message.channel.send("ERROR: Promote Error: That user is not on the mentioned team!")

            else:
                await message.channel.send("ERROR: Promote Error: You do not have the required roles to promote!")

        elif command == "demote":
            #Grabs server staff for override.
            owners = str(await cfgGet_RoleServerOwner(message.guild)).split(',')
            server_staff = str(await cfgGet_RoleServerStaff(message.guild)).split(',')

            #Grabs team owners and team staff for authentication
            team_owners = str(await cfgGet_RoleTeamOwner(message.guild)).split(',')
            team_staff = str(await cfgGet_RoleTeamStaff(message.guild)).split(',')

            #Checks if message author is either an owner, server staff, or team owner.
            if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in server_staff] or \
                [i for i in [str(role.id) for role in message.author.roles] if i in team_owners]:

                #Checks if a member was mentioned.
                try:
                    member_mentions[0]
                except IndexError:
                    await message.channel.send("ERROR: Demote Error: You must mention a member!")
                else:

                    #Checks if a team was mentioned. A staff role does not need to be mentioned here.
                    try:
                        role_mentions[0]
                    except IndexError:
                        await message.channel.send("ERROR: Demote Error: You must mention a team!")
                    else:

                        #Checks if user is on team
                        if role_mentions[0] in member_mentions[0].roles:

                            #Checks if user is staff.
                            if [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_staff]:

                                #Checks if author is a team owner. Checks override.
                                if role_mentions[0] in message.author.roles or \
                                    [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                                    #Removes staff role.
                                    for role in member_mentions[0].roles:
                                        if str(role.id) in team_staff:
                                            while role in member_mentions[0].roles:
                                                try:
                                                    await member_mentions[0].remove_roles(role)
                                                except discord.errors.Forbidden:
                                                    await message.channel.send("ERROR: Demote Error: Unable to remove the staff role! Check permissions.")
                                                    pass
                                                else:
                                                    await message.channel.send(member_mentions[0].mention + " has been demoted from " + role.mention)

                                else:
                                    await message.channel.send("Error: Demote Error: You are not on that team.\n`Tip: Do not mention the role you are demoting from!`")

                            #If user is not staff, check if they are team owners.
                            elif [i for i in [str(role.id) for role in member_mentions[0].roles] if i in team_owners]:

                                #Checks if author is server staff or server owner.
                                if [i for i in [str(role.id) for role in message.author.roles] if i in owners] or \
                                    [i for i in [str(role.id) for role in message.author.roles] if i in server_staff]:

                                    #Removes team owner role.
                                    for role in member_mentions[0].roles:
                                        if str(role.id) in team_owners:
                                            while role in member_mentions[0].roles:
                                                try:
                                                    await member_mentions[0].remove_roles(role)
                                                except discord.errors.Forbidden:
                                                    await message.channel.send("ERROR: Demote Error: Unable to remove the team owner role! Check permissions.")
                                                    pass
                                                else:
                                                    await message.channel.send(member_mentions[0].mention + " has been demoted from " + role.mention)

                                else:
                                    await message.channel.send("Error: Demote Error: Only server staff and server owners can demote team owners!")

                            else:
                                await message.channel.send("Error: Demote Error: That user is not currently staff.")

                        else:
                            await message.channel.send("Error: Demote Error: That user is not on that team.")

            else:
                await message.channel.send("Error: Demote Error: You do not have permission to do that.")

        elif command == "servers":
            await message.channel.send("Currently connected to " + str(sum(1 for x in client.guilds)) + " servers.")

        elif command == "invite":
            await message.channel.send("To invite this bot, check out the offical MagicLeague Development server!\nhttps://discord.gg/fTWQQAn")

        elif command == "help":
            pl = "`MagicLeague 2 Help Guide`\n" + \
            "`getid <@member, @role, #channel>` Returns the ID of a mentioned role, member, or channel.\n" + \
            "`sign <@member> <@team>` Sign a free agent to your team.\n" + \
            "`release <@member> <@team>` Releases a member from your team.\n" + \
            "`promote <@member> <@team> <@team_staff_role>` Promotes a member of a team to the tagged team staff role.\n" + \
            "`demote <@member> <@team>` Demotes a team staff member.\n" + \
            "`servers` Returns the number of servers the bot is currently connected to.\n" + \
            "`invite` Returns a link to the offical MagicLeague server, with a guide on how to install this bot.\n" + \
            "`help` Shows this text.\n" + \
            "`stats <game>` Provides competitive stats for various videogames. See `stats list` for details.\n" + \
            "`MagicLeague 2 version: " + version_num + "`"
            await message.channel.send(pl)

        elif command == "stats":
            try:
                flags[0]
            except IndexError:
                await message.channel.send("ERROR: Missing flag: Game")
                pass
            else:

                #Posts overwatch stats.
                if flags[0] == "overwatch":

                    #Checks if battletag is given.
                    try:
                        flags[1]
                    except IndexError:
                        await message.channel.send("ERROR: Missing flag: Battletag")
                    else:

                        #Sets headers for HTTP GET
                        headers = {
                            'User-Agent': 'MagicLeague Discord Bot',
                            'From': 'email@gmail.com'
                        }

                        #Changes # in battletag to a dash.
                        tag = str(flagsOriginal[1]).replace("#","-")

                        #Creates call URL for OWAPI.
                        call = "https://owapi.net/api/v3/u/" + tag + "/stats"

                        #Sends loading message and gets stats.
                        wait1 = await message.channel.send("Searching OWAPI Stats...")
                        response = requests.get(call, headers=headers)

                        #Deletes loading message.
                        await wait1.delete()

                        #Converts returned data to Python Dictionary.
                        stats = response.json() #https://github.com/SunDwarf/OWAPI/blob/master/api.md

                        #Creates second call URL for OWAPI.
                        call = "https://owapi.net/api/v3/u/" + tag + "/heroes"

                        #Posts loading message and gets second set of stats.
                        wait2 = await message.channel.send("Searching OWAPI Heroes...")
                        response = requests.get(call, headers=headers)

                        #Deletes loading message.
                        await wait2.delete()

                        #Converts returned data to Python Dictionary
                        heroes = response.json()

                        #Sorts dictionary into array by playtime.
                        top3 = [["Junkrat",heroes['us']['heroes']['playtime']['competitive']['junkrat']],["Soldier76",heroes['us']['heroes']['playtime']['competitive']['soldier76']],["Hanzo",heroes['us']['heroes']['playtime']['competitive']['hanzo']],["Bastion",heroes['us']['heroes']['playtime']['competitive']['bastion']],["Torbjorn",heroes['us']['heroes']['playtime']['competitive']['torbjorn']],["Winston",heroes['us']['heroes']['playtime']['competitive']['winston']],["D.Va",heroes['us']['heroes']['playtime']['competitive']['dva']],["Ana",heroes['us']['heroes']['playtime']['competitive']['ana']],["Reinhardt",heroes['us']['heroes']['playtime']['competitive']['reinhardt']],["Lucio",heroes['us']['heroes']['playtime']['competitive']['lucio']],["Pharah",heroes['us']['heroes']['playtime']['competitive']['pharah']],["McCree",heroes['us']['heroes']['playtime']['competitive']['mccree']],["Reaper",heroes['us']['heroes']['playtime']['competitive']['reaper']],["Zarya",heroes['us']['heroes']['playtime']['competitive']['zarya']],["Mercy",heroes['us']['heroes']['playtime']['competitive']['mercy']],["Symmetra",heroes['us']['heroes']['playtime']['competitive']['symmetra']],["Zenyatta",heroes['us']['heroes']['playtime']['competitive']['zenyatta']],["Widowmaker",heroes['us']['heroes']['playtime']['competitive']['widowmaker']],["Mei",heroes['us']['heroes']['playtime']['competitive']['mei']],["Tracer",heroes['us']['heroes']['playtime']['competitive']['tracer']],["Roadhog",heroes['us']['heroes']['playtime']['competitive']['roadhog']],["Genji",heroes['us']['heroes']['playtime']['competitive']['genji']]]

                        #Sorts the array by seconds of playtime.
                        top3.sort(key=lambda x: x[1])

                        #Reverses array to make largest number first.
                        top3.reverse()

                        #Trims all but the top 3.
                        top3 = top3[:-19]

                        #Creates payload to send as well as generates HH:MM:SS timestamps for playtime.
                        pl = "```OVERWATCH STATS (ALPHA)\n\n" \
                            "Battletag: " + tag + "\n" \
                            "Level: " + str(stats['us']['stats']['competitive']['overall_stats']['level']) + "\n" \
                            "Prestige: " + str(stats['us']['stats']['competitive']['overall_stats']['prestige']) + "\n" \
                            "Competitive Wins: " + str(stats['us']['stats']['competitive']['overall_stats']['wins']) + "/" + str(stats['us']['stats']['competitive']['overall_stats']['games']) + "\n" \
                            "Competitive Rank: " + str(stats['us']['stats']['competitive']['overall_stats']['comprank']) + "\n" \
                            "Competitive Kills: " + str(stats['us']['stats']['competitive']['game_stats']['eliminations']) + "\n" \
                            "Competitive Deaths: " + str(stats['us']['stats']['competitive']['game_stats']['deaths']) + "\n" \
                            "Competitive KDR: " + str(stats['us']['stats']['competitive']['game_stats']['kpd']) + "\n\n" \
                            "Competitive Playtime (Top 3):\n" \
                            "    " + str(top3[0][0]) + ": " + str("%d:%02d.%02d" % (int(top3[0][1]), (top3[0][1]*60)%60, (top3[0][1]*3600)%60)) + "\n" \
                            "    " + str(top3[1][0]) + ": " + str("%d:%02d.%02d" % (int(top3[1][1]), (top3[1][1]*60)%60, (top3[1][1]*3600)%60)) + "\n" \
                            "    " + str(top3[2][0]) + ": " + str("%d:%02d.%02d" % (int(top3[2][1]), (top3[2][1]*60)%60, (top3[2][1]*3600)%60)) + "\n" \
                            "```"

                        #Sends message.
                        await message.channel.send(pl)

                elif flags[0] == "csgo":
                    await message.channel.send("ERROR: Command error: Apologies! That function is not implemented yet!")

                elif flags[0] == "tf2":
                    await message.channel.send("ERROR: Command error: Apologies! That function is not implemented yet!")

                #Lists all of the games supported.
                elif flags[0] == "list":
                    pl = "`stats >`\n" \
                        "    `overwatch battle#tag`: Loads Overwatch stats from OWAPI!\n" \
                        "    `csgo ni`: Loads CS:GO stats from CS:GO Stats! [Not Implemented]\n" \
                        "    `tf2 ni`: Loads Team Fortress 2 stats from Team Fortress 2 Stats! [Not Implemented]\n"
                    await message.channel.send(pl)

                else:
                    await message.channel.send("ERROR: Invalid flag: Game\/List")
        else:
            logger.info("Ignoring invalid command.")

#Run client.
client.run('KEY')
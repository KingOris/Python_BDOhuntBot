from discord.ext.commands import Bot

Bot_Prefix = ("?", "~")
TOKEN = "NTM4NDY1Mzc5NjY0NTI3NDEx.Dy1zeQ.3FwlKeRU5Am1bS4MqmKH-gxpfAc"

client = Bot(command_prefix=Bot_Prefix)
guild_name_list = []

g_l_file = open("GuildName", "r")
gnames = g_l_file.readline()
while gnames:
    guild_name_list.append(gnames)
    gnames = g_l_file.readline()
g_l_file.close()

"""""
@client.command(name='hunting',
                description="Show bounty hunting list",
                brief="Show hunting list"
                )
#async def hunting():
    for HuntingDic in listHunting:
        await client.say('Guild' + ' ' + HuntingDic.guild + ' ' + 'CharacterName' + ' ' + HuntingDic.name)
"""""


@client.command()
async def adding(guild, name):
    add_hunt_list(guild, name)
    await client.say(
        'Guild' + ' ' + guild + ' ' + 'CharacterName' + ' ' + name + ' has been added')


@client.command()
async def listing():
    for guildName in guild_name_list:
        await client.say("Guild: " + guildName)
        file = open(guildName, "r")
        try:
            names = file.readline()
            while names:
                if names != " ":
                    await client.say(names)
                    names = file.readline()
        except IOError:
            await client.say("No hunting list")
    file.close()

def add_hunt_list(guildName, name):
    try:
        file = open(guildName, "a")
        file.write(name + "\n")
        file.close()
        guild_name_list.append(guildName)
    except IOError:
        newFile = open(guildName, "+")
        newFile.write(name + "\n")
        newFile.close()


client.run(TOKEN)

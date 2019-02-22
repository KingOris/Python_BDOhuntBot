from discord.ext.commands import Bot

"""""
@Created by Yuhang chen(Kingoris)
@Date: 2/20/2019
@Discription:
    This bot is for record hunting people in Black Desert online
"""""
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


@client.command(name='adding',
                description="Adding [guild] [name] for hunting",
                brief="Adding [guild] [name]")
async def adding(guild, name):
    add_hunt_list(guild, name)
    await client.say(
        'Guild' + ' ' + guild + ' ' + 'CharacterName' + ' ' + name + ' has been added')


@client.command(name='listing',
                description="List all data",
                brief="List all data")
async def listing():
    if len(guild_name_list) != 0:
        for guildName in guild_name_list:
            await client.say("Guild: " + guildName)
            file = open(guildName, "r")
            try:
                names = file.readline()
                while names:
                    if names != " ":
                        await client.say("-"+names)
                        names = file.readline()
            except IOError:
                await client.say("No hunting list")
        file.close()
    else:
        await client.say("No hunting list")


def add_hunt_list(guildName, name):
    file = open(guildName, "a")
    file.write(name + "\n")
    file.close()
    guild_name_list.append(guildName)
    guild_name = open("GuildName", "a")
    guild_name.write(guildName + "\n")
    guild_name.close()


client.run(TOKEN)

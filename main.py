import discord
from decouple import config

client = discord.Client()

bot_token = config('TOKEN')
prefix = ';'
cap = 250
check = False

def __init__(self):
    self.prefix = ';'
    self.cap = 250
    self.check = False


@client.event
async def on_ready():
    print('We have logged in arse {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(
        type=discord.ActivityType.playing, name=prefix + "spam across all servers"
    ))


@client.event
async def on_message(message):
    if message.context.startswith(prefix + 'stop'):
        global check
        check = True


try:
    @client.event
    async def on_message(message):

        send = ""
        global prefix
        global cap

        todo = message.content.split(prefix, 1)[1].split(' ' + prefix)

        if message.author == client.user:
            return

        if message.content.startswith(prefix + 'help'):
            await message.channel.send(">>> ***Hey! " + message.author.name + ''',*** you can *spam* messages into any text channel just by typing 
             `''' + prefix + '''spam ''' + prefix + '''[your text] ''' + prefix + '''[number of times to send]`
              _Example_ : `''' + prefix + '''spam ''' + prefix + '''I am Spamcord ''' + prefix + '''10` \n \n Wanna change the prefix `''' + prefix + '''`, I got you covered - type `''' + prefix + '''changepf <your prefix here>`
              
              **ENJOY TROLLING  YOUR FRIENDS XD** :joy:''')

        if message.content.startswith(prefix + 'changepf'):
            prefix = message.content.split(' ')[1]
            await message.channel.send(
                    'Yay! I successfully changed the prefix to ' + prefix + ", on the request of " + message.author.name)

        if message.content.startswith(prefix + 'hello') or message.content.startswith(prefix + 'hi'):
            await message.channel.send('Hello! ' + message.author.name)

        if message.content.startswith(prefix + 'spam'):
            try:
                if int(todo[2]) > cap:
                    await message.channel.send("Sorry But due to DISCORD Limitations We are not allowed to spam more than " + str(cap) + " messages to this channel. Please enter a number less than that :D")
                elif int(todo[2]) < 1:
                    await message.channel.send("Please enter a valid number ^_^")
                else:
                    for i in range(int(todo[2])):
                        global check
                        await message.channel.send(todo[1])
                        if check:
                            check = False
                            break
            finally:
                print(IndexError)

        if message.content.startswith(prefix + 'setcap'):
            await message.channel.send("Noice! now the spam cap is set to " + message.content.split(' ')[1] + ", instead of " + str(cap) + ", on the request of " + message.author.name)
            cap = int(message.content.split(' ')[1])

        if message.content.startswith(prefix + 'cap'):
            await message.channel.send("The current spam cap is " + str(cap))

finally:
    print(Exception)
client.run(bot_token)

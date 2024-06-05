import discord
from openai import OpenAI

#MTIzOTA4NTQ4MjA1MTI0NDA2Mg.GlY4Yh.M74t3TbBkdl12RAMe01QuegZXVMqvRpDPjWYvk

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
model = OpenAI()

@client.event
async def on_ready():
    print('We have logged in as' + str(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Hello"):
        await message.channel.send("Hello!")

client.run('MTIzOTA4NTQ4MjA1MTI0NDA2Mg.GlY4Yh.M74t3TbBkdl12RAMe01QuegZXVMqvRpDPjWYvk')


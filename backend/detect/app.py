import discord
from openai import OpenAI
import os


intents = discord.Intents.default()
intents.message_content = True
token = os.environ["TOKEN"]
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

client.run(token)

import discord
from openai import OpenAI
import os
from pathlib import Path
import hashlib
import google.generativeai as genai

intents = discord.Intents.default()
intents.message_content = True
token = os.getenv('TOKEN')
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as' + str(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Hello"):
        await message.channel.send("Hello!")

    genai.configure(api_key=os.getenv('GOOGLE_API'))
    generation_config = {
        "temperature": 1,
         "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
    }
    model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                              generation_config=generation_config,)
                              # safety_settings = Adjust safety settings
                              # See https://ai.google.dev/gemini-api/docs/safety-settings)

    prompt_parts = [
            "\n This is a discord message from a user: '"+message.content+"'. Does it have profanity?",
    ]
    response = model.generate_content(prompt_parts)
    await message.channel.send(response.text)

client.run(token)

# bot.py
import os

import discord
from dotenv import load_dotenv
import random
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break;
    
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    answers = [
        'Jakub Ráček má ho velký jako vláček',
        'Tomáš David je velký debil',
        'Milan Šmatlubec je můj otec'
    ]

    if message.content == '!random':
        response = random.choice(answers)
        await message.channel.send(response)

client.run(TOKEN)
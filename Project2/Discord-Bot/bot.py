import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    rick_and_morty_quotes = [
        'Wubba Lubba Dub Dub!',
        'What, so everyone’s supposed to sleep every single night now? You realize that nighttime makes up half of all time?',
        'Boom! Big reveal! I turned myself into a pickle!',
        'Nobody exists on purpose. Nobody belongs anywhere. We’re all going to die. Come watch TV.',
        'Weddings are basically funerals with a cake.',
        'Honey, stop raising your father’s cholesterol so you can take a hot funeral selfie.',
    ]

    if message.content == 'towel!':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(hitchhiker_quotes)
        await message.channel.send(response)

    if message.content == '!pickle':
        response = random.choice(rick_and_morty_quotes)
        await message.channel.send(response)

client.run(TOKEN)

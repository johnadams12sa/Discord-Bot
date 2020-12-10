#does not compile atm, just a bare bones scratching 12/10/20 Ron

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to the server!')

client.run(TOKEN)

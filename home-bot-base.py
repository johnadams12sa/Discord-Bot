#does not compile atm, just a bare bones scratching 12/10/20 Ron

import os
import greeting

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user} has connected to the server!')

@client.event
async def on_message(message):
	#checks if the message is from the bot itself, we don't want a loop
	if message.author == client.user:
		return
	
	if message.content.startswith('$hello'):
		await message.channel.send(greeting.greet(message.author))

client.run(TOKEN)

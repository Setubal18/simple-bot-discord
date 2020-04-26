import random

import discord

from config import TOKEN
from guildFunctions import getGuild
from messagens import sw_quotes

client = discord.Client()

@client.event
async def on_ready():
	guild = getGuild()
	print(
		f'{client.user} has connected to Discord! \n'
		f'{guild.name}(id: {guild.id})'
	)


@client.event
async def on_member_join(member):
	guild = getGuild()

	await member.create_dm()
	await member.dm_channel.send(
		f'Olá {member.name}, Bem-vindo ao {guild.name} guild'
	)


@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if '!sw' in message.content.lower():
		res = random.choice(sw_quotes)
		await message.channel.send(res)
	elif message.content == 'raises-exption':
		raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
	with open('err.log', 'a') as f:
		if event == 'on_message':
			f.write(f'Unhandled message: {args[0]}\n')
		else:
			raise


client.run(TOKEN)
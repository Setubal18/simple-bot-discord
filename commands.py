import random

import discord
from discord.ext import commands

from config import TOKEN
from messagens import st_quotes, sw_quotes

bot = commands.Bot(command_prefix='!')


@bot.command(name='st', help='Responde com uma frase aleatória de Star Trek')
async def startrek(ctx):
	res = random.choice(st_quotes)
	print(res)
	await ctx.send(res)


@bot.command(name='roll', help='Roll a Dice')
async def roll(ctx, number_of_dice=1, number_of_sides=20):
	dice = [
		str(random.choice(range(1, number_of_sides + 1)))
		for _ in range
		(number_of_dice)
	]

	await ctx.send(', '.join(dice))


@bot.command(name='create_channel')
@commands.has_guild_permissions()
async def create_channel(ctx, channel_name):
	print('print ctx', ctx)
	print('-------------------------')
	guild = ctx.guild
	if channel_name:
		existing_channel = discord.utils.get(guild.channels, name=channel_name)
		if not existing_channel:
			print(f'Novo Canal criado:{channel_name}')
			await guild.create_text_channel(channel_name)
		else:
			await ctx.send('Canal já existe')
	else:
		raise discord.DiscordException


@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.errors.CheckFailure):
		await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)

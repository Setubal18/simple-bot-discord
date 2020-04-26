import discord

from config import GUILD_ID

client = discord.Client()


def getGuild():
	return discord.utils.find(
		lambda g: str(g.id) == GUILD_ID, client.guilds
	)

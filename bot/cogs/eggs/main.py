from discord.ext.commands import Cog
from .._utils import is_valid, BOT_NAME
import asyncio
from re import search, match

class General(Cog, name="Eggs"):
	def __init__(self, client):
		self.bot = client

	@Cog.listener("on_message")
	async def gaygames(self, msg):
		if is_valid(self.bot, msg) and msg.guild.id == 433298614564159488:
			for gaygame in (
				"кс",
				"cs",
				"мм",
				"mm",
				"рафт",
				"raft",
				"фортнайт",
				"fortnite"
				"раст",
				"rust",
				"osu",
				"осу",
				"destiny",
				"дестини",
				"дестени",
			):
				if search(f"\\b{gaygame}\\b", msg.content.lower()):
					await msg.channel.send(f"{gaygame}? Ебать ты гей 🤡, иди в мут нахуй")
					old_perms = msg.channel.overwrites_for(msg.author)
					temp_perms = msg.channel.overwrites_for(msg.author)
					temp_perms.send_messages = False
					await msg.channel.set_permissions(msg.author, overwrite=temp_perms)
					await asyncio.sleep(20)
					await msg.channel.set_permissions(msg.author, overwrite=old_perms)
					break

def setup(client):
	client.add_cog(General(client))
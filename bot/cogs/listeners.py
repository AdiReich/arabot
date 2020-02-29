from discord.ext import commands
from discord.ext.commands import Cog
from discord.ext.commands.errors import *
from ._utils import setPresence
#import discord


class Listeners(Cog):
	def __init__(self, client):
		self.bot = client

	@Cog.listener()
	async def on_ready(self):
		await setPresence(self.bot, 3, "#lewd")
		print("Ready!")
		#await startTimer()

	"""
	from datetime import datetime, timedelta

	async def startTimer(self):
		now = datetime.now
		resets = [0, 3, 5, 7]
		while True:
			# Find next event reset date
			async for i in arange(len(resets)):
				today = now()
				if resets[i] <= today.weekday() < resets[i + 1]:
					reset = (today + timedelta(days=resets[i + 1] - today.weekday()
						)).replace(hour=0, minute=0, second=0, microsecond=0)
					break
			# Count down
			while True:
				await asyncio.sleep(60)
				totalSeconds = (reset - now()).total_seconds()
				if totalSeconds <= 0:
					break
				hours = int(totalSeconds / 3600)
				minutes = int(totalSeconds % 3600 / 60) + 1
				await bot.get_channel(678423053306298389).edit(name=f"🌍 {hours}h {minutes}m")
"""

	@Cog.listener()
	async def on_command_error(self, ctx, error):
		if hasattr(ctx.command, "on_error") or isinstance(
			error, ( # Ignore following errors
			commands.CommandNotFound,
			MissingPermissions,
			CheckFailure,
			BadArgument,
			MissingRequiredArgument,
			)
		):
			return
		raise error


def setup(client):
	client.add_cog(Listeners(client))
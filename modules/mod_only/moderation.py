from __future__ import annotations

import disnake
from disnake.ext import commands

class moderation(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self._bot: commands.Bot = bot
    
def setup(bot: commands.Bot) -> None:
    bot.add_cog(moderation(bot))

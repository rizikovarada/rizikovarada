from __future__ import annotations

import disnake
from disnake.ext import commands

class ready(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self._bot: commands.Bot = bot
        
    @commands.Cog.listener("on_ready")
    async def _is_ready(self) -> None:
        await self._bot.change_presence(activity=disnake.Activity(
            type=disnake.ActivityType.watching, name="r/rizikovarada"))
    
def setup(bot: commands.Bot) -> None:
    bot.add_cog(ready(bot))
    
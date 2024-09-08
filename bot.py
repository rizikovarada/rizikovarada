from __future__ import annotations

import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot_instance = commands.Bot(command_prefix='>', intents=intents, owner_id=1193170416991207436)

from os import listdir
for file in listdir('modules/'):
    if not file.endswith('.py'): continue
    bot_instance.load_extension(f'modules.{file[:-3]}')
    
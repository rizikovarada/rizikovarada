from __future__ import annotations

import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
bot_instance = commands.Bot(command_prefix=">", intents=intents, owner_id=1193170416991207436)

from os import path, listdir

def _recursive_modules(path_local: str) -> None:
    for file in listdir(path_local):
        full_path = path.join(path_local, file)
        
        if path.isdir(full_path): 
            _recursive_modules(full_path)
        elif file.endswith(".py"):
            module_name = full_path[:-3].replace(path.sep, ".")
            bot_instance.load_extension(module_name)

_recursive_modules(path.join(".", "modules"))

from __future__ import annotations

from config import env_cnf

import disnake
from bot import bot_instance

if __name__ == "__main__" and env_cnf.token is not None:
    try:
        bot_instance.run(env_cnf.token)
    except disnake.errors.LoginFailure as e: # TODO: write unique error message for this exception >
        print("It seems you did not provide the bot token for the launch, please try again")
elif env_cnf.token is None:
    print("It seems you did not provide the bot token for the launch, please try again")
    
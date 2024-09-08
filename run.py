from __future__ import annotations

from config import env_cnf

from bot import bot_instance

if __name__ == "__main__" and env_cnf.token is not None:
    bot_instance.run(env_cnf.token)
    
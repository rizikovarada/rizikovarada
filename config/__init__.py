from __future__ import annotations

from dotenv import load_dotenv; load_dotenv()
from os import environ

from dataclasses import dataclass

@dataclass
class env_cnf: 
    token: str | None = environ.get("TOKEN")
    
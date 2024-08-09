from os import getenv
from typing import Any

from dotenv import load_dotenv


class Config:
    def __init__(self, env_file: str = ".env"):
        load_dotenv(env_file)

    def get(self, key: str, default: Any = None):
        return getenv(key, default)

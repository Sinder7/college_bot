from dotenv import load_dotenv
from dataclasses import dataclass
from environs import Env


@dataclass
class Bots():
    token: str

@dataclass
class Settings():
    bot: Bots

def get_settings(path: str) -> str:
    env = Env()
    env.read_env(path)

    return Settings(
        bot=Bots(
            token = env.str("TOKEN")
        )
    )

settings = get_settings('.env')
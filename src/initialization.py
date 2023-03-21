from wonda.bot import Bot
from tortoise import Tortoise

from src.config import *
from src import blueprints, middlewares
from src.database.data import Data


async def setup_database() -> None:
    await Tortoise.init(
        db_url="sqlite://db.sqlite",
        modules={"models": ["src.database.user", "src.database.data"]},
    )

    await Tortoise.generate_schemas()
    
    if await Data.get_or_none(id=1):
        await Data.create()


def setup_blueprints(bot: Bot) -> None:
    for bp in blueprints.bps:
        bp.load(bot)


def setup_middlewares(bot: Bot) -> None:
    for bp in middlewares.bps:
        bp.load(bot)


def setup_bot() -> Bot:
    bot = Bot(BOT_TOKEN)

    setup_blueprints(bot=bot)
    setup_middlewares(bot=bot)

    return bot



from wonda.bot import Blueprint, Message
from wonda.bot.rules.message import Command
from wonda.api.utils import File

from src.database.user import User
from src.keyboards import Keyboard
from src.const import Path

bp = Blueprint("Default telegram command /start")


@bp.on.message(Command("start"))
async def start_handler(message: Message):
    await message.ctx_api.send_photo(
        caption=(
            f"📄 Здравствуйте, {message.from_.first_name}!\n"
            "• Выберите вариант, который вас интересует."
        ),
        photo=File.from_path(Path.menu),
        chat_id=message.chat.id,
        reply_markup=Keyboard.menu
    )

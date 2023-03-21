from wonda.bot import Blueprint, Message
from wonda.bot.rules import Text
from wonda.bot.updates import BotUpdateType, CallbackQuery

from src.keyboards import Keyboard

bp = Blueprint("UPDATE: Back to menu")


@bp.on.raw_update(BotUpdateType.CALLBACK_QUERY, CallbackQuery, Text("menu"))
async def back_to_menu_handler(update: Message):
    await update.ctx_api.send_message(
        f"📄 {update.from_.first_name}, вы в меню.",
        update.message.chat.id,
        reply_markup=Keyboard.menu
    )

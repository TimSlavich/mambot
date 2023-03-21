from wonda.bot import Blueprint, Message
from wonda.bot.rules import Text
from wonda.bot.updates import BotUpdateType, CallbackQuery
from wonda.tools.text import ParseMode

from src.keyboards import Keyboard

bp = Blueprint("UPDATE: Get info")


@bp.on.raw_update(BotUpdateType.CALLBACK_QUERY, CallbackQuery, Text("info"))
async def info_handler(update: Message):
    await update.ctx_api.send_message(
        "📘 **Информация**\n"
        "\n"
        "🤖 Этот бот **позволяет** клиентам **записаться** на приём к косметологу\.\n"
        "\n"
        "💄 Предоставляемые процедуры:\n"
        "• Массаж лица\n"
        "• Корбокси\-терапия не инъекционная\n"
        "• Чистка лица\n"
        "• Редермализация __\(увлажнение и улучшение состояния кожи\, лифтинг с помощью инъекции\)__\n"
        "• Мезотерапия для лица и волос __\(витаминные инъекции\)__\n"
        "• Агментация губ\n"
        "• Инъекции ботекса\n"
        "• Антицеллюлитный массаж\n"
        "• Лечебный массаж",
        update.message.chat.id,
        reply_markup=Keyboard.back_to_menu,
        parse_mode=ParseMode.MARKDOWN
    )

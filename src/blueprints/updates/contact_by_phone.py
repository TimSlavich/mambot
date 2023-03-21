from wonda.bot import Blueprint, Message, BaseStateGroup
from wonda.bot.rules import Text, State
from wonda.bot.updates import BotUpdateType, CallbackQuery
from wonda.tools.text import ParseMode

from src.database.user import User
from src.config import ADMIN_IDS
from src.keyboards import Keyboard

bp = Blueprint("UPDATE: Contact by phone")


class MenuState(BaseStateGroup):
    CONTACTS_INFO = "contacts_info"
    CONTACT_BY_PHONE = "contact_by_phone"


@bp.on.raw_update(BotUpdateType.CALLBACK_QUERY, CallbackQuery, Text("contact_by_phone"))
async def contact_by_phone_handler(update: Message):
    await update.ctx_api.send_message(
        "☎️ Наши контакты:\n"
        "\n"
        "• Vodafone: `+38 (050) 726 80-89`\n"
        "• Київстар: `+38 (068) 682 12-00`\n"
        "\n"
        "💡 Вы можете отправить свой номер телефона для связи с вами\.",
        update.message.chat.id,
        reply_markup=Keyboard.send_phone,
        parse_mode=ParseMode.MARKDOWN
    )
    await bp.state_dispenser.set(update.message.chat.id, MenuState.CONTACT_BY_PHONE)


@bp.on.message(State(MenuState.CONTACT_BY_PHONE))
async def send_phone(message: Message, user: User):
    for admin_id in ADMIN_IDS:
        await message.ctx_api.send_message(
            f"☎️ Заявка от {message.contact.first_name}\n"
            f"• Номер телефона: `{message.contact.phone_number}`",
            chat_id=admin_id,
            parse_mode=ParseMode.MARKDOWN
        )
    await bp.state_dispenser.finish(message.chat.id)

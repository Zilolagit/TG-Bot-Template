from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.states import MenuState
from db.models import User
from bot.reply_button_builder import build_reply_buttons
from bot.utils import save_user

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user = {"id": message.from_user.id,
            "username": message.from_user.username}
    await save_user(**user)
    texts = [KeyboardButton(text=_("🍜 Restaurant Menu")), KeyboardButton(text=_("📞 Call Center")),
             KeyboardButton(text=_("Language 🇺🇿/🇺🇸"))]
    size = (2,1)
    mk = await build_reply_buttons(texts, size)
    await message.answer(_("Main Menu:"), reply_markup=mk)


@main_router.message(F.text == __("📞 Call Center"))
async def call_handler(message: Message) -> None:
    await message.answer(_("You can contact with us in this number:\n📞 +998945672335"))

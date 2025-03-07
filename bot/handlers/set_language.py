from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, KeyboardButton
from aiogram.utils.i18n import lazy_gettext as __
from aiogram.utils.i18n import gettext as _
from bot.reply_button_builder import build_reply_buttons
from bot.states import MenuState
from bot.utils import save_user

language_router = Router()

@language_router.message(F.text == __("Language 🇺🇿/🇺🇸"))
async def language_handler(message : Message , state : FSMContext):
    texts = [KeyboardButton(text="Uzbek") , KeyboardButton(text="English")]
    size = (2,1)
    markup = await build_reply_buttons(texts , size)
    await state.set_state(MenuState.language)
    await message.answer(_("Choose language") , reply_markup=markup)

@language_router.message(MenuState.language)

async def set_lang_handler(message : Message , state : FSMContext , i18n):
    map = {
        "Uzbek" : "uz",
        "English" : "en",
    }
    code = map[message.text]
    await state.update_data(locale = code)
    i18n.current_locale = code
    user = {"id": message.from_user.id,
            "username": message.from_user.username}
    await save_user(**user)
    texts = [KeyboardButton(text=_("🍜 Restaurant Menu")), KeyboardButton(text=_("📞 Call Center")),
             KeyboardButton(text=_("Language 🇺🇿/🇺🇸"))]
    size = (2,1)
    mk = await build_reply_buttons(texts, size)
    await message.answer(_("Main Menu:"), reply_markup=mk)


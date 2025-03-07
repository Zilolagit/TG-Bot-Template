import types
from itertools import repeat

from aiogram import Router, F
from aiogram.types import KeyboardButton, Message
from aiogram.utils.i18n import lazy_gettext as __, gettext as _
from bot.reply_button_builder import build_reply_buttons
from db.models import Menu, Category

food_router = Router()

@food_router.message(F.text == __("🍜 Restaurant Menu"))
async def main_menu_handler(message: Message):
    texts = [KeyboardButton(text=_("🥗 Salads")), KeyboardButton(text=_("🌭 Fast Food")),
             KeyboardButton(text=_("🍵 Issiq Taomlar")), KeyboardButton(text=_("⬅️ Back")),
            ]
    size = (2,2)
    mk = await build_reply_buttons(texts, size)
    await message.answer(_("Restaurant Menu:"), reply_markup=mk)



@food_router.message(F.text == __("🥗 Salads"))
async def main_menu_handler(message: Message):
    categories = await Category.get_all()
    cat_id = None
    for i in categories:
        if i.name == 'salad':
            cat_id = i.id
    reponse = await Menu.get_all()
    menus = []
    for i in reponse:
        if i.category_id == cat_id:
            menus.append(i)
    print(cat_id)
    print(menus)
    print(categories)
    texts = [KeyboardButton(text=_(text.name)) for text in menus]
    texts.extend([KeyboardButton(text='◀️ Back')])
    sizes = (2, repeat)
    mk = await build_reply_buttons(texts, sizes)
    await message.answer(_("Salads:"), reply_markup=mk)


@food_router.message(F.text == __("🌭 Fast Food"))
async def main_menu_handler(message: Message):
    categories = await Category.get_all()
    cat_id = None
    for i in categories:
        if i.name == 'fast food':
            cat_id = i.id
    reponse = await Menu.get_all()
    menus = []
    for i in reponse:
        if i.category_id == cat_id:
            menus.append(i)
    print(cat_id)
    print(menus)
    print(categories)
    texts = [KeyboardButton(text=_(text.name)) for text in menus]
    texts.extend([KeyboardButton(text='◀️ Back')])
    sizes = (2, repeat)
    mk = await build_reply_buttons(texts, sizes)
    await message.answer(_("Fast Foods:"), reply_markup=mk)



@food_router.message(F.text == __("🍵 Issiq Taomlar"))
async def main_menu_handler(message: Message):
    categories = await Category.get_all()
    cat_id = None
    for i in categories:
        if i.name == 'hot mils':
            cat_id = i.id
    reponse = await Menu.get_all()
    menus = []
    for i in reponse:
        if i.category_id == cat_id:
            menus.append(i)
    print(cat_id)
    print(menus)
    print(categories)
    texts = [KeyboardButton(text=_(text.name)) for text in menus]
    texts.extend([KeyboardButton(text='◀️ Back')])
    sizes = (2, repeat)
    mk = await build_reply_buttons(texts, sizes)
    await message.answer(_("Hot Mils:"), reply_markup=mk)


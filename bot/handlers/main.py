from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

main_router = Router()

@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello")
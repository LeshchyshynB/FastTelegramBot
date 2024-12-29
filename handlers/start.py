from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline import get_inline_keyboard

# Handler for command /start
async def start_command(message: Message):
    await message.answer("Hello! It`s /start.", reply_markup=get_inline_keyboard())

# Handler registration
def register_start_handler(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
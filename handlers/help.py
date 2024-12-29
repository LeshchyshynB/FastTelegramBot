from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Handler for command /help
async def help_command(message: Message):
    await message.answer("Hello! It`s  /help.")

# Handler registration
def register_help_handler(dp: Dispatcher):
    dp.message.register(help_command, Command("help"))
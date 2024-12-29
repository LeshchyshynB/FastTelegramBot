from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Handler registration
def register_general_handler(dp: Dispatcher):
    dp.message.register(cool_command, Command("cool"))
    dp.message.register(foo_command, Command("foo"))
    
# Handler for command /cool
async def cool_command(message: Message):
    await message.answer("cool")

# Handler for command /foo
async def foo_command(message: Message):
    await message.answer("foo")
    
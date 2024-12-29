from aiogram import types
from aiogram.types import CallbackQuery
from aiogram import Dispatcher


# Handler registration for callbacks
def register_callback_handlers(dp: Dispatcher):
    dp.callback_query.register(process_callback)
    

# Handler for callbacks buttons
async def process_callback(callback_query: CallbackQuery):
    data = callback_query.data
    if data == "btn-1":
        await callback_query.message.answer("Button 1 pressed!")
    elif data == "btn-2":
        await callback_query.message.answer("Button 2 pressed!")

    await callback_query.answer()


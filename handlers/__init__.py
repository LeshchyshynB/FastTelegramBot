from aiogram import Dispatcher
from .start import register_start_handler
from .help import register_help_handler
from .general import register_general_handler
from .callback import register_callback_handlers


def register_handlers(dp: Dispatcher):
    register_start_handler(dp)
    register_help_handler(dp)
    register_general_handler(dp)
    register_general_handler(dp)
    register_callback_handlers(dp)

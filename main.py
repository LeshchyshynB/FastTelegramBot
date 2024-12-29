from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_handlers
import asyncio
from middlewares.message_logger import MessageLogger

async def main():
	# Init Bot and Dispatcher
	bot = Bot(token=TOKEN)
	dp = Dispatcher()

	# Handlers registration
	register_handlers(dp)
	dp.update.middleware.register(MessageLogger())

	await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
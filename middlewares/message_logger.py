from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update
from .logging.logging import Logging

class MessageLogger(BaseMiddleware):
	async def __call__(self, handler, event: Update, data):
		if event.message:
			message = event.message
			Logging.info(f"Message from {message.from_user.first_name} {message.from_user.last_name} - @{message.from_user.username} ({message.from_user.id}): {message.text}")
		elif event.callback_query:
			message = event.callback_query 
			Logging.info(f"Message from {message.from_user.first_name} {message.from_user.last_name} - @{message.from_user.username} ({message.from_user.id}): {message.data}")
		else:
			Logging.info(f"type: {type(event)}")
		# Logging.info(f"type: {type(data)}\n {data}\n")
		# Logging.info(f"type: {type(handler)}\n {handler}")
		
		return await handler(event, data)
	

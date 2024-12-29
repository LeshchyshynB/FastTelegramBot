from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_keyboard():
	button1 = InlineKeyboardButton(text="Button 1", callback_data="btn-1")  # button with callback_data
	button2 = InlineKeyboardButton(text="Button 2", callback_data="btn-2")
	button3 = InlineKeyboardButton(text="Site example", url="https://example.com")  # button for redirect to URL

	keyboard = InlineKeyboardMarkup(inline_keyboard=[
		[button1, button2],
		[button3]
	])

	return keyboard


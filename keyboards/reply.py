from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_reply_keyboard():
    # Button creating
    button1 = KeyboardButton("Button 1")
    button2 = KeyboardButton("Button 2")
    button3 = KeyboardButton("Button 3")
    
    # Create ReplyKeyboardMarkup with buttons
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # resize_keyboard=True allows to change size of keyboard
    keyboard.add(button1, button2, button3)
    
    return keyboard
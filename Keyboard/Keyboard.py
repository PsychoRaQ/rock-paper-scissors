from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Функция генерации клавиатуры (список с кнопками передается извне)
def keyboard_generator(keyboard_name,*args) -> ReplyKeyboardBuilder:
    kb_builder = ReplyKeyboardBuilder()
    buttons = [KeyboardButton(text=f'{i}') for i in keyboard_name]
    kb_builder.row(*buttons, width=2)
    return kb_builder

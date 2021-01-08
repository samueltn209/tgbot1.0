from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup,KeyboardButton

start_ = InlineKeyboardButton('Начать', callback_data='starting')
start_btn = InlineKeyboardMarkup().add(start_)

registration = InlineKeyboardButton("Регистрация", callback_data='reg')
info = InlineKeyboardButton("Подробнее", callback_data='info')
reg_btns = InlineKeyboardMarkup().row(registration, info)

read_db = InlineKeyboardButton('База данных', callback_data='read_db')
admin_btns = InlineKeyboardMarkup().add(read_db)
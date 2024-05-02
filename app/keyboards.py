from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def create_user_link_markup(user_id):
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Go to Profile", url=f"http://127.0.0.1:8000/users/{user_id}")]
    ])
    return markup

"""
dict_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='My dict',
                          url=f"http://127.0.0.1:8000/users/{user_id}"]
    ])
"""

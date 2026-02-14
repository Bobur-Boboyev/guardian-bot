from telegram import (
    Update,
    InlineKeyboardMarkup, InlineKeyboardButton,
)
from telegram.ext import CallbackContext

from ..config import constants

def start_command(update: Update, context: CallbackContext):
    bot_username = context.bot.username

    url = f"https://t.me/{bot_username}?startgroup=true"

    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Guruhga qo'shish", url=url)]
    ])

    update.message.reply_html(
        text=constants.start_msg.format(name=update.effective_user.full_name),
        reply_markup=keyboard)
        
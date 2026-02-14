from telegram import (
    Update,

)
from telegram.ext import CallbackContext
from bot.AI import detection
from bot.database import DataBase

def group_chat(update: Update, context: CallbackContext):
    if update.message and update.message.text:
        DataBase.save_message(
            chat_id=update.effective_chat.id,
            message_id=update.message.message_id,
            full_name=update.effective_user.full_name,
            text=update.message.text
        )


def chat_message(update: Update, context: CallbackContext):
    is_bawdy = detection.is_bawdy(update)
    if is_bawdy:
        update.message.reply_text("Vaqtinchalik bloklandingiz!")
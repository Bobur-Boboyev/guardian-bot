from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from .config import settings
from .filters import CustomFilters
from .handlers.command_handlers import start_command
from .handlers.message_handlers import group_chat, chat_message

def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler(command='start', callback=start_command, filters=CustomFilters.is_private)
    )
    dispatcher.add_handler(
        MessageHandler(filters=CustomFilters.is_group, callback=group_chat)
    )
    dispatcher.add_handler(
        MessageHandler(filters=CustomFilters.is_group, callback=chat_message)
    )

    updater.start_polling()
    updater.idle()

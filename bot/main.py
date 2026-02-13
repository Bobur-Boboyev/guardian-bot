from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)

from .config import settings
from .handlers.command_handlers import start_command

def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        CommandHandler('start', start_command)
    )

    updater.start_polling()
    updater.idle()

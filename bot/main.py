from telegram.ext import (
    Updater,
    CommandHandler,
)

from .config import settings
from .handlers import (
    start_command,
)


def main() -> None:
    updater = Updater(settings.BOT_TOKEN)
    dispatcher = updater.dispatcher

    # comand handlers
    dispatcher.add_handler(CommandHandler(command="start", callback=start_command))

    updater.start_polling()
    updater.idle()

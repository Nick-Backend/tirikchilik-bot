from telegram import Update
from telegram.ext import CallbackContext


def start_command(update: Update, context: CallbackContext):
    print("start command is running")

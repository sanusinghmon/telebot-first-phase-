from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


import requests
import time


messages = ['/start.']
for message in messages:
    base_url = 'https://api.telegram.org/bot5413394611:AAFE_SLHcKs4orJrL3KrKBqOzlIdwEDI0nM/sendMessage?chat_id=-1001628930827&text={} '.format(
        messages)
    string = "'messages'"
    output = eval(string)
    requests.get(base_url, output)
    time.sleep(60)




updater = Updater("5413394611:AAFE_SLHcKs4orJrL3KrKBqOzlIdwEDI0nM",
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")


def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /info - TO get info of skyverse 
    /about skyverse - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /skyverse website - To get skyverse link""")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))  # Filters out unknown commands
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
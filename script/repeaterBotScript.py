# For the Repeater Bot

import  telepot
# your bot key
bot = telepot.Bot("228412441:AAH0hKP-WOlcFGsZRaSCETVKIFBZf7C4gXc")


def handle(msg):
    chat_id = msg['chat']['id']
    chat_msg = msg['text']

    bot.sendMessage(chat_id, chat_msg)

bot.message_loop(handle)

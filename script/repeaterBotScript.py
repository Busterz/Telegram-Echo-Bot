# For the Repeater Bot

import  telepot
# your bot key
bot = telepot.Bot("[YOUR_TOKEN]")


def handle(msg):
    chat_id = msg['chat']['id']
    chat_msg = msg['text']

    bot.sendMessage(chat_id, chat_msg)

bot.message_loop(handle)

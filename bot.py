import telebot

token = '1777310948:AAHUvK9sMrJ24jWNJ3BPCucLX5l9hLh24Tc'

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()
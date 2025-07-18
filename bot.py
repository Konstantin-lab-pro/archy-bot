import telebot
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в ARCHY — маршрут поддержки и развития вашего проекта.")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.send_message(message.chat.id, "Спасибо за сообщение. Мы с вами на связи.")

bot.polling()

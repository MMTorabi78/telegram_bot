import telebot
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./bot_tel/.env")

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

bot.infinity_polling()
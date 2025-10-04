import telebot
import os
from dotenv import load_dotenv
import logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv(dotenv_path="./bot_tel/.env")

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    telebot.logger.info("triggered /start command")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="Choose an option")
    markup.add(KeyboardButton("about"), KeyboardButton("help"))
    bot.send_message(message.chat.id, 'hi this is a simple bot for a test', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "about")
def about(message):
    bot.send_message(message.chat.id, "This is a simple test bot created using the Telebot library.")

@bot.message_handler(func=lambda message: message.text == "help")
def help(message):
    bot.send_message(message.chat.id, "Available commands:\n/start - Start the bot\n/about - About the bot\n/help - Show this help message")

bot.infinity_polling()
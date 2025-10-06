import telebot
import os
from dotenv import load_dotenv
import logging
import requests
load_dotenv(dotenv_path="./bot_tel/.env")

DOWNLOAD_DIR = "/home/mtorabi/python/bot_tel/downloads/"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

API_TOKEN = os.environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Send a link → Get the file.")

def download_file(url):
    local_filename = url.split('/')[-1]
    file_path = DOWNLOAD_DIR + local_filename
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filename

@bot.message_handler(func=lambda message: True)
def download_file_url(message):
    logger.info(message.text)
    url = message.text
    try:
        file_path = download_file(url)
        bot.send_document(chat_id=message.chat.id, reply_to_message_id=message.message_id, document=open(
            file_path, "rb"), caption="file downloaded successfully, ENJOY!")
        os.remove(file_path)
    except:
        raise
        bot.reply_to(message, text="problem downloading the requested file")

bot.infinity_polling()
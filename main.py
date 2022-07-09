import telebot
import logging

TOKEN = "5309905882:AAGaktQJAxGIoKjA-VQb3baoiMZKgeu1Ywk"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


bot = telebot.TeleBot("5309905882:AAGaktQJAxGIoKjA-VQb3baoiMZKgeu1Ywk")
logger.info(dir(bot))

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
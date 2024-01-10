import telebot
from extensions import CurrencyConverter, APIException
import config

bot = telebot.TeleBot(config.TG_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_instructions(message):
    bot.send_message(message.chat.id, "Привет! Чтобы узнать цену валюты, отправьте сообщение в формате: <имя валюты, цену которой хотите узнать> <имя валюты в которой надо узнать цену первой валюты> <количество>. Доступные валюты: /values")

@bot.message_handler(commands=['values'])
def send_currency_values(message):
    bot.send_message(message.chat.id, "Доступные валюты: евро, доллар, рубль")

@bot.message_handler(content_types=['text'])
def get_currency_price(message):
    try:
        base, quote, amount = message.text.split()
        result = CurrencyConverter.get_price(config.keys[base], config.keys[quote], float(amount))
        bot.send_message(message.chat.id, f"Цена {amount} {base} в {quote}: {result}")
    except APIException as e:
        bot.send_message(message.chat.id, f"Ошибка: {e.message}")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {str(e)}")

bot.polling()

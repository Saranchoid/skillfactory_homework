import requests
import json
import config

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        headers = {
            'authorization': f'Apikey {config.CC_TOKEN}'
        }

        url = f'https://api.exchangerate-api.com/v4/latest/{base}'
        response = requests.get(url, headers=headers)
        data = response.json()

        if 'error' in data:
            raise APIException('Ошибка при получении данных о курсе валют')

        if quote not in data['rates']:
            raise APIException('Неправильно указана валюта')

        rate = data['rates'][quote]
        result = rate * amount
        return result

class APIException(Exception):
    def __init__(self, message):
        self.message = message

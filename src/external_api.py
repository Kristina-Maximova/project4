import os

import requests
import requests.exceptions
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")
url = "https://api.apilayer.com/exchangerates_data/convert"


def get_converted_amount(transaction: dict) -> float:
    """Функция, возвращающая сумму транзакции в рублях."""
    try:
        amount = transaction["operationAmount"]["amount"]  # строка с суммой транзакции
        code_of_currency = transaction["operationAmount"]["currency"]["code"]
    except KeyError:
        return float(0)

    if code_of_currency != "RUB":
        try:
            payload = {
                "amount": f"{amount}",
                "from": f"{code_of_currency}",
                "to": "RUB"
            }
            headers = {
                "apikey": f"{API_KEY}"
            }

            response = requests.get(url, headers=headers, params=payload)

            status_code = response.status_code
            if status_code == 200:
                data = response.json()  # ответ от сервера
                return round(float(data["result"]), 2)
            else:
                return float(0)

        except requests.exceptions.RequestException:
            print("Ошибка конвертации")
            return float(0)

    elif code_of_currency == "RUB":
        return round(float(amount), 2)

    else:
        return float(0)


# if __name__ == "__main__":
#     a = get_converted_amount({'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
#                               'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
#                               'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
#                               'to': 'Счет 11776614605963066702'})
#     print(a)

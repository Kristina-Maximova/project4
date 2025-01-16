from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: "str") -> Iterator:
    """Генераторная функция,  поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if transactions:
        given_currency = 0
        for transaction in transactions:
            if "operationAmount" in transaction:
                if transaction["operationAmount"]["currency"]["code"] == currency:
                    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency,
                                                   transactions)
                    given_currency += 1
                    # return filtered_transactions
            elif "currency_code" in transaction:
                if transaction["currency_code"] == currency:
                    filtered_transactions = filter(lambda x: x["currency_code"] == currency,
                                                   transactions)
                    given_currency += 1
            else:
                print("Нет транзакций с указанной валютой или неверно задана валюта")
                return iter([])
        if given_currency != 0:
            return filtered_transactions
    else:
        return iter([])


def transaction_descriptions(transactions: list[dict]) -> Iterator | str:
    """Генераторная функция, поочередно возвращает описание каждой операции"""
    # return (x["description"] for x in transactions)
    if transactions:
        n = 0
        while n < len(transactions):
            if "description" in transactions[n]:
                x = transactions[n].get("description")
                yield x
            n += 1
    return iter([])


def get_card_sample(nums: str) -> str:
    """Вспомогательная функция, приводящая строку из 16 символов к шаблону '**** **** **** ****'"""
    return f"{nums[0:4]} {nums[4:8]} {nums[8:12]} {nums[12:]}"


def card_number_generator(start: int | str, stop: int | str) -> Iterator:
    """"""
    if int(stop) >= 10000000000000000 or not isinstance(int(start), int) or not isinstance(int(stop), int) or int(
            start) > int(stop):
        raise ValueError("Неверно введен диапазон номеров")
    x = (get_card_sample((str(num)[::-1] + "0" * (16 - len(str(num))))[::-1]) for num in range(int(start), int(stop)))
    return x


if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]
    # descriptions = transaction_descriptions(transactions)
    # for _ in range(2):
    #     print(next(descriptions))

    usd_transactions = filter_by_currency(transactions, "USD")
    for _ in range(2):
        print(next(usd_transactions))

    # for card_number in card_number_generator(34567234567888, 34567234567890):
    #     print(card_number)

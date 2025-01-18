from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: "str") -> Iterator:
    """Генераторная функция,  поочередно выдает транзакции,
    где валюта операции соответствует заданной"""
    if transactions:
        given_currency = 0
        for transaction in transactions:
            if "operationAmount" in transaction:
                if transaction["operationAmount"]["currency"]["code"] == str(currency):
                    filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == str(currency),
                                                   transactions)
                    given_currency += 1
            elif "currency_code" in transaction:
                if transaction["currency_code"] == currency:
                    filtered_transactions = filter(lambda x: x["currency_code"] == str(currency),
                                                   transactions)
                    given_currency += 1
            else:
                print("Нет транзакций с указанной валютой или неверно задана валюта")
                return iter([])
        if given_currency != 0:
            return filtered_transactions
        else:
            return iter([])
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
            else:
                yield iter("")
                n += 1
    return iter("")


def get_currency_name(data: list) -> Iterator | str:
    if data:
        n = 0
        while n < len(data):
            if "currency_name" in data[n]:
                x = data[n].get("currency_name")
                yield x
                n += 1
            elif "operationAmount" in data[n] and "currency" in data[n]["operationAmount"] and "name" in \
                    data[n]["operationAmount"]["currency"]:
                x = data[n]["operationAmount"]["currency"].get("name")
                yield x
                n += 1
            else:
                yield iter("")
                n += 1
    return iter("")


def get_card_sample(nums: str) -> str:
    """Вспомогательная функция, приводящая строку из 16 символов к шаблону '**** **** **** ****'"""
    return f"{nums[0:4]} {nums[4:8]} {nums[8:12]} {nums[12:]}"


def card_number_generator(start: int | str, stop: int | str) -> Iterator:
    """Функция, генерирующая номера карт в заданном диапазоне значений"""
    if int(stop) >= 10000000000000000 or not isinstance(int(start), int) or not isinstance(int(stop), int) or int(
            start) > int(stop):
        raise ValueError("Неверно введен диапазон номеров")
    x = (get_card_sample((str(num)[::-1] + "0" * (16 - len(str(num))))[::-1]) for num in range(int(start), int(stop)))
    return x

# if __name__ == "__main__":
#
#     a = get_currency_name(tr)
#     print(next(a))

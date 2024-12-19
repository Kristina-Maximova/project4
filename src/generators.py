def filter_by_currency(transactions: list[dict], currency: "str"):
    if transactions:
        given_currency = 0
        for transaction in transactions:

            if transaction["operationAmount"]["currency"]["code"] == currency:
                given_currency += 1
        if given_currency == 0:
            raise ValueError("Нет транзакций с указанной валютой или неверно задана валюта")
        filtered_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
        return filtered_transactions
    else:
        return iter([])


def transaction_descriptions(transactions: list[dict]):
    # return (x["description"] for x in transactions)
    if transactions:
        n = 0
        while n < len(transactions):
            if "description" in transactions[n]:
                x = transactions[n].get("description")
                yield x
            n += 1
    return iter([])


def get_card_sample(nums: str):
    return f"{nums[0:4]} {nums[4:8]} {nums[8:12]} {nums[12:]}"


def card_number_generator(start: int | str, stop: int | str):
    if int(stop) >= 10000000000000000 or not isinstance(int(start), int) or not isinstance(int(stop), int) or int(
            start) > int(stop):
        raise ValueError("Неверно введен диапазон номеров")
    x = (get_card_sample((str(num)[::-1] + "0" * (16 - len(str(num))))[::-1]) for num in range(int(start), int(stop)))
    return x


# if __name__ == "__main__":
#
#     descriptions = transaction_descriptions(transactions)
#     for _ in range(5):
#         print(next(descriptions))
#
#     usd_transactions = filter_by_currency(transactions, "USD")
#     for _ in range(2):
#         print(next(usd_transactions))
#
#     for card_number in card_number_generator(34567234567888, 34567234567890):
#         print(card_number)

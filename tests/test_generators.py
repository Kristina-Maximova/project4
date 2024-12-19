import pytest
from src.generators import filter_by_currency, transaction_descriptions, get_card_sample, card_number_generator


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert (next(usd_transactions)) == {'date': '2018-06-30T02:08:58.425572',
                                        'description': 'Перевод организации',
                                        'from': 'Счет 75106830613657916952',
                                        'id': 939719570,
                                        'operationAmount': {'amount': '9824.07',
                                                            'currency': {'code': 'USD', 'name': 'USD'}},
                                        'state': 'EXECUTED',
                                        'to': 'Счет 11776614605963066702'}
    assert (next(usd_transactions)) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                                        'operationAmount': {'amount': '79114.93',
                                                            'currency': {'name': 'USD', 'code': 'USD'}},
                                        'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                                        'to': 'Счет 75651667383060284188'}


def test_filter_by_currency_invalid_currency(transactions):
    with pytest.raises(ValueError) as exc_info:
        usd_transactions = filter_by_currency(transactions, "EUR")
        for _ in range(1):
            next(usd_transactions)
        assert str(exc_info.value) == "Нет транзакций с указанной валютой или неверно задана валюта"


def test_filter_by_currency_for_empty():
    usd_transactions = filter_by_currency([], "USD")
    assert list((usd_transactions)) == []


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert (next(descriptions)) == "Перевод организации"
    assert (next(descriptions)) == "Перевод со счета на счет"


def test_transaction_descriptions_for_empty():
    descriptions = transaction_descriptions([])
    assert list(descriptions) == []


@pytest.mark.parametrize(
    "start, stop, expected",
    [("15", "17", ["0000 0000 0000 0015", "0000 0000 0000 0016"]),
     (15, 17, ["0000 0000 0000 0015", "0000 0000 0000 0016"]),
     ("34567234567888", "34567234567890", ["0034 5672 3456 7888", "0034 5672 3456 7889"])]
)
def test_card_number_generator(start, stop, expected):
    new_numbers = list(card_number_generator(start, stop))
    assert new_numbers == expected


def test_card_number_generator_invalid_start_stop():
    with pytest.raises(ValueError) as inf:
        card_number = card_number_generator(18, 1)
        for _ in range(1):
            next(card_number)
        assert str(inf.value) == "Неверно введен диапазон номеров"


def test_get_card_sample():
    assert get_card_sample("1234567890123456") == "1234 5678 9012 3456"

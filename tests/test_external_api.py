from unittest.mock import patch

from src.external_api import get_converted_amount

API_KEY = "test"


@patch("requests.get")
def test_get_converted_amount(mock_get):
    """Тест на корректную работу"""
    mock_get.return_value.json.return_value = {
        "date": "2025-01-02",
        "info": {"rate": 111.493093, "timestamp": 1735807144},
        "query": {"amount": 9824.07, "from": "USD", "to": "RUB"},
        "result": 1095315.950149,
        "success": "true",
    }
    mock_get.return_value.status_code = 200

    assert (
        get_converted_amount(
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        )
        == 1095315.95
    )
    mock_get.assert_called()


def test_get_converted_amount_from_RUB():
    """Обработка транзакции, если сумма в рублях изначально"""
    assert (
        get_converted_amount({"operationAmount": {"amount": "9824.07", "currency": {"name": "руб", "code": "RUB"}}})
        == 9824.07
    )


@patch("requests.get")
def test_get_converted_amount_wrong(mock_get):
    """Проверяем, что при ошибочном ответе от сервера функция вернет 0.0"""
    mock_get.return_value.json.return_value = ConnectionError
    mock_get.return_value.status_code = 418
    assert get_converted_amount(
        {"operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}}}
    ) == float(0)
    mock_get.assert_called()


def test_get_converted_amount_invalid_data():
    assert get_converted_amount({"Fake_content": "test"}) == float(0)

from unittest.mock import patch

import pytest

from src.main import (
    create_report,
    get_data_by_choice,
    main,
    sort_by_choice_by_description,
    sort_by_choice_currency,
    sort_by_choice_date,
    sort_by_choice_state
)


@patch("src.main.get_transactions_from_csv_file", return_value=["fake_data"])
@patch("builtins.input", side_effect=["2"])
def test_get_data_by_choice(mock_input, mock_get):
    """Тест с заданным пользовательским вводом"""
    fake_data = get_data_by_choice()
    assert fake_data == ["fake_data"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.get_transactions", return_value=["fake_data2"])
@patch("builtins.input", side_effect=["1"])
def test_get_data_by_choice_1(mock_input, mock_get):
    """Тест с заданным пользовательским вводом"""
    fake_data = get_data_by_choice()
    assert fake_data == ["fake_data2"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.get_transactions_from_excel_file", return_value=["fake_data3"])
@patch("builtins.input", side_effect=["3"])
def test_get_data_by_choice_2(mock_input, mock_get):
    """Тест с заданным пользовательским вводом"""
    fake_data = get_data_by_choice()
    assert fake_data == ["fake_data3"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.filter_by_state", return_value=["fake_data4"])
@patch("builtins.input", side_effect=["EXECUTED"])
def test_sort_by_choice_state(mock_input, mock_get):
    test_data = sort_by_choice_state(["fake_data_4"])
    assert test_data == ["fake_data4"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.sort_by_date", return_value=["fake_data5"])
@patch("builtins.input", side_effect=["да", "1"])
def test_sort_by_choice_date(mock_input, mock_get):
    test_data = sort_by_choice_date(["fake_data_5"])
    assert test_data == ["fake_data5"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.sort_by_date", return_value=["fake_data7"])
@patch("builtins.input", side_effect=["да", "2"])
def test_sort_by_choice_date_1(mock_input, mock_get):
    test_data = sort_by_choice_date(["fake_data_7"])
    assert test_data == ["fake_data7"]
    mock_input.assert_called()
    mock_get.assert_called()


@patch("src.main.filter_by_currency", return_value=iter(["fake_data6"]))
@patch("builtins.input", side_effect=["да"])
def test_sort_by_choice_currency(mock_input, mock_get):
    sort_by_choice_currency(["fake_data_6"])
    mock_input.assert_called_once()
    mock_get.assert_called_once()


@patch("src.main.sort_by_description", return_value=["fake_data7"])
@patch("builtins.input", side_effect=["да", "открытие"])
def test_sort_by_choice_by_description(mock_input, mock_get):
    data_fake_7 = sort_by_choice_by_description(["fake_data_7"])
    assert data_fake_7 == ["fake_data7"]
    mock_input.assert_called()
    mock_get.assert_called_once()


@patch("builtins.input", side_effect=["нет"])
def test_sort_by_choice_by_description_1(mock_input):
    data_fake_8 = sort_by_choice_by_description(["fake_data_8"])
    assert data_fake_8 == ["fake_data_8"]
    mock_input.assert_called_once()


@pytest.mark.parametrize(
    "data, expected",
    [
        (
            [
                {
                    "id": "4653425",
                    "state": "EXECUTED",
                    "date": "2020-03-10T07:48:21Z",
                    "amount": "22131",
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "",
                    "to": "Счет 58936710508356884628",
                    "description": "Открытие вклада",
                }
            ],
            [["10.03.2020", "Открытие вклада", "", "Счет **4628", "Cумма: 22131", "Ruble", ""]],
        ),
        (
            [
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                }
            ],
            [
                [
                    "12.09.2018",
                    "Перевод организации",
                    "Visa Platinum 1246 37** **** 3588 -> ",
                    "Счет **1657",
                    "Cумма: 67314.70",
                    "",
                    "руб.",
                ]
            ],
        ),
        (
            [
                {
                    "id": 4739714.0,
                    "state": "CANCELED",
                    "date": "2021-03-16T09:50:38Z",
                    "amount": 29700.0,
                    "currency_name": "Baht",
                    "currency_code": "THB",
                    "from": "Discover 5448680041474638",
                    "to": "Счет 81509213611289630443",
                    "description": "Перевод организации",
                }
            ],
            [
                [
                    "16.03.2021",
                    "Перевод организации",
                    "Discover 5448 68** **** 4638 -> ",
                    "Счет **0443",
                    "Cумма: 29700.0",
                    "Baht",
                    "",
                ]
            ],
        ),
    ],
)
def test_create_report(data, expected):
    assert create_report(data) == expected


@patch("src.main.create_report", return_value=["fake_seis"])
@patch("src.main.sort_by_choice_by_description", return_value=["fake_cinco"])
@patch("src.main.sort_by_choice_state", return_value=["fake_cuatro"])
@patch("src.main.sort_by_choice_date", return_value=["fake_tres"])
@patch("src.main.sort_by_choice_currency", return_value=["fake_dos"])
@patch("src.main.get_data_by_choice", return_value=["fake_uno"])
def test_main(mock_get_1, mock_get_2, mock_get_3, mock_get_4, mock_get_5, mock_get_6, capsys):
    main()
    mock_get_1.assert_called_once()
    mock_get_2.assert_called_once()
    mock_get_3.assert_called_once()
    mock_get_4.assert_called_once()
    mock_get_5.assert_called_once()
    mock_get_6.assert_called_once()
    captured = capsys.readouterr()
    assert (captured.out) == (
        "Привет!\n"
        "Добро пожаловать в программу работы c банковскими транзакциями\n"
        "Распечатываю итоговый список транзакций...\n"
        "Всего банковских операций в выборке: 1\n"
        "\n"
        "f a\n"
        "ke\n"
        "_ s\n"
        "\n"
    )

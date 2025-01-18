import pytest

from src.main import get_data_by_choice, sort_by_choice_date, sort_by_choice_state, sort_by_choice_currency, \
    sort_by_choice_by_description

from unittest.mock import patch


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
    data_test_6 = sort_by_choice_currency(["fake_data_6"])
    mock_input.assert_called_once()
    mock_input.assert_called_once()


"""Распечатываю итоговый список транзакций...
Всего банковских операций в выборке: 2

10.07.2021 Открытие вклада
Счет **5996
Cумма: 27596 Ruble

10.03.2020 Открытие вклада
Счет **4628
Cумма: 22131 Ruble
"""

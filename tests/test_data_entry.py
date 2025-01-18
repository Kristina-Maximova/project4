import csv
from unittest.mock import mock_open, patch

from src.data_entry import get_transactions_from_csv_file, get_transactions_from_excel_file


def test_get_transactions_from_csv_file():
    """Тест на корректное чтение csv-файла"""
    mock_csv_content = "id;amount;currency_code;description\n650703;16210;PEN;Перевод организации\n"
    expected_result = [
        {"id": "650703", "amount": "16210", "currency_code": "PEN", "description": "Перевод организации"}
    ]
    # можно писать with patch("builtins.open", ...)
    with patch("src.data_entry.open", mock_open(read_data=mock_csv_content), create=True):
        with patch("csv.DictReader", return_value=csv.DictReader(mock_csv_content.splitlines(), delimiter=";")):
            result = get_transactions_from_csv_file("fake_file.csv")
            assert result == expected_result
            csv.DictReader.assert_called_once()


@patch("src.data_entry.pd.read_excel", return_value="")
def test_get_transactions_from_excel_file(mock_get):
    """Тест на обработку пустого файла"""
    fake = get_transactions_from_excel_file("fake_path")
    assert fake == []
    mock_get.assert_called()


def test_get_transactions_from_csv_file_empty():
    """Чтение файла при отсутствии файла или неверном пути"""
    assert (get_transactions_from_csv_file("wrong_path")) == []


# def test_get_transactions_from_csv_file_wrong_data():
#     """Тест на чтение файла с некорректными данными"""
#     mock_wrong_csv_data = ["id;amount;currency_code;description\n650703;16210;PEN;Перевод организации\n"]
#     with patch("builtins.open", mock_open(read_data=mock_wrong_csv_data), create=True):
#         with pytest.raises(Exception) as inf:
#             assert str(inf.value) == "TypeError: initial_value must be str or None, not list"


def test_get_transactions_empty_filename():
    """проверяет, что функция возвращает пустой список, если имя файла пустое."""
    result = get_transactions_from_excel_file("")
    assert result == []


@patch("pandas.read_excel")
def test_file_not_found(mock_read_excel):
    """Тест проверяет, что функция возвращает пустой список, если файл не найден."""
    mock_read_excel.side_effect = FileNotFoundError
    result = get_transactions_from_excel_file("test_file.xlsx")
    assert result == []

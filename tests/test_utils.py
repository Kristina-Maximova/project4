import json
from unittest.mock import Mock, patch
from src.utils import get_transactions
import os.path

path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
path_for_test = os.path.join(os.path.dirname(__file__), "..", "tests", "test_utils.py")

@patch("json.load")
def test_get_transactions_with_success(mock_transactions):
    """Тест на корректную работу"""
    mock_transactions.return_value = [{"test": "1"}, {"test": "2"}]
    test_transactions = get_transactions(path_to_file)
    assert test_transactions == [{"test": "1"}, {"test": "2"}]
    mock_transactions.assert_called()


def test_get_transactions_with_invalid_path(capsys):
    """Тест при отсутствии файла для чтения или неверном пути """
    test_transactions1 = get_transactions("wrong_path")
    captured = capsys.readouterr()
    assert test_transactions1 == []
    assert (captured.out) == "Файл не найден\n"


def test_get_transactions_with_invalid_data(capsys):
    """Тест при неуспешном декодировании файла"""
    test_transactions1 = get_transactions(path_for_test)
    captured = capsys.readouterr()
    assert test_transactions1 == []
    assert (captured.out) == "Ошибка декодирования файла\n"


def test_get_transactions_with_empty_data():
    """Тест на работу функции с пустым списком"""
    mock_data = Mock(return_value=[])
    json.load = mock_data
    assert get_transactions(path_to_file) == []
    mock_data.assert_called()

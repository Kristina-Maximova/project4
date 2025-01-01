import json
from unittest.mock import patch
from src.utils import get_transactions
import os.path
path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")



@patch('json.load')
def test_get_transactions_with_success(mock_transactions):
    mock_transactions.return_value = [{"test": "1"} ,{"test": "2"}]
    test_transactions = get_transactions(path_to_file)
    assert test_transactions == [{"test": "1"} ,{"test": "2"}]
    mock_transactions.assert_called


def test_get_transactions_with_invalid_path():
    test_transactions1 = get_transactions("wrong_path")
    assert test_transactions1 == []



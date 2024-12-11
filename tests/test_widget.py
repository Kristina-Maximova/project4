import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "string_with_number, mask", [
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("", ""),
        ("Счет 73654108430135874305", "Счет **4305")
    ])
def test_mask_account_card(string_with_number: str, mask: str) -> None:
    assert mask_account_card(string_with_number) == mask


def test_mask_account_card_invalid_input() -> None:
    with pytest.raises(ValueError) as exc_info:
        mask_account_card("Строка без чисел или с меньшим/большим числом, например, *7000")
        assert str(exc_info.value) == "Неверный ввод данных"


def test_get_date(correct_string_with_date: str) -> None:
    assert get_date(correct_string_with_date) == "11.12.2024"


def test_get_date_for_empty() -> None:
    assert get_date("") == ""


def test_get_date_invalid_input() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_date("24-03-11T02:26:18.671407")
        get_date("2024.03.118.67140724-03-11")
        get_date("Строка без чисел")
        assert str(exc_info.value) == "Неверный ввод данных"

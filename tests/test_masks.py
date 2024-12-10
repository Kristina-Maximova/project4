import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number_1: str, card_mask_1: str) -> None:
    assert get_mask_card_number(card_number_1) == card_mask_1
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("7000")
        assert str(exc_info.value) == "Неверный ввод данных"


def test_get_mask_card_number_for_empty() -> None:
    assert get_mask_card_number("") == ""


def test_get_mask_account(account_number_1: str, account_mask_1: str) -> None:
    assert get_mask_account(account_number_1) == account_mask_1
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("9999 9999 0000 0022 2222")
        assert str(exc_info.value) == "Неверный ввод данных"


def test_get_mask_account_for_empty() -> None:
    assert get_mask_account("") == ""

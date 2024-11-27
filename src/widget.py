import re
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_or_account: str) -> str:
    """Функция для маскировки номеров карт и счетов"""
    pattern = r"\d{16,20}"
    match = re.search(pattern, card_or_account)
    number_start_index = match.start()
    card_or_account_number = card_or_account[match.start():]

    if len(card_or_account_number) == 20:
        mask_account = get_mask_account(card_or_account_number)
        return card_or_account[:number_start_index] + mask_account
    elif len(card_or_account_number) == 16:
        mask_card = get_mask_card_number(card_or_account_number)
        return card_or_account[:number_start_index] + mask_card
    else:
        return ""


def get_date(line_with_date: str) -> str:
    """Функция, возвращающая из строки дату в формате (ДД.ММ.ГГГГ)"""
    if line_with_date:
        return line_with_date[8:10] + "." + line_with_date[5:7] + "." + line_with_date[:4]



if __name__ == "__main__":
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))

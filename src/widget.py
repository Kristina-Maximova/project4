import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Функция для маскировки номеров карт и счетов"""
    if card_or_account:

        pattern = r"\d{16,20}"
        match = re.search(pattern, card_or_account)
        if match is None:
            raise ValueError("Неверный ввод данных")
        else:
            number_start_index = match.start()  # No error!
            card_or_account_number = card_or_account[number_start_index:]

            if len(card_or_account_number) == 20:
                mask_account = get_mask_account(card_or_account_number)
                return card_or_account[:number_start_index] + mask_account
            elif len(card_or_account_number) == 16:
                mask_card = get_mask_card_number(card_or_account_number)
                return card_or_account[:number_start_index] + mask_card
    return ""


def get_date(line_with_date: str) -> str:
    """Функция, возвращающая из строки дату в формате (ДД.ММ.ГГГГ)"""

    if line_with_date:
        date_pattern = r"^\d{4}-\d{2}-\d{2}"
        if re.search(date_pattern, line_with_date) is None:
            raise ValueError("Неверный ввод данных")

        return line_with_date[8:10] + "." + line_with_date[5:7] + "." + line_with_date[:4]
    else:
        return ""


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(get_date("2024-03-11T02:26:18.671407"))

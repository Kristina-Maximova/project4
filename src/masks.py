import re


def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """
    if card_number:
        if len(card_number) == 16:
            return (
                card_number[0:4]
                + " "
                + card_number[4:6]
                + re.sub(r"\d", r"*", card_number[6:8])
                + " "
                + re.sub(r"\d", r"*", card_number[8:12])
                + " "
                + card_number[-4:]
            )
        raise ValueError("Неверный ввод данных")
    return ""


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    """
    if account_number:
        if len(account_number) == 20:
            return "**" + account_number[-4:]
        raise ValueError("Неверный ввод данных")
    return ""

import re

card_number_given = input("Введите номер карты\n")
account_number_given = input("Введите номер счета\n")


def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """

    if len(card_number) != 16:
        return "Некорректный ввод номера карты. Введите 16 цифр без пробелов"
    else:
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


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    """
    if len(account_number) != 20:
        return "Некорректный ввод номера счета. Введите 20 цифр без пробелов"
    else:
        return "**" + account_number[-4:]

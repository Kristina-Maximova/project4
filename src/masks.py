import re


def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """

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

    return "**" + account_number[-4:]

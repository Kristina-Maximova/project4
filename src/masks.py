import re
# import logging
from src.loggers import masks_logger


def get_mask_card_number(card_number: str) -> str:
    """
    принимает на вход номер карты и возвращает ее маску
    """
    masks_logger.info(f"Маскируется номер карты: {card_number}")
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
        masks_logger.error("Неверный ввод данных")
        raise ValueError("Неверный ввод данных")
    masks_logger.warning("Нет данных")
    return ""


def get_mask_account(account_number: str) -> str:
    """
    принимает на вход номер счета и возвращает его маску
    """
    masks_logger.info(f"Маскируется номер счета: {account_number}")
    if account_number:
        if len(account_number) == 20:
            return "**" + account_number[-4:]
        raise ValueError("Неверный ввод данных")
    return ""


if __name__ == "__main__":
    card_number_ = get_mask_card_number("7700645323459855")
    account_number_ = get_mask_account("76852000871200000098")
    print(f"{card_number_}\n{account_number_}\n")

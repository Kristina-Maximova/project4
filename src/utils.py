import json
import os.path
from typing import Any

from src.loggers import utils_logger

# Создаем абсолютный путь к файлу
path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_transactions(path: str) -> list | Any:
    """Функция для чтения данных о транзакциях из json-файла"""
    utils_logger.info(f"Чтение файла {path}")
    try:
        with open(path, encoding="utf-8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)

            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                utils_logger.warning("Декодирование файла завершилось ошибкой")
                return []

    except FileNotFoundError:
        print("Файл не найден")
        utils_logger.error("Файл не найден")
        return []

    if not transactions_data or not isinstance(transactions_data, list):
        utils_logger.warning("Данные не являются списком или пустые")
        return []
    else:
        utils_logger.info("Данные из файла получены")
        return transactions_data


def unpack_dict(dict_: dict, newkey: str = "") -> dict:
    """Рекурсивная функция, распаковывающая словарь с вложенными словарями в линейный словарь,
    где ключи - последнее значение ключа перед значением"""
    new_dict = {}
    for key, value in dict_.items():
        newkey = key
        if isinstance(value, dict):
            new_dict.update(unpack_dict(value, newkey))
        else:
            new_dict[newkey] = value
    return new_dict

# if __name__ == "__main__":
#     transactions_ = get_transactions(path_to_file)
#     print(transactions_)

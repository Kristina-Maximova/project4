import json
import os.path

# Создаем абсолютный путь к файлу
path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_transactions(path: str) -> list[dict]:
    """Функция для чтения данных о транзакциях из json-файла"""
    try:
        with open(path, encoding="utf-8") as transactions_file:
            try:
                transactions_data = json.load(transactions_file)

            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
                return []

    except FileNotFoundError:
        print("Файл не найден")
        return []

    if not transactions_data or not isinstance(transactions_data, list):
        return []
    else:
        return transactions_data


if __name__ == "__main__":
    transactions_ = get_transactions(path_to_file)
    print(transactions_)

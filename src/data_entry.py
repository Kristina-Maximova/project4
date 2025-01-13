import csv
import os

from mypy.util import DecodeError

from tests.conftest import transactions

path_to_current_file = os.path.dirname(os.path.abspath(__file__))
path_to_csv_file = os.path.join(path_to_current_file, "..", "data", "transactions.csv")


def get_trensactions_from_csv_file(path_to_file: str) -> list | list[dict]:
    try:
        try:
            with open(path_to_file, encoding="utf-8") as csv_file:
                reader_csv = csv.DictReader(csv_file, delimiter=";")
                if reader_csv:
                    return [row for row in reader_csv]
                else:
                    return []
        except Exception as e:
            print(f"Ошибка при чтении csv-файла: {e}")
    except FileNotFoundError:
        print("csv-файл не найден ")
        return []


if __name__ == "__main__":
    transactions_1 = get_trensactions_from_csv_file(path_to_csv_file)
    print(transactions_1[-5:])

import csv
import os

import pandas as pd

path_to_current_file = os.path.dirname(os.path.abspath(__file__))
path_to_csv_file = os.path.join(path_to_current_file, "..", "data", "transactions.csv")
path_to_excel_file = os.path.join(path_to_current_file, "..", "data", "transactions_excel.xlsx")


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
            return []
    except FileNotFoundError:
        print("csv-файл не найден ")
        return []


def get_transactions_from_exel_file(path_to_file: str) -> list[dict] | list:
    try:
        excel_data = pd.read_excel(path_to_file)
        if not excel_data.empty:
            return list(excel_data.to_dict(orient="records"))
        else:
            return []
    except Exception as e:
        print(f"Ошибка при чтении ecxell-файла: {e}")
        return []


if __name__ == "__main__":
    # transactions_1 = get_trensactions_from_csv_file(path_to_csv_file)
    # print(transactions_1[-5:])
    transactions_2 = get_transactions_from_exel_file(path_to_excel_file)
    print(transactions_2[-5:])

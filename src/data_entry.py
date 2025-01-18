import csv
import os

import pandas as pd

path_to_current_file = os.path.dirname(os.path.abspath(__file__))
path_to_csv_file = os.path.join(path_to_current_file, "..", "data", "transactions.csv")
path_to_excel_file = os.path.join(path_to_current_file, "..", "data", "transactions_excel.xlsx")


def get_transactions_from_csv_file(path_to_file: str) -> list | list[dict]:
    """ Cчитывание данных по транзакциям из csv-файла."""
    try:
        with open(path_to_file, encoding="utf-8") as csv_file:
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            return [row for row in reader_csv]
    except Exception as e:
        print(f"Ошибка при чтении csv-файла: {e}")
        return []


def get_transactions_from_excel_file(path_to_file: str) -> list[dict] | list:
    """Считывание данных по транзакциям из excel-файла"""
    try:
        excel_data = pd.read_excel(path_to_file)
        if not excel_data.empty:
            return list(excel_data.to_dict(orient="records"))
        else:
            return []
    except Exception as e:
        print(f"Ошибка при чтении ecxell-файла: {e}")
        return []

# if __name__ == "__main__":
#      transact_csv = get_transactions_from_csv_file(path_to_csv_file)
#      transct_xlsx = get_transactions_from_excel_file(path_to_excel_file)
#      print(transact_csv[-5:])
#      print(transct_xlsx[-2:])

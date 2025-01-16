import os

from src.utils import get_transactions
from src.data_entry import get_transactions_from_csv_file, get_transactions_from_excel_file
from src.processing import filter_by_state, sort_by_date, sort_by_description
from src.generators import filter_by_currency, get_currency_name
from src.widget import get_date

path_to_current_file = os.path.dirname(os.path.abspath(__file__))
path_to_json_file = os.path.join(path_to_current_file, "..", "data", "operations.json")
path_to_csv_file = os.path.join(path_to_current_file, "..", "data", "transactions.csv")
path_to_excel_file = os.path.join(path_to_current_file, "..", "data", "transactions_excel.xlsx")


def get_data_by_choice() -> list | None:
    """Получение данных о транзакциях по выбору пользователя из JSON-файла, CSV-файла либо XLSX-файла"""
    while True:
        choice = (input("Выберите необходимый пункт меню:\n"
                        "1. Получить информацию о транзакциях из JSON-файла\n"
                        "2. Получить информацию о транзакциях из CSV-файла\n"
                        "3. Получить информацию о транзакциях из XLSX-файла)\n"))

        if choice not in ["1", "2", "3"]:
            print("Введите число 1 - 3 для выбора пункта меню")
            continue
        else:
            if choice == "1":
                print("Для обработки выбран JSON-файл.")
                data = get_transactions(path_to_json_file)
                return data
            if choice == "2":
                print("Для обработки выбран CSV-файл.")
                data = get_transactions_from_csv_file(path_to_csv_file)
                return data
            if choice == "3":
                print("Для обработки выбран XLSX-файл.")
                data = get_transactions_from_excel_file(path_to_excel_file)
                return data


def sort_by_choice_state(data: list) -> list:
    """Фильтрация транзакций по выбранному пользователем значению стратуса"""
    while True:
        choice = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                       "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")
        if choice.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {choice} недоступен")
            continue
        else:
            sorted_data_ = filter_by_state(data, state=choice.upper())
            print(f"Операции oтфильтрованы по статусу {choice.upper()}")
            return sorted_data_


def sort_by_choice_date(data: list) -> list:
    """ Фильтрация транзакций по дате по выбору пользователя"""
    while True:
        choice = input("Отсортировать операции по дате? Да/Нет\n")
        if choice.lower() not in ["да", "нет"]:
            continue
        else:
            if choice.lower() == "да":
                while True:
                    choice_1 = (input("Отсортировать:\n"
                                      "1. по убыванию\n"
                                      "2. по возрастанию\n"))
                    if choice_1 not in ["1", "2"]:
                        print("Введите 1 или 2")
                        continue
                    elif choice_1 == "1":
                        sorted_data_ = sort_by_date(data)
                        return sorted_data_
                    else:
                        sorted_data_ = sort_by_date(data, reverse=False)
                        return sorted_data_
            elif choice.lower() == "нет":
                return data


def sort_by_choice_currency(data: list) -> list:
    """ Фильтрация транзакций по валюте по выбору пользователя"""
    while True:
        choice = input("Выводить только транзакции в рублях? Да/Нет\n")
        if choice.lower() not in ["да", "нет"]:
            continue
        elif choice.lower() == "да":
            sorted_data_ = list(filter_by_currency(data, "RUB"))
            return sorted_data_
        else:
            return data


def sort_by_choice_by_description(data: list) -> list:
    """ Фильтрация по выбору пользователя по ключевому слову в описании"""
    while True:
        choice = input("Отфильтровать операции по определенному слову в описании? Да/Нет\n")
        if choice.lower() not in ["да", "нет"]:
            continue
        elif choice.lower() == "нет":
            return data
        elif choice.lower() == "да":
            keyword = input("Введите ключевое слово для фильтрации\n")
            try:
                sorted_data_ = sort_by_description(data, keyword)
                return sorted_data_
            except Exception as e:
                print(f"Ошибка при фильтрации по ключевому слову: {e}")
                return []

def create_report(data: list) -> list:
    """ Формирование вывода отчета по фильтрации операций"""
    if data:
        report = ["","",]
        for transaction in data:
            if "date" in transaction:
                report.append(get_date(transaction["date"]))
                pass




def main() -> list | str:
    """ Общая логика процесса фильтрации транзакций"""
    print("Привет!\nДобро пожаловать в программу работы c банковскими транзакциями")
    transactions_data = get_data_by_choice()

    sorted_data = sort_by_choice_by_description(
        sort_by_choice_currency(
            sort_by_choice_date(
                sort_by_choice_state(transactions_data))))
    if sorted_data:
        data_count = len(sorted_data)
        print("Распечатываю итоговый список транзакций...")

        print(f"Всего банковских операций в выборке: {data_count}")
        print(sorted_data)
    else:
        print("Не найдено ни одной транзакции, подходящей под заданные условия фильтрации")


if __name__ == "__main__":
    main()

import os

from src.utils import get_transactions, unpack_dict
from src.data_entry import get_transactions_from_csv_file, get_transactions_from_excel_file
from src.processing import filter_by_state, sort_by_date, sort_by_description
from src.generators import filter_by_currency
from src.widget import get_date, mask_account_card

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
    # defaultdict?
    if data:
        full_report = []
        # разворачиваем словари в линейные, если есть вложенные словари.
        # ! Меняются ключи, если json-файл источник транзакций
        for transaction in data:
            report = []
            simple_transaction = unpack_dict(transaction)
            # for k in simple_transaction:
            try:
                report.append(get_date(simple_transaction.get("date", "")))
                d = simple_transaction.get("description", "")
                report.append(d)
                x = (simple_transaction.get("from", ""))
                if "открытие" not in d.lower():
                    report.append(mask_account_card(x) + " -> ")
                else:
                    report.append(mask_account_card(x))
                y = simple_transaction.get("to", "")
                report.append(mask_account_card(y))
                s = simple_transaction.get("amount", "")
                report.append(f"Cумма: {s}")
                v = simple_transaction.get("currency_name", "")
                report.append(v)
                v = simple_transaction.get("name", "")
                report.append(v)
            except KeyError:
                continue
            full_report.append(report)
        return full_report
    return []


def main() -> list | str:
    """ Общая логика процесса фильтрации транзакций"""
    print("Привет!\nДобро пожаловать в программу работы c банковскими транзакциями")
    transactions_data = get_data_by_choice()

    # """ создаем объект с defaultdict на базе полученных данных,
    # чтобы избежать KeyError при отсутствии каких-то ключей в данных"""
    # transactions_data = []
    # for transaction in transactions_data_:
    #     def_dict = defaultdict(str)
    #     for key, value in transaction.items():
    #         def_dict[key] = value
    # transactions_data.append(def_dict)
    # - ! теряются значения при такой обработке

    sorted_data = sort_by_choice_by_description(
        sort_by_choice_currency(
            sort_by_choice_date(
                sort_by_choice_state(transactions_data))))
    if sorted_data:
        data_count = len(sorted_data)
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {data_count}\n")
        # print(sorted_data)
        report_ = create_report(sorted_data)
        for item in report_:
            print(item[0] + " " + item[1])
            print(item[2] + item[3])
            print(item[4] + " " + item[5] + "\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под заданные условия фильтрации")


if __name__ == "__main__":
    main()

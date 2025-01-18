import re
from collections import Counter
from src.widget import get_date


def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict] | list:
    """Функция для фильтрации списка словарей по ключу state,
    значение ключа по-умолчанию 'EXECUTED'"""
    new_list_of_dict = []
    for unit_dict in list_of_dict:
        if "state" in unit_dict:
            if unit_dict["state"] == state:
                new_list_of_dict.append(unit_dict)
    return new_list_of_dict


def sort_by_date(list_of_dict: list[dict], reverse: bool = True) -> list[dict] | list:
    """Сортирует список словарей по дате, по умолчанию по убыванию, если второй аргумент не указан как 'False'"""
    if not list_of_dict:
        return []
    else:
        for item in list_of_dict:
            if "date" not in item or item["date"] == "":
                raise ValueError("Нет данных для сортировки")

        list_of_date = sorted(list_of_dict, key=lambda x: list(map(int, get_date(x["date"]).split(".")))[::-1],
                              reverse=reverse)
        return list_of_date


def sort_by_description(list_of_dict: list[dict], keyword: str) -> list | list[dict]:
    """Cортирует список транзакций по ключевому слову в описании операции"""
    if not list_of_dict:
        return []
    else:
        # filtered_data = []
        # for transaction in list_of_dict:
        #     if re.search(keyword, transaction["description"], flags=re.IGNORECASE):
        #         filtered_data.append(transaction)
        try:
            return [transaction for transaction in list_of_dict if
                    re.search(str(keyword), transaction["description"], flags=re.IGNORECASE)]
        except Exception as e:
            print(f"Ошибка при фильтрации по ключевому слову в описании: {e}")
            return []


def count_descriptions(list_of_dict: list[dict], categories: list) -> dict:
    """Подсчет операций с определенными в списке категорий описаниями транзакций. """
    sample_of_categories = []
    try:
        for category in categories:
            for transaction in list_of_dict:
                if not transaction["description"]:
                    continue
                else:
                    if transaction["description"].lower() == category.lower():
                        sample_of_categories.append(transaction["description"].lower())
        result = dict(Counter(sample_of_categories))
        return result
    except Exception as e:
        print(f"Ошибка при подсчете операций заданных категорий {e}")
        return {}

# if __name__ == "__main__":
#      result = sort_by_description("oткрытие", ["transactions"])
#     # keyword = input("Введите слово для фильтрации: \n").lower()
#     keyword = "перевод"
#     data = [{"id": 939719570,
#              "state": "EXECUTED",
#              "date": "2018-06-30T02:08:58.425572",
#              "operationAmount": {
#                  "amount": "9824.07",
#                  "currency": {
#                      "name": "USD",
#                      "code": "USD"
#                  },]
#
#     filtered_data = sort_by_description([{"kz": 1, "fd": 2}, {"kz": 3, "jk": 4}], "организ")
#     print(filtered_data[0:1])
#     category = ["Перевод организации", "Перевод со счета на счет", "что-то еще"]
#     dict_by_categoies = count_descriptions(data, category)
#     print(dict_by_categoies)

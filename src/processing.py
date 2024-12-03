from typing import List


def filter_by_state(list_of_dict: List[dict], state='EXECUTED') ->list[dict]:
    """Функция для фильтрации списка словарей по ключу state,
    значение ключа по-умолчанию 'EXECUTED'"""
    new_list_of_dict = []
    for unit_dict in list_of_dict:
        if "state" in unit_dict:
            if unit_dict["state"] == "EXECUTED":
                new_list_of_dict.append(unit_dict)
    return new_list_of_dict


if __name__ == "__main__":
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

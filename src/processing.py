from typing import List

from src.widget import get_date


def filter_by_state(list_of_dict: List[dict], state: str ="EXECUTED") -> list[dict]:
    """Функция для фильтрации списка словарей по ключу state,
    значение ключа по-умолчанию 'EXECUTED'"""
    new_list_of_dict = []
    for unit_dict in list_of_dict:
        if "state" in unit_dict:
            if unit_dict["state"] == state:
                new_list_of_dict.append(unit_dict)
    return new_list_of_dict


def sort_by_date(list_of_dict: List[dict], reverse: bool =True) -> List[dict]:
    """Функция для сортировки списка словарей по дате"""
    list_of_date = sorted(
        list_of_dict, key=lambda x: list(map(int, get_date(x["date"]).split(".")))[::-1], reverse=reverse
    )
    return list_of_date


if __name__ == "__main__":
    print(
        filter_by_state(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            state="CANCELED",
        )
    )
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

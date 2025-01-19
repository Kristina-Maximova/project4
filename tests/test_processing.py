import pytest

from src.processing import count_descriptions, filter_by_state, sort_by_date, sort_by_description


def test_filter_by_state(
        list_of_dictionaries: list[dict],
        list_of_dictionaries_sorted_by_default_state: list[dict],
        list_of_dictionaries_sorted_by_canseled_state: list[dict],
) -> None:
    assert filter_by_state(list_of_dictionaries) == list_of_dictionaries_sorted_by_default_state
    assert filter_by_state(list_of_dictionaries, state="CANCELED") == list_of_dictionaries_sorted_by_canseled_state


def test_filter_by_state_for_invalid_state() -> None:
    assert filter_by_state([{"id": 41428829, "date": "2019-07"},
                            {"id": 939719570, "date": "2018-06"}]) == []

    assert filter_by_state([{"id": 594226727, "state": "", "date": "2018-09"},
                            {"id": 615064591, "state": "", "date": "2018-10"}]) == []


def test_sort_by_date(
        list_of_dictionaries: list[dict],
        list_of_dictionaries_sorted_by_date: list[dict],
        list_of_dictionaries_sorted_by_date_from_early: list[dict],
        list_of_dictionaries_with_same_date: list[dict],
) -> None:
    assert sort_by_date(list_of_dictionaries) == list_of_dictionaries_sorted_by_date
    assert sort_by_date(list_of_dictionaries, reverse=False) == list_of_dictionaries_sorted_by_date_from_early
    assert sort_by_date(list_of_dictionaries_with_same_date) == list_of_dictionaries_with_same_date


@pytest.mark.parametrize("my_list_of_dict, reverse, expected_value",
                         [
                             ([{"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                               {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
                               {"id": 594226727, "date": "2018-10-30T21:27:25.241689"},
                               {"id": 615064591, "date": "2018-08-30T08:21:33.419441"}],
                              True,
                              [{"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
                               {"id": 594226727, "date": "2018-10-30T21:27:25.241689"},
                               {"id": 615064591, "date": "2018-08-30T08:21:33.419441"},
                               {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}],
                              ),
                             ([], True, []),
                             ([{"id": 41428829, "date": "2020-08-30T08:21:33.419441"},
                               {"id": 939719570, "date": "2020-08-31T21:27:25.241689"},
                               {"id": 594226727, "date": "2018-10-30T21:27:25.241689"},
                               {"id": 615064591, "date": "2018-08-30T08:21:33.419441"}],
                              False,
                              [{"date": "2018-08-30T08:21:33.419441", "id": 615064591},
                               {"date": "2018-10-30T21:27:25.241689", "id": 594226727},
                               {"date": "2020-08-30T08:21:33.419441", "id": 41428829},
                               {"date": "2020-08-31T21:27:25.241689", "id": 939719570}]
                              )])
def test_sort_by_date_else(my_list_of_dict: list[dict], reverse: bool, expected_value: list[dict]) -> None:
    assert sort_by_date(my_list_of_dict, reverse) == expected_value


def test_sort_by_date_invalid_date() -> None:
    with pytest.raises(ValueError):
        sort_by_date(
            [
                {"id": 41428829, "Datetime": "2020-08-30T08:21:33.419441"},
                {"id": 939719570, "Datetime": "2020-08-31T21:27:25.241689"},
                {"id": 594226727, "Datetime": "2018-10-30T21:27:25.241689"},
                {"id": 615064591, "Datetime": "2018-08-30T08:21:33.419441"},
            ]
        )
        sort_by_date(
            [
                {"date": "", "id": 615064591},
                {"date": "", "id": 594226727},
                {"date": ".33.419441", "id": 41428829},
                {"date": "2020.08.31T21:27:25.241689", "id": 939719570},
            ]
        )


def test_sort_by_description(csv_transactions):
    """
    Тест на корректную работу и обработку пустого списка
    """
    result = sort_by_description(csv_transactions, "открытие")
    null_result = sort_by_description([], "открытие")
    assert result == [
        {
            "id": "4137938",
            "state": "EXECUTED",
            "date": "2023-01-04T13:13:34Z",
            "amount": "15560",
            "currency_name": "Real",
            "currency_code": "BRL",
            "from": "",
            "to": "Счет 38164279390569873521",
            "description": "Открытие вклада",
        }
    ]
    assert null_result == []


def test_sort_by_description_1(transactions, capsys):
    result = sort_by_description("oткрытие", transactions)
    captured = capsys.readouterr()
    assert result == []
    assert (captured.out) == (
        "Ошибка при фильтрации по ключевому слову в описании: " "string indices must be integers, not 'str'\n"
    )


def test_count_descriptions_(csv_transactions):
    category = ["Перевод организации", "Перевод со счета на счет", "что-то еще"]
    result = count_descriptions(csv_transactions, category)
    assert result == {"перевод со счета на счет": 1}

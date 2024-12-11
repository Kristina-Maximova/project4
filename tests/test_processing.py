from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(list_of_dictionaries: list[dict],
                         list_of_dictionaries_sorted_by_default_state: list[dict],
                         list_of_dictionaries_sorted_by_canseled_state: list[dict]) -> None:
    assert filter_by_state(list_of_dictionaries) == list_of_dictionaries_sorted_by_default_state
    assert filter_by_state(list_of_dictionaries, state="CANCELED") == list_of_dictionaries_sorted_by_canseled_state


def test_filter_by_state_for_invalid_state() -> None:
    assert filter_by_state([
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"}]) == []
    assert filter_by_state([
        {"id": 594226727, "state": "", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"}]) == []


def test_sort_by_date(list_of_dictionaries: list[dict],
                      list_of_dictionaries_sorted_by_date: list[dict],
                      list_of_dictionaries_sorted_by_date_from_early: list[dict],
                      list_of_dictionaries_with_same_date: list[dict]) -> None:
    assert sort_by_date(list_of_dictionaries) == list_of_dictionaries_sorted_by_date
    assert sort_by_date(list_of_dictionaries, reverse=False) == list_of_dictionaries_sorted_by_date_from_early
    assert sort_by_date(list_of_dictionaries_with_same_date) == list_of_dictionaries_with_same_date

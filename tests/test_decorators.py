import re

from src.decorators import division, log


def test_log_decorators(capsys):
    """Тест на перехват вывода в консоль при корректной работе функции"""
    division(600, 4.6)
    captured = capsys.readouterr()

    assert (
        re.sub(r"\d", r"*", str(captured.out))
        == "Function division started ****-**-** at **********.**\n"
        + "division ok\n"
        + "division running time: *.*\n"
        + "\n"
    )


def test_log_with_errors(capsys):
    """Тест на перехват вывода в консоль при ошибке в работе функции"""
    division(8, 0)
    captured = capsys.readouterr()
    # print(captured)
    assert (captured.out.split("\n"))[1] == "division error: division by zero. Inputs: (8, 0), {}"


def test_log_file_entry():
    """Тест на запись в файл при корректной работе функции"""

    @log("log1")
    def hello():
        return "Hello!"

    hello()

    with open(r"..\logs\log1.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        assert content[-4] == "hello ok\n"


def test_log_file_entry_with_error():
    """Тест на запись в файл при ошибке в работе функции"""

    @log("log2")
    def division2(a, b):
        return a / b

    division2(6, 0)
    with open(r"..\logs\log2.txt", "r", encoding="utf-8") as file:
        content = file.readlines()
        assert content[-5] == "division2 error: division by zero. Inputs: (6, 0), {}\n"

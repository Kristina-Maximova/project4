import os
from datetime import date
from functools import wraps
from time import time
from typing import Any, Callable

# import logging


def log(filename: str = "") -> Callable:
    """ Декоратор для вывода данных о работе функции."""

    def my_decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | None:
            date_ = date.today()
            start_time = time().__round__(2)
            start_info = f"Function {func.__name__} started {date_} at {start_time}"

            try:
                result = func(*args, **kwargs)
                info = f"{func.__name__} ok"

            except Exception as exc:
                info = f"{func.__name__} error: {exc}. Inputs: {args}, {kwargs}\n"
                result = None

            finally:
                end_time = time()
                if end_time > start_time:
                    running_time = round((end_time - start_time), 2)
                else:
                    running_time = 0.0  # надо  разобраться, как округлять, а то вылезает то +, то - число
                end_info = f"{func.__name__} running time: {running_time}\n"

                if filename:
                    os.makedirs("..\\logs", exist_ok=True)
                    filepath = os.path.join("..\\logs", f"{filename}.txt")

                    with open(filepath, "a", encoding="utf-8") as file:
                        file.write(f"{start_info}\n")
                        file.write(f"{info}\n")
                        file.write(f"{end_info}\n\n")

                else:
                    print(start_info)
                    print(info)
                    print(end_info)
            return result

        return wrapper

    return my_decorator


@log()
def division(a: float, b: float) -> float:
    return a / b

# if __name__ == "__main__":
#     x = division(6, 0)
#     print(x)

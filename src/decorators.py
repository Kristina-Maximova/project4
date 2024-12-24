import os
from functools import wraps
from time import time
from datetime import date


# import logging


def log(filename: str = "") -> [callable(callable(any))]:
    """ Декоратор для вывода данных о работе функции."""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            date_ = date.today()
            start_time = time()
            start_info = f"Function {func.__name__} started {date_} at {start_time}"

            try:
                result = func(*args, **kwargs)
                info = f"{func.__name__} ok"

            except Exception as exc:
                info = f"{func.__name__} error: {exc}. Inputs: {args}, {kwargs}\n"
                result = None
            # else:
            # info = f"{func.__name__} ok"
            # return result

            finally:
                end_time = time()
                running_time = end_time - start_time  # надо  разобраться, как округлять

                end_info = f"{func.__name__} running time: {running_time}\n"

                if filename:
                    os.makedirs("logs", exist_ok=True)
                    filepath = os.path.join("logs", f"{filename}.txt")

                    with open(filepath, "a", encoding="utf-8") as file:
                        file.write(start_info)
                        file.write(f"{info}\n")
                        file.write(end_info)

                else:
                    print(start_info)
                    print(info)
                    print(end_info)
            return result

        return wrapper

    return my_decorator


@log()
def division(a, b):
    return a / b


x = division(8, 4)
print(x)

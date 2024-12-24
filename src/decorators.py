from idlelib.iomenu import encoding

from encodings.utf_16 import encode
from fileinput import filename
import os
from functools import wraps


# import logging

def log(filename: str = ""):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                info = f"{func.__name__} ok"


            except Exception as exc:
                info = f"{func.__name__} error: {exc}. Inputs: {args}, {kwargs}"
                result = None
            # else:
            # info = f"{func.__name__} ok"
            # return result

            if filename:
                os.makedirs("logs", exist_ok=True)
                filepath = os.path.join("logs", f"{filename}.txt")

                with open(filepath, "a", encoding="utf-8") as file:
                    file.write(f"{info}\n")
            else:
                print(info)



            return result

        return wrapper

    return my_decorator


@log("log")
def division(a, b):
    return a / b


x = division(8, 0)
print(x)

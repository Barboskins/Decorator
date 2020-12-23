"""Написать декоратор - логгер. Он записывает в файл дату и время вызова функции,
имя функции, аргументы, с которыми вызвалась и возвращаемое значение."""

from datetime import datetime
from typing import Callable
import os

def logger(something_func):
  def file_write(*args, **kwargs):
    result = something_func(*args, **kwargs)
    with open ("data_something_func.txt","w") as file:
      file.write(f"Вызвана функция {something_func.__name__}\n "
                 f"Дата и время вызова функции {datetime.now()}\n С аргументами {args, kwargs}\n "
                 f"Получили результат {result}")
  return file_write


@logger
def multiplayer(a,b):
  return a*b

if __name__ == '__main__':
 multiplayer(10,2)

"""Написать декоратор из п.1, но с параметром – путь к логам."""

def creating_a_decorator_with_arguments(path_to_logs):
    def logger(something_func):
        def file_write(*args, **kwargs):
            result = something_func(*args, **kwargs)
            with open(path_to_logs, "w") as file:
                file.write(
                    f"Вызвана функция {something_func.__name__}\n "
                    f"Дата и время вызова функции {datetime.now()}\n С аргументами {args, kwargs}\n "
                    f"Получили результат {result}")
            return something_func(*args, **kwargs)

        return file_write

    return logger


file_path = os.path.join(os.getcwd(), "data_something_func_2.txt")


@creating_a_decorator_with_arguments(file_path)
def multiplayer(a, b, c, d):
    return a * b * c * d
if __name__ == '__main__':
 multiplayer(10,2,40,8)

"""Применить написанный логгер к приложению из любого предыдущего д/з. См. old_work.py"""







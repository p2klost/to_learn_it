# Создайте декоратор ignore_duplicates, который не позволяет 
# выполнить функцию два раза подряд с одинаковыми 
# аргументами. 
# Пример: 
# @ignore_duplicates 
# def send_message(text): 
#     print(f"Отправлено: {text}") 
# Вызовы 
# send_message("Привет") 
# send_message("Привет") 
# send_message("Как дела?") 
# send_message("Как дела?") 
# send_message("Привет") 
# должны вывести 
# Отправлено: Привет 
# Повторный вызов проигнорирован. 
# Отправлено: Как дела? 
# Повторный вызов проигнорирован. 
# Отправлено: Привет 

from typing import Callable, Any
from functools import wraps

def ignore_duplicates(func: Callable) -> Callable:
    argument = []
    
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Callable | str:
        nonlocal argument

        if argument == [args,kwargs]:
            argument = []
            print("Повторный вызов проигнорирован.")
        else:
            argument = [args,kwargs]
            return func(*args,**kwargs)
    return wrapper


@ignore_duplicates 
def send_message(text): 
    print(f"Отправлено: {text}") 

# Вызовы 
send_message("Привет") 
send_message("Привет") 
send_message("Как дела?") 
send_message("Как дела?") 
send_message("Привет") 
# должны вывести 
# Отправлено: Привет 
# Повторный вызов проигнорирован. 
# Отправлено: Как дела? 
# Повторный вызов проигнорирован. 
# Отправлено: Привет 
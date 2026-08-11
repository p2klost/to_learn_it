# Напишите декоратор limit_calls, который ограничивает 
# количество вызовов функции. 
# Декоратор принимает три параметра: 
# ●  limit — максимальное количество вызовов; 
# ●  message — сообщение, которое выводится после 
# достижения лимита; 
# ●  default — значение, которое возвращается вместо 
# результата функции после достижения лимита. 
# Пример: 
# @limit_calls( 
#     limit=3, 
#     message="Лимит вызовов исчерпан!", 
#     default=None 
# ) 
# def get_data(name, age): 
#     print(f"Получаем данные: {name}, {age}") 
#     return f"{name}: {age}" 
 
# print(get_data("Иван", 20)) 
# print(get_data("Анна", 25)) 
# print(get_data("Петр", 30)) 
# print(get_data("Мария", 22)) 
 
# Первые три вызова должны выполнить функцию. 
# Четвёртый и последующие вызовы должны вывести: 
# Лимит вызовов исчерпан! 
 
# и вернуть: 
# None 
 
# При этом декоратор должен сохранять количество вызовов 
# отдельно для каждой декорированной функции. 
# Например: 
# @limit_calls(2, "Лимит!", 0) 
# def add(a, b): 
#     return a + b 
 
 
# @limit_calls(3, "Больше нельзя!", []) 
# def get_items(category): 
#     return ["item1", "item2"] 
 
# У add и get_items должны быть независимые счётчики. 
# Дополнительное условие: декорируемая функция может 
# принимать любое количество *args и **kwargs.

from typing import Callable, Any
from functools import wraps

def limit_calls(limit: int, message: str, default: Any) -> Callable:
    def dec_func(func: Callable) -> Callable:
        funcname = func.__name__
        func_limits = dict()
        func_limits[f"{funcname}_calls"] = 0

        @wraps(func)
        def wrapper(*args: Any,**kwargs: Any) -> str | Any:
            
            if func_limits[f"{funcname}_calls"] != limit:
                func_limits[f"{funcname}_calls"] += 1
                return func(*args,**kwargs)
            else: 
                func_limits[f"{funcname}_calls"] += 1 # чтобы считало все вызовы, даже после превышения лимита
                print(message)
                return default
        return wrapper
    
    return dec_func


@limit_calls( 
    limit=3, 
    message="Лимит вызовов исчерпан!", 
    default=None 
) 
def get_data(name, age): 
    print(f"Получаем данные: {name}, {age}") 
    return f"{name}: {age}" 
 
print(get_data("Иван", 20)) 
print(get_data("Анна", 25)) 
print(get_data("Петр", 30)) 
print(get_data("Мария", 22)) 

@limit_calls(2, "Лимит!", 0) 
def add(a, b): 
    return a + b 

print(add(5,2))
print(add(3,6))
print(add(2,2))
 
@limit_calls(3, "Больше нельзя!", []) 
def get_items(category): 
    return [category[0], category[1]] # поменял, чтобы возвращало значения из списка, а не просто строки "item1", "item2" как написано в условии задания (но наверное так и подразумевалось, что там будут значения листа)

print(get_items(["power",2]))
print(get_items(["level",6]))
print(get_items(["number",2]))
print(get_items(["money",8]))

# print(get_data.__closure__[2].cell_contents) # func_limits
# print(add.__closure__[2].cell_contents) # func_limits
# print(get_items.__closure__[2].cell_contents) # func_limits
# каждый вызов функции с декоратором создает новый словарь c кол-вом вызовов (для каждой функции отдельно)
# если под словом "отдельно" подразумевалось делать общий (словарь), но на каждую функцию отдельно, то я вижу один выход - выводить словарь func_limits за декоратор и передавать туда ключ (функция): значение (кол-во вызовов)

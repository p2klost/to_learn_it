# Напишите декоратор repeat, который позволяет 
# автоматически повторять вызов функции несколько раз. 
 
# Декоратор принимает два параметра: 
 
#     times — количество повторений; 
#     separator — строка, которая выводится между 
# результатами. 
 
# Пример: 
 
# @repeat(times=3, separator="---") 
# def greet(name): 
#     return f"Привет, {name}!" 
 
# print(greet("Иван")) 
 
# Ожидаемый результат: 
 
# Привет, Иван! 
# --- 
# Привет, Иван! 
# --- 
# Привет, Иван! 
 
# При этом декоратор должен корректно работать с 
# функциями, которые принимают несколько параметров: 
 
# @repeat(times=2, separator="=") 
# def add(a, b): 
#     return a + b 
 
# print(add(5, 3)) 
 
# Результат: 
 
# 8 
# = 
# 8 
 
# Условия: 
# ●  Использовать декоратор с параметрами. 
# ●  Использовать *args и **kwargs. 
# ●  Не изменять код декорируемой функции. 
# ●   Сохранить результаты всех выполнений функции и 
# объединить их в одну строку, используя separator в 
# качестве разделителя. Декоратор должен вернуть 
# полученную объединённую строку. 

from typing import Callable, Any
from functools import wraps

def repeat(times: int, separator: str) -> Callable:

    def dec_func(func: Callable) -> Callable:

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            func_result = []
            for i in range(times,0,-1):
                if i > 0:
                    func_result.append(f"{func(*args,**kwargs)}")
            return f"\n{separator}\n".join(func_result)
        return wrapper
    return dec_func

@repeat(times=3, separator="---") 
def greet(name): 
    return f"Привет, {name}!" 
 
print(greet("Иван"))

# Ожидаемый результат: 
 
# Привет, Иван! 
# --- 
# Привет, Иван! 
# --- 
# Привет, Иван! 

@repeat(times=2, separator="=") 
def add(a, b): 
    return a + b 

print(add(5, 3))

# Результат: 
 
# 8 
# = 
# 8 



 
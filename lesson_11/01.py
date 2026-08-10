# Напишите функцию power_factory(power), которая 
# возвращает новую функцию. 
# Возвращаемая функция должна принимать число x и 
# возводить его в степень power, которая была передана при 
# создании замыкания. 
# Пример работы: 
# square = power_factory(2) 
# cube = power_factory(3) 
 
# print(square(5))  # 25 
# print(cube(2))    # 8 
# print(square(10)) # 100 
# Требования: 
# ●  Использовать замыкание. 
# ●  Переменная power должна быть захвачена внутренней 
# функцией. 
# ●  Не использовать глобальные переменные.

from typing import Callable

def power_factory(power: int | float) -> Callable:

    def pow_func(x: float | int) -> float | int:
        return x ** power

    return pow_func

square = power_factory(2) 
# print(square.__closure__[0].cell_contents) # переменная power захвачена фнутренней функцией, результат 2
cube = power_factory(3) 
# print(cube.__closure__[0].cell_contents) # переменная power захвачена фнутренней функцией, результат 3

print(square(5))  # 25 
print(cube(2))    # 8 
print(square(10)) # 100 
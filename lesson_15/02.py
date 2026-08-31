"""
Создайте класс Car, описывающий автомобиль.Реализуйте 
приватные атрибуты для марки (__make), модели (__model) и 
пробега (__mileage). Добавьте геттер и сеттер для пробега.  В сеттере проверьте условие: пробег не может быть 
отрицательным числом, а также не может уменьшаться 
(новый пробег должен быть больше или равен старому). 
"""

class Car:

    def __init__(self, make: str, model: str, mileage: float | int) -> None:
        self.__make = make
        self.__model = model
        self.__mileage = mileage

    @property
    def about(self) -> float | int:
        return print(f"Марка вашего автомобиля - {self.__make}, модель - {self.__model}. Пробег машины составляет {self.__mileage} км.")
    
    @property
    def mileage(self) -> float | int:
        return self.__mileage

    @mileage.setter
    def mileage(self, value: float | int) -> None:
        if 0 > value:
            raise ValueError("Пробег не может быть отрицательным.")
        elif not value >= self.__mileage:
            raise ValueError("Пробег не может уменьшаться.")
        else:
            self.__mileage = value

my_car = Car("Nisan", "2123", 300)
print(my_car.mileage)

my_car.mileage = 300
print(my_car.mileage)

my_car.mileage = 320
print(my_car.mileage)

print(my_car.about) # получить информацию об автомобиле

my_car.mileage = 280
print(my_car.mileage)

my_car.mileage = -20
print(my_car.mileage)
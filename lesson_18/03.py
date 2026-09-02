"""
Есть интернет-магазин. 
Сейчас существуют три вида скидки: 
●  обычная — 5%; 
●  постоянный клиент — 10%; 
●  VIP — 20%. 
Нужно реализовать расчёт скидки. 
Главное условие 
Код расчёта заказа не должен содержать конструкцию: 
if discount_type == ... 
для каждого нового типа скидки. 
Добавьте возможность легко создать новую стратегию 
скидки. 
Усложнение 
Добавьте: 
●  скидку на день рождения; 
●  скидку по промокоду. 
При этом существующий код расчёта заказа менять не 
должен.
"""

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price: int | float) -> int | float:
        pass

class DefaultDiscount(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.05

class UsualClientDiscount(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.1

class VIPDiscount(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.2

class BirthdayDiscount(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.25

class PromoDiscount(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.15

class Order:

    def __init__(self,price: int | float,discount_type: type[Discount]) -> None:
        self.price = price
        self.discount_type = discount_type

    @property
    def discount_price(self) -> int | float:
        return f"{self.price - self.discount_type.calculate(self.price):.2f}"

get1 = Order(250,DefaultDiscount())
get2 = Order(250,UsualClientDiscount())
get3 = Order(250,VIPDiscount())
get4 = Order(250,BirthdayDiscount())
get5 = Order(250,PromoDiscount())

print(get1.discount_price)
print(get2.discount_price)
print(get3.discount_price)
print(get4.discount_price)
print(get5.discount_price)
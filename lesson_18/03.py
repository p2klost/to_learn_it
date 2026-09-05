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

class DefaultDiscountStrategy(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.05

class UsualClientDiscountStrategy(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.1

class VIPDiscountStrategy(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.2

class BirthdayDiscountStrategy(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.25

class PromoDiscountStrategy(Discount):
    def calculate(self, price: int | float) -> int | float:
        return price * 0.15

class Order:

    def __init__(self,price: int | float,discount_type: type[Discount]) -> None:
        self.price = price
        self.discount_type = discount_type

    @property
    def discount_price(self) -> float:
        return round(self.price - self.discount_type.calculate(self.price),2)

get1 = Order(250,DefaultDiscountStrategy())
get2 = Order(250,UsualClientDiscountStrategy())
get3 = Order(250,VIPDiscountStrategy())
get4 = Order(250,BirthdayDiscountStrategy())
get5 = Order(250,PromoDiscountStrategy())

print(get1.discount_price)
print(get2.discount_price)
print(get3.discount_price)
print(get4.discount_price)
print(get5.discount_price)
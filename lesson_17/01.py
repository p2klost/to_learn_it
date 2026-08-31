"""
Базовый класс Order. У заказа должны быть: 
●  номер; 
●  сумма; 
●  статус. 
Реализуйте методы: 
●  pay() 
●  cancel() 
Заказ нельзя отменить после оплаты. Если пользователь 
пытается выполнить недопустимую операцию, должно 
возникать собственное исключение: InvalidOrderStateError. 
Создайте иерархию: 
 
OrderError
    └── InvalidOrderStateError 
●  Добавьте __str__:  Объект заказа должен красиво 
отображаться: Заказ #1001: 250 EUR, статус: оплачено 
●  Добавьте __eq__:Два заказа считаются одинаковыми, 
если у них одинаковый номер.
"""

class OrderError(Exception):
    pass


class InvalidOrderStateError(OrderError):
    pass


class Order:

    def __init__(self, number: int, summ: float | int, status: str) -> None:
        self.number = number
        self.summ = summ
        self.status = status

    def pay(self) -> None:
        if self.status == "не оплачено":
            self.status = "оплачено"
            print("Заказ оплачен.")
        elif self.status == "отменен":
            print("Заказ был отменен.")
        else:
            print("Заказ уже оплачен.")

    def cancel(self) -> None:
        if self.status == "оплачено":
            raise InvalidOrderStateError("Заказ нельзя отменить после оплаты.")
        elif self.status == "отменен":
            print("Заказ уже отменен.")
        else:
            self.status = "отменен"
            print("Заказ отменен.")

    def __str__(self) -> str:
        return f"Заказ #{self.number}: {self.summ} EUR, статус: {self.status}."

    def __eq__(self,other) -> None:
        return self.number == other.number


num1 = Order(32,250,"не оплачено")
num2 = Order(32,150,"не оплачено")

# num1.cancel()
# num1.pay()
# num1.cancel()
# print(num1)
# print(num1 == num2)
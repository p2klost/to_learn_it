"""
Создайте класс BankAccount, который представляет 
банковский счёт. У объекта должны быть: 
owner — имя владельца; _balance — текущий баланс. 
Реализуйте методы: 
●  deposit(amount) — пополнение счёта; 
●  withdraw(amount) — снятие денег; 
●  get_balance() — получение текущего баланса. 
 
Правила: 
●  нельзя пополнить счёт на отрицательную или нулевую 
сумму; 
●  нельзя снять отрицательную или нулевую сумму; 
●  нельзя снять больше денег, чем есть на счёте. 
 
Замените get_balance() на property, чтобы баланс можно 
было получать так: 
"""

class BankAccount:

    def __init__(self, owner: str, balance: int | float) -> None:
        self.owner = owner
        self._balance = balance

    def deposit(self,amount: int | float) -> int | float:
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Сумма пополнения счёта должна быть болше нуля.")

    def withdraw(self,amount: int | float) -> int | float:
        if amount > self._balance:
            raise ValueError("Сумма снятия больше остатка по текущему счету.")
        
        if amount > 0:
            self._balance -= amount
        else:
            raise ValueError("Сумма снятия со счёта должна быть болше нуля.")

    @property
    def get_balance(self) -> int | float:
        return self._balance


user1 = BankAccount("Pavel", 300)

# print(user1.get_balance)
# user1.deposit(10)
# user1.deposit(0)
# user1.deposit(-20)
# print(user1.get_balance)

# user1.withdraw(20)
# user1.withdraw(0)
# user1.withdraw(-20)
# user1.withdraw(320)
# print(user1.get_balance)
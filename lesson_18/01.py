"""
Создайте класс History, который хранит список действий 
пользователя: history = History([ "login", "open_profile", 
"edit_profile", "logout" ]) 
Сделайте объект History итерируемым. При переборе 
действия должны возвращаться по одному. 
 
for action in history: 
    print(action) 
 
Усложнение: Добавьте возможность создавать несколько 
независимых итераций: 
 
for action in history: 
    ... 
 
for action in history: 
    ... 
 
Обе итерации должны начинаться с первого элемента. 
"""
from typing import Iterator

class HistoryIter:

    def __init__(self,actions: list) -> None:
        self.actions = actions
        self.index = 0

    def __iter__(self) -> Iterator:
        return self
    
    def __next__(self) -> str:
        if self.index == len(self.actions):
             raise StopIteration

        action = self.actions[self.index]
        self.index += 1
        return action

class History:

    def __init__(self,actions: list) -> None:
        self.actions = actions

    def __iter__(self) -> Iterator:
        return HistoryIter(self.actions)

history = History([ "login", "open_profile", "edit_profile", "logout" ]) 

for action in history: 
    print(action) 

for action in history: 
    print(action) 
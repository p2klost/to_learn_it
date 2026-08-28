"""
Создайте класс Item, представляющий предмет в инвентаре 
персонажа. 
Каждый предмет имеет: 
●  name — название; 
●  weight — вес; 
●  price — стоимость. 
Необходимо перегрузить операторы: 
●  + — объединяет два предмета в «набор» и возвращает 
их общую стоимость; 
●  < — сравнивает предметы по весу; 
●  == — считает предметы одинаковыми, если совпадают 
их названия; 
●  str() — выводит предмет в удобном формате. 
 
Дополнительное усложнение(необязательно) 
Добавьте класс Inventory и перегрузите оператор +, чтобы 
можно было написать: 
inventory + sword 
и получить новый инвентарь, содержащий исходные 
предметы и меч.
"""

class Inventory:

    def __init__(self,items: list) -> None:
        self.items = items

    def __add__(self, other):
        return self.items.append(other)
    
    def __str__(self) -> str:
        str_items = list()
        for i in self.items:
            str_items.append(i.name)
        return f"Ваш инвентарь: {', '.join(str_items)}."
    
class Item:

    def __init__(self,name,weight,price) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __add__(self, other) -> None:
        print(f"Ваш набор состоит из: {self.name}, {other.name}.")
        return self.price + other.price

    def __lt__(self, other) -> None:
        return self.weight < other.weight

    def __eq__(self, other) -> None:
        return self.name == other.name

    def __str__(self) -> str:
        return f"Предмет {self.name} весит {self.weight} кг и его цена составляет {self.price} рублей."


sword = Item("sword", 3, 10)

wand = Item("wand", 1, 20)

shield = Item("shield", 6, 15)

inventory = Inventory([shield,wand])

# print(inventory)
# inventory + sword 
# print(inventory)

# print(sword + wand)
# print(sword < wand)
# print(sword == sword)
# print(sword == shield)
# print(sword)
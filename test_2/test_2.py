

class Warrior:

    def __init__(self, health: int, attack: int) -> None:
        self._health = health
        self.attack = attack

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self,new_health: int) -> None:
        if new_health <= 0:
            raise ValueError("Здоровье не может быть отрицательным.")
        else:
            self._health = new_health

    def take_damage(self,damage: int) -> int:
        if damage >= self._health:
            raise ValueError("Здоровье не может быть меньше или равно нулю.")
        else:
            self._health -= damage

    def attack_target(self,target) -> int:
        return target.take_damage(self.attack)

    def is_alive(self) -> bool:
        return True if self._health > 0 else False

    def __str__(self) -> None:
        return f"{self.__class__.__name__}, HP: {self._health}, ATK: {self.attack}"


    def __add__(self, par: int):
        return self.__class__(self._health+par,self.attack+par)

    def __mul__(self, par: int):
        return self.__class__(self._health*par,self.attack*par)

class Fighter(Warrior):
        
    def __init__(self, health: int, attack: int = 7) -> None:
        super().__init__(health, attack)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self,new_health: int) -> None:
        if new_health <= 0:
            raise ValueError("Здоровье не может быть отрицательным.")
        else:
            self._health = new_health

    def take_damage(self,damage: int) -> int:
        super().take_damage(damage)

    def attack_target(self,target) -> int:
        super().attack_target(target)

    def is_alive(self) -> bool:
        super().is_alive()

    def __str__(self) -> None:
        return super().__str__()
    
    def __add__(self, par: int):
        return super().__add__(par)

    def __mul__(self, par: int):
        return super().__mul__(par)

class Mage(Warrior):

    def __init__(self, health: int, attack: int, magic: int = 6) -> None:
        super().__init__(health, attack)
        self.magic = magic

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self,new_health: int) -> None:
        if new_health <= 0:
            raise ValueError("Здоровье не может быть отрицательным.")
        else:
            self._health = new_health

    def take_damage(self,damage: int) -> int:
        if damage-self.magic >= self._health:
            raise ValueError("Здоровье не может быть меньше или равно нулю.")
        else:
            self._health -= damage

    def attack_target(self,target) -> int:
        if target.attack < self.magic:
            return target.take_damage(self.attack+self.magic)
        else: 
            return super().attack_target(target)
        
    def is_alive(self) -> bool:
        super().is_alive()

    def __str__(self) -> None:
        return f"{self.__class__.__name__}, HP: {self._health}, ATK: {self.attack}, MAG: {self.magic}"
    
    def __add__(self, par: int):
        return super().__add__(par)

    def __mul__(self, par: int):
        return super().__mul__(par)
    
class Paladin(Warrior):
        
    def __init__(self, health: int = 50, attack: int = 6) -> None:
        super().__init__(health, attack)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self,new_health: int) -> None:
        if new_health <= 0:
            raise ValueError("Здоровье не может быть отрицательным.")
        else:
            self._health = new_health

    def take_damage(self,damage: int) -> int:
        super().take_damage(damage)

    def attack_target(self,target) -> int:
        hp_before = target._health
        super().attack_target(target)
        if hp_before > target._health and self.attack*0.2+self._health < 50:
            self._health = self.attack*0.2+self._health

    def is_alive(self) -> bool:
        super().is_alive()

    def __str__(self) -> None:
        return super().__str__()
    
    def __add__(self, par: int):
        return super().__add__(par)

    def __mul__(self, par: int):
        return super().__mul__(par)

class Army:

    def __init__(self,clist: list) -> None:
        self.list = clist
        self.index = 0

    def add_members(self, unit_class, count) -> list:
        for i in range(count):
            self.list.append(unit_class)

    def __iter__(self) -> None:
        return self

    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        member = self.list[self.index]
        self.index += 1
        return member

    def __len__(self) -> int:
        return len(self.list)

    def __getitem__(self,ind) -> int:
        return self.list[ind]

    def __add__(self, par: int):
        for i in self.list:
            i.health = i.health+par
            i.attack += par

    def __mul__(self, par: int):
        for i in self.list:
            i.health = i.health*par
            i.attack *= par
    
def fight(unit1, unit2) -> bool:
    while True:
        try:
            unit1.attack_target(unit2)
        except ValueError:
            return True
        
        try:
            unit2.attack_target(unit1)
        except ValueError:
            return False

w1 = Warrior(50,10)
f1 = Fighter(20)
m1 = Mage(21,5)

# f1.health = 70
# a1 = Army([])
# a1.add_members(Fighter, 3) 
# a1.add_members(Mage, 2) 
# a1.add_members(Paladin, 1)

# print(a1.list)

a1 = Army([])
a1.add_members(Fighter(20), 1) 
a1.add_members(Mage(30,6), 1) 
a1.add_members(Paladin(), 1)

for warrior in a1: 
    print(warrior) 
print(len(a1)) 
print(a1[0])
print(a1[1:3])

print(print(a1.list[0]))
stronger_army = a1 + 5
print(print(a1.list[0]))
stronger_army2 = a1 * 2
print(a1.list)
print(print(a1.list[0]))
# print(f1)
# print(m1)
# fight1 = fight(f1, m1)

# print(f1 *2)
# print(f1)
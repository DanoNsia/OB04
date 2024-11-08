from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец стреляет из лука."

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon
        print(f"{self.name} выбирает {self.weapon.__class__.__name__.lower()}.")

    def attack(self):
        if self.weapon:
            print(self.weapon.attack())
        else:
            print("У бойца нет оружия.")

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

# Шаг 4: Реализация боя
def fight(fighter: Fighter, monster: Monster):
    fighter.attack()
    print(f"{monster.name} побежден!\n")

# Демонстрация
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч и атакует
sword = Sword()
fighter.change_weapon(sword)
fight(fighter, monster)

# Боец выбирает лук и атакует
bow = Bow()
fighter.change_weapon(bow)
fight(fighter, monster)
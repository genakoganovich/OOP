from random import randint
class Person:
    count = 0
    def __init__(self, c):
        self.id = Person.count
        Person.count += 1
        self.command = c
class Hero(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.level = 1

    def up_level(self):
        self.level += 1

class Soldier(Person):
    def __init__(self, c):
        Person.__init__(self, c)
        self.my_hero = None

    def follow(self, hero):
        self.my_hero = hero.id

h1 = Hero(1)  # первый герой
h2 = Hero(2)  # второй герой
army1 = []  # первая армия
army2 = []  # вторая армия
for i in range(20):
    n = randint(1, 2)
    if n == 1:
        army1.append(Soldier(n))  # добавление солдата в первую армию
    else:
        army2.append(Soldier(n))  # добавление солдата во вторую армию

print(len(army1), len(army2))  # численность армий
if len(army1) > len(army2):  # повышение уровня героя для команды с большей численностью
    h1.up_level()
elif len(army1) < len(army2):
        h2.up_level()

army1[0].follow(h1)  # первому солдату следовать за 1 героем
print(army1[0].id, h1.id)  # номера первого солдата и первого героя
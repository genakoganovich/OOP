from random import randint
class Soldier: # класс описывающий одного солдата
    def __init__(self,name='Noname',health = 100): # конструктор
        self.name = name # задаем имя воина
        self.health = health # задаем начальное здоровье

    def set_name(self, name):
        self.name = name # есть возможность поменять имя

    def make_kick(self, enemy): # метод моделирующий атаку на солдата enemy
        enemy.health -= 20 # при атаке здоровье врага уменьшаем на 20
        if enemy.health<0 :
            enemy.health = 0
        self.health += 10 # а собственное здоровье увеличиваем на 10
        print(self.name, "бьет", enemy.name) # выводим кто кого бьет
        print('%s = %d' % (enemy.name, enemy.health)) # выводим состояние врага
#-----------------------------------------------------------------------------
class Battle:
    def __init__(self,u1,u2): # конструктор
    # композиция: класс включает двух солдат u1 и u2
        self.u1 = u1
        self.u2 = u2
        self.result = "Сражения не было" # строка для хранения состояния сражения

    def battle(self): # метод моделирующий сражение
        while self.u1.health > 0 and self.u2.health > 0:
            n = randint(1, 2) # определяем, кто атакует
            if n == 1:
                self.u1.make_kick(self.u2) # если атакует первый
            else:
                self.u2.make_kick(self.u1) # если атакует второй
        if self.u1.health > self.u2.health:# определяем, кто победил
            self.result = self.u1.name + " ПОБЕДИЛ"
        elif self.u2.health > self.u1.health:
            self.result = self.u2.name + " ПОБЕДИЛ"

    def who_win(self):  # вывод результата
        print(self.result)
 # -----------------------------------------------------------------------------
first = Soldier('Mr. First', 140)  # созаем 1 солдата с именем Mr. First и здоровьем 140
second = Soldier()  # созаем 2 солдата с паметрами по умолчанию
second.set_name('Mr. Second')  # меняем имя 2 солдата
b = Battle(first, second)  # создаем объект Battle
b.battle()  # запускаем сражение
b.who_win()  # выводим итог

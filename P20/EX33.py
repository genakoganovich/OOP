class Equipment:
    def __init__(self, name, make, year):
        self.name = name # производитель
        self.make = make # модель
        self.year = year # год выпуска
    def action(self):
        return 'Не определено'
    def __str__(self):
        return f'{self.name} {self.make} {self.year}'
#------------------------------------------------
class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series # серия
    def __str__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'
    def action(self):
        return 'Печатает'
#------------------------------------------------
class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return 'Сканирует'
#------------------------------------------------
class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)
    def action(self):
        return 'Копирует'
#------------------------------------------------
sklad = []
# создаем объект сканер и добавляем
scaner = Scaner('Mustek','BearPow 1200CU', 2010)
sklad.append(scaner)
# создаем объект ксерокс и добавляем
xerox = Xerox('Xerox','Phaser 3120', 2019)
sklad.append(xerox)
# создаем объект принтер и добавляем
printer = Printer("1200",'hp', 'Laser Jet', 2018)
sklad.append(printer)
# выводим склад
print("На складе имеются:")
for x in sklad:
    print(x,end=' ')
    print(x.action())
# забираем со склада все принтеры
for x in sklad:
    if isinstance(x,Printer):
        sklad.remove(x)
# выводим склад
print("\nНа складе осталось:")
for x in sklad:
    print(x,end=' ')
    print(x.action())

class MyClass:
    def __init__(self, valuel, value2): # Конструктор
        self.x = valuel
        self.у = value2

c = MyClass(100, 300) # Создаем экземпляр класса
print(c.x, c.у) # Вывод: 100 300
class MyClass:
    def __init__(self, у):
        self.x = у

    def __add__(self, y):
        print("Экземпляр слева")
        return self.x + y

    def __radd__(self, y):
        print("Экземпляр справа")
        return self.x + y

    def __iadd__(self, y):
        print("Сложение с присваиванием")
        self.x += y
        return self


c = MyClass(50)
print(c + 10)  # Вывод: Экземпляр слева 60
print(20 + c)  # Вывод: Экземпляр справа 70
c += 30  # Вывод: Сложение с присваиванием
print(c.x)  # Вывод: 80

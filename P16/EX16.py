class MyClass:
    def __init__(self, x):
        self.__x = x
        self.y = x ** 2


a = MyClass(2)
print(a.y)  # вывод 4
print(a._MyClass__x) # вывод: 2
print(a.__x)  # ошибка, объект не имеет атрибута __x
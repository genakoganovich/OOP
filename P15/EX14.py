class Class1:
    def __init__(self, val):
        self.x = val

    def func(self):  # Абстрактный метод
    # Возбуждаем исключение
        raise NotImplementedError("Нельзя вызывать абстрактный метод")


class Class2(Class1):  # Наследуем абстрактный метод
    def func(self):  # Переопределяем метод
        print(self.x)


с2 = Class2(10)
с2.func()  # Вывод: 10
c1 = Class1(20)

try:  # Перехватываем исключения
    c1.func()  # Ошибка. Метод func() не переопределен
except NotImplementedError as msg:
    print(msg)  # Вывод: Нельзя вызывать абстрактный метод

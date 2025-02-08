class Classl:
    # Базовый класс для класса Class2
    def func1(self):
        print("Метод funс1() класса Classl")


class Class2(Classl):
    # Класс Class2 наследует класс Classl
    def func2(self):
        print("Метод func2() класса Class2")


class Class3(Classl):
    # Класс Class3 наследует класс Classl
    def func1(self):
        print("Метод funс1() класса Class3")

    def func2(self):
        print("Метод func2() класса Class3")

    def func3(self):
        print("Метод func3() класса Class3")

    def func4(self):
        print("Метод func4() класса Class3")


class Class4(Class2, Class3):
    # Множественное наследование
    def func4(self):
        print("Метод func4() класса Class4")


c = Class4()  # Создаем экземпляр класса Class4
c.func1()  # Вывод: Метод func1() класса Class3
c.func2()  # Вывод: Метод func2() класса Class2
c.func3()  # Вывод: Метод func3() класса Class3
c.func4()  # Вывод: Метод func4() класса Class4

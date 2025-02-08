class Class1:
# Базовый класс
    def funс1(self):
        print("Метод funс1() класса Class1")
    def func2(self) :
        print("Метод func2() класса Class1")

class Class2(Class1):
# Класс Class2 наследует класс Classl
    def func3(self):
        print("Метод func3() класса Class2")
    
c = Class2() # Создаем экземпляр класса Class2
c.funс1() # Выведет: Метод funcl() класса Classl
c.func2() # Выведет: Метод func2() класса Classl
c.func3() # Выведет: Метод func3() класса Class2
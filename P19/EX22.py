class A:
    @staticmethod
    def meth():
        print('meth')


A.meth()  # вызываем статический метод (без параметров) принадлежащий классу A
a = A()
a.meth()  # вызываем статический метод без параметров через экземпляр класса A

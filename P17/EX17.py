class Duck:
    def quack(self):
        print("Quaaaaaack!")

    def feathers(self):
        print("У утки белые и серые перья.")


class Person:
    def quack(self):
        print("Человек подражает утке.")

    def feathers(self):
        print("Человек берет перо с земли и показывает его.")

    def name(self):
        print("John Smith")


def in_the_forest(obj):
    obj.quack()
    obj.feathers()


donald = Duck()
john = Person()
in_the_forest(donald)  # в функцию передан экземпляр класса Duck
in_the_forest(john)  # в функцию передан экземпляр класса Person
print()
mylist = (donald, john)  # список из разнотипных элементов
for somebody in mylist:  # перебор элементов списка
    somebody.quack()  # вызывается соответствующий метод

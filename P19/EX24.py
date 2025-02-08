class MyClass():
    TOTAL_OBJECTS = 0

    def __init__(self):
        MyClass.TOTAL_OBJECTS = MyClass.TOTAL_OBJECTS + 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)


# Создаем объекты
my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
# Вызываем classmethod
MyClass.total_objects()

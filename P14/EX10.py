class MyClass:
    def __init__(self):
        self.x = 50
        self.arr = [1, 2, 3, 4, 5]

    def __eq__(self, y):  # Перегрузка оператора ==
        return self.x == y

    def __contains__(self, у):  # Перегрузка оператора in
        return у in self.arr


c = MyClass()
print("Равно" if c == 50 else "He равно")  # Вывод: Равно
print("Равно" if c == 51 else "He равно")  # Вывод: He равно
print("Есть" if 5 in c else "Нет")  # Вывод: Есть

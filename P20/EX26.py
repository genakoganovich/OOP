from math import gcd
from random import randint


class My_Fraction:
    def __init__(self, num, den):
        if num != 0 and den != 0:
            k = gcd(num, den)  # находим НОД
            self.num = num // k  # числитель
            self.den = den // k  # знасенатель
        else:
            raise ValueError

    @staticmethod
    def generate(num_min, num_max, den_min, den_max):
        return My_Fraction(randint(num_min, num_max), randint(den_min, den_max))

    def __str__(self):  # Метод преобразования дроби в строку
        return f'{self.num}/{self.den}'

    def __mul__(self, other):  # Умножение дробей
        if isinstance(other, My_Fraction):  # перегрузка умножения на дробь
            return My_Fraction(self.num * other.num, self.den * other.den)

        if isinstance(other, int):  # перегрузка умножения на целое число
            return My_Fraction(self.num * other, self.den)
        return self  # для остальных типов возвращаем значение самого объекта


def __truediv__(self, other):  # Деление дробей
    if isinstance(other, My_Fraction):  # перегрузка деления на дробь
        return My_Fraction(self.num * other.den, self.den * other.num)

    if isinstance(other, int):  # перегрузка деления на целое число
        return My_Fraction(self.num, self.den * other)
    raise TypeError  # для остальных типов вызываем исключение
# ----------------------------------------------------------------------
# Список из 5 случайных дробей:
a = [My_Fraction.generate(1, 9, 1, 9) for i in range(5)]
for f in a:
    b = My_Fraction.generate(1, 9, 1, 9)  # дробь для правого операнда
    cm = f * b
    print(f'{f} * {b} = {cm}')  # пример умножения на дробь
    cd = f / b
    print(f'{f} / {b} = {cd}')  # пример деления на дробь
    n = randint(1, 9)  # число для правого операнда
    cm = f * n
    print(f'{f} * {n} = {cm}')  # пример умножения на число
    cd = f / n
    print(f'{f} / {n} = {cd}')  # пример деления на число
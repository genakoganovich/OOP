class B:
    n = 5

    def adder(v):
        return v + B.n


print(B.n)  # Вывод: 5
print(B.adder(4))  # Вывод: 9

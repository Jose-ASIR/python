n = int(input("Introduce un número entero positivo: "))

for i in range(1, n + 1, 2):
    if i + 2 > n:
        print(i)
    else:
        print(i, end=", ")
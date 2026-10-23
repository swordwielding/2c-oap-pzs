# Дано вещественное число X и целое число N (> 0). Найти значение выражения X - X^3/(3!) + X^5/(5!) - ... 
# ... + (-1)^N-X^2-N+1/((2-N+1)!) (N! = 12 ...N). Полученное число является приближенным значением функции sin в точке X.

import math


x = float(input("введите вещетвенное число x: "))
n = int(input("введите целое число N (> 0): "))

while type(x) != float:
    try:
        x = float(x)
    except ValueError:
        print("число введено неппраивльо")
        x = float(input("введите вещетвенное число x: "))

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("число введено неппраивльо")
        n = int(input("введите целое число N (> 0): "))

res = 0.0

for i in range(n+1):
    term = ((-1) ** i) * (x ** (2 * i + 1)) / math.factorial(2 * i + 1)
    res += term

print(res)
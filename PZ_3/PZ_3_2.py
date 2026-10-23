a = int(input("введите целове число №1: "))
b = int(input("введите целове число №2: "))

if a == b:
    a = 0
    b = 0
else:
    a = a+b
    b = a+b

print(a, b)
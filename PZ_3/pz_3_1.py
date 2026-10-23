a = int(input("введите целове число №1: "))
b = int(input("введите целове число №2: "))
c = int(input("введите целове число №3: "))

while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("число введено неппраивльо")
        a = int(input("введите целове число №1: "))

while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("число введено неппраивльо")
        b = int(input("введите целове число №2: "))

while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("число введено неппраивльо")
        c = int(input("введите целове число №3: "))

if (a == b) or (a == c) or (b == c):
    print("верно, есть пара совпадающих")
else:
    print("неверно, совпадающих числе нету")
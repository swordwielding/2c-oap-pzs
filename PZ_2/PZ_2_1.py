n = int(input("Введите трехзначное число: "))

last = n % 10

first = n // 10

res = last * 100 + first

print("Полученное число:", res)
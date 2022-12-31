# 1. Вычислить число c заданной точностью d
# Пример: при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤ 10^{-10}

import math

d = input("Введите числа: ").split(",")
count = 1
x = math.pi
if int(d[1]) == 1:
    for i in range(len(d[1])):
        count *= 10
    c = int(str(int(x * count))[::-1])
    c /= 10
    print(str(c)[::-1])
else: print("Вы ввели неправильное число!")

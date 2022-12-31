# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input("Введите число: "))
index = 2
array = []
while number >= index:
    if number % index == 0:
        array.append(index)
        number //= index
        i = 2
    else:
        index += 1
print(array)

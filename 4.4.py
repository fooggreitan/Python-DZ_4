# 4. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

data = open('file (4.4).txt', 'w')
k = int(input("Введите число: "))
answer = []
a = 0
b = 0

if k == 0:
    answer.append("Решений нет!")
else:
    for i in range(k, 0, -1):

        a = random.randint(0, 100)
        b = random.randint(0, 100)

        if a == 0:
            k -= 1
            a = 1
            if b == 0:
                if i == 0:
                    answer.append(f'')
                else:
                    answer.append(f'')
            else:
                if i == 0:
                    answer.append(f' {b}')
                else:
                    answer.append(f'')
        else:
            if a == 1:
                if b == 0:
                    if i == 0:
                        answer.append(f'x**{i}')
                    else:
                        answer.append(f'x**{i} ')
                else:
                    if i == 1:
                        answer.append(f'x + {b}')
                    else:
                        answer.append(f'x + ')
            else:
                if b == 0:
                    if i == 0:
                        answer.append(f'{a}x**{i}')
                        a = 0
                    else:
                        if i == 1:
                            answer.append(f'{a}x')
                            a = 0
                        else:
                            answer.append(f'{a}x**{i} + ')
                else:
                    if i == 1:
                        answer.append(f'{a}x + {b}')
                        a = 0
                    else:
                        answer.append(f'{a}x**{i} + ')
                        a = 0

    answer.append(" = 0 ")

data.writelines(answer)
data.close()

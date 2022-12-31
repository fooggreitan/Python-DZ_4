# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
def remace(meaning2):
    dictEquaction = {}
    meaning2 = meaning2.replace(' - ', ' -').replace(' + ', ' +')
    meaning2 = meaning2.split()
    meaning2 = meaning2[:-2]
    for i in range(len(meaning2)):
        meaning2[i] = meaning2[i].replace('+', '').split('x**')
        dictEquaction[int(meaning2[i][1])] = int(meaning2[i][0])
    return dictEquaction

def sum(dict1, dict2):
    dict3 = {}
    maximum = (max(max(dict1), max(dict2)))
    for i in range(maximum, -1, -1):
        first = dict1.get(i)
        second = dict2.get(i)
        if first != None or second != None:
            dict3[i] = (first if first != None else 0) + (second if second != None else 0)
    return dict3

def res(dict3):
    result = ''
    for i in dict3.items():
        if result == '':
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))
            elif i[1] > 0:
                result += str(abs(i[1])) + 'x**' + str(abs(i[0]))
        else:
            if i[1] < 0:
                result += ' - ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))
            elif i[1] > 0:
                result += ' + ' + str(abs(i[1])) + 'x**' + str(abs(i[0]))
        result = result.replace('x**1', 'x').replace('x**0', '').replace('1x**', 'x**')
    return result + ' = 0'

data1 = open('firstFile (4.5).txt', 'r')
meaning1 = data1.readline()
data2 = open('secondFile (4.5).txt', 'r')
meaning2 = data2.readline()

dictEquaction1 = remace(meaning1)
dictEquaction2 = remace(meaning2)

dict3 = sum(dictEquaction1, dictEquaction2)

dict3 = res(dict3)

data3 = open('answerFile (4.5).txt', 'w')
data3.writelines(dict3)
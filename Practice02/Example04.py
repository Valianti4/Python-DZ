'''
Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''

from random import randint

print('Введите целое число.')
n = int(input())
list = [str(i) for i in range(-n, n + 1)]
print(f'Последовательность: {list}')
list2 = []
for i in range(-n, n + 1):
    list2.append(randint(-n, n))
list3 = []
for i in list2:
    if not i in list3:
        list3.append(i)
file = open('d:\Testirovshik\Python\DZ\Practice02\Python_Example04.txt', 'w')
for i in list3:
    file.write(str(i) + '\n')
file.close()
with open('d:\Testirovshik\Python\DZ\Practice02\Python_Example04.txt', "r") as file:
    for line in file:
        print(line.strip())
print(f'Произведение выбранных элементов списка: {list3[0] * list3[1] * list3[2]}.')
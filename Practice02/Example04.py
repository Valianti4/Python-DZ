'''
Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''
# Я всё-таки рискнул решить эту задачу в том ключе, в каком и начинал её решать.
# Потом, естественно, напишу для себя второй вариант решения этой задачи.
from random import randint

print('Введите целое число.')
n = int(input())
list = [str(i) for i in range(-n, n + 1)]
print(f'Последовательность: {list}')
list2 = []
for i in range(-n, n + 1):
    list2.append(randint(-n, n))
file = open('Python_Example04.txt', 'w')
for i in list2:
    file.write(str(i) + '\n')
file.close()
with open('Python_Example04.txt', "r") as file:
    for line in file:
        print(line.strip())
print(f'Произведение выбранных элементов списка: {list2[0] * list2[1] * list2[2]}.')
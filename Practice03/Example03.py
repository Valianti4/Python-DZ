'''
Задача 3. Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между 
максимальным и минимальным значением дробной части элементов.    
Пример:    
[1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''


import random

print('Для того, чтобы узнать разницу между максимальным и минимальным значением дробной части элементов списка, состоящего из вещественных чисел, для задания размера списка введите целое число.')
num = int(input())

def create_list(list):
    list = []
    for i in range(num):
        list.append(round(random.uniform(0, num), 2))
    print(f'Cписок: {list}')
    return list

def float_dif(list):
    min = 1
    max = 0
    for i in list:
        if (i - int(i)) <= min:
            min = i - int(i)
        if (i - int(i)) >= max:
            max = i - int(i)
    dif = round((max - min), 2)
    print(f'Разница между максимальным и минимальным значением дробной части элементов списка равна {dif}.')

list = create_list(list)
float_dif(list)
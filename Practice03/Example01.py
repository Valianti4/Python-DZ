'''
Задача 1. Задайте список из нескольких чисел. 
Напишите программу, которая найдёт сумму элементов списка, 
стоящих на нечётной позиции.    
Пример:    
[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
from random import randint

print('Чтобы задать список от 1 до определённого целого числа, введите это число.')
num = int(input())

def Mult_odds(list):
    list = []
    sum = 0
    for i in range(num):
        list.append(randint(0, num))
    print(f'Список: {list}')

    for i in range(len(list)):
        if i % 2 != 0:
            sum += int(list[i])
    print(f'Сумма элементов списка на нечётных позициях равна {sum}.')

Mult_odds(list)
'''
Задача 5. Реализуйте алгоритм перемешивания списка.
'''


from operator import index
import random
from random import randint

print('Чтобы задать случайный список, состоящий из определённого числа элементов, пожалуйста, введите это число')
num = int(input())

def create_list(list):
    list = []
    for i in range(num):
        list.append(randint(-num, num - 1))
    print(f'Начальный случайный список: {list}')
    return list

def shuffle_list(list):
    res = []
    for i in range(len(list)):
        index = randint(0, len(list) - 1)
        res.append(list[index])
        list.remove(list[index])
    print(f'Итоговый список с перемешанными элементами: {res}')

list = create_list(list)
shuffle_list(list)
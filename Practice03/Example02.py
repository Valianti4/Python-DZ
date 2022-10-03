'''
Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.    
Пример:    
[2, 3, 4, 5, 6] => [12, 15, 16];
[2, 3, 5, 6] => [12, 15]
'''


from random import randint

print('Чтобы задать список от 1 до определённого целого числа, введите это число.')
num = int(input())

def create_list(list):
    list = []
    for i in range(num):
        list.append(randint(0, num))
    print(f'Начальный список: {list}')
    return list

def mult_couples(list):
    list_res = []
    for i in range((len(list) + 1) // 2):
        list_res.append(list[i] * list[len(list) -1 - i])   
    print(f'Список произведения числовых пар списка: {list_res}')

list = create_list(list)
mult_couples(list)
'''
Задача 3. Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
'''


from random import randint

print('Чтобы задать список, введите число:')
num = int(input())

def create_list(list):
    list = []
    for i in range(num):
        list.append(randint(0, num))
    if num > 0:
        print(f'Начальный список: {list}')
    return list

def non_repeat_elements(list):
    res_list = []
    if num > 0:
        for i in list: 
            if i not in res_list:
                res_list.append(i) 
        print(f"Список из неповторяющихся элементов: {res_list}")
    else: print('Вы ввели неверное число. Пожалуйста, введите целое число больше 0.')

list = create_list(list)
non_repeat_elements(list) 
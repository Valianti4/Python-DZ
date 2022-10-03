'''
Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''


from random import randint

print('Введите целое число.')
n = int(input())

def create_list(list):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    print(f'Последовательность: {list}')
    return list

def mult_index(list):
    res = []
    for i in range(-n, n + 1):
        res.append(randint(-n, n))
    file = open('Python_Example04.txt', 'w')
    for i in res:
        file.write(str(i) + '\n')
    file.close()
    with open('Python_Example04.txt', "r") as file:
        for line in file:
            print(line.strip())
    print(f'Произведение выбранных элементов списка: {res[0] * res[1] * res[2]}.')
    
list = create_list(list)
mult_index(list)
'''
Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. 
Позиции хранятся в файле file.txt в одной строке одно число.
'''


print('Введите целое число.')
n = int(input())
list = [str(i) for i in range(-n, n + 1)]
print(f'Последовательность: {list}')

f = open('d:\Testirovshik\Python\DZ\Practice02\Python_Example04.txt', 'w')
for i in list([0], [2], [5]):
    f.write(i + '\n')
f.close()
# with open('d:\Testirovshik\Python\DZ\Practice02\Python_Example04.txt', "r") as f:
#     for line in f:
#         print(line.strip())
# res = [str(i) for i in range(-n, n + 1)]
# res = map(int, res)
# import math
# print(f'Произведение элементов списка: {math.prod(res)}')
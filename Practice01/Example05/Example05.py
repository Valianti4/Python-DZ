'''
Задача 5. Напишите программу, которая принимает на вход координаты двух точек 
и находит расстояние между ними в 2D пространстве.    
    Пример:    
    A (3,6); B (2,1) -> 5,09
    A (7,-5); B (1,-1) -> 7,21
'''


print('Введите координату x для точки A:')
print('x1: ', end = '')
x1 = int(input())
print('Введите координату y для точки A:')
print('y1: ', end = '')
y1 = int(input())
print('Введите координату x для точки B:')
print('x2: ', end = '')
x2 = int(input())
print('Введите координату y для точки B:')
print('y2: ', end = '')
y2 = int(input())
import math
res = round(math.sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1)), 2)
res = int(res * 100)
res = float(res / 100)
print(f'Расстояние между точками равно: {res}.')
'''
Задача 2. Напишите программу, которая принимает на вход число N 
и выдает набор произведений чисел от 1 до N.    
    Пример:    
    Пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
'''


print('Чтобы увидеть последовательность результатов произведения чисел от 1 до определённого целого числа, пожалуйста, введите это число. ')
n = int(input())
if n > 0:
    j = 1
    print('[', end = '')
    for i in range(1, n + 1):        
        j = j * i
        if i < (n + 1) -1: print(f'{j}', end = ', ')
        else: print(f'{j}', end = '')
    print(']')
else: print('Вы ввели неверное число. Пожалуйста, введите целое число больше 0.')
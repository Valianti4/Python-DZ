'''
Задача 5. Задайте число. Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.    
Пример:    
 для k = 8 список будет выглядеть так: 
 [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]  
'''


print('Чтобы составить список чисел Фибоначчи для числа в диапазоне от -N до N, введите целое число больше 0.')
k = int(input())

def Create_fibonacci(k):    
    list_fibo = []
    a, b = 1, 1
    for i in range(k - 1):
        list_fibo.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k):
        list_fibo.insert(0, a)
        a, b = b, a - b             
    return list_fibo   
     
print(f'Список чисел Фибоначчи: {Create_fibonacci(k + 1)}')
list_fibo = Create_fibonacci(k)

'''
Задача 2. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.
'''


print('Чтобы задать список, введите число:')
num = int(input())

def mult_elements(num):
    i = 2
    list = []
    a = num
    while i <= num:
        if num % i == 0:
            list.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f'Список простых множителей числа {a}: {list}.')

mult_elements(num)
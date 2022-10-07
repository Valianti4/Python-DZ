'''
Задача 4. Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.    
Пример:    
k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
'''


from random import randint, choice

print('Чтобы записать в файл многочлен степени k, введите целое число:')
k = int(input())

def get_string(num: int):
    line = ''
    signs = ['+ ', '- ']
    while num:
        occ = randint(0, 100)
        if occ:
            line += f'{occ} * x ^ {num} '
            line += choice(signs)
        num -= 1
    line += f'{randint(0, 100)} = 0'
    return line

with open('Task04.txt', "w",) as file:
    if k > 0:
        file.write(get_string(k))
    file.close()
'''
Задача 1. Вычислить число c заданной точностью d    
Пример:    
при d = 0.001, π = 3.141    10^(-1) ≤ d ≤10^(-10)
'''


print('Чтобы вычислить число c заданной точностью d, введите d:')
d = float(input())

def exas_pi(exas=1.0e-5):
    s = 0
    d = 1
    sgn = 1
    while True:
        a = 4 / d
        s = s + sgn * a
        if a < exas:
            return s
        sgn = -sgn
        d = d + 2
 
print(f'Число c заданной точностью d равно {round((exas_pi()), 3)}.')
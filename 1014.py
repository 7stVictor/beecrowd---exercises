# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

X = Y = 0
# .3f km/l
for m in range(0, 2):
    if m == 0:
        X += int(input())
    if m == 1:
        Y += float(input())
calc = X/Y
print(f'{calc:.3f} km/l')

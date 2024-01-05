# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A, B, C = input().split()
valores = [A, B, C]
novo = []
for cada_letra in valores:
    novo.append(float(cada_letra))
A, B, C = novo
a = 0.5 * A * C
b = 3.14159 * (C**2)
c = 0.5 * (A+B) * C
d = B**2
e = A*B
calc = [a, b, c, d, e]
areas = ('TRIANGULO:', 'CIRCULO:', 'TRAPEZIO:','QUADRADO:', 'RETANGULO:')
cont = 0
while cont < len(calc):
    print(f'{areas[cont]} {calc[cont]:.3f}')
    cont += 1
import os
os.system('cls')
# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A, B, C = input().split()
l = [A, B, C]
nova_lista = []
for c in range(0, 3):
    nova_lista.append(int(l[c]))
print(f'{max(nova_lista)} eh o maior')

from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()
l = [x1, y1, x2, y2]
nova_lista = []
for index in range(0, 4):
    nova_lista.append(float(l[index]))
x1, y1, x2, y2 = nova_lista
calc = sqrt(((x2-x1)**2) + ((y2-y1)**2))
print(f'{calc:.4f}')


segundos = int(input())
tempo = []
while len(tempo) != 3:
    horas = segundos // 3600
    tempo.append(horas)
    minutos = (segundos%3600) // 60
    tempo.append(minutos)
    seg = segundos % 60
    tempo.append(seg)
print(f'{tempo[0]}:{tempo[1]}:{tempo[2]}')
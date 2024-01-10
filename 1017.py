
# quantos litros necessarios para a viagem com :.3f

# carro faz 12km/l

# input do tempo gasto (em horas) 10 horas
# input da velocidade media em km/h 85km/h
horas = 0
velocidade = 0
consumo_medio = 12
for c in range(0, 2):
    x = int(input())
    if horas != 0:
        velocidade += x
    else:
        horas += x
calc = (horas*velocidade)/consumo_medio
print(f'{calc:.3f}')
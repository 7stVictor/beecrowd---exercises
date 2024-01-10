# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. 
# Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, 
# caso haja uma divisão por 0 ou raiz de numero negativo.



# if sqrt(0) and sqrt(-1) = "Impossivel calcular"
# else print(:.5f)

A, B, C = input().split()
variaveis = [A, B, C]
float_var = []
for index in range(0, len(variaveis)):
    float_var.append(float(variaveis[index]))
A, B, C = float_var
try:
    calc1 = round(B**2, 2) - (4 * A * C) # 200.01
    raiz = round(calc1**0.5, 5)
    div = 2*A
    x1 = (-B+raiz)/(div)
    x2  = (-B-raiz)/(div)
    print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')
except:
    print(f'Impossivel calcular')

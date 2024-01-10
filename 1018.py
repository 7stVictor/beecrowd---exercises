


# notas = (100, 50, 20, 10, 5, 2, 1)
# valor = int(input())
# divisao = []

# for c in range(0, len(notas)):
#     calc = valor // notas[c]
#     divisao.append(calc)
#     valor = valor - (notas[c]*calc)
# for index in range(0, len(divisao)):
#     ind = divisao[index]
#     ind2 = notas[index]
#     print(f'{ind} nota(s) de R$ {ind2},00')




cedulas = [100, 50, 20, 10, 5, 2, 1]
valor = int(input())
v = valor
inteiros = []
for index in range(0, len(cedulas)):
    calc = valor // cedulas[index]
    inteiros.append(calc)
    valor -= cedulas[index]*calc
print(f'{v}')
for c in range(0, len(inteiros)):
    c2 = cedulas[c]
    print(f'{inteiros[c]} nota(s) de R$ {c2},00')
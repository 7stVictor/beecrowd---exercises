
####################################
# lista = codigo, quantidade = input().split()
# numeros = []
# codigos = [('Cachorro Quente', 4), ('X-Salada', 4.5), ('X-Bacon', 5), ('Torrada simples', 2), ('Refrigerante', 1.5)]
# for c in range(0, len(lista)):
#     numeros.append(int(lista[c]))
# ean = numeros[0]-1
# value = codigos[ean][1]*numeros[1]
# print(f'Total: R$ {value:.2f}')
####################################

####################################
cod, quantidade = map(int, input().split())
valor = [4, 4.5, 5, 2, 1.5]
print(f'Total: R$ {valor[cod-1]*quantidade:.2f}')
####################################

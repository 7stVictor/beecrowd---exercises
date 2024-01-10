# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, 
# e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se 
# a variável A for par escrever a mensagem 
# "Valores aceitos", senão escrever "Valores nao aceitos".

#############################################
# criando nova lista com numeros inteiros
A, B, C, D = input().split()
build_int = [A, B, C, D]
new_int = []
for index in range(0, len(build_int)):
    new_int.append(int(build_int[index]))
A, B, C, D = new_int
##############################################

if B > C and D > A and C+D > A+B and C and D > 0 and A % 2 == 0:
    print(f'Valores aceitos')
else:
    print(f'Valores nao aceitos')
cedula = [100, 50, 20, 10, 5, 2] 
moeda = [1, 0.50, 0.25, 0.10, 0.05, 0.01] 
cedulas = []
moedas = []
valor = float(input())
valor += +0.00000000000006
for c in range(0, len(cedula)):
    div = valor // cedula[c]
    div2 = valor-(div*cedula[c])
    valor = div2
    cedulas.append(int(div))
for m in range(0, len(moeda)):
    div3 = valor // moeda[m]
    div4 = valor - (div3*moeda[m])
    valor = div4
    moedas.append(int(div3))
print('NOTAS:')
for index in range(0, len(cedulas)):
    print(f'{cedulas[index]} nota(s) de R$ {cedula[index]}.00')
print('MOEDAS:')
for index2 in range(0, len(moedas)):
    print(f'{moedas[index2]} moeda(s) de R$ {moeda[index2]:.2f}')


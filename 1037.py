# Você deve fazer um programa que leia um valor qualquer e 
# apresente uma mensagem dizendo em qual dos seguintes intervalos
# ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
# Obviamente se o valor não estiver em nenhum destes intervalos, 
# deverá ser impressa a mensagem “Fora de intervalo”.






x = float(input())

if x >= 0 and x <= 25:
    print('Intervalo [0,25]')
elif x > 25 and x <= 50:
    print('Intervalo (25,50]')
elif x > 50 and x <= 75:
    print('Intervalo (50,75]')
elif x > 75 and x <= 100:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')
    
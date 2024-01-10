# int(input())
# informar anos, meses e dias
# todos os anos com 365 dias e todo mes com 30 dias



# dias = int(input())
# tempo = []
# while len(tempo) != 3:
#     anos = dias // 365
#     tempo = tempo + [anos]
#     meses = (dias - (anos*365)) // 30
#     tempo = tempo + [meses]
#     dias = (dias - (anos*365))-(meses*30)
#     tempo = tempo + [dias]
# print(f'{tempo[0]} ano (s)\n{tempo[1]} mes (es)\n{tempo[2]} dia (s)')

tempo = []
while len(tempo) != 3:
    x = int(input())
    c = x // 365
    tempo = tempo + [c]
    ca = (x - (c*365)) // 30 # 2 MESES
    tempo = tempo + [ca]
    cal = (x - (c*365))-(ca*30)
    tempo = tempo + [cal]
print(f'{tempo[0]} ano (s)\n{tempo[1]} mes (es)\n{tempo[2]} dia (s)')
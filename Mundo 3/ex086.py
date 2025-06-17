matriz = list()
um = list()
dois = list()
tres = list()



for c in range (0,3):
    primeira = int(input(f'Digite o valor de [0, {c}]'))
    um.append(primeira)
for c in range (0,3):
    primeira = int(input(f'Digite o valor de [1, {c}]'))
    dois.append(primeira)
for c in range (0,3):
    primeira = int(input(f'Digite o valor de [2, {c}]'))
    tres.append(primeira)

matriz.append(um)
matriz.append(dois)
matriz.append(tres)

print('-='*20)


print(' ',matriz[0][0], ' ' , matriz[0][1],' ', matriz[0][2])
print(' ',matriz[1][0],' ', matriz[1][1],' ', matriz[1][2])
print(' ',matriz[2][0],' ', matriz[2][1],' ', matriz[2][2])
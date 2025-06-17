matriz = list()
um = list()
dois = list()
tres = list()
pares= list()
somapares = 0
somaterceira = 0
maiorsegunda = 0

for c in range (0,3):
    primeira = int(input(f'Digite o valor de [0, {c}]'))
    um.append(primeira)
    if primeira % 2 == 0:
        pares.append(primeira)
        somapares += primeira
for c in range (0,3):
    primeira = int(input(f'Digite o valor de [1, {c}]'))
    dois.append(primeira)
    if primeira % 2 == 0:
        pares.append(primeira)
        somapares += primeira
    if primeira > maiorsegunda:
        maiorsegunda = primeira        
for c in range (0,3):
    primeira = int(input(f'Digite o valor de [2, {c}]'))
    tres.append(primeira)
    somaterceira += primeira
    if primeira % 2 == 0:
        pares.append(primeira)
        somapares += primeira
    

matriz.append(um)
matriz.append(dois)
matriz.append(tres)

print('-='*20)

print(' ',matriz[0][0], ' ' , matriz[0][1],' ', matriz[0][2])
print(' ',matriz[1][0],' ', matriz[1][1],' ', matriz[1][2])
print(' ',matriz[2][0],' ', matriz[2][1],' ', matriz[2][2])

print(f'A soma de todos os valores pares {pares} é {somapares}')
print(f'A soma dos valores da terceira coluna {tres} é {somaterceira}')
print(f'O maior valor da segunda linha é {maiorsegunda}')



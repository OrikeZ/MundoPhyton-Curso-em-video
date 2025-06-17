pessoas = list()
dados = list()
maiorpeso = list()
menorpeso = list()

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(int(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    maiorpeso = dados[:]
    menorpeso = dados[:]
    dados.clear()
    cont = str(input('Deseja continuar? [S/N]').upper())    
    if cont == 'N':
        break
    
for p in pessoas:
    if p[1] > maiorpeso[1]:
        maiorpeso[1] = p[1]
        maiorpeso[0] = p[0]
    elif p[1] < menorpeso[1]:
        menorpeso[1] = p[1]
        menorpeso[0] = p[0]

print('-='*30)
print(f'Ao todo você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorpeso[1]}Kg. Peso de {maiorpeso[0]}')
print(f'O menor peso foi de {menorpeso[1]}Kg. Peso de {menorpeso[0]}')


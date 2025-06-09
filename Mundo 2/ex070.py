total = 0
maisde1000 = 0
barato = 5000000
while True:
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: R$ '))
    total += preco
    if preco > 1000:
        maisde1000 += 1
    if preco < barato:
        barato = preco
        nomebarato = produto
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar == 'N':
        break
print(f'Total gasto: R$ {total:.2f}')
print(f'Total de produtos acima de R$ 1000: {maisde1000}')
print(f'Produto mais barato: {nomebarato} com preço de R$ {barato:.2f}')
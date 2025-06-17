listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.9,
            'Estojo', 8,
            'Mochila', 75)

print('-' * 40)
print(f'{"Tabela de preços":^40}' )
print('-' * 40)

for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    if item % 2 ==1:
        print(f'R${listagem[item]:>8}')
print('-'*40)
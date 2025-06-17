num = list
escolha =''

while escolha != 'N':
    numero = (int(input('Digite um valor: ')))
    if num.count(numero) == 0:
        num.append(numero)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor Duplicado" Não será adicionado"')
    escolha = str(input('Quer continuar? [S/N] ').upper())
num.sort()

print('-='*30)

print(f'Você digitou os valores {num}')    
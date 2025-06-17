# galera = [['Vinicius', 25], ['Joao', 39],['Maria',19],['Jorge', 15]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmai = totmen = 0

for c in range(0,5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #limpa a lista de dado, que já foi copiada para a lista galera com o comando acima

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'No total foram {totmai} maiores de idade e {totmen} menores de idade')
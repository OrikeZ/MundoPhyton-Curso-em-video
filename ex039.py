#Desafio 39

idade = int(input('Digite sua idade: '))

if idade == 18:
    print('Você precisa se alistar este ano')
elif idade == 17:
    print('Você precisará se alistar daqui 1 ano')
elif idade < 17:
    print('Você precisará se alistar em {} anos'.format(-int(idade - 18)))
elif idade == 19:
    print('Você passou 1 ano do momento de se alistar!')
else:
    print(('Você passou {} anos do momento de se alistar!'.format(int(idade - 18 ))))
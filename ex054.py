import datetime

maiores = 0
menores = 0

for c in range (1,7+1):
    ano = int(input('Digite o ano de nascimento: '))
    idade = int(datetime.datetime.now().year - ano)
    if idade < 18:
        menores = menores+1
    elif idade >= 18:
        maiores = maiores+1

print('Ao todo são {} maiores de idade, e {} menores de idade'.format(maiores, menores))

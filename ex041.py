#desafio 41

import datetime

anonasc = int(input('Digite o ano de nascimento: '))
idade = int(datetime.datetime.now().year - anonasc)

print('Você possui {} anos de idade'.format(idade))

if   idade > 0 and idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JUNIOR')
elif idade > 19 and idade <= 20:
    print('SENIOR')
elif idade > 20 and idade <= 110:
    print('MASTER')
else:
    print('Voce digitou uma data de nascimento inválida')




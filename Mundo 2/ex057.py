sexo = ''

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo (M/F): ').upper())
    if sexo != 'M' and sexo != 'F':
        print('Você digitou errado, {} não é válido, digite novamente'.format(sexo))
print('Processo finalizado')
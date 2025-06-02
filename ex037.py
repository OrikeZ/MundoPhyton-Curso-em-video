#Desafio 37

numero = int(input('Digite um Número: '))
conversor = int(input('digite uma opção para converter  1 para Binário 2 para octal  3 para hexadecimal: '))

if conversor ==1:
    print('{} convertido em binário é: {}'.format(numero, bin(numero)))
elif conversor ==2:
    print('{} convertido em Octal é: {}'.format(numero, oct(numero)))
elif conversor ==3:
    print('{} convertido em hexadecimal é: {}'.format(numero, hex(numero)))
else:
    print('Você não digitou uma opção válida, inicie o processo novamente')

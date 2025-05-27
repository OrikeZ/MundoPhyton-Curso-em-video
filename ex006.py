#Desafio 16

import math
import random

numero = float(input('digite um numero: '))

print('a parte inteira desse numero é {}'.format(math.floor(numero)))

#Desafio 19

nome = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))

resultado = [nome,nome2,nome3,nome4]
escolha = random.choice(resultado)


print('O sorteado para apagar o quadro foi: {}'.format(escolha))


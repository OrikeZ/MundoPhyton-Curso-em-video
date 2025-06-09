import random
import math
n = 0
while True:
    n = int(input('Par ou Impar? 1 para Par ou 2 para Impar: '))
    n2 = int(input('Digite um numero de 1 a 10: '))
    computador = math.floor(random.random() * 10) + 1
    jogo = n2 + computador
    print(f'Você escolheu {n2} e o computador escolheu {computador}. Deu {jogo}.')
    if jogo % 2 == 0 and n2 % 2 == 0:    
        print('Você escolheu Par, o resultado é Par. Você ganhou!')
    elif jogo % 2 == 0 and n2 % 2 != 0:
        print('Você escolheu Impar, o resultado é Par. Você perdeu!')
        break
    elif jogo % 2 != 0 and n2 % 2 == 0:
        print('Você escolheu Par, o resultado é Impar. Você perdeu!')
        break
    elif jogo % 2 != 0 and n2 % 2 != 0:
        print('Você escolheu Impar, o resultado é Impar. Você ganhou!')  
        
print('Fim do jogo.')

#Desafio 28
import random

n = int(random.random()*6)
print(n)
chute = int(input('Chute um numero entre 0 e 5: '))


if chute == n:
    print('Parabéns, você acertou!')
else:
    chute = int(input('Você errou! chute novamente: '))
    if chute == n:
        print('Você acertou, parabéns!')
    else:
        chute = int(input('Você errou! chute novamente: '))
        if chute == n:
            print('Você acertou, Parabéns!')
        else:
            chute = int(input('Voce errou, tente novamente: '))
            if chute == n:
                print('Voce acertou! Parabéns')
            else:
                chute = int(input('oce errou, tente novamente: '))
                if chute == n:
                    print('Você acertou, parabéns')
                else:
                    print('Voce excedeu o limite de tentativas!')

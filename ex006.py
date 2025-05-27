#Desafio 16

import math
import random

numero = float(input('digite um numero: '))

print('a parte inteira desse numero é {}'.format(math.floor(numero)))

#desafio 17

co = float (input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

print('A hipotenusa do valor é: {:.2f}'.format(math.hypot(co,ca)))

#Desafio 18

angulo = float(input('Digite o angulo: '))
seno = math.sin(math.radians(angulo))
print('O seno é: {:.2f}'.format(seno))
coseno = math.cos(math.radians(angulo))
print('O Coseno é: {:.2f}'.format(coseno))
tangente = math.tan(math.radians(angulo))
print('A tangente é {:.2f}: '.format(tangente))



#Desafio 19

nome = str(input('Digite o primeiro nome: '))
nome2 = str(input('Digite o segundo nome: '))
nome3 = str(input('Digite o terceiro nome: '))
nome4 = str(input('Digite o quarto nome: '))

resultado = [nome,nome2,nome3,nome4]
escolha = random.choice(resultado)


print('O sorteado para apagar o quadro foi: {}'.format(escolha))

#Desafio 20

nome5 = str(input('Digite o primeiro nome: '))
nome6= str(input('Digite o segundo nome: '))
nome7 = str(input('Digite o terceiro nome: '))
nome8 = str(input('Digite o quarto nome: '))

lista = [nome5, nome6,nome7,nome8]

random.shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))

#Desafio 21

import pygame

pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
pygame.event.wait()












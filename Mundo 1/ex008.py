#frase = 'teste de python'
#listaFrases = frase.split()
#print(listaFrases[2][3])
from os.path import split

#Desafio 22

nome = str(input('Digite seu nome completo: '))
semespaco = len(nome) - nome.count(' ')
primeironome = nome.split()
print('O nome com todas as letras maicusculas: {}'.format(nome.upper()))
print('O nome com todas as letras minusculas: {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(semespaco))
print('Seu primeiro nome tem {} letras'. format(len(primeironome[0])))

#Desafio 23

numero = input('Digite um numero entre 0 e 9999: ')

print('Unidade: {}'.format(numero[0]))
print('Dezena: {}'.format(numero[1]))
print('Centena: {}'.format(numero[2]))
print('milhas: {}'.format(numero[3]))

#Desafio 24
cidade = (input('Digite o nome da sua cidade'))
cidadep = "santo" in cidade

print('O nome da cidade citada inicia com santo?: {}'.format(cidadep))

#desafio 25

nome25 = input('Digite seu nome completo: ')
listanomes = nome25.upper().split()


print ('o seu nome possui a palavra silva? {}'.format("SILVA" in listanomes))









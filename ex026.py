from itertools import count

frase = input('Digite uma frase: ')
frasemaiuscula = frase.upper()
print('Na frase digitada a letra "A" aparece {} vezes'.format(frasemaiuscula.count('A')))
print('na primeira aparição foi no indice {}'.format(frasemaiuscula.find('A')))
print('ultima aparição foi no indice {}'.format(frasemaiuscula.rfind('A')))
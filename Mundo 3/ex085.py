lista = list()
impar = list()
par = list()

for c in range (0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
impar.sort()
par.sort()
lista.append(par)
lista.append(impar)
        

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')


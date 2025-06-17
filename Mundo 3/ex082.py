num =[]
impar = []
par = []

while True:
    numero = int(input('Digite um número: '))
    num.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
    print('-=' *20) 
    escolha = str(input('Você deseja continuar? [S/N] ').upper())
    print('-=' *20) 
    if escolha == 'N':
        break
    
print('-=' *20)     
    
print(f'A lista completa é {num}\nos números impares são {impar}\ne os numeros pares são {par}')
    
print('-=' *20) 
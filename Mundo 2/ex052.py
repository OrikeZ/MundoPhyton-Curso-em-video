numero = int(input("Digite um número: "))
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    
print('{} '.format(c), end=' ')
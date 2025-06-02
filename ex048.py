soma = 0

for c in range (1, 500+1):
    if c % 2 != 0 and c % 3 == 0:
        soma += c

print('A soma entre todos os impares e divisiveis de 3 entre 1 e 500 é {}'.format(soma))


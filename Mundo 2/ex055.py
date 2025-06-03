maior = 0
menor = 100

for c in range (0,5):
    peso = float(input('Digite seu peso: '))
    if maior < peso:
        maior = peso

    if menor > peso:
        menor = peso

print('O maior peso inserido foi {}, e o menor foi {}'.format(maior, menor))

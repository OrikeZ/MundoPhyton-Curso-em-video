valores = []
for cont in range (0,5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'\nNa posição {c}. encontrei o valor: {v}!', end='')
print('\nCheguei ao final da lista')

a= [2,3,4,7]
b = a 
b[2] = 8

print(f'Lista A {a}')
print(f'Lista B {b}')


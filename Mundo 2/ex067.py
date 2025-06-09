n = 0
while True:
    n = int(input('Digite um numero para saber sua tabuada ou um numero negativo para sair: '))
    if n < 0:
        break
    print(f'Tabuada do {n}:')
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa encerrado.')
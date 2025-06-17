num = []

while True:
    num.append(int(input('Digite um número: ')))
    escolha = str(input('Você deseja continuar? [S/N]').upper())
    if escolha == 'N':
        break
quantidade = len(num)
num.sort(reverse=True)

print(f'Ao todo foram digitados {quantidade} números!')
print(f'A lista dos números inseridos de forma decrescente é {num}')
if num.count(5) != 0:
    print(f'O número 5 está na lista')
else:
    print(f'O número 5 não está presente na lista')
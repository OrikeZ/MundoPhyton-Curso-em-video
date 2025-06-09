n = int(input('Digite o valor a ser sacado:'))
total = n
cedulas = [50, 20, 10, 5, 2, 1]
print(f'Total a ser sacado: R$ {total}')
for cedula in cedulas:
    quantidade = total // cedula
    if quantidade > 0:
        print(f'Total de {quantidade} cédulas de R$ {cedula}')
    total %= cedula
    if total == 0:
        break

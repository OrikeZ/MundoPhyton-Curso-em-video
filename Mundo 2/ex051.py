primeiro = int(input('Digite o termo: '))
razão = int(input('Digite a razao: '))
decimo = primeiro + (10 - 1) * razão
for c in range(primeiro, decimo + razão, razão):
    print('{}'.format(c), end=' -> ')
   
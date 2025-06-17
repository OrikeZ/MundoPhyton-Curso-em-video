num = []
num.append(int(input('Digite um valor: ')))
maior = num[0:]
menor = num[0:]

for cont in range (0,4):
    num.append(int(input('Digite um valor: ')))
    if num[cont] > maior[0]:
        maior = num[cont]

print(maior)
print(menor)
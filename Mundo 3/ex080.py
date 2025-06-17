num = list(range(0,4))

num.append(int(input('Digite o 1º valor: ')))

for indicie, valor in enumerate(num):
    escolha = int(input(f'Digite o {indicie + 2}º valor: '))
    if escolha < num[0]:
        num.pop(0)
        num.insert(0, escolha)
    elif escolha > num[0] and escolha < num[1]:
        num.pop(1)
        num.insert(1,escolha)
    elif escolha > num[2] and escolha < num[3]:
        num.pop(2)
        num.insert(2, escolha)
    elif escolha > num[3] and escolha < num[4]:
        num.pop(3)
        num.insert(3, escolha)
    else:
        num.pop(4)
        num.insert(4,escolha)
     
print(num)
    


import random

segredo = int(random.random()*11)
chute = 15
tentativas = 0
while chute != segredo:
    chute = int(input('Chute um valor: '))
    tentativas += 1
    print(segredo)
print('Você conseguiu advinhar com {} tentativas!'.format(tentativas))

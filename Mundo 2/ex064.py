print('Bem vindo! Insira a quantidade de números que você desejar! Ao digitar 999 o programa será encerrado!')

n = 0
soma = 0
contagem = 0

while n != 999:
    n = int(input('Insira um número: '))
    if n != 999:
        soma+=n
        contagem+=1
    elif n == 999:
        print('Você finalizou o programa!')
print('Você inseriu um total de {} números, e a soma dos números inseridos é {}'.format(contagem, soma))

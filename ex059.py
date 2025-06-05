
m = 0

print('Insira 2 valores e após isso selecione a opção desejada!')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa')  

while m != 5:
    m = int(input('Digite uma opção: '))
    if m == 1:
        print('A soma de {} e {} é {}'.format(n1,n2,n1+n2))
        print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa') 
    elif m == 2:
        print('A multiplicação de {} por {} resulta em {}'.format(n1,n2,n1*n2))
        print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa') 
    elif m == 3:
        if n1 > n2:
            print('Entre {} e {}, {} é maior'.format(n1,n2,n1))
            print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa') 
        else:
            print('Entre {} e {}, {} é maior'.format(n1,n2,n2))
            print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa') 
    elif m == 4:
        print('Ok insira a seguir os dois novos números!')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('Selecione uma opção: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do programa') 
    elif m == 5:
        print('Que pena! você saiu do programa!')
    else:
        print('Você inseriu uma opção inválida, tente novamente!')

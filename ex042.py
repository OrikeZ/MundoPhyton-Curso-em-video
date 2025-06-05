n1 = float(input('Digite o comprimento da primeira reta: '))
n2 = float(input('Digite o comprimento da segunda reta: '))
n3 = float(input('Digite o comprimento da terceira reta: '))

if n1+n2>n3 and n1+n3>n2 and n3+n2>n1:
    print('As tres retas podem formar um triangulo')
    if n1==n2 and n2==3:
        print('O triangulo é um equilátero')
    elif n1==n2 and n2 != n3:
        print('O triangulo é um isósceles')
    elif n1 !=n2 and n2 == n3:
        print('O triangulo é um isósceles')
    elif n1 != n2 and n3 == n1:
        print('O triangulo é um isósceles')
    elif n1!=n2 and n2 != n3:
        print('O triangulo é um Escaleno')
else:
    print('as retas nao podem formar um triagulo')




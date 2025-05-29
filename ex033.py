n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite outro numero: '))

if n1>n2>n3:
    print('o maior numero é {}'.format(n1))
else:
    if n2>n1>n3:
        print('O maior numero é {}'.format(n2))
    else:
            print('O maior numero é {}'.format(n3))

if n1<n2<n3:
    print('O menor numero é {}'.format(n1))
else:
    if n2<n1<n3:
        print('O menor numero é {}'.format(n2))
    else:
        print('O menor numero é {}'.format(n3))

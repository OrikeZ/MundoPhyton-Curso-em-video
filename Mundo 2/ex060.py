n = int(input('Digite um valor '))
f = 1
soma = 0
while f != n and f > 0:
    if n!=f:
        print('{}x{}'.format(n, f), end='x')
        f = n-1
        soma+=n*f
    
        print('Fatorial nao funciona para numeros negativos')
print('= {}'.format(soma))

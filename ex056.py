somaidade = 0
mediaidade = somaidade
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range (1, 5):
    print(('--------{}ª PESSOA--------'.format(p)))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome  
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    
        
print('A média de idade do grupo é de {} anos'.format(somaidade/4))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))

   
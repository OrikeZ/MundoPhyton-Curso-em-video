n = 0
soma = 0
contagem = 1
media = soma/contagem
menor = n
maior = n
escolha = 'S'


while escolha == 'S':
    n = int(input('Digite um número inteiro:'))
    if n < menor:
        menor = n
    if n > maior:
        maior = n
    soma += n 
    contagem+=1
    print('A média dos números inseridos é {}, o menor é {}, e o maior é {}'.format(media, menor, maior))
    escolha = str(input('Selecione uma opção [S] para continuar e [N] para parar!').upper())

print('Você decidiu parar, a média entre os números inseridos é {}, o menor é {}, e o maior é {}'.format(media,menor,maior))

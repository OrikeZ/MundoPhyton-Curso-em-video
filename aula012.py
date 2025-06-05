#Condições aninhadas
nome = str(input('Qual é o seu nome: '))

if nome == 'Vinicius':
    print('Bem vindo Vinicius')
elif nome == 'Gabriel':
    print('Bem vindo Gabriel')
else:
    print('Bem vindo {}'.format(nome))
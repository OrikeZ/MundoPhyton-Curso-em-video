#Desafio 44

valor = float(input('Digite o valor do produto: '))
pagamento = int(input('Digite a forma de pagamento \n 1 para em dinheiro \n 2 para a vista no cartao \n 3 em até 2x no cartão \n 4 para 3x ou mais vezes no cartão:'))

dinheiro = 10*valor/100
cartao1 = 5*valor/100
tresvezes = 20*valor/100

if pagamento == 1:
    print('O valor com 10% de desconto ficará R${:.2f}'.format(float(valor-dinheiro)))
elif pagamento == 2:
    print('O valor com 5% de desconto ficará R${:.2f}'.format(float(valor-cartao1)))
elif pagamento == 3:
    print('O valor em até 2x não possui desconto, portanto ficará R${:.2f}'.format(valor))
elif pagamento == 4:
    print('O valor com 20% de juros ficará R${:.2f}'.format(float(valor+tresvezes)))

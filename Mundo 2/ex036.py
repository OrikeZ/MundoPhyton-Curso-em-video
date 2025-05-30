casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = float(input('Digite em quantos anos vai ser pago: '))
salario30 = int(30*salario/100)
prestacao = casa/anos

if prestacao > salario30:
    print('Emprestimo negado')
elif prestacao == salario30:
    print('Emprestimo tb negado')
else:
    print('Emprestimo aprovado')
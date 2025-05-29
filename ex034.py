salario = float(input('Digite o salário do funcionario: '))


if  salario > 1250:
    print('O salário com o aumento ficará: {}'.format(salario+salario*0.10))
else:
    print('O salário com o aumento ficará: {}'.format((salario+salario*0.15)))
expressao = str(input('Digite a expressão matemática: '))

contagemaberta = expressao.count('(')
contagemfechada = expressao.count(')')

if contagemaberta != contagemfechada:
    print("A expressão está inválida")
else:
    print('A expressão é válida!')
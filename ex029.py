#Desafio 29

velo = int(input('Digite a velocidade do carro: '))
multa = (velo-80)*7

if velo > 80:
    print('Você excedeu a velocidade permitida, sua multa será de R$ {},00 reais'.format(multa))
else:
    print('Sua velocidade está dentro do permitido!')

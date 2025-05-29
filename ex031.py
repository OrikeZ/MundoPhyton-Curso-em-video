kilometragem = int(input('Digite a distancia em kilometros da sua viagem: '))

if kilometragem <= 200:
    print('A sua viagem custará: R$ {:.2f}'.format(float(kilometragem*0.50)))
else:
    print('A sua viagem custará: R$ {:.2f}'.format((float(kilometragem*0.45))))

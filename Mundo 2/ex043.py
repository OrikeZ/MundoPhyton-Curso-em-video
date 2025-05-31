#Desafio 43

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
altura2 = float(altura*altura)
imc = float(peso/altura2)

if imc < 18.5:
    print('Abaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')



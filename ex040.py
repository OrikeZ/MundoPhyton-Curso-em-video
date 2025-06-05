 #Desafio 40

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda note: '))
media =( nota1 + nota2) / 2

print('Sua média foi {}'.format(media))

if media < 5.0 :
    print('REPROVADO')
elif media >= 5.0 and media <= 6.9:
     print('RECUPERAÇÃO')
elif media >= 7.0:
    print('APROVADO')
else:
    print('Você digitou as notas de forma incorreta!')
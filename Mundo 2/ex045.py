import random

escolha = (int(input('PEDRA PAPEL TESOURA!: \n 1 para Pedra \n 2 para papel \n 3 para tesoura: ')))

jogo = [1,2,3]

resultado = random.choice(jogo)

if escolha == resultado:
    print('{} EMPATE'.format(escolha))
elif escolha == 1 and resultado == 2:
    print('PAPEL, você perdeu')
elif escolha == 1 and resultado == 3:
    print('tesoura, você venceu')
elif escolha == 2 and resultado == 3:
    print('TESOURA, você perdeu')
elif escolha == 2 and resultado == 1:
    print('Pedra, você venceu')
elif escolha == 3 and resultado ==1:
    print('Pedra, você perdeu!')
elif escolha == 3 and resultado == 2:
    print('Papel, você venceu')
else:
    print('Você selecionou uma opção inválida! Jogue novamente')

n = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n2 = int(input('Digite um número entre 0 e 20: '))
while True:
    if n2 >= 0 and n2 <= 20:    
        print(f'{n2} por extenso é {n[n2]}')
        break
    else:
        print('Você inseriu um número incorreto! Tente novamente.')
        n2 = int(input('Digite um número entre 0 e 20: '))
    

    

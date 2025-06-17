num = []

for c in range (0,5):
    num.append(int(input(f'Digite um valor para a Posição {c}: ')))

maior = 0
menor = 5000000
posicaomaior = []
posicaomenor = []


for inidice, valor in enumerate(num):
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
posicaomaior.append(num.index(maior))
posicaomenor.append(num.index(menor))   

posi = posicaomaior[0]
posic = posicaomenor[0] 


print("-=" *30)
      
        
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {maior} na posição {posi}')
print(f'O menor valor digitado foi {menor} na posição {posic}')

print('-='*30)
    
      
    
    

# print(f'O maior valor digitado foi {num.} nas posições {}')
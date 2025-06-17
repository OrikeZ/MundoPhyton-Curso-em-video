palavras = ('Aprender', 'Programar', 'Linguagem', 'Python', 'Lista', 'Teste')

for vogal in palavras:
    print(f'\nNa palavra {vogal} temos: ', end='')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')  
        
        
        
              
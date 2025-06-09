maiores = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M/F): ').strip().upper()
    if idade >= 18:
        maiores += 1
    elif sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = input('Deseja continuar? (S/N): ').strip().upper()
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres}')
        
    
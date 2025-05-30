#Desafio numero 005

n = int(input('Digite um numero: '))

print('O numero antecessor a {}, é {:},e seu sucessor é {:}'.format(n,n-1,n+1))

#Desafio número 006

n2 = int(input('Digite um numero: '))

print('O dobro de {}, é {}, o triplo é {}, e a raiz quadrada dele é {}'. format(n2, n2*2, n2*3, int(n2**(1/2))))

#Desafio número 007
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('A média entre as notas {}, e {}, é {}'.format(nota1, nota2, (nota1+nota2)/2))

#Desafio número 008
metragem = int(input('Digite a quantidade de metros:'))

print('A conversão de {}, em centimetros é {}cm , e em milimetros é {}mm'. format(metragem, metragem*100, metragem*1000))

#Desafio número 009
n3 = int(input('Digite um número: '))

print('A tabuada do número {} é: \n {}x1: {},{}x2: {},{}x3: {},{}x4: {},{}x5: {} \n {}x6: {},{}x7: {},{}x8: {},{}x9: {},{}x10 {}'.format(n3, n3, n3*1, n3, n3*2, n3, n3*3,n3, n3*4,n3, n3*5,n3, n3*6,n3, n3*7,n3, n3*8,n3, n3*9,n3, n3*10))

#Desafio número 010
dolar = float(input('Digite quantos reais você tem na sua carteira: '))

print('Com {} que você possui na carteira, consegue comprar {} Dólares'.format(dolar, dolar/3.27))

#Desafio numero 011

altura = float(input('digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura*largura

print('Para pintar essa parede de {}m x {}m, visto que cada 2m² vai uma lata, e sua parede tem {}m², será necessário {}l de tinta'.format(altura, largura, area, area/2))

#Desafio numero 012
preco = float(input('Digite o preço do produto: '))
print('O preço do produto era R${}, e com 5% de desconto ficará: R${}'.format(preco, preco-(preco*(5/100))))

#Desafio numero 013
salario = float(input('Digite o salário do funcionário: '))
print('O salário R${}, com aumento de 15% ficará R${}'.format(salario, salario+(salario*(15/100))))

#Desafio numero 014
temp = float(input('Digite a temperatura em Celcius:'))
print('A temperatura em F é: {}'.format((9*temp)/5+32))

#Desafio numero 015
km = float(input('Quantos kilometros você percorreu com o carro? '))
dias = int(input('Quantos dias você permaneceu com o carro? '))
pagkm = km*0.15
pagdias = dias*60

print('O valor a pagar é: R${}'.format(float(pagkm+pagdias)))




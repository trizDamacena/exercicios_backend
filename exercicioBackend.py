''''PRIMEIRO '''
print("Primeira Questão: ")
nome = 'joao'
print(nome)

''''Segundo'''
print("\nSegunda Questão: ")
a = 5
b = 10
soma = a + b
subtracao = a - b
multi = a * b
divisao = a / b

print(f' Soma: {soma}\n Subtração: {subtracao}\n Multiplicação: {multi} \n Divisão: {divisao}')

''''Terceira'''
print("\nTerceira Questão: ")
preco = 50
desc = 10
novo_preco = preco - desc

print(novo_preco)

''''Quarta'''
print("\nQuarta Questão: ")
resultado = 10 + 5 * 2
print(f'Resultado da expressão: {resultado}')

'''Quinta'''
print("\nQuinta Questão: ")
texto = "150"
texto = int(texto)
print(f'O resultado de {texto} * 2: ', texto*2)

''''Sétima'''
print("\nSétima Questão: ")
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
print('O resultado é: ',a + b)

''''Oitava'''
print("\nOitava Questão: ")
x = int(input("Digte o valor x: "))
y = int(input("Digite o valor y: "))
print('O valor da divisão inteira é: ', x // y)

''''Nona'''
print("\nNona Questão: ")
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

print('O primeiro valor é maior que o segundo: ', num1 > num2)

print('\nDécima')
idade = int(input("Digite a sua idade: "))
dias = idade * 365
print(f'Você viveu aproximadamente {dias} dias')

print('\nDécima primeira')
base = int(input('Digite o valor da base: '))
expo = int(input('Digite o valor do expoente: '))
print(f'O resultado de {base} elevado a {expo} é:', base ** expo)


print('\nDécima segunda')
preco = int(input('Digite o preço: '))
preco = str(preco)
print(f'O preço é R${preco}')

print('\nDécima terceira')
raio = float(input('Informe o valor do raio: '))
pi = 3.14
area = pi * raio ** 2
print(f'A area do circulo é: {area}')

print('\nDécima quarta')
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
a, b = b,a
print(f'O primeiro valor: {a}\nO segundo valor: {b}')


print('\nDécima quinta')
nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5))/10
print(f'A média é: {media}')

print("\nDécima sexta")
x1= int(input('Digite o valor do X1: '))
y1 = int(input('Digite o valor do Y1: '))
x2 = int(input('Digite o valor do X2: '))
y2 = int(input('Digite o valor de Y2: '))

distancia = ((x2 - x1)**2 + (y2 - y1)**2)
distancia = distancia ** 0.5
print(f' A distância entre os ponto é: {distancia:.2f}')

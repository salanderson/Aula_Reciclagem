
# # Exibir 3 strings diferentes.
# nome = input('Digite seu nome: ')
# segundonome = input('Digite o segundo nome: ')
# sobrenome = input('Digite seu sobrenome: ')

# print(f'Seu nome e {nome} {segundonome} {sobrenome}')


# Escrever um programa que exiba uma mensagem se uma variavel for menor do que 10 e outra mensagem se a variavel for maior ou igual a 10.

# numeroaleatorio = int(input('Digite um numero: '))
# if numeroaleatorio < 10:
#     print(f'O numero {numeroaleatorio} e menor do que 10 ')
# elif numeroaleatorio >= 10:
#     print(f'O numero {numeroaleatorio} e maior ou igual a 10')


# Escreva um programa que exiba um mensagem se uma variavel for menor ou igual a 10, outra mensagem se a variavel for maior do que 10, mas menor ou igual
# a 25, e ainda outra mensagem se a variavel for maior do que 25.

# numerodigitado = int(input('Digite um numero: '))
# if numerodigitado <= 10:
#     print(f'Numero digitado= {numerodigitado} e menor ou igual a 10')
# elif numerodigitado > 10 and numerodigitado <= 25:
#     print(f'Numero digitado= {numerodigitado} e maior do que 10 mais e menor ou igual a 25.')
# else:
#     print(f'O numero digitado= {numerodigitado} e maior do que 25')


# Crie um programa que divida duas variaveis e exiba o resto.
# numero1 = int(input('Digite um numero: '))
# numero2 = int(input('Digite outro numero: '))

# resto = numero1 % numero2
# print(f'Resto da divisão: {resto}')

# Crie um programa que recebe duas variaveis, as divida, e exiba o quociente.
# numero1 = int(input('Digite um numero: '))
# numero2 = int(input('Digite outro numero: '))

# resultado = numero1 / numero2
# print(f'O resultado da divisão e: {resultado}')


# Escreva um programa com uma variavel age que receba um inteiro e exiba strings diferentes dependendo de que inteiro age receber.

age = int(input('Digite sua Idade: '))


if age <= 18:
    variavel1 = 'Jovem'
    print(f'Sua idade e: {age} e voce e {variavel1}')
elif age >= 18 and age <= 50:
    variavel2 = 'Adulto'
    print(f'Sua idade e: {age} e voce e {variavel2}')
elif age > 50:
    variavel3 = 'Idoso'
    print(f'Sua idade e : {age} e voce e {variavel3}')
        




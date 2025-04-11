"""
Aula 104 
Introduçao as funçoes (def) em python
Funçoes sao trechos de codigos usados para
replicar determinada açao ao longo do seu cofigo.
Elas podem receber valores para parametros (argumentos)
e retornar um valor especifico.
Por padrão, funçoes Python retornam None (nada).

"""
# def Print(a, b, c):
#     print('Varias1')
#     print('Varias2')
#     print('Varias3')

# Print(1, 2, 3)

# def imprimir(a, b, c):
#     print(a, b, c)
# imprimir(1, 2, 3)

# def saudacao(nome='Sem nome'):
#     print(f'Ola, {nome}!')

# saudacao('Anderson')
# saudacao('teste')
# saudacao()

"""
Aula - 106
Argumentos nomeados e nao nomeados em funçoes Python
Argumentos nomeados tem nome com sinal de igual
Argumentos nao nomeados recebe apenas o argumento (valor)
"""

# def soma(x, y, z):
#     #Definicao
#     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# soma(1, 2, 3)
# soma(1, y=2, z=5)


# print(1,2,3, sep='-')

"""
Aula - 107
Valores padrao para parametros
Ao definir uma funçao, os parametros podem
ter valores padrã. Caso o valor nao seja
enviado para o parametro, o valor padrão sera usado.

"""

# def soma(x, z=None, y=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y +z)
#     else:
#         print(f'{x=} {y=}, x + y')

# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)
# soma(y=9, z=0, x=7)

""" 
Aula 108 - 109
Escopo de funçoes em python
Escopo sginifica o local.
O escopo global e o escopo onde todo o codigo e alcançavel
O escopo local e o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""
# x = 1

# def escopo():
#     global x
#     x = 10

#     def outra_funcao():
#         global x
#         x = 11
#         y =2
#         print(x, y)

#     outra_funcao()

#     print(x)

# print(x)
# escopo()
# print(x)

""" 
Aula 110
Retorno de valores das funçoes (return)

"""

# def soma(x, y):
#     return x + y

# # variavel = soma(1, 2)
# # variavel = int('1')
# soma1 =  soma(2, 2)
# soma2 =  soma(3, 3)
# print(soma1 + soma2)

"""  
args - Argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
Aula 111 - 112 - 113
"""
# Lembre-te de desempacotamento
# x,y, *resto = 1, 2, 3, 4
# print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0

    for numero in args:
        total += numero
    return total

soma_1_2_3 = soma(1, 2, 3, 4, 5 ,6)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
print(*numeros)
"""
Exercicios com funçoes

Crie uma funçao que multiplica todos os argumentos
nao nomeados recebidos
Retorne o total para uma variavel e mostre o valor da variavel

Crie uma funçao que fala se o numero e par ou impar
Retorne se o numero  e par ou impar.

Aula 113

"""
def multiplicacao(*args):
    total = 1

    for numero in args:
        total *= numero
    return total
multiplica = multiplicacao(1, 2, 3, 4)
print(multiplica)

def par_impar(numero):
    if numero % 2 == 0:
        return f'O numero é par {numero}'
    return f'O numero e impar {numero}'

print(par_impar(12))
print(par_impar(3))
print(par_impar(8))
print(par_impar(20))
print(par_impar(9))
        

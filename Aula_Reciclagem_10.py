'''
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimento reutilizaveis - indices e fatiamento
Metodos uteis: append, insert, pop, del, clear, extend, +

'''
# aula 82
#       +01234
#       -54321

string = 'ABCDE' # 5 caracteres (len)
# print(bool([])) #falsy
# print(lista, type(lista))

lista = [123, True, 'Anderson Saldanha', 1.2, []]
lista[-3] = 'Maria'
print(lista)
print(lista[2], type(lista[2]))
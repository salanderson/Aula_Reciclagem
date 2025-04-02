"""
Desempacotamento em chamadas
de metodos e funçoes
Aula 96

"""

string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3,'Eduarda']
tupla = 'Python', 'e', 'legal'

salas = [
    # 0     1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0     1       2
    ['Luiz', 'Joao', 'Eduarda',(0, 10, 20, 30, 40)], # 2

]


# a, b,*_, u= lista
# print(a, u)

print(*salas)
print(*salas, end='\n')
print('*' * 80)
print(*salas, sep='\n')
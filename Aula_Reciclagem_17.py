""" 
Lista de lista e seus indices
Aula - 94 95
"""

salas = [
    # 0     1
    ['Maria', 'Helena', ], # 0
    # 0
    ['Elaine', ], # 1
    # 0     1       2
    ['Luiz', 'Joao', 'Eduarda',(0, 10, 20, 30, 40)], # 2

]

# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(sala)
    for aluno in sala:
        print(aluno)
        
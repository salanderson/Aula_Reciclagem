""" 
enumerator - enumera iteraveis (indices)

Aula - 89
"""

#[(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'Joao')]
lista = ['Maria', 'Helena', 'Luiz', 'Joao']
lista.append('Joca')

for indice, nome in enumerate(lista):
    print(indice, nome, lista[indice])
""" 
for in com listas

"""

# Aula - 86

""" Jeito facil de numera uma lista """
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')

conta = 0

for nome in lista:
    print(conta, nome)
    conta += 1
print('*' * 50)


""" Modo correto de numera uma lista """
lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
indices = range(len(lista))

for indice in  indices:
    print(indice, lista[indice])
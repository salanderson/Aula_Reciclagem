""" 
Listas em Python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimento reutilizaveis - indeices e fatiamento
Metodos uteis:

    append - Adiciona um item ao final
    insert - Adiciona um item no indice escolhido
    pop - Remove do final ou do indice escolhido
    del - apaga um indice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    Create Read Update Delete
    Criar, ler, alterar, apagar = lista[i] (CRUD)

    Aula 83 - 85
"""

# lista_a = [1,2,3]
# lista_b = [4,5,6]
# lista_c = lista_a + lista_b

# print(lista_c)

# lista_d = lista_a.extend(lista_b)

# print(lista_d)
# print(lista_a)

lista_a = ['sheldon', 'leonard', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[3] = 'Qualquer coisa'

print(f'imprmir a lista A {lista_a}')
print('=' * 70)
print(f'imprimi a lista B {lista_b}')

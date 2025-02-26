"""
Iterando strings com while
Aula - 65
"""

nome = 'ANDERSON'

add_nome = 0
novo_nome = ''

while add_nome < len(nome):
    letra = nome[add_nome]
    novo_nome += f'*{letra}'
    add_nome += 1

novo_nome += '*'

print(novo_nome)
    

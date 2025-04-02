""" 
split e join com list e str
split - divide uma string
join - une uma string
Aula 93
"""

frase = '   Olha so que     , coisa interesante         '
lista_frases_cruas = frase.split(',')

lista_frase = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frase.append(lista_frases_cruas[i].strip())

print(lista_frases_cruas)
print(lista_frase)

frase_unidas = '-'.join(lista_frase)
print(frase_unidas)
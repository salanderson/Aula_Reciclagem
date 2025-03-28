'''
Iteravel -> str, range, etc
iterador -> quem sabe entregrar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador

'''

# for letra in texto

texto =  'Anderson'

iterador = iter(texto) # iterator

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
print('X' * 20)  
# Este metodo e mais facil de fazer um iterador
for letra in texto:
    print(letra)
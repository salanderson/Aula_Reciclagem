frase = 'contando quantas letras repetidas esta frase vai gerar'

i = 0
qtd = 0
letra_mais_repete = ''

while i < len(frase):
    iterando_frase  = frase[i]

    if letra_mais_repete == ' ':
        i+=1
        continue

    qtd_letra = frase.count(iterando_frase)


    if qtd < qtd_letra:
        qtd = qtd_letra
        letra_mais_repete = iterando_frase
    i+= 1

print(qtd, letra_mais_repete)
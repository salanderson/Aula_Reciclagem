frase = 'Iterando e contando quantas letras se repetem nesta frase'

i = 0
qtd = 0
letras_mais_repete = ''

while i < len(frase):
    frase_iteravel = frase[i]

    qtd_letra = frase.count(frase_iteravel)
    print(frase_iteravel, qtd_letra)

    if qtd < qtd_letra:
        qtd = qtd_letra
        letras_mais_repete = frase_iteravel.upper()
    i+= 1

print('A letra que mais se repete na frase e a letra 'f"{letras_mais_repete}" ' que repete ' f'{qtd}X')
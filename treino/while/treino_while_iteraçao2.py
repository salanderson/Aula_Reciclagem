frase = 'testando quantas vezes um letra se repete em' \
'uma frase e contanto usando iteração com o laço while'

i = 0 
qtd = 0
letra_maior = ''

while i < len(frase):

    iterando_frase = frase[i]

    if iterando_frase == ' ':
        i+= 1
        continue

    qtd_letra = frase.count(iterando_frase)

    if qtd < qtd_letra:
        qtd = qtd_letra
        letra_maior = iterando_frase.upper()

    i+= 1

print('A letra que mais se repetiu foi '
      f'"{letra_maior}" que repetiu {qtd}X')
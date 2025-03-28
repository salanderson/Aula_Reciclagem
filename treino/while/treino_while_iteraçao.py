frase = 'testando quantas vezes uma letra se repete em ' \
'uma frase e contanto usando iteração com o laço while e count para contar as letras.'

i = 0

qtd = 0
qtd_letras = ''

while i < len(frase):

    letras_frase = frase[i]

    if letras_frase == ' ':
        i+= 1
        continue

    letras_mais_aparece = frase.count(letras_frase)

    if qtd < letras_mais_aparece:
        qtd = letras_mais_aparece
        qtd_letras = letras_frase.upper()

    i += 1

print('A letra que mais aparece e a letra '
      f'"{qtd_letras}" que apareceu {qtd}X  na frase.\n "{frase}"')
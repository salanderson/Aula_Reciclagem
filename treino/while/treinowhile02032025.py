frase = 'estudando o laço de repitaçao while para contar as letras e mostrar qual mais se repete'

i = 0
contador_frase = 0

qtd_letra = 0
letra_mais_repte = ''

while i < len(frase):
    iterando_frase = frase[i]
    if iterando_frase == ' ':
        i+=1
        continue
    contador_frase = frase.count(iterando_frase)

    if qtd_letra < contador_frase:
        qtd_letra = contador_frase
        letra_mais_repte = iterando_frase.upper()

    i+= 1

print('A letra que mais se repetiu foi a letra 'f'"{letra_mais_repte}" repetiu {qtd_letra}X')
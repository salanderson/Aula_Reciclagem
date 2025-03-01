# estudo com while e indices
# Aula  69, 70

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua Idade: '))

# i = 0

# while i < len(nome):
#     dados_nome = nome[i]
#     print(f'{dados_nome}')

#     i+= 1

frase = 'O python é uma linguagem de programação'\
'multiparadigma. ' \
'python foi criado por guido van Rossum.'

i = 0
qtd = 0
letra_aparece_mais = ''

while i < len(frase):

    letra = frase[i]

    if letra == ' ':
        i+=1
        continue
    
    qtd_letras_aparece = frase.count(letra)

    if qtd < qtd_letras_aparece:
        qtd = qtd_letras_aparece
        letra_aparece_mais = letra
    i+=1

print('A letra que apareceu mais vezes foi '
    f'"{letra_aparece_mais}" que apareceu '
    f'{qtd}X'  
)
 
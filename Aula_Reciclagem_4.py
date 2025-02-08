# Aula 47 - 48 - Exercicio
# 

nome = input('Digite seu nome: ') 
idade = input('Digite sua idade: ')
qtd_letras = len(nome)
nomeinvertido = (nome[::-1])

if nome != '' and idade != '':

    print(f'Seu nome e {nome}')
    print(f'Seu nome invertido e {nomeinvertido}')

    if ' ' in nome:
        print(f'Seu nome e {nome} e contem espaços.')
    else:
        print('Seu nome nao contem espaços')

    print(f'Seu nome tem {qtd_letras} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
    
else:
    print('Seu nome e ou a sua idade nao foram digitados')
    


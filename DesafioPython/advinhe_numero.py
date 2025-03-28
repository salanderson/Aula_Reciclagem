'''
2 - Adivinhe o Número
O programa deve gerar um número aleatório entre 1 e 100, e o usuário deve adivinhar
o número. O jogo continua até que ele acerte. O programa deve dar dicas se o número
digitado for maior ou menor que o número correto.

'''
from random import randint

print('=' * 18)
print('Jogo de Advinhação')
print('=' * 18)

numero_aleatorio = randint(1,100)
numero_digitado = 0
tentativas = 0

while numero_digitado != numero_aleatorio:
    tentativas +=1
    numero_digitado = int(input('Digite um numero de 1 a 100: '))

    if numero_digitado < numero_aleatorio:
        print('O numero digitado e menor, tente outra vez')
    elif numero_digitado > numero_aleatorio:
        print('O numero digitado e maior, tente outra vez')
    elif numero_digitado == numero_aleatorio:
        print('Parabens!! Voce acertou o numero secreto..'f'{numero_aleatorio}')


    



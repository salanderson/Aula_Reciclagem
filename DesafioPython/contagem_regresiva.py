'''
6. Contagem Regressiva
Solicite um número ao usuário e faça uma contagem regressiva até zero. 

'''

numero = int(input('Digite um numero para contagem regresiva:'))

contagem = 0

while  numero > contagem:
    numero -= 1
    print(f'Contagem regressiva {numero}')
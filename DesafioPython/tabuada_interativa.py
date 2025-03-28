'''
9 - Tabuada Interativa
Peça ao usuário para inserir um número e exiba a tabuada desse número de 1 a 10. O programa só deve parar se o usuário digitar 0. - 

'''

numero = int(input('Digite um numero ou 0 para sair: '))
cont = 0
print('Tabuada Iterativa')

while cont <= 10:

    if numero == 0:
        
        break
    
    resultado = numero * cont
    print(f'{numero} * {cont} = {resultado}')

    cont += 1

    

    


"""
8 - Números Pares
Peça um número ao usuário e exiba todos os números pares de 0 até esse número usando while. 

"""

numero = int(input('Digite um numero: '))

contador = 0

print(f'Aqui estão todos os numeros pares que estão entre 0 e {numero}')

while contador < numero:

    contador += 1
    
    if contador % 2 == 0:
        resultado = contador
        # print(f'Aqui estão todos os numeros pares que estão entre 0 e {numero}, numeros pares = {contador}')

        print(f'Numeros pares = {contador}')
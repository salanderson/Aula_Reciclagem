"""
Peça ao usuário para inserir números inteiros. 
Some os números positivos e pare quando
o usuário digitar um número negativo. 
Exiba a soma total no final.

"""

print('Digite numeros positivos para continua somando e 1 numero negativo para a soma')
numero = 0

while numero >= 0:
    numero = int(input('Digite: '))

    soma = numero + numero
    print(soma)
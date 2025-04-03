import random

# Neste bloco acima gera o corpo de 9 numeros do CPF, EX: 032.234.098 de forma aleatoria usando Random

contador = 0
corpo = ''

while contador < 9:
    contador += 1
    numeros = random.randint(0, 9)
    for i in str(numeros):
        corpo += i
    
        corpo_cpf = corpo

# Neste bloco gera o primeiro digito verificador

contador_cpf = 11
digito_1 = 0
num_gerador = 0

for num in corpo_cpf:
    contador_cpf -= 1
    num_gerador += int(num) * contador_cpf * 10
    num_modelo = num_gerador % 11

    if num_modelo > 9:
        digito_1 == 0
    else:
        digito_1 = num_modelo

print(f'primeiro digito verificador gerado: {digito_1}')

# Neste bloco gera o segundo digito veirficador e concatena os 9 digitos com o primeiro e o segundo

corpo_cpf_dig1 = corpo_cpf + str(digito_1)
contador_cpf_2 = 10
digito_2 = 0
num_gerador_dig_2 = 0

for num2 in corpo_cpf_dig1:
    contador_cpf_2 -= 1
    num_gerador_dig_2 += int(num2) * contador_cpf_2 * 10
    num_modelo_dig_2 = num_gerador_dig_2 % 11

    if num_modelo_dig_2 > 9:
        digito_2 == 0
    else:
        digito_2 = num_modelo_dig_2
print(f'segundo digito verificador gerado: {digito_2}')

cpf_gerado = corpo_cpf_dig1 + str(digito_2)

print(f'O CPF: {cpf_gerado} foi gerado com sucesso!')




    



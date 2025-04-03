"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
    7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado e 0
contrario disso:
    resultado e o valor da conta

O primeiro digito do CPF é 7

Aula - 98 - 103
"""

cpf = input('Digite o cpf: ')

nove_digitos = cpf[:9]
contador = 10
calculo_digito = 0
p_digito = 0

for digito in nove_digitos:
    calculo_digito += int(digito) * contador * 10
    contador -= 1


    calculo_mod1 = calculo_digito % 11

    if calculo_digito % 11 > 9:
        p_digito = 0
    else:
        p_digito = calculo_digito % 11


dez_digito = cpf[:10]
contador_final = 11
calculo_digito_final = 0
u_digito = 0   

for digito_final in dez_digito:
    calculo_digito_final += int(digito_final) * contador_final * 10
    contador_final -= 1 

    if calculo_digito_final % 11 > 9:
        u_digito = 0
    else:
        u_digito = calculo_digito_final % 11

# print(u_digito)
cpf_validado = nove_digitos + str(p_digito) + str(u_digito)

if cpf == cpf_validado:
    print(f'O cpf {cpf} e valido')
else:
    print(f'CPF: {cpf} informado e invalido!')



        
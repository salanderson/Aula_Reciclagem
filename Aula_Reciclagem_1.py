# Aula 22
# type convertion, typecasting, coercion e o ato de converter um tipo em outro
# tipos imutaveis e primitivos:
# str, int, float, bool

# print('1', type('1')) -> type('1') mostra o tipo da variavel ou do valor

# print(int('1'), type(int('1'))) - int('1') convertendo um valor str para int 

# print(float('1') + 1) -> converte o str para ponto flutuante(float)
# print(type(float('1') + 1)

# print(bool(''))-> quando nao existe um valor o resultado e falso
# print(bool(' '))-> se existir um valor a operação passa a ser verdadeira

# print(11 + 'b')-> o python nao entende uma soma de int mais uma str
# print(str('11') + 'b')-> nao e possivel somar str o python entende que e para juntar os dois
# valores e concatena

# Aula 31 -> formatar strings usando f'exemplo de {formataçao}, 
# formatação de numeros com ponto flutuantes {formataçao:.2f}'

#  exercicio aula 24 com o exercicio da aula 29 - Calculadora de IMC
nome = input('Digite seu Nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = int(input('Digite o ano de nascimento: '))
maior_de_idade = idade >= 18
altura_metros = float(input('Digite sua altura(Ex: 1.30): '))
peso = float(input('Digite seu peso(Ex: 70.6): '))
altura_ao_quadrado = altura_metros * altura_metros
imc = peso / altura_ao_quadrado
print('-' * 40)
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('E maior de idade?:', maior_de_idade)
print('Altura em metros:', altura_metros)
print('seu IMC e de: ', imc)

if imc <= 16:
    print('Magreza Grave')
elif imc >= 16 and imc <= 16.9:
    print('Status: magreza moderada')
elif imc >= 18.6 and imc <= 24.9:
    print('Status: Peso Ideal') 
elif imc >= 25 and imc <= 29.9:
    print('Status: Sobrepeso')
elif imc >= 30 and imc <= 34.9:
    print('Status: Obesidade grau I')
elif imc >= 35 and imc <= 39.9:
    print('Status: Obesidade grau II ou severa')
else:
    print('Status: Obesidade grau III ou morbida')

print('-' * 40)
print('-' * 40)
print('Relatorio Final')
print('-' * 40)
print('-' * 40)

dados_finais_nome = f'{nome} {sobrenome} sua idade e {idade} anos'
dados_finais_idade = f'voce nasceu em {ano_nascimento} é Maior de Idade: {maior_de_idade}'
dados_finais_alt_peso = f'sua altura é {altura_metros} e seu IMC {imc:.2f}'

print(dados_finais_nome, dados_finais_idade, dados_finais_alt_peso)





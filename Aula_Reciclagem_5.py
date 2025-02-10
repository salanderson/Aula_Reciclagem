# Introdução ao try/except
# try -> tentar executar o codigo
# except -> ocorreu algum erro ao tentar executar

# Aula - 49

numero_str = input('Digite o numero a ser dobrado: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} e {numero_float * 2:.2f}')
except:
    print('Isso nao e um numero')
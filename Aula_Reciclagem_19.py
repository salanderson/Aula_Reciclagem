""" 
Operação ternaria (condicional de uma linha)
<valor> if <condicao> else <outro valor>
Aula 97
"""

condicao = 10 == 10
variavel = 'valor' if condicao else 'outro valor'
print(variavel)

digito = 9 # > 9 = 0
novo_digito = digito if digito <= 9 else 0
print(novo_digito)
novo_digito = 0 if digito > 9 else digito
print(novo_digito)

print('valor' if False else 'outro valor' if True else 'fim')
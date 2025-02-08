# Formatação de Strings Aulas 32 - 34 

# a = 'A'
# b = 'B'
# c = 1.1

# string = 'a={} b={} c={}'
# formato = string.format(a, b, c)

# print(formato)


# if / elif      / else
# se / se nao se / se nao

# entrada = input('Voce quer "entrar" ou "sair"? ')

# if entrada == 'entrar':
#     print('Voce entrou no sistema')
# elif entrada == 'sair':
#     print('Voce saiu do sistema')
# else:
#     print('Opçao invalida digite entrar ou sair do sistema.')

nome = 'Anderson'
preco = 1000.95897643
variavel = '%s, o preço e R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d e %08X' % (1500, 1500))

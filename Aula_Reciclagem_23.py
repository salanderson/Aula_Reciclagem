"""
Higher Order Functions
Funçoes de primeira classe
Aula 114 - 115
"""

# def saudacao(msg, nome):
#     return f'{msg}, {nome}!'

# def executa(funcao, *args):
#     return funcao(*args)

# print(executa(saudacao, 'Bom dia', 'Anderson'))

# print(executa(saudacao, 'Boa noite', 'Maria'))

""" 
 Closure e funçoes que retornam outras funçoes

 Aula 116

"""
# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar

# falar_bom_dia = criar_saudacao('Bom dia')
# falar_boa_noite = criar_saudacao('Boa noite')

# for nome in ['Maria', 'Joao', 'Luiz']:
#     print(falar_bom_dia(nome))
#     print(falar_boa_noite(nome))

"""  
Aula 117 - 118 - Exercicios
Crie funçoes que duplicam, triplicam e quadriplicam
o numero recebido como parametro.

"""
def criar_funcao(multiplica):
    def multiplicador(numero):
        return numero * multiplica
    return multiplicador

duplicar = criar_funcao(2)
triplicar = criar_funcao(3)
quadriplicar = criar_funcao(4)

print(duplicar(2))
print(triplicar(2))
print(quadriplicar(2))
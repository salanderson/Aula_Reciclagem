""" 
Faça uma lista de compra com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de indices inexitentes na lista

Aula - 90 - 91

"""
import os


lista_compras = []

while True:

    print('[i]inserir [a]apagar [l]listar')
    opcao = input('Selecione a opção: ')

    if opcao == 'i':
        os.system('cls')
        descricao = input('Digite a descriçao: ')
    
        lista_compras.append(descricao)
        

    elif opcao == 'a':
        apagar_valor = input('Digite o valor: ')

        try:
            indice = int(apagar_valor)
            del lista_compras[indice]
        except IndexError:
            print('Nao existe este indice na lista')
        except ValueError:
            print('Digite apenas o numero do indice que deseja apagar')
    
    elif opcao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Nao a nada para listar')

        for i, descricao in enumerate(lista_compras):
            
            print(i, descricao)
    
    else:
        print('Opcao invalida')
        continue

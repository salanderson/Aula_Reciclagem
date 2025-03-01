'''
Crie um programa que exibe um menu com opções
(exemplo: 1 - Dizer "Olá", 2 - Exibir a data atual, 3 - Sair). 
O programa só encerra quando o usuário escolher a opção de sair. 
'''

from datetime import datetime

print('Menu Iterativo \n Digite: \n 1- Saudação \n 2- Data atual \n 3- Sair')

opcao = int(input('Selecione a opçao:'))
data_atual = datetime.now()

while opcao < 4:
    
    if opcao == 1:
        print('Ola')
        break
    elif opcao == 2:
        print(data_atual)
        break
    elif opcao == 3:
        print('Finalizado')
        break
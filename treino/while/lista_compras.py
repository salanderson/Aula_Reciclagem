import os

lista_compras = []


while True:

    print('Digite [i]inserir [a]apagar [l]listar')
    opcao = input('Digita a opçao: ')

    if opcao == 'i':
        os.system('cls')
        descricao = input('Digite o nome: ')
        lista_compras.append(descricao)

    elif opcao == 'a':
       os.system('cls')
       apagar_dados = input('digite o indice para apagar: ')

       try:
        indice = int(apagar_dados)
        del lista_compras[indice]
       except ValueError:
           print('Digite apenas numeros')
       except IndexError:
           print('Nao existe este indice para apa')

    elif opcao == 'l':
        
        if len(lista_compras) == 0:
            print('Nao existe dados para imprimir')

        for i, descricao in enumerate(lista_compras):
            print(i, descricao)

    else:
        print('Opçao invalida')
    
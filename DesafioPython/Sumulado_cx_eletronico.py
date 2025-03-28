'''
10. Simulação de Caixa Eletrônico
Peça um valor de saque ao usuário e exiba quantas notas de R$50, R$20, R$10 e R$5 serão entregues. O programa deve continuar pedindo valores até que o usuário digite 0.

'''



print('Digite 0 para sair')

cedulas = 0
valor_sacado = 0

while True:
    saque = int(input('Digite o valor para saque: '))

    if saque == 0:
        print('Sistema Finalizado')
        break

    if saque % 5 != 0:
        print('Nao exite notas menores que 5') 
        saque = int(input('Digite o valor para saque: '))
        continue


    valor_50 = saque // 50
    saque %= 50

    valor_20 = saque // 20
    saque %= 20

    valor_10 = saque // 10
    saque %= 10

    valor_5  = saque // 5
    saque %= 5

    
    print('Notas entregues')

    if valor_50 > 0:
        print(f'Foi entregue {valor_50} notas de R$50')
    
    if valor_20 > 0:
        print(f'Foi entregue {valor_20} notas de R$20')
    
    if valor_10 > 0:
        print(f'Foi entregue {valor_10} notas de R$10')
    
    if valor_5 > 0:
        print(f'Foi entregue {valor_5} notas de R$5')

    cedulas = valor_50 + valor_20 + valor_10 +valor_5
    valor_sacado = 50 * valor_50 + 20 * valor_20 + 10 * valor_10 + 5 * valor_5
    print(f'Total de cedulas entregue = {cedulas} total do saque = {float(valor_sacado):.2f}')

    
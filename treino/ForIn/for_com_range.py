for i in range(10):

    if i == 3:
        print('pulando para o proximo')
        continue
    for j in range(1, 3):
        print(i, j)

    if i == 8:
        print('nao vai chegar ao Else')

else:
    print('Finalizando com Else')
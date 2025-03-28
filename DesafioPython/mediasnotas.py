''''
'7 - Média de Notas
Peça notas ao usuário até que ele digite um número negativo. Depois, exiba a média das notas digitadas.'

'''

soma = 0
qtd = 0

print('Para sair do sistema digite 0')
while True:
   nota = float(input('Digite uma nota: '))
   
   if nota == 0:
      break
   soma += nota
   qtd += 1


media = soma / qtd
print('Sua nota final foi: 'f'{media:.2f}')

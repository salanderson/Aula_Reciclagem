'''
Peça para o usuário digitar uma senha e continue 
pedindo até que ele digite a senha correta.
'''

login = 'Admin'
senha = '102030'

senha_digitada = '0'

while senha_digitada != senha:
    senha_digitada = input('Digite a senha: ')

    if senha_digitada != senha:
         print('Senha incorreta, digite novamente')
    
    if senha_digitada == senha:
        print('Bem Vindo' f'{login}')
        break

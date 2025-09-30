#questao 2 de estrutura de repetição

user = input('digite seu nome: ')
pswd = input('digite sua senha: ')

while pswd == user:
    print('erro: nome e usuarios iguais')
    pswd = input('digite sua senha: ')

print(f'\n User: {user}\n Password: {pswd}\n\n registrado')
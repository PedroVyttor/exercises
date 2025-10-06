#desenvolva um algoritmo em python que receba o username, email e a senha
#cadastrada pelo usuario. o programa deve pedir para repetir
#o email, caso não contenha "@".

#o  programa deve pedir para repetir a senha se:
#a quantidade de caracteres for menor que oito.

user = input('digite seu nome de usuario: ')

login = input('Digite seu email: ') .lower()

while '@gmail.com' not in login:
    login= input('Coloque o @ corretamente: ') .lower()

senha = input('Digite sua senha: ')
while len(senha) < 8:
    senha = input('digite sua senha novamente') .lower()

print(f' User: {user}\n Email: {login}\n Password: {senha}\n \n Conta registrada com sucesso')


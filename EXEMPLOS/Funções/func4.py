import random

def validarEmail(email):
    if '@' not in email:
        print('Tá faltando o @ ai')
        return False

    if 'gmail' not in email:
        print('Ta faltando o gmail')
        return False

    if '.com' not in email:
        print('Ta faltando o .com')
        return False

email = input('Digite seu email: ')
validarEmail(email)

print(validarEmail(email))
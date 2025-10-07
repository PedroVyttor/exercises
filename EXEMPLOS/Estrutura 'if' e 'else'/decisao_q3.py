#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M -
#Masculino, Sexo Inválido.

sexo = input('digite seu sexo (f ou m): ') .lower()

if sexo == 'f':
    print('sexo feminino')

if sexo == 'm':
    print('sexo masculino')
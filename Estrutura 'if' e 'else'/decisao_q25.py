#25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?"
#
# O programa deve no final emitir uma classificação sobre a 7
# participação da pessoa no
#crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4
#como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

p1 = input('telefonou para a vitima? ')
p2 = input('esteve no local do crime?')
p3 = input('mora perto da vitima? ')
p4 = input('devia para a vitima? ')
p5 = input('ja trabalhou com a vitima? ')
qtde = 0

#PERGUNTAS
if p1 == 'sim':
    qtde = qtde + 1
if p2 == 'sim':
    qtde = qtde + 1
if p3 == 'sim':
    qtde = qtde + 1
if p4 == 'sim':
    qtde = qtde + 1
if p5 == 'sim':
    qtde = qtde + 1

#CLASSIFICACAO
if qtde == 2:
    print('suspeito')
elif qtde == 3 or qtde == 4:
    print('cumplice')
elif qtde > 4:
    print('assassino')

else:
    print('ofende ninguem')
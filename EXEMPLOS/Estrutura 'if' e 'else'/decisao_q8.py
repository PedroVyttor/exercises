#Faça um programa que pergunte o preço de três produtos e informe qual
# produto você deve comprar, sabendo que a
#decisão é sempre pelo mais barato.

print('produto 1: Copo de Vidro')
vidro = 20

print('produto 2: Copo de Alumínio')
aluminio = 16

print('produto 3: Copo de Plastico')
plastico = 9

quest = input('deseja saber o valor dos tres copos? ' ) .lower()
if quest ==  'sim' or quest == 'desejo' or quest == 'claro' or quest == 's' or quest == 'positivo' or quest == 'ss' or quest == ' sim' or quest == 'si':
    print('copo de plastico -> R$9,00\n')
    print('copo de aluminio -> R$16,00\n')
    print('copo de vidro -> R$20,00\n')
    quest2 = int(input('posso ajudar em algo mais? \n' + '1. Qual produto devo comprar? (mais barato) \n' + ' 2. Sair\n'))
    if quest2 == 1:
        print('recomendo o copo de plastico -> R$9,00')
        quest3 = int(input('posso ajudar com algo mais? \n' + '2. Sair\n' ))
        if quest3 == 2:
            print('tenha um bom dia.')

    if quest2 == 2:
       print('tenha um bom dia.')
       quit()

if quest == 'nao' or quest == 'não' or quest == 'n' or quest == 'negativo' or quest == 'nop' or quest == 'nam':
    print('tá bom.')


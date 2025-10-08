#Faça um programa com python que leia um nome do cantor/cantora que tocou em cada um dos 15
# dias de festas em carrapateira.
# Se o cantor/cantora se chamar Adryan, encerre o código e diga que essa noite foi pancada

for noite in range (15):
    nome = input('informe o nome do cantor ou cantora: ')
    if nome.lower() == 'adryan':
        print('Esse cantor é pancada''')
        break

    print('Foi tranquilo.')
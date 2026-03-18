temp = float(input('Digite a temperatura atual: '))
umid = float(input('Digite o umido: '))

if temp >= 30 and umid <= 70:
    print('Clima agradavel')

else:
    print('Clima desagradavel')
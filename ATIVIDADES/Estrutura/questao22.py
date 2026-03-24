idaus = int(input('Digite sua idade:'))

if idaus < 5:
    print('entrada gratuita')
elif idaus >=5 and idaus <= 12:
    print('valor do ingresso: R$10,00')

elif idaus >=13 and idaus <= 59:
    print('valor do ingresso: R$ 20,00')

elif idaus >= 60:
    print('valor do ingresso: R$ 15,00')
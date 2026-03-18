pag = input('digite a forma de pagamento (pix ou dinheiro): ').lower()

if pag == 'pix' or pag == 'dinheiro':
    print('forma aceita')

else:
    print(f'forma não aceita: {pag}')
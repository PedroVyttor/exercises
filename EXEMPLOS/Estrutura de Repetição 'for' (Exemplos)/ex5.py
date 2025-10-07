#detectar numero primo

qtde = 0

num = int(input('digite um numero:'))

for i in range (1, num + 1):
    if num % i == 0:
        qtde += 1

if qtde == 2:
    print('e numero primo')
else:
    print('nao e numero primo')
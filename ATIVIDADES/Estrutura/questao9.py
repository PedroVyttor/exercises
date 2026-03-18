valor = (int(input('Digite um valor: ')))
if valor >= 100:
    centenas = valor // 100
    valor = valor - (centenas * 100)
    print(centenas, 'nota(s) de 100')
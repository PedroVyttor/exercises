numero = 0
temndivisivel = "N"
while numero >= 0:
    numero = int(input('Digite um numero: '))
    if numero % 10 == 0:
        temndivisivel = "S"

if temndivisivel == "S":
    print('Existe multiplo de 10 nesse conjunto')
else:
    print('Não existe multiplo de 10 nesse conjunto')
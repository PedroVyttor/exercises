#mostre todos os numeros primos que o usuario definir (entre valor 1 e valor 2)

val = int(input('digite um numero: '))
val2 = int(input('digite outro numero: '))

for num in range (val, val2):
    qtde = 0

    for i in range(1, num + 1):
        if num % i == 0:
            qtde += 1

    if qtde == 2:
        print(num)
print(f'\nTodos estes valores entre {val} e {val2} são numeros primos.')
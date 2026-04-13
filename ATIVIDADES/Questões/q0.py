#criar uma calculadora - crie uma calculadora usando while e break
#operações: somar, subtrair, dividir, e multiplicar

while True:
    print('-----calculadora lá-----'
        '\n1- Somar'
        '\n2- Subtrair'
        '\n3- Multiplicar'
        '\n4- Dividir'
        '\n5- Raiz quadrada'
        '\n0- Sair')

    num = int(input('Selecione as opções: '))
    if num == 1:
        soma = float(input('Digite um valor: '))
        soma2 = float(input('Digite outro valor: '))

        resultado = soma + soma2
        print(f'O resultado é: {resultado}')

    elif num == 2:
        sub = float(input('Digite um valor: '))
        sub2 = float(input('Digite outro valor: '))

        resultado = sub - sub2
        print(f'O resultado é: {resultado}')

    elif num == 3:
        mult = float(input('Digite um valor: '))
        mult2 = float(input('Digite outro valor: '))

        resultado = mult * mult2
        print(f'O resultado é: {resultado}')

    elif num == 4:
        divi = float(input('Digite um valor: '))
        divi2 = float(input('Digite outro valor: '))

        resultado = divi / divi2
        print(f'o resultado é: {resultado}')

    elif num == 5:
        raiz = int(input('Digite o valor: '))

        resultado = raiz ** 2
        print(f'O resultado é: {resultado}')

    elif num == 0:
        break
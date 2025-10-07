#Menu de seleções:
# Calcular IMC,
# verificar pressão arterial
# e checar nome (1, 2 e 3).

op = 99

while op != 0:
    print('-------MENU-------')                                 #Menu
    print('1 - Calcular o IMC')
    print('2 - Verificar pressão arterial')
    print('3 - Checar nome')
    print('0 - Sair \n')

    op = int(input('Digite a opcao desejada: '
                   ''))

    if op == 1:                                                 #Opção 1
        peso = float(input('Digite seu peso: '))
        altura = float(input('Digite sua altura: \n'))

        imc = peso / altura ** 2
        print(f'Seu IMC é: {imc} \n')

    elif op == 2:                                               #Opção 2
        pmax = int(input('Digite a pressao maxima:  '))
        pmin = int(input('Digite a pressao minima: '))
        if pmax >= 8 and pmax <= 11 and pmin >= 6 and pmin <= 8:
            print('Voce está bem \n')
        else:
            print('Chame o SAMU')

    elif op == 3:                                               #Opção 3
        nome = input('Digite seu nome: ').lower()
        if nome == 'jacinto':
            print('\n Voce e o desmantelo em pessoa')
        else:
            print('Ai ta tudo bem, meu filho é um prefeito')

    elif op == 0:
        print('SISTEMA ENCERRADO')

    else:
        print('Opção invalida')
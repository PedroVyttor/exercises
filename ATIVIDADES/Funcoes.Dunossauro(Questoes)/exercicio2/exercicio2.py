#Faça um programa para imprimir:
#1
#1   2
#1   2   3
#.....
#1   2   3   4  ...  n

#Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.

def imprimirEnesimo(n):
    if n  <= 0:
        print('0')
    contador = 1

    while n >= 0:
        qtd = 1
        text = ''

        while qtd < contador:
            text += str(qtd) + ' '
            qtd += 1

        print(text)
        contador += 1
        n -= 1

imprimirEnesimo(10)
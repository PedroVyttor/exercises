#Faça um programa para imprimir:
#1
#2   2
#3   3   3
#.....
#n   n   n   n   n   n  ... n

#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def imprimirEnesimo(n):
    if n  <= 0:
        print('0')
    contador = 1

    while n > 0:
        qtd = contador
        text = ''

        while qtd > 0:
            text += str(contador) + ' '
            qtd -= 1

        print(text)
        contador += 1
        n -= 1

imprimirEnesimo(200)



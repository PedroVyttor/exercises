#questao 1 de estrutura de repetição
#Faca um programa que peça uma nota, entre zero e dez.
#Mostre uma mensagem caso o valor seja
# inválido e continue
#pedindo até que o usuario informe um valor válido.

n1 = int(input('digite uma nota entre zero e dez: '))
while n1 not in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print('bolas')
    n1 = int(input('digite uma nota entre zero e dez: '))
else:
    print('NUMERO')
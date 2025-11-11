#questao 4 da lista de estrutura de repetição
#ss 1.2%
#cz 1.5%

#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
#entrada e permita repetir a operação.

popcz = int(input('qual e a popul. inicial'))
popss = int(input('qual e a popul. inicial'))
qtdeanos = 0
txcz = float(input('taxa de cz: '))
txss = float(input('taca de ss: '))

while popcz < popss:
    popcz = popcz + (popcz * txcz)
    popss = popss + (popss * txss)
    qtdeanos += 1

print(f'em anos, demorou {qtdeanos}')
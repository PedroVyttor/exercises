#questao 4 da lista de estrutura de repetição
#ss 1.2%
#cz 1.5%
#sousa
#cajazeiras

popcz = 70000
popss = 80000
qtdeanos = 0

while popcz < popss:
    popcz = popcz + (popcz * 0.015)
    popss = popss + (popss * 0.012)
    qtdeanos += 1

print(f'em anos, demorou {qtdeanos}')
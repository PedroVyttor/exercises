#questao 15

n = int(input('digite qual termo da sequencia: '))

ant = 0
atu = 1

for i in range (n):
    prox = ant + atu
    ant = atu
    atu = prox

    print(prox)
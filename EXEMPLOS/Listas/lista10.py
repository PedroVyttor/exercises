megasena = []

while len(megasena) < 6:
    num = int(input('Digite um numero entre 1 e 60: '))
    megasena.append(num)
    while num in megasena:
        num = int(input('Digite outro numero entre 1 e 60: '))
    if len (megasena) == 6:
        break
print(megasena)
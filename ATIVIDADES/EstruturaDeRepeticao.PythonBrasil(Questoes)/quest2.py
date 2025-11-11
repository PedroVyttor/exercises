total = int(input('Diga o total de eleitores: '))

contador = 0
v1 = 0
v2 = 0
v3 = 0

while contador < total:
    voto = int(input('qual seu voto? 1, 2 '))
    if voto == 1:
        v1 += 1
    if voto == 2:
        v2 += 1
    if voto == 3:
        v3 += 1
    contador += 1

print(f'v1 {v1}')
print(f'v2 {v2}')
print(f'v3 {v3}')
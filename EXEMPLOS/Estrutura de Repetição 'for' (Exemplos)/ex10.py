#peça ao usuario um numero de voltas que um carro percorre em uma pista.
#Para cada volta, pergunte ao usuario quanto tempo ele gastou na volta
#imprima o menor tempo digitado...

volt = int(input('numero de voltas: '))
menor = float(input('tempo da volta: '))

for i in range(volt - 1):
    temp = float(input('tempo da volta: '))
    if temp < menor:
        menor = temp

print(f'Voltas: {volt}')
print(f'Menor tempo: {menor}')
#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))
n3 = int(input('digite mais um numero: '))

maior = n1

if n2  > maior:
    maior = n2
if n3 > maior:
    maior = n3

print(f'O maior número e: {maior}')
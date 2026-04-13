#faça um algoritmo que peça 10 numeros ao usuario e faça o somatório e a média
#usando 'for'

soma = 0

for i in range(10):
    num = int(input('Digite um numero: '))
    soma += num

print(f'Soma: {soma}')
print(f'Media: {soma/10}')
#Desenvolva um algoritmo que calcule a média aritmética
# de quatro números. Os números deverão ser fornecidos pelo
#desenvolvedor (você) e o algoritmo deverá exibir a média
#como resultado.

print('Digite as quatro notas: ')

n1 = int(input('Digite a nota 1: '))
n2 = int(input('Digite a nota 2: '))
n3 = int(input('Digite a nota 3: '))
n4 = int(input('Digite a nota 4: '))

media = (n1 + n2 + n3 + n4) / 4

print(f'A media final é: {media}')
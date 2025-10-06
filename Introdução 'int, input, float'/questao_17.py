#Determine a, b e c na fórmula de Bhaskara

a = float(input('Digite um numero (a): '))
b = float(input('Digite um numero (b): '))
c = float(input('Digite um numero (c): '))

delta = b ** 2 - 4 * a * c

x1 = (-b + delta ** (1/2)) / (2 * a)
x2 = (-b - delta ** (1/2)) / (2 * a)

print(f'O valor de x1 e: {x1}')
print(f'O valor de x2 e: {x2}')

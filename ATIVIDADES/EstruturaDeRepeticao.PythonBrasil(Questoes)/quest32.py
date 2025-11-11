#faça um programa que calcule o fatorial de um numero inteiro fornecido pelo usuario. Ex: *** *** ***
#ser conforme o exemplo abaixo:  "com FOR"
#Fatorial  de: 5
#5! = 5 . 4. 3 . 2 . 1 = 120

num = int(input('digite um numero: '))
fat = 1

print(f'{num}! = ', end = '')
for i in range (num, 1, -1):
    fat *= i
    print(f'{i} . ', end = '')

print(f'1 = {fat}')

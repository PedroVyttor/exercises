#Faça um algoritmo que o desenvolvedor coloque os
# valores de altura e peso para o programa calcular
# o IMC = Índice de Massa Corporal

p1 = int(input('Peso: '))
p2 = int(input('Altura: '))

imc = p1 / ( p2 **2 )

print(f'O resultado é:  {imc }')
#Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
# informar se os valores podem ser um
#triângulo. Indique, caso os lados formem um triângulo,
# se o mesmo é: equilátero, isósceles ou escaleno.

#Dicas:
#Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes;


#tirângulo (equilatero, isosceles ou escaleno)
lad1 = float(input('Digite o valor de lado1: '))
lad2 = float(input('Digite o valor de lado2: '))
lad3 = float(input('Digite o valor de lado3: '))

if lad1 + lad2 > lad3 and lad1 + lad3 > lad2 and lad2 + lad3 > lad1:
    #equilatero
    if lad1 == lad2 and lad3 == lad1:
        print('Triângulo Equilátero')

    #isosceles
    elif lad1 == lad2 or lad3 == lad1:
        print('triangulo isosceles')

    #escaleno
    elif lad1 != lad2 and lad3 != lad1 and lad2 != lad3:
        print('triangulo escaleno')

    else:
        print('Não existe')

else:
    print('não existe')
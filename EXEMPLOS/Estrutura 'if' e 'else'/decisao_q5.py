#Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por
#aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.


print('Digite suas notas abaixo')
n1 = float(input('nota 1: '))
n2 = float(input('nota 2: '))
n3 = float(input('nota 3: '))
n4 = float(input('nota 4: '))

media =  (n1 + n2 + n3 + n4) / 4

if media == 10:
    print('aprovado com distincao')

elif media >= 7:
    print('aprovado')

else:
    print('reprovado')
#Faça um programa que leia duas notas dos alunos do p1 (40 alunos).
#O programa deve ler o nome de cada aluno também. Ao Final, informe
#a média e o nome do aluno com a maior nota.

print('---- NOTA ----')

nome_maior = ''
maior_media = 0
soma = 0

for aluno in range (4):
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    nome = input('Digite seu nome: ')
    media = (n1 + n2) / 2

    if media > maior_media:
        maior_media = media
        nome_maior = nome

    soma += media

media_turma = soma / 40
print(f' a maior media da turma é de {nome_maior}.\n Nome: {nome_maior} \n Media: {media_turma}')
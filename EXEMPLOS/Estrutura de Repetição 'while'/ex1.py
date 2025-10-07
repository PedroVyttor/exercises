#estrutura de repetição (quantidade de alunos que possuem mais
#de 19 anos e a média da quantidade dos mesmos)

soma = 0
qtde = 0
idade = int(input('digite sua idade: '))
pos18 = 0

while idade >0:
    qtde += 1
    soma = soma + idade
    if idade > 18:
        pos18 += 1
    idade = int(input('digite sua idade: '))

if qtde > 0:
    media =  soma / qtde
    print(f'a media de idade dos alunos e {media}')
    print(pos18 , 'foi a quantidade de alunos com mais de 18 anos')
else:
    print('nenhuma idade calida foi digitada')
print('---frequencia---')
nome = input('digite o nome do aluno: ')

#abrindo o arquivo em modo leitura
meu_arquivo = open('C:\\Users\\kidca\\Downloads\\arquivo.txt')
qtde = 0

#lendo as linhas do arquivo
linhas = meu_arquivo.readlines()

for linha in linhas:
    if nome in linha:
        qtde += 1

#fechando o arquivo
meu_arquivo.close()

print(f'O aluno {nome} estava presente {qtde} vezes.')
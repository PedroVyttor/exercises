#arquivo

#criar um arquivo
#escrita = 'w' se tiver criado, ele sobrescreve tudo
#append = 'a'
#leitura = 'r'

arquivo = open('professores.txt', 'r')

linhas = arquivo.readlines()
arquivo.close()
for linha in linhas:
    texto = linha.replace('\n', '')
    if len(texto) > 0:
        print(texto)

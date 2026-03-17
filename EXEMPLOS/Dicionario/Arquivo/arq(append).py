#arquivo

#criar um arquivo
#escrita = 'w' se tiver criado, ele sobrescreve tudo
#append = 'a'
#leitura = 'r'

arquivo = open('professores.txt', 'a')
for i in range(1):
    texto = input('Digite o nome do professor: ')
    arquivo.write(texto)
    arquivo.write('\n' + texto)
arquivo.close()

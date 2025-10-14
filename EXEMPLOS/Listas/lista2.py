#lista

nomes = []

#append adiciona ao final da lista
nomes.append('Maria')
nomes.append('Pedro')

#usuario adiciona na lista
for i in range(3):
    nome = input('Digite um nome:')
    nomes.append(nome)

print(nomes)
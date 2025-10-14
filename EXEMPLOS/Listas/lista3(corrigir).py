#construa um programa em python que possua um menu om 3 poções:
#1-cadastrar produtp
#2-listar todos os produtos
#0-Sair

op = 123
lista = ['Meia', 'Boia', 'Blusa', 'PlayStation 7 Ultra Pro 16K 200FPS']

print('=====MENU=====')
print(' 1 - Cadastrar Produto\n 2 - Listar todos os produtos\n 3 - Remover produto  da lista\n 4 - Buscar produto\n 0 - Sair')

select = int(input('Selecione: '))

if select == 1:
    nome = input('Digite o nome do produto:')
    lista.append(nome)

elif select == 2:
    for i in range(len(lista)):
        print(i, ' - ', select[i])

    ind = int(input('Digite o indice do elemento que voce quer editar: '))
    edit = int(input('Digite o edicao: '))
    lista[ind] = edit
    print(lista)

elif select == 3:
    for i in range(len(lista)):
        navi = input('Digite o nome do produto que quer excluir: ')
        print(i, ' - ', lista[i])
    ind = int

#incremente uma opção 4 em que o usuario busque um produto
#e o programa informe se ele está ou não na lista (use for para percorrer)

elif select == 4:
    for i in range(len(lista)):
        navi = input('Digite o nome do produto: ').lower()
        print(i, ' - ', lista[i])

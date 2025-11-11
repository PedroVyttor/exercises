#construa um programa em python que possua um menu com 3 opções:
#1-cadastrar produto
#2-listar todos os produtos
#0-Sair

lista = ['Meia', 'Boia', 'Blusa', 'PlayStation 7 Ultra Pro 16K 200FPS']

while True:
    print('\n===== MENU =====')
    print('1 - Cadastrar Produto')
    print('2 - Listar todos os produtos')
    print('3 - Remover produto da lista')
    print('4 - Buscar produto')
    print('0 - Sair')

    select = int(input('Selecione: '))

    if select == 1:
        nome = input('Digite o nome do produto: ')
        lista.append(nome)
        print('Produto cadastrado com sucesso!')

    elif select == 2:
        print('\nProdutos cadastrados:')
        for i in range(len(lista)):
            print(i, '-', lista[i])

    elif select == 3:
        print('\nProdutos:')
        for i in range(len(lista)):
            print(i, '-', lista[i])
        nome = input('digite o nome do produto que quer excluir: ')
        if nome in lista:
            lista.remove(nome)
            print('produto removido com sucesso!')
        else:
            print('produto não encontrado.')

    elif select == 4:
        nome = input('digite o nome do produto que deseja buscar: ')
        encontrado = False
        for item in lista:
            if item.lower() == nome.lower():
                encontrado = True
                break
        if encontrado:
            print(f'produto encontrado na lista: {nome}')
        else:
            print('produto nao encontrado.')

    elif select == 0:
        print('encerrando o programa...')
        break

    else:
        print('opcao invalida. tente novamente.')


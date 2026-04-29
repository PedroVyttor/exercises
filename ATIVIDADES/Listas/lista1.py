contatos = []

while True:
    print('Bem-vindo a ContactPython App'
          '1- Criar contato'
          '2- Buscar contato por nome'
          '3- Listar contatos'
          '4- Alterar contatos'
          '5- Apagar contatos'
          '6- Buscar contato por número'
          '0- Sair')

    opcao = int(input('Digite a opção: '))
    if opcao == 0:
        break

    elif opcao == 1:
        nome = input('Digite o nome do contato: ')
        celular = input('Digite o celular: ')
        contatos.append([nome, celular])

    elif opcao == 2:
        print('-' * 50)
        nome = input('Digite o nome do contato: ')
        for c in contatos:
            if c[0] == nome:
                print(c[0], '-', c[1])
        print('-' * 50)

    elif opcao == 3:
        print('-' * 50)
        for c in contatos:
            print(c[0], '-',  c[1])
        print('-' * 50)

    elif opcao == 4:
        print('-' * 50)
        print('Para alterar, informe o dado abaixo: ')
        celular = input('Digite o celular do contato: ')
        for posicao in range(len(contatos)):
            if contatos[posicao][1] == celular:
                nome = input('Digite o novo nome: ')
                celular = input('Digite o novo celular: ')
                contatos[posicao] = [nome, celular]
                print('\n\nContato alterado com sucesso\n\n')
        print('-' * 50)

    elif opcao == 6:
        print('-' * 50)
        celular = int(input('Digite o numero do contato: '))
        for c in contatos:
            if c[1] == celular:
                print(c[0], '-', c[1])
        print('-' * 50)


contatos = []

while True:
    print('Bem-vindo a ContactPython App'
          '1- Criar contato'
          '2- Buscar contato por nome'
          '3- Listar contatos'
          '4- Alterar contatos'
          '5- Apagar contatos'
          '0- Sair')

    opcao = int(input('Digite a opção: '))
    if opcao == 0:
        break

    elif opcao == 1:
        nome = input('Digite o nome do contato: ')
        celular = input('Digite o celular: ')
        contatos.append([nome, celular])

    elif opcao == 3:
        print('-' * 50)
        for c in contatos:
            print(c[0], '-',  c[1])
        print('-' * 50)





#funções com parâmetros de entrada e sem retorno

def exibir_nome_completo(nome, sobrenome):
    nome = input('Digite seu nome: ')
    sobrenome = input('digite seu sobrenome: ')

    if len(nome) == 0 or len(sobrenome) == 0:
        print('Nome invalido!')
    else:
        print(f'Meu nome completo é {nome} {sobrenome}')

exibir_nome_completo('Pedro', 'Vyttor')
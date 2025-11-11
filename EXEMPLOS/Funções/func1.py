#funções
#determinar um bloco de código a ser executado mediante chamada

#1 - facilita o reaproveitamento de código
#2 - modularizada o código e ajuda a organizar
#3 - proporciona melhor manutenção do código em posterior

#funções sem parâmetros de entrada e sem retorno

#declarar uma função

def saudar_pessoas():
    nome = input('Digite seu nome: ')
    print(f'Olá, {nome}, beleza?')

#chamar = saudar_pessoas()

#for_in_range(3)
for i in range(3):
    saudar_pessoas()
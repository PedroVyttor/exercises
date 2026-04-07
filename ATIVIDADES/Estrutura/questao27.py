entrada = input('Deseja entrar no lugar? (S/N)').upper()
homem = 0
mulher = 0

while entrada == 'S':
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        print('Maior de idade, pode entrar de boas')
        sieks = input('Digite seu sieks (M/F): ').upper()

        if sieks == 'M':
            homem = homem + 1
        elif sieks == 'F':
            mulher = mulher + 1
        print(f'Qtde homens: {homem}, Qtde mulheres: {mulher}')
        print(f'quantidade de pessoas na bixa (Fila em PT-PT): {mulher + homem}')

    else:
        print('Menor de idade, cai fora')
        break

else:
    print('Tá bom')
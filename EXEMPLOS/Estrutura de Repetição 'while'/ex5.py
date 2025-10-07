nome = 'paulo carlos da nobrega silva dantas'
qtde = 0

for i in range (len(nome)):
    if nome[i] == ' ':
        qtde += 1

print(f'A quantidade de espaço nesse nome completo é {qtde}')
print(f'A quantidade total de caracteres é de {len(nome)}')
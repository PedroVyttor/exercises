#criar lista, inserir na lista, remover da lista, alterar ma lista

#percorrer uma lista
alunos = ['uno', 'dos', 'tres', 'cuatro']

#print('uno' in alunos)

print(' "A" in "Alunos": ')
print('a' in 'alunos')

#alternativa

print(' Alternativa: ')
achei = False
for a in alunos:
    if 'cinco' == a:
        achei = True
        break

print(achei)
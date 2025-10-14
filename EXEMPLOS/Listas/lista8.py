#remover pelo conteudo do item
alunos = ['kaique', 'denis', 'ygor', 'carlos']

expul = input('Diga o nome do aluno expulso: ').lower()
if expul in alunos:
    alunos.remove(expul)
    print('Essa pessoa foi expulsa')

else:
    print('Essa pessoa nao foi expulsa')

print(alunos)
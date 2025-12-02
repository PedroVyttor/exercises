sorteio = {'a':'friend', 'b':'jota'}

#atualizar/sobrescrever
sorteio['a'] = 'humano'

print(sorteio)
#removendo o par(chave:valor)
del(sorteio['a'])
print(sorteio)

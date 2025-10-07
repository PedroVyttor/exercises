#estrutura de repetição: for

#desenvolva um algoritmo em python que o usuário fornaça a quantidade de pacientes atendidos. o programa deve receber
#também como entrada a idade de cada paciente, para ao final gerar a idade média de atendimento no consultório.

pac = int(input('digite a quantidade de pacientes: '))
soma = 0

for pac in range (pac):
    idade = int(input('digite a idade do paciente: '))
    soma = soma + idade

media = soma / pac
print(f'a media de idade dos pacientes e de: {media}')
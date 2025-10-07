#Faça um programa que o usuario digite o time do coração e o jogador prefetido.
# o programa deve executar até que alguem digite
#que o time é o sousa e oo jogador é o Neymar.

nome = input('Digite o jogador preferido') .lower()
time = input('digite o time prederido') .lower()

while nome != 'neymar' and time != 'sousa':
    nome = input('Digite o jogador preferido') .lower()
    time = input('digite o time prederido') .lower()

print('voce gosta de um time horrivel ou de um jogador bandido')


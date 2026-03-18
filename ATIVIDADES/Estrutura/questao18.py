nums = int(input('Digite um dia da semana (1 a 7): '))

if nums == 6 or nums == 7:
    print('fim de semana')

elif nums > 7 or nums <= 0 :
    print('incorreto')
else:
    print('dia útil')
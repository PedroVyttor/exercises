#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('digite uma letra: ') .lower()

if letra != 'a' and letra != 'e' and letra != 'i' and letra != 'o' and letra != 'u':
    print('a letra digitada é CONSOANTE')

else:
    print('a letra digitada é VOGAL')
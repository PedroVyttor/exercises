senha = input('Digite a senha: ')
confirmar = input('Confirme a senha: ')

tem_especial = ('@' in senha or'!' in senha or'+' in senha or'-' in senha or '.' in senha)

if len(senha) < 8:
    print('a senha deve ter no mínimo 8 caracteres.')
elif not tem_especial:
    print('a senha deve conter pelo menos um caractere especial (@!+-.).')
elif senha != confirmar:
    print('as senhas não coincidem.')
else:
    print('senha valida')
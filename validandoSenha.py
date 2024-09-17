def conferirSenha():
    senha = str('2536gustavo')
    if senha == input('Digite sua senha: '):
        print('Acessou o perfil')
    else:
        print('Sengha incorreta!')
conferirSenha()
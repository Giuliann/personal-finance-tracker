from Controle_gastos.Backend.Database.models import Login
from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.security import verify_senha
from Controle_gastos.Backend.security import hash_senha

def up_login():
    email = input('Digite o email que gostaria de atualizar: ')
    login = (session.query(Login)
                    .filter(Login.email == email)
                    .first())
    if not login:
        print('Email não encontrado')

    print('O que gostaria de alterar?')
    print('[1] Email')
    print('[2] Senha')
    print('[3] Nome')
    select = int(input('> '))

    match select:
        case 1:
            new_email = input('Digite um novo email: ')
            user_senha = input('Digite a senha do email: ')
            
            if not verify_senha(user_senha, login.senha):
                print('Senha incorreta')
                return

            if new_email == email:
                print('Você já usa esse email')
            else:
                login_update = (session.query(Login)
                                 .filter(Login.email == email)
                                 .update({Login.email: new_email}))
                session.commit(login_update)
                print('Login atualizado com sucesso!')
        case 2:
            new_senha = hash_senha(input('Digite a Nova senha: '))
            senha = input('Digite a antiga senha para confirmar mudança: ')
            if not verify_senha(senha, login.senha):
                print('Senha incorreta')
                return
            
            login_update = (session.query(Login)
                            .filter(Login.email == email)
                            .update({Login.senha: new_senha}))
            session.commit(login_update)
            print('Login atualizado com sucesso!')


    
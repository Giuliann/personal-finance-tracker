from Controle_gastos.Backend.Database.models import Login
from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.security import verify_senha

def delete_login():
    email = input('Digite o email que gostaria de deletar: ')
    login = (session.query(Login)
                .filter(Login.email == email)
                .first())

    if not login:
        print('Email não existe...')

    senha = input('Digite a senha do email: ')

    if not verify_senha(senha, login.senha):
        print('Senha errada tente novamente')
        return
    
    print('Conta deletada com sucesso!')


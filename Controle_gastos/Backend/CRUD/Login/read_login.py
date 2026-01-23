from Controle_gastos.Backend.Database.models import Login
from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.security import verify_senha

def verify_login():
    email = input('Digite o email que gostaria de verificar: ')
    user_senha = input('Digite a senha do seu email: ')
    login = (session.query(Login)
            .filter(Login.email == email)
            .first())
    if not login:
        print('Email não encontrado')
        return
    if not verify_senha(user_senha, login.senha):
        print('Senha errada, tente novamente')
        return

    print('Login feito com sucesso')

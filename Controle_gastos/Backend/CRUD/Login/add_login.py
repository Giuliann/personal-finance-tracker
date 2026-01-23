from Controle_gastos.Backend.Database.models import Login, Person
from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.security import hash_senha
from Controle_gastos.Backend.Token import new_token, salvar_token

def new_login():
    nome = Person(nome= input('Digite o nome da Pessoa: ').strip().title())
    email = input('Digite seu email: ')
    user_senha = input('Digite sua senha: ')
    senha_hash = hash_senha(user_senha)
    login = Login(email= email, senha= senha_hash)
    login.pessoa = nome


    if session.query(Login).filter(Login.email == email).first():
        print('Já existe uma conta com esse email')
        return
    else:
        session.add_all([nome, login])
        session.commit()
    
    print('Deseja permancer o logado nesse dispositivo ?')
    print('[1] Sim')
    print('[2] Não')
    select = int(input('> '))

    if select == 1:
        token = new_token()
        salvar_token(token= token)
        print('Login Realizado')

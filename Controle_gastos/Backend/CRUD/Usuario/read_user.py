from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person

### Função lista os usuarios da tabela "Person" do banco: ###

def list_users():
    lista_usuarios = session.query(Person).all()
    if not lista_usuarios:
        print('Ainda não exites nenhuma Pessoa...')
        return None
    else:
        for pessoas in lista_usuarios:
            print(f'{pessoas.id} - {pessoas.nome}')
            
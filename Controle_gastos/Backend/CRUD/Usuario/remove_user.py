from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person
from Controle_gastos.Backend.CRUD.Usuario.read_user import list_users

### Função exibe a lista de usuarios e permite deletar um usuario do banco: ###

def delete_user():
    list_users()
    print('Selecione a Pessoa que deseja remover')
    print('Digite o id da Pessoa: ')
    select = int(input('> '))
    pessoa_delete = (session.query(Person)
                     .filter(Person.id == select)
                     .first())
    session.delete(pessoa_delete)
    session.commit()
from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person
from Controle_gastos.Backend.CRUD.Usuario.read_user import list_users

### Função exibe a lista de usuarios e permite fazer altearções em um usuario do banco: ###

def up_user():
    list_users()
    print('Selecione a Pessoa que deseja atualizar')
    print('Digite o id da Pessoa: ')
    select = int(input('> '))
    novo_nome = str(input('Atualize o nome do usuario: '))
    pessoa_update = (session.query(Person)
                     .filter(Person.id == select)
                     .update({Person.nome: novo_nome}))
    session.commit()
    print('Nome atualizado com sucesso')
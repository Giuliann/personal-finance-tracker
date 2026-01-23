from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person, Login
### Função adiciona novo usuario ao banco: ###

def new_user():
        nome = input('Digite o nome da Pessoa: ').strip().title()
        user = Person(nome= nome)
        session.add(user)
        session.commit()
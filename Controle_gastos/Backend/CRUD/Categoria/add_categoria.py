from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Categorie

### Função adiciona uma nova categoria: ###

def new_categoria():
    while True:
        nome_categoria = input('Digite o nome da Categoria: ').strip().title()
        categoria = Categorie(cat_name= nome_categoria)
        session.add(categoria)
        session.commit()
        print(f'{categoria.cat_name} Adicionado com sucesso')
        print('\n\nDeseja adicionar mais Categorias?')
        print('[1] Sim')
        print('[2] Não')
        select = int(input('> '))
        match select:
            case 1:
                return new_categoria()
            case 2:
                break
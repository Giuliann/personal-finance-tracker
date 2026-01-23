from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Categorie
from Controle_gastos.Backend.CRUD.Categoria import list_categoria

### Função exibe a lista de categorias e permite deletar uma categoria do banco: ###

def delete_categoria():
    list_categoria()
    print('Selecione a Categoria que deseja remover')
    print('Digite o id da Categoria: ')
    select = int(input('> '))
    categoria_delete = (session.query(Categorie)
                        .filter(Categorie.id == select)
                        .first())
    session.delete(categoria_delete)
    session.commit()
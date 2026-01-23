from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Categorie
from Controle_gastos.Backend.CRUD.Categoria import list_categoria

### Função exibe a lista de categorias e permite atualizar uma categoria do banco: ###

def up_categoria():
    list_categoria()
    print('Selecione a Categoria que deseja remover')
    print('Digite o id da Categoria: ')
    select = int(input('> '))
    novo_nome = str(input('Atualize o nome da categoria: '))
    categoria_delete = (session.query(Categorie)
                        .filter(Categorie.id == select)
                        .update({Categorie.cat_name: novo_nome}))
    session.commit()
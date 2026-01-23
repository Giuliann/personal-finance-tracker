from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Categorie

### Função lista as categorias da tabela "Categorie" do banco: ###

def list_categoria():
    lista_categorias = session.query(Categorie).all()
    if not lista_categorias:
        print('Ainda não exites nenhuma Categoria...')
        return None
    else:
        for categorias in lista_categorias:
            print(f'{categorias.id} - {categorias.cat_name}')
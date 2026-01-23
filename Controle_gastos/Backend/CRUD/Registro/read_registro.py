from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person, Categorie, Registro

### Função lista todos os registro do banco: ###
def list_gastos():
    lista_gasto = (session.query(Person.nome, Categorie.cat_name, Registro.item_name, Registro.pagamento, Registro.valor, Registro.data)
                   .join(Person, Registro.id_pessoas == Person.id)
                   .join(Categorie, Registro.id_categoria == Categorie.id)
                   .all())
    if not lista_gasto:
        print('Ainda não exites nenhum registro...')
        return None
    else:
        for nome, categoria, item, pagamento, valor, data in lista_gasto:
            print(f'{nome} | {categoria} | {item} - {pagamento} R${valor:.2f} Data: ({data})')
        
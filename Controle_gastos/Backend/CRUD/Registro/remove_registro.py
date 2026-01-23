from Controle_gastos.Backend.Database.db import session
from Controle_gastos.Backend.Database.models import Person, Categorie, Registro

def delete_registro():
    lista_registros = (session.query(Person.nome, Categorie.cat_name, Registro.item_name, Registro.pagamento, Registro.valor, Registro.data)
                   .join(Person, Registro.id_pessoas == Person.id)
                   .join(Categorie, Registro.id_categoria == Categorie.id)
                   .all())
    if not lista_registros:
        print('Ainda não existe nenhum registro...')
    else:
        for nome, categoria, item, pagamento, valor, data in lista_registros:
            print(f'{nome} | {categoria} | {item} - {pagamento} R${valor:.2f} Data: ({data})')
    

    print('Selecione o Registro que deseja remover')
    print('Digite o id do Registro: ')
    select = int(input('> '))
    registro_delete = session.query(Registro).filter_by(id= select).first()
    session.delete(registro_delete)
    session.commit()
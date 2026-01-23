from Controle_gastos.Backend.Database.db import session
from datetime import datetime, date
from Controle_gastos.Backend.Database.models import Person, Categorie, Registro
from Controle_gastos.Backend.CRUD.Usuario.read_user import list_users
from Controle_gastos.Backend.CRUD.Categoria.read_categoria import list_categoria

def up_registro():
    lista_registros = (session.query(Person.nome, Categorie.cat_name, Registro.item_name, Registro.pagamento, Registro.valor, Registro.data)
                   .join(Person, Registro.id_pessoas == Person.id)
                   .join(Categorie, Registro.id_categoria == Categorie.id)
                   .all())
    if not lista_registros:
        print('Ainda não existe nenhum registro...')
    else:
        for nome, categoria, item, pagamento, valor, data in lista_registros:
            print(f'{nome} | {categoria} | {item} - {pagamento} R${valor:.2f} Data: ({data})')
    

    print('Selecione o Registro que deseja atualizar')
    print('Digite o id do Registro: ')
    select = int(input('> '))

    print('O que você gostaria de atualizar no registro?')
    print('[1] Nome Pessoa')
    print('[2] Categoria')
    print('[3] Nome do Produto')
    print('[4] Forma de Pagamento')
    print('[5] Valor')
    print('[6] Data')
    num = int('> ')
    match num:
        case 1:
            list_users()
            novo_user = int(input('Digite o id do novo usuario: '))
            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.id_pessoas: novo_user}))
        case 2:
            list_categoria()
            nova_categoria = int(input('Digite o id da nova categoria: '))
            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.id_categoria: nova_categoria}))
        case 3:
            novo_produto = input('Digite o novo nome produto: ')
            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.item_name: novo_produto}))
        case 4:
            print('Escolha a nova forma de pagamento: ')
            print('[1] Debito ')
            print('[2] Credito')
            forma_de_pagamento = int(input('> '))

            if forma_de_pagamento == 1:
                forma_de_pagamento = 'Debito'
            elif forma_de_pagamento == 2:
                forma_de_pagamento = 'Credito'

            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.pagamento: forma_de_pagamento}))
        case 5:
            novo_valor = float(input('Digite o novo valor do produto: '))
            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.valor: novo_valor}))
        case 6:
            print('Informe nova data: ')
            print('[1] Usar data atual')
            print('[2] Fornecer uma data')
            num = int(input('> '))
            if num == 1:
                nova_data = date.today()
            elif num == 2:
                print('Digite a data no formato (dd/mm/aaaa): ')
                num = input('> ')
                nova_data = datetime.strptime(select, '%d/%m/%Y').date()
            else:
                print('Essa opção não existe, usando data atual...')
                nova_data = date.today()

            registro_att = (session.query(Registro)
                            .filter(Registro.id == select)
                            .update({Registro.data: nova_data}))
    session.commit()
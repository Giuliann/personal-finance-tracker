from Controle_gastos.Backend.Database.db import session
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from Controle_gastos.Backend.Database.models import Registro
from Controle_gastos.Backend.CRUD.Categoria import list_categoria, new_categoria
from Controle_gastos.Backend.CRUD.Usuario import list_users, new_user

### Função adiciona um novo Registro ao banco de dados: ###

def new_registro():
    while True:
        Item_nome = input('Digite o nome do produto: ').strip().title()
        valor = float(input('Digite o valor do item: R$'))
        
        # Forma de Pagamento: 
        print('Qual a forma de Pagamento: ')
        print('[1] Debito')
        print('[2] Credito')
        forma_pagar = int(input('> '))
        if forma_pagar == 1:
            forma_pagar = 'Debito'
            parcelas = 1
        
        elif forma_pagar == 2:
            forma_pagar = 'Credito'
            print('Quantas parcelas você quer pagar?')
            for x in range(1, 12):
                print(f'{x}x de {valor/x:.2f}R$')
            select = int(input('> '))
            parcelas = select
        
        else:
            print('Não existe essa opção...')


    # Consulta a tabela das categorias: 
        list_categoria()
        print('Escolha a categoria do seu registro: ')
        print('Digite o id da Categoria: ')
        select = int(input('> '))
        categoria_id = select

    # Consulta a tabela dos usuarios: 
        list_users()
        print('Selecione a pessoa que fez a compra')
        print('Digite o id da Pessoa: ')
        select = int(input('> '))
        pessoa_id = select
    

    # Registro da data: 
        print('Deseja usar a data atual ou fornecer uma data?')
        print('[1] Usar data atual')
        print('[2] Fornecer uma data')
        select = int(input('> '))
        if select == 1:
            data = date.today()
        elif select == 2:
            print('Digite a data no formato (dd/mm/aaaa): ')
            select = input('> ')
            data = datetime.strptime(select, '%d/%m/%Y').date()
        else:
            print('Essa opção não existe, usando data atual...')
            data = date.today()

    # Registra:
        for i in range(parcelas):
            valor_parcela = valor / parcelas
            data_parcela = data + relativedelta(months= i)
            registro = Registro(item_name= Item_nome, valor= valor_parcela,pagamento= forma_pagar, parcelas= parcelas - i, data= data_parcela, id_categoria= categoria_id, id_pessoas = pessoa_id)
            session.add(registro)
        session.commit()
        print('Registro feito com Sucesso')
        print('\n\nDeseja adicionar mais Registros?')
        print('[1] Sim')
        print('[2] Não')
        select = int(input('> '))
        match select:
            case 1:
                return new_registro()
            case 2:
                break
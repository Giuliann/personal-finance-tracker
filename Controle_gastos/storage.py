from db import session, Person, Categorie, Registro
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

#==========================#
###       Pessoas        ###
#==========================#

### Função adiciona novo usuario ao banco: ###
def add_user():
    while True:
        nome = input('Digite o nome da Pessoa: ')
        user = Person(nome= nome)
        session.add(user)
        session.commit()
        print(f'{user.nome} adicionado(a) com Sucesso!!')
        print('\n\nDeseja adicionar mais pessoas?')
        print('[1] Sim')
        print('[2] Não')
        select = int(input('> '))
        match select:
            case 1:
                return add_user()
            case 2:
                break


### Função lista os usuarios da tabela "Person" do banco: ###
def list_users():
    lista_users = session.query(Person).all()
    if not lista_users:
        print('Ainda não exites nenhuma Pessoa...')
        return None
    else:
        for pessoas in lista_users:
            pessoa = session.query(Person).filter_by(id= pessoas.id).first()
            print(f'{pessoa.id} - {pessoa.nome}')

    return lista_users

### Função exibe a lista de usuarios e permite deletar um usuario do banco: ###
def remove_user():
    lista_pessoas = session.query(Person).all()
    for pessoas in lista_pessoas:
        pessoa = session.query(Person).filter_by(id= pessoas.id).first()
        print(f'{pessoa.id} - {pessoa.nome}')

    print('Selecione a Pessoa que deseja remover')
    print('Digite o id da Pessoa: ')
    select = int(input('> '))
    pessoa_delete = session.query(Person).filter_by(id= select).first()
    session.delete(pessoa_delete)
    session.commit()
#==========================#
###      Categorias      ###
#==========================#

### Função adiciona uma nova categoria: ###
def add_categoria():
    while True:
        nome_categoria = input('Digite o nome da Categoria: ')
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
                return add_categoria()
            case 2:
                break

### Função lista as categorias da tabela "Categorie" do banco: ###
def list_categoria():
    lista_categorias = session.query(Categorie).all()
    if not lista_categorias:
        print('Ainda não exites nenhuma Categoria...')
        return None
    else:
        for categorias in lista_categorias:
            categoria = session.query(Categorie).filter_by(id= categorias.id).first()
            print(f'{categoria.id} - {categoria.cat_name}')
    return lista_categorias

### Função exibe a lista de categorias e permite deletar uma categoria do banco: ###
def remove_categoria():
    lista_categorias = session.query(Categorie).all()
    for categorias in lista_categorias:
        categoria = session.query(Categorie).filter_by(id= categorias.id).first()
        print(f'{categoria.id} - {categoria.cat_name}')

    print('Selecione a Categoria que deseja remover')
    print('Digite o id da Categoria: ')
    select = int(input('> '))
    categoria_delete = session.query(Categorie).filter_by(id= select).first()
    session.delete(categoria_delete)
    session.commit()

#==========================#
### Registro de Gastos ###
#==========================#

### Função adiciona um novo Registro ao banco de dados: ###
def add_registro():
    while True:
        Item_nome = input('Digite o nome do produto: ')
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
        list_categoria = session.query(Categorie).all()
        for categorias in list_categoria:
            categoria = session.query(Categorie).filter_by(id= categorias.id).first()
            print(f'[{categoria.id}] {categoria.cat_name}')
    
        print('Escolha a categoria do seu registro: ')
        print('Digite o id da Categoria: ')
        select = int(input('> '))
        categoria_id = select

    # Consulta a tabela dos usuarios: 
        list_pessoa = session.query(Person).all()

        for pessoas in list_pessoa:
            pessoa = session.query(Person).filter_by(id= pessoas.id).first()
            print(f'[{pessoa.id} {pessoa.nome}]')


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
                return add_registro()
            case 2:
                break

    

### Função lista todos os registro do banco: ###
def lista_gastos():
    lista_gasto = session.query(Registro).all()
    if not lista_gasto:
        print('Ainda não exites nenhum registro...')
        return None
    else:
        for gastos in lista_gasto:
            dono_compra = session.query(Person).filter_by(id= gastos.id_pessoas).first()
            categorias_compra = session.query(Categorie).filter_by(id= gastos.id_categoria).first()
            print(f'{dono_compra.nome} | {categorias_compra.cat_name} | {gastos.item_name} - {gastos.pagamento} R${gastos.valor:.2f} ({gastos.data})')
    
    return lista_gasto

def remove_registro():
    lista_registros = session.query(Registro).all()
    for registros in lista_registros:
        registro = session.query(Registro).filter_by(id= registros.id).first()
        dono_compra = session.query(Person).filter_by(id= registro.id_pessoas).first()
        print(f'{registro.id}  Compra: {dono_compra.nome} | {registro.item_name} | {registro.pagamento}  R${registro.valor:.2f} - ({registro.data})')

    print('Selecione o Registro que deseja remover')
    print('Digite o id do Registro: ')
    select = int(input('> '))
    registro_delete = session.query(Registro).filter_by(id= select).first()
    session.delete(registro_delete)
    session.commit()
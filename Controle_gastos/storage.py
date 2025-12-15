from db import session, Person, Categorie, Registro
from datetime import datetime

#==========================#
###       Pessoas        ###
#==========================#

### Função adiciona novo usuario ao banco: ###
def add_user(nome):
    user = Person(nome= nome)
    session.add(user)
    session.commit()
    print(f'{user.nome} adicionado(a) com Sucesso!!')

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
def add_categoria(nome_categoria):
    categoria = Categorie(cat_name= nome_categoria)
    session.add(categoria)
    session.commit()
    print(f'{categoria.cat_name} Adicionado com sucesso')

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
def add_registro(Item_nome, valor):

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

    # Registra: 
    data_atual = datetime.now().strftime("%d-%m-%Y")
    registro = Registro(item_name= Item_nome, valor= valor, data= data_atual, id_categoria= categoria_id, id_pessoas = pessoa_id)
    session.add(registro)
    session.commit()
    print('Registro feito com Sucesso')

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
            print(f'{dono_compra.nome} | {categorias_compra.cat_name} | {gastos.item_name} - R${gastos.valor:.2f} ({gastos.data})')
    
    return lista_gasto

def remove_registro():
    lista_registros = session.query(Registro).all()
    for registros in lista_registros:
        registro = session.query(Registro).filter_by(id= registros.id).first()
        dono_compra = session.query(Person).filter_by(id= registro.id_pessoas).first()
        print(f'{registro.id}  Compra: {dono_compra.nome} | {registro.item_name} | R${registro.valor:.2f} - ({registro.data})')

    print('Selecione o Registro que deseja remover')
    print('Digite o id do Registro: ')
    select = int(input('> '))
    registro_delete = session.query(Registro).filter_by(id= select).first()
    session.delete(registro_delete)
    session.commit()
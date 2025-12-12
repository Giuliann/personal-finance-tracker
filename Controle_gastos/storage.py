from db import session, Person, Categorie, Registro
from datetime import datetime

#==========================#
### Pessoas e Categorias ###
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
            print(f'{pessoas.nome}')

    return lista_users

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
            print(f'{categorias.cat_name}')
    return lista_categorias


#==========================#
### Registro de Gastos ###
#==========================#

### ###
def add_registro(Item_nome, valor):

    # Consulta a tabela das categorias: 
    list_categoria = session.query(Categorie).all()
    cont = 1
    for categorias in list_categoria:
        print(f'[{cont}] {categorias.cat_name}')
        cont += 1
    print('Escolha a categoria do seu registro: ')
    select = int(input('> '))
    categoria_id = list_categoria[select - 1].id

    # Consulta a tabela dos usuarios: 
    list_pessoa = session.query(Person).all()
    cont = 1
    for pessoas in list_pessoa:
        print(f'[{cont} {pessoas.nome}]')
        cont += 1
    print('Selecione o a pessoa que fez a compra')
    select = int(input('> '))
    pessoa_id = list_pessoa[select - 1].id

    # Registra: 
    data_atual = datetime.now().strftime("%d-%m-%Y")
    registro = Registro(item_name= Item_nome, valor= valor, data= data_atual, id_categoria= categoria_id, id_pessoas = pessoa_id)
    session.add(registro)
    session.commit()
    print('Reistro feito com Sucesso')

def lista_gastos():
    lista_gasto = session.query(Registro).all()
    return lista_gasto
### Importações para funcionamento do banco ###
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base


db = create_engine("sqlite:///personal-finance-tracker/Controle_gastos/Banco/banco.db")
Session = sessionmaker(bind= db)
session = Session()
Base = declarative_base()

### Tabelas do Banco ###
# Tabela de Pessoas:
class Person(Base):
    __tablename__ = 'pessoas'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    nome = Column('nome', String)

    # Inicialização da Classe Pessoas:
    def __init__(self, nome):
        self.nome = nome

# Tabela de Categoria: 
class Categorie(Base):
    __tablename__ = 'categorias'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    cat_name = Column('nome', String)

    # Inicialização da Classe Categoria:
    def __init__(self, cat_name):
        self.cat_name = cat_name

# Tabela de Registro dos Gastos:
class Registro(Base):
    __tablename__ = 'registros'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    item_name = Column('nome item', String)
    valor = Column('valor', Integer)
    date = Column('data', String)
    id_categoria = Column('categoria', ForeignKey('categorias.id'))
    id_pessoas = Column('pessoa', ForeignKey('pessoas.id'))

    # Inicialização da Classe Gastos:
    def __init__(self, item_name, valor):
        self.item_name = item_name
        self.valor = valor
        self.data = datetime.now().date()


Base.metadata.create_all(bind= db)

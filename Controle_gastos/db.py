### Importações para funcionamento do banco ###
from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey, Date
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
    nome = Column('nome', String(50))

    # Inicialização da Classe Pessoas:
    def __init__(self, nome):
        self.nome = nome

# Tabela de Categoria: 
class Categorie(Base):
    __tablename__ = 'categorias'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    cat_name = Column('nome', String(20))

    # Inicialização da Classe Categoria:
    def __init__(self, cat_name):
        self.cat_name = cat_name

# Tabela de Registro dos Gastos:
class Registro(Base):
    __tablename__ = 'registros'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    item_name = Column('nome_item', String(30))
    valor = Column('valor', Float)
    pagamento = Column('pagamento', String)
    parcelas = Column('parcelas', Integer)
    data = Column('data', Date)
    id_categoria = Column('id_categoria', ForeignKey('categorias.id'))
    id_pessoas = Column('id_pessoas', ForeignKey('pessoas.id'))

    # Inicialização da Classe Gastos:
    def __init__(self, item_name, valor, pagamento, parcelas, data, id_categoria, id_pessoas):
        self.item_name = item_name
        self.valor = valor
        self.pagamento = pagamento
        self.parcelas = parcelas
        self.data = data
        self.id_categoria = id_categoria
        self.id_pessoas = id_pessoas


Base.metadata.create_all(bind= db)

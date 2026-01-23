from Controle_gastos.Backend.Database.db import db, Base, relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date

### Tabelas do Banco ###

# Tabela de Login: 
class Login(Base):
    __tablename__ = 'login'
    
    id = Column('id', Integer, primary_key= True)
    email = Column('email', String(30), unique= True)
    senha = Column('senha', String)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'),unique= True, nullable=False)
    pessoa = relationship("Person", back_populates="login", uselist=False)

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

# Tabela de Pessoas:
class Person(Base):
    __tablename__ = 'pessoas'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    nome = Column('nome', String(50))
    login = relationship("Login", back_populates="pessoa")

    # Inicialização da Classe Pessoas:
    def __init__(self, nome):
        self.nome = nome

# Tabela de Cartões: 
class Cartao(Base):
    __tablename__ = 'cartao'

    id = Column('id', Integer, primary_key= True, autoincrement= True)
    limite = Column('limite', Float)
    data_fechamento = Column('fechamento', Integer)
    data_vencimento = Column('vancimento', Integer)
    pessoa_id = Column('dono', Integer, ForeignKey('pessoas.id'))


    # Inicialização da Classe de Cartões: 
    def __init__(self, limite, fechamento, vencimento):
        self.limite = limite
        self.data_fechamento = fechamento
        self.data_vencimento = vencimento
        
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
    pessoas_id = Column('pessoas_id', ForeignKey('pessoas.id'))

    # Inicialização da Classe Gastos:
    def __init__(self, item_name, valor, pagamento, parcelas, data, id_categoria, pessoas_id):
        self.item_name = item_name
        self.valor = valor
        self.pagamento = pagamento
        self.parcelas = parcelas
        self.data = data
        self.id_categoria = id_categoria
        self.id_pessoas = pessoas_id


Base.metadata.create_all(bind= db)
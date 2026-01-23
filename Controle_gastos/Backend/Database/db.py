### Importações para funcionamento do banco ###
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship


db = create_engine("sqlite:///Controle_gastos/Backend/Database/banco.db")
Session = sessionmaker(bind= db)
session = Session()
Base = declarative_base()
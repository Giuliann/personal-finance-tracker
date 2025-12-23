from db import Person, Categorie, Registro, session
from datetime import datetime

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

# Adiciona Relatorio: 
def relatorio_pessoa():
    while True:
        print('Qual pessoa você gostaria de ver o relatorio?')
        lista_pessoas = session.query(Registro).all()
        for pessoas in lista_pessoas:
            pessoa = session.query(Person).filter_by(id= pessoas.id).first()
            print(f'{pessoa.id} - {pessoa.nome}')
        print('Digite o id da pessoa: ')
        select = int(input('> '))

        print('Selecione o mês: ')
        for mes in meses:
            print(f'{mes}')


from db import Person, Categorie, Registro, session
from sqlalchemy import func
from storage import list_users
from datetime import date

ano_atual = date.today().year
meses = { 1: 'Janeiro', 
          2: 'Fevereiro',
          3: 'Março',
          4: 'Abril',
          5: 'Maio',
          6: 'Junho',
          7: 'Julho',
          8: 'Agosto',
          9: 'Setembro',
         10: 'Outubro',
         11: 'Novembro',
         12: 'Dezembro'}

# Exibe Relatorio Pessoal e Mensal do Usuario:  
def relatorio_pessoa():
    while True:
        # Seleciona a pessoa para relatorio: 
        print('Qual pessoa você gostaria de ver o relatorio?')
        list_users()
        print('Digite o id da pessoa: ')
        select = int(input('> '))
        pessoa_id = select

        # Seleciona o mês do relatorio: 
        print('Selecione o mês: ')
        for num, mes in meses.items():
            print(f'[{num}] {mes}')

        print('Digite o número relacionado ao mês: ')
        select = int(input('> '))
        if select < 1 or select > 12:
            print('Mês Invalido...')

        inicio_mes = date(ano_atual, select, 1)
        if select == 12:
            fim_mes = date(ano_atual + 1, 1, 1)
        else:
            fim_mes = date(ano_atual, select + 1, 1)

        # Lista de Gastos Mensal do usuario: 
        lista_mensal = (session.query(Registro)
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes).all())
        
        pessoa = session.query(Person).filter_by(id= pessoa_id).first()
        print(f'Lista de Produtor comprados entre {inicio_mes} e {fim_mes}: \n')
        for relatorio in lista_mensal:
            print(f'{pessoa.nome}: | {relatorio.item_name} | {relatorio.pagamento} {relatorio.parcelas}x de {relatorio.valor:.2f}R$  Data: {relatorio.data}')

        # Total Gasta no mês pelo usuario: 
        gasto_mensal_t = (session.query(func.sum(Registro.valor))
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes).scalar()) or 0

        # Media gasta no mês pelo usuario: 
        gasto_mensal_m = (session.query(func.avg(Registro.valor))
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes).scalar()) or 0
            
        # 
        gasto_categoria = (session.query(Categorie.cat_name, func.sum(Registro.valor).label('total')).join(Categorie,Registro.id_categoria == Categorie.id)
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .group_by(Categorie.cat_name).all())
            

        print(f'\n\nO valor gasto total no mês foi: {gasto_mensal_t:.2f}R$')
        print(f'A media mensal foi {gasto_mensal_m:.2f}')
        print('\n\nGastos por Categoria: ')
        for categoria, total in gasto_categoria:
            print(f'{categoria}: {total:.2f}R$')
                    


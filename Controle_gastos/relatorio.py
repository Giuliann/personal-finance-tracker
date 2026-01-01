from db import Person, Categorie, Registro, session
from datetime import date
from sqlalchemy import func
from storage import list_users
from utils import futuro, passado, meses

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
        for num, mes in meses().items():
            print(f'[{num}] {mes}')

        print('Digite o número relacionado ao mês: ')
        select = int(input('> '))
        if select < 1 or select > 12:
            print('Mês Invalido...')

        print('Digite o ano do relatorio: ')
        ano = int(input('> '))
        if ano > futuro():
            print('O ano que você digitou é muito no futuro')
            print('Usando ano atual...')
            ano = date.today().year

        elif ano < passado():
            print('O ano digitado está muito no passado')
            print('Usando ano atual...')
            ano = date.today().year


        inicio_mes = date(ano, select, 1)
        fim_mes = date(ano, select + 1, 1)

        # Lista de Gastos Mensal do usuario: 
        lista_mensal = (session.query(Registro)
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .all())
        
        if not lista_mensal:
            print('Não existe relatorio para esse mês')
            print('Volte novamente quando tiver feito algum registro')
            break
        
        pessoa = session.query(Person).filter_by(id= pessoa_id).first()
        print(f'Lista de Produtor comprados entre {inicio_mes} e {fim_mes}: \n')
        for relatorio in lista_mensal:
            print(f'{pessoa.nome}: | {relatorio.item_name} | {relatorio.pagamento} {relatorio.parcelas}x de {relatorio.valor:.2f}R$  Data: {relatorio.data}')

        # Total Gasta no mês pelo usuario: 
        gasto_mensal_t = (session.query(func.sum(Registro.valor))
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .scalar()) or 0

        # Media gasta no mês pelo usuario: 
        gasto_mensal_m = (session.query(func.avg(Registro.valor))
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .scalar()) or 0
            
        # 
        gasto_categoria = (session.query(Categorie.cat_name, func.sum(Registro.valor).label('total'))
                            .join(Categorie,Registro.id_categoria == Categorie.id)
                            .filter(Registro.id_pessoas == pessoa_id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .group_by(Categorie.cat_name)
                            .all())
            

        print(f'\n\nO valor gasto total no mês foi: {gasto_mensal_t:.2f}R$')
        print(f'A media mensal foi {gasto_mensal_m:.2f}')
        print('\n\nGastos por Categoria: ')
        for categoria, total in gasto_categoria:
            print(f'{categoria}: {total:.2f}R$')

        print('Gostaria de vizualizar outro relatorio?')
        print('[1] Sim ')
        print('[2] Não ')
        select = int(input('> '))
        if select == 1:
            relatorio_pessoa()
        elif select == 2:
            break
        else:
            print('Não existe essa opção')
            print('Voltando para menu...')
            break
        

def relatorio_total():
    while True:
        print('Digite o mês que gostaria de fazer relatorio: ')
        for num, mes in meses().items():
            print(f'[{num}] {mes}')

        print('\nSelecione o mês: ')
        select = int(input('> '))

        if select < 1 or select > 12:
            print('Mês invalido...')

        print('Digite o ano do relatorio: ')
        ano = int(input('> '))

        if ano > futuro():
            print('O ano que você digitou é muito no futuro')
            print('Usando ano atual...')
            ano = date.today().year

        elif ano < passado():
            print('O ano digitado está muito no passado')
            print('Usando ano atual...')
            ano = date.today().year

        inicio_mes = date(ano, select, 1)
        fim_mes = date(ano, select + 1, 1)

        lista_mensal = (session.query(Person.nome, Categorie.cat_name, Registro.valor, Registro.pagamento, Registro.parcelas, Registro.item_name, Registro.data)
                        .join(Person, Registro.id_pessoas == Person.id)
                        .join(Categorie, Registro.id_categoria == Categorie.id)
                        .filter(Registro.data >= inicio_mes)
                        .filter(Registro.data <= fim_mes)
                        .all())
        if not lista_mensal:
            print('Não existe relatorio para esse mês')
            print('Volte novamente quando tiver feito algum registro')
            break
        
        for pessoa, cat_name, valor, pagamento, parcelas, item, data in lista_mensal:
            print(f'{pessoa}: | {cat_name} | {item} {pagamento}  {parcelas}x {valor:.2f}R$ Data: {data}')


        # Total gasto no mês: 
        gasto_mensal_t = (session.query(func.sum(Registro.valor))
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .scalar()) or 0

        # Media gasta no mês: 
        gasto_mensal_m = (session.query(func.avg(Registro.valor))
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .scalar()) or 0
        
        # Gasto por pessoa:
        gasto_pessoa = (session.query(Person.nome, func.sum(Registro.valor))
                        .join(Person, Registro.id_pessoas == Person.id)
                        .filter(Registro.data >= inicio_mes)
                        .filter(Registro.data <= fim_mes)
                        .group_by(Person.nome)
                        .all()
                        )

        # Gasto total por categoria: 
        gasto_categoria = (session.query(Categorie.cat_name, func.sum(Registro.valor).label('total'))
                            .join(Categorie, Registro.id_categoria == Categorie.id)
                            .filter(Registro.data >= inicio_mes)
                            .filter(Registro.data <= fim_mes)
                            .group_by(Categorie.cat_name)
                            .all())

        print(f'\n\nTotal gasto no mês {gasto_mensal_t:.2f}R$')
        print(f'Media gasta no mês {gasto_mensal_m:.2f}R$') 


        print('\n\nGasto por pessoa: ')
        for pessoa, valor in gasto_pessoa:
            print(f'{pessoa}: {valor:.2f}')

        print('\n\nGastos por Categoria: ')
        for categoria, total in gasto_categoria:
            print(f'{categoria}: {total:.2f}R$')              

        print('Gostaria de vizualizar outro relatorio?')
        print('[1] Sim ')
        print('[2] Não ')
        select = int(input('> '))
        if select == 1:
            relatorio_pessoa()
        elif select == 2:
            break
        else:
            print('Não existe essa opção')
            print('Voltando para menu...')
            break


def grafico():
    print('')
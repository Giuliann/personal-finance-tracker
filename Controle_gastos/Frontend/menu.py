### Inicio do Programa ###
from Controle_gastos.Backend.CRUD.Usuario import new_user, list_users, delete_user, up_user
from Controle_gastos.Backend.CRUD.Registro import new_registro, list_gastos, delete_registro, up_registro
from Controle_gastos.Backend.CRUD.Categoria import new_categoria, list_categoria, delete_categoria, up_categoria
from Controle_gastos.Backend.relatorio import relatorio_pessoa, relatorio_total
from Controle_gastos.Backend.CRUD.Login import new_login, verify_login
from Controle_gastos.Backend.Token import carregar_token, verify_token
from Controle_gastos.Backend.utils import limpar

token = carregar_token()

if token and verify_token():
    print('Login automatico')
else:
    print('Gostaria de fazer login')
    print('[1] Sim')
    print('[2] já tenho uma conta')
    print('[3] Não')
    select = int(input('> '))

    if select == 1:
        new_login()
    elif select == 2:
        verify_login()
    else:
        print('ok continue com o programa...')


limpar()

def menu():
    print('--' * 25)
    print('Bem vindo ao menu do Sistema de Controle de Gastos')
    print('--' * 25)
    print('\n')

    ### Menu de Interação ###
    while True:
        print('Escolha uma opção:')
        print('[1] Adicionar ')
        print('[2] Remover ')
        print('[3] Novo Gasto ')
        print('[4] Relatorio ')
        print('[5] Listar todos os gastos')
        print('[6] Fechar Programa')

        select = int(input('> '))
        match select:
            case 1:
                print('O que gostaria de adicionar?')
                print('[1] Pessoa ')
                print('[2] Categoria ')
                select = int(input('> '))
                if select == 1:
                    new_user()
                elif select == 2:
                    new_categoria()
                else:
                    print('Não existe essa opção')
                    print('Voltando para menu...')
                    menu()
            case 2:
                print('O que gostaria de remover?')
                print('[1] Pessoa ')
                print('[2] Categoria ')
                print('[3] Registro ')
                select = int(input('> '))
                if select == 1:
                    delete_user()
                elif select == 2:
                    delete_categoria()
                elif select == 3:
                    delete_registro()
                else:
                    print('Não existe essa opção')
                    print('Voltando para menu...')
                    menu()
            case 3:
                print('Deseja adicionar um novo gasto?')
                print('[1] Sim')
                print('[2] Não')
                select = int(input('> '))

                if select == 1:
                    new_registro()
                elif select == 2:
                    menu()
                else:
                    print('Não existe essa opção')
                    print('Voltando para menu...')
                    menu()
            case 4:
                print('Você gostaria de vizualizar o relatorio: ')
                print('[1] Pessoal ')
                print('[2] Total ')
                select = int(input('> '))
                if select == 1:
                    relatorio_pessoa()
                elif select == 2:
                    relatorio_total()
                else:
                    print('Não existe essa opção')
                    print('Voltando para menu...')
                    menu()
            case 5:
                print('Gostaria de listar todos os gastos?')
                print('[1] Sim ')
                print('[2] Não ')
                select = int(input('> '))
                if select == 1:
                    list_gastos()
                elif select == 2:
                    menu()
                else:
                    print('Não existe essa opção')
                    print('Voltando para menu...')
                    menu()
            case 6:
                exit('Fim do Programa...')
            case _:
                print('Função não existe')
                print('Tente novamente...')
menu()
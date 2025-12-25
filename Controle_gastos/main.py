### Inicio do Programa ###
from storage import add_user, remove_user, add_categoria, remove_categoria, add_registro, remove_registro, lista_gastos
from relatorio import relatorio_pessoa

def menu():
    print('--' * 25)
    print('Bem vindo ao menu do Sistema de Controle de Gastos')
    print('--' * 25)
    print('\n')

    ### Menu de Interação ###
    while True:
        print('Escolha uma opção:')
        print('(0) Inserir Novos Usuarios e novas Categorias ')
        print('(1) Inserir Novo Gasto')
        print('(2) Listar Gastos')
        print('(3) Relatorio Geral')
        print('(4) Remover Gasto, Usuarios e Categorias')
        print('(5) Fechar Programa...')

        select = int(input('> '))
        match select:
            case 0:
                print('Você Gostaria de Adicionar um novo Usuario ou uma nova Categoria ?')
                print('[1] Novo Usuario')
                print('[2] Nova Categoria')
                print('[3] Voltar Para o Menu')

                select = int(input('> '))
                match select:
                    case 1:
                        add_user()
                        input('\nPresione ENTER para continuar...\n\n')

                    case 2:
                        add_categoria()
                        input('\nPresione ENTER para continuar...\n\n')

                    case 3:
                        menu()

            case 1:
                print('Você Gostaria de Adicionar um novo Gasto ?')
                print('[1] Adicionar novo Gasto')
                print('[2] Voltar para o Menu')
                select = int(input('> '))

                match select:

                    case 1:
                        add_registro()
                        input('\nPresione ENTER para continuar...\n\n')

                    case 2: 
                        menu()

            case 2:
                lista_gastos()
                input('\nPresione ENTER para continuar...\n\n')
                
            case 3:
                relatorio_pessoa()
            case 4:
                print('O que você deseja remover:')
                print('[1] Remover Usuario')
                print('[2] Remover Categoria')
                print('[3] Remover Registro')
                select = int(input('> '))
                match select:
                    case 1:
                        remove_user()
                    case 2:
                        remove_categoria()
                    case 3:
                        remove_registro()
            case 5:
                exit('Fim do Progama')

            case _:
                print('O número que você digitou não representa nenhuma das opções do menu')

        
menu()
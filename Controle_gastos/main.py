### Inicio do Programa ###
from storage import add_user, add_categoria, add_registro, lista_gastos

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
        print('(4) Remover Gasto')
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
                        nome = input('Digite o nome da Pessoa: ')
                        add_user(nome)
                        input('\nPresione ENTER para continuar...\n\n')

                    case 2:
                        nome_categoria = input('Digite o nome da Categoria: ')
                        add_categoria(nome_categoria)
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
                        Item_nome = input('Digite o nome do item: ')
                        valor = input('Digite o valor do item: R$')
                        add_registro(Item_nome, valor)
                        input('\nPresione ENTER para continuar...\n\n')

                    case 2: 
                        menu()

            case 2:
                lista_gastos()
                if not lista_gastos():
                    print('Ainda não exites nenhum gasto...')
                    input('\nPresione ENTER para continuar...\n\n')
                    
                else:
                    for gastos in lista_gastos():
                        print(f'{gastos.item_name} {gastos.valor}')
                        input('\nPresione ENTER para continuar...\n\n')

            case 3:
                print('Função ainda não implementada')
            case 4:
                print('Função ainda não implementada')
            case 5:
                exit('Fim do Progama')

            case _:
                print('O número que você digitou não representa nenhuma das opções do menu')

        
menu()
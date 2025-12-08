### Inicio do Programa ###
def menu():
    print('Bem vindo ao menu do Sistema de Controle de Gastos')

    ### Menu de Interação ###
    while True:
        print('Escolha uma opção:')
        print('(1) Inserir Novo Gasto')
        print('(2) Listar Gastos')
        print('(3) Relatorio Geral')
        print('(4) Remover Gasto')
        print('(5) Fechar Programa...')
        select = int(input(''))
        match select:
            case 1:
                print('Função ainda não implementada')
            case 2:
                print('Função ainda não implementada')
            case 3:
                print('Função ainda não implementada')
            case 4:
                print('Função ainda não implementada')
            case 5:
                exit('Fim do Progama')
            case _:
                print('O número que você digitou não representa nenhuma das opções do menu')

        
menu()
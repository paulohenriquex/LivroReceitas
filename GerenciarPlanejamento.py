def GerenciarPlanejamento(conn):
    
    while True:
            try:
                print('1 - Planejar cardápio')
                print('2 - Alterar item do cardápio')
                print('3 - Excluir item do cardápio')
                print('0 - Sair')
                opcao = int(input())
                if opcao == 1:
                    planejarCardapio(conn)
                elif opcao == 2:
                    alterarItemCardapio(conn)
                elif opcao == 3:
                    excluirItemCardapio(conn)
                elif opcao == 0:
                    break
                else:
                    print('Opcao inválida.')
            except ValueError:
                print('Digite um número válido.')


def planejarCardapio(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT *FROM receitas')
    receitas = cursor.fetchall()
    for receita in receitas:
        print('')
        print(receita)
        print()
    # nome = int(input('Digite o ID da receita: '))



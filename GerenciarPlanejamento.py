from datetime import datetime

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

    busca = int(input('Digite o id da receita: '))
    cursor.execute('SELECT *FROM receitas WHERE id = %s',(busca,))
    idReceita = cursor.fetchone()[0]
    while True:
        try:
            dataInput = input('Digite a data da refeição (DD/MM/AAAA) ')
            dataRefeicao = datetime.strptime(dataInput, '%d/%m/%Y').date()
            break
        except ValueError:
            print("Formato de data inválido. Por favor, digite novamente no formato DD/MM/AAAA.")
    print("Data da refeição:", dataRefeicao)
    try:
        cursor.execute('INSERT INTO planejamento (idReceita,data) VALUES (%s,%s) ',(idReceita,dataRefeicao,))
        conn.commit()
    except ValueError:
        print('Erro ao adicionar ao banco de dados.')
import psycopg2

def GerenciarReceitas(conn):

        while True:
            try:
                    
                print('1 - Cadastrar Receita')
                print('2 - Listar Receitas')
                print('3 - Atualizar Receitas')
                print('4 - Excluir Receitas')
                print('0 - Sair')
                opcao = int(input())
                if opcao == 1:
                    cadastrarReceitas(conn)
                elif opcao == 2:
                    listarReceitas(conn)
                elif opcao == 3:
                    atualizarReceitas(conn)
                elif opcao == 4:
                    excluirReceitas(conn)
                elif opcao == 0:
                    break
                else:
                    print('Opcao inválida.')
            except ValueError:
                print('Número inválido, digite uma opção válida.')
def cadastrarReceitas(conn):
    cursor = conn.cursor()
    nomeReceita = input('Digite o nome da receita: ').capitalize()
    if nomeReceita == 'S':
        return
    cursor.execute('INSERT INTO receitas (nome) VALUES (%s) RETURNING id',(nomeReceita,))
    idReceita = cursor.fetchone()[0]
    conn.commit()
    while True:
        nomeIngrediente = input('Digite o nome do ingrediente ou (s) para sair: ').capitalize()
        if nomeIngrediente == 'S':
            break
        cursor.execute('SELECT id FROM produtos WHERE nome = %s',(nomeIngrediente,))
        idProduto = cursor.fetchone()[0]
        percapta = float(input('Digite o percapta do produto: '))
        try:
            cursor.execute('INSERT INTO ingredienteReceita (idProduto,idReceita,percapta) VALUES (%s,%s,%s)',(idProduto,idReceita,percapta,))
            conn.commit()
        except ValueError:
            print('Erro ao adicionar ao banco de dados.')

def listarReceitas(conn):
    cursor = conn.cursor()
    cursor.execute('''SELECT r.nome, ir.idProduto, p.nome, ir.percapta 
    FROM receitas r
    JOIN ingredienteReceita ir ON r.id = ir.idReceita
    JOIN produtos p ON ir.idProduto = p.id''')
    receitas = cursor.fetchall()
    
    if not receitas:
        print('Nenhuma receita cadastrada.')
        return
    
    receita_atual = None
    for receita in receitas:
        if receita[0] != receita_atual:
            if receita_atual:
                print()
            print(f'Nome da Receita: {receita[0]}')
            print('Ingredientes:')
            receita_atual = receita[0]
        print(f'- {receita[2]} (percapta: {receita[3]})')

def atualizarReceitas(conn):
    print('Atualizar Receita')

def excluirReceitas(conn):
    try:
        buscarId = input('Digite o ID da receita para excluir: ')
        cursor  = conn.cursor()
        cursor.execute('DELETE FROM receitas WHERE id = %s',(buscarId,))
        conn.commit()
        print('Receita excluida com sucesso.')
    except psycopg2.Error as e:
        print(f'Erro ao exlcuir receita: {e}.')
    
    
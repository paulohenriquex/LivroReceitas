import psycopg2

def GerenciarProdutos(conn):

        while True:
            try:
                print('1 - Cadastrar Produto')
                print('2 - Listar Produtos')
                print('3 - Atualizar Produto')
                print('4 - Excluir Produto')
                print('0 - Sair')
                opcao = int(input())
                if opcao == 1:
                    cadastrarProdutos(conn)
                elif opcao == 2:
                    listarProdutos(conn)
                elif opcao == 3:
                    atualizarProduto(conn)
                elif opcao == 4:
                    excluirProdutos(conn)
                elif opcao == 0:
                    break
                else:
                    print('Opcao inválida.')
            except ValueError:
                print('Digite um número válido.')

def cadastrarProdutos(conn):
    try:
        cursor = conn.cursor()
        nome = input('Nome do produto: ').capitalize()
        preco = float(input('Preço: '))
        quantidade = float(input('Quantidade: '))
        medida = input('Medida: ')
        cursor.execute('INSERT INTO produtos (nome,preco,quantidade,medida)VALUES(%s,%s,%s,%s)',(nome,preco,quantidade,medida))
        print('Produto adicionado com sucesso.')
        conn.commit()

    except Exception as e:
            print(f'Erro: {e}')
            return None
 

def listarProdutos(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    for produto in produtos:
        if produto:
            print(produto)
        else:
            print('Nenhum produto cadastrado.')

def atualizarProduto(conn):

    try:
        buscarProduto = input('Digite o produto a ser alterado: ').capitalize()
        novoNome = input('Digite o novo nome: ')
        novoPreco = float(input('Digite o novo preço: '))
        novaQuantidade = float(input('Digite a nova quantidade: '))
        novaMedida = input('Digite a nova medida: ')
        
        cursor  = conn.cursor()
        cursor.execute('UPDATE produtos SET nome = %s, preco = %s, quantidade = %s, medida = %s WHERE nome = %s',(novoNome,novoPreco,novaQuantidade,novaMedida,buscarProduto))
        conn.commit()
        print('Produto atualizado com sucesso.')
    except psycopg2.Error as e:
        print(f'Erro ao atualizar produto: {e}')

def excluirProdutos(conn):
    try:
        idProduto = input('Digite o id do produto a ser excluido: ')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id = %s',(idProduto))
        conn.commit()
        print('Produto excluido com sucesso.')
    except psycopg2.Error as e:
        print(f'Erro ao excluir produto: {e}')
    
    
import psycopg2
import getpass
import GerenciarProdutos as gp
import GerenciarReceitas as gr
import GerenciarPlanejamento as gpl

def conexao():
    try:
        conn = psycopg2.connect(
            host='localhost',
            user='postgres',
            dbname='LivroReceitas',
            password=getpass.getpass("Senha do banco de dados: ")
        )
        print('Conexão realizada com sucesso!')
        return conn
    except Exception as e:
        print(f'Erro: {e}')
        exit()

def criarTabelas(conn):
    cursor  = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS produtos (id SERIAL PRIMARY KEY,nome VARCHAR(100),preco FLOAT, quantidade FLOAT, medida VARCHAR(10))')
    cursor.execute('CREATE TABLE IF NOT EXISTS receitas (id SERIAL PRIMARY KEY,nome VARCHAR(100))')
    cursor.execute('CREATE TABLE IF NOT EXISTS ingredienteReceita (id SERIAL PRIMARY KEY,idProduto INTEGER REFERENCES produtos(id),idReceita INTEGER REFERENCES receitas(id), percapta FLOAT)')
    conn.commit()

def main(conn):
    while True:
            try:
                print('1 - Produtos')
                print('2 - Receitas')
                print('3 - Planejar cardápio')
                print('0 - Sair')
                opcao  = int(input())
                if opcao == 1:
                    gp.GerenciarProdutos(conn)
                elif opcao == 2:
                    gr.GerenciarReceitas(conn)
                elif opcao == 3:
                    gpl.GerenciarPlanejamento(conn)
                elif opcao == 0:
                    break
                else:
                    print('Opção inválida!')
            except ValueError:
                    print('Digite um número válido: ')

if __name__ == '__main__':
    conn = conexao()
    criarTabelas(conn)
    if conn:
        main(conn)
    else:
        print('Erro na conexão com o banco de dados')
        
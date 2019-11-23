from dao import DataBaseAccess, sqlite3
from veiculo import Veiculo


class LocacaoDAO:
    def __init__(self):
        '''Se conecta ao banco de dados'''
        self.database = DataBaseAccess()
        self.database.connect()
        self.database.persist()

    def view(self):
        resultado = None
        try:
            self.database.execute('SELECT * FROM veiculo')
            resultado = self.database.fetchall()
        except sqlite3.Error:
            print('Falha ao tentar selecionar os registros.')
        return resultado

    def view_venda(self, id):
        '''Retorna nome, valor de venda e quantidade no estoque do produto da tabela produto.'''
        resultado = None
        try:
            self.database.execute(
                'SELECT id, nome, valor_venda, quantidade FROM produto WHERE id=?', (id))
            resultado = self.database.fetchall()
        except sqlite3.Error:
            print('Falha ao tentar selecionar os registros.')
        return resultado

    def update_estoque(self, nova_quantidade, id):
        '''Atualiza os registros no Banco de Dados.'''
        try:
            self.database.execute(
                'UPDATE produto SET quantidade = quantidade-? WHERE id=? ', (nova_quantidade, id))
            self.database.persist()
        except sqlite3.Error:
            print('Falha ao tentar inserir registros na tabela produto.')

    def close(self):
        '''Fechando conexão com o banco de dados.'''
        self.database.disconnect()
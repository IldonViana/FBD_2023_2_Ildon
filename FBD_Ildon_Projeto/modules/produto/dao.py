from modules.produto.modelo import Produto
from modules.produto.sql import SQLProduto
from server.connect import Connect


class DAOProduto(SQLProduto):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, produto: Produto):
        if not isinstance(produto, Produto):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (produto.nome, produto.marca, produto.categoria))
        self.connection.commit()
        return produto

    def get_by_nome(self, nome):
        query = self._SELECT_BY_NOME
        cursor = self.connection.cursor()
        cursor.execute(query, (nome,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    def get_produto_por_id(self, id):

        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchone()
        if not results:
            return None
        cols = [desc[0] for desc in cursor.description]
        results = dict(zip(cols, results))

        return results

    def delete_produto_by_id(self, id):
        if self.get_produto_por_id(id):
            query = self._DELETE_BY_ID
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, (id,))  # Quando tenta apagar uma referencia da erro em tempo de execução
                self.connection.commit()
                return True
            except:
                return False
        return False

    def update_produto_by_id(self, produto: Produto, id):

        query = self._UPDATE_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (produto.nome, produto.marca, produto.categoria, id))
        self.connection.commit()

        return True

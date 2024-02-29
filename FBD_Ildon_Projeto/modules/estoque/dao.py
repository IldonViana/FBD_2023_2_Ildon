from modules.estoque.modelo import Estoque
from modules.estoque.sql import SQLEstoque
from server.connect import Connect


class DAOEstoque(SQLEstoque):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, estoque: Estoque):
        if not isinstance(estoque, Estoque):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (estoque.id_produto, estoque.quant_lote, estoque.quant_disponivel, estoque.preco_venda))
        self.connection.commit()
        return estoque

    def get_by_id_produto(self, id_produto):
        query = self._SELECT_BY_ID_PRODUTO
        cursor = self.connection.cursor()
        cursor.execute(query, (id_produto,))
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

    def get_estoque_por_id(self, id):

        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchone()
        if not results:
            return None
        cols = [desc[0] for desc in cursor.description]
        results = dict(zip(cols, results))

        return results

    def delete_estoque_by_id(self, id):
        if self.get_estoque_por_id(id):
            query = self._DELETE_BY_ID
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, (id,))  # Quando tenta apagar uma referencia da erro em tempo de execução
                self.connection.commit()
                return True
            except:
                return False
        return False

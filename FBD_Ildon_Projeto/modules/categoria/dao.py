from modules.categoria.modelo import Categoria
from modules.categoria.sql import SQLCategoria
from server.connect import Connect


class DAOCategoria(SQLCategoria):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def salvar(self, categoria: Categoria):
        if not isinstance(categoria, Categoria):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (categoria.nome,))
        self.connection.commit()
        return categoria

    # def get_by_nome(self, nome):
    #     query = self._SELECT_BY_NOME
    #     cursor = self.connection.cursor()
    #     cursor.execute(query, (nome,))
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = [dict(zip(cols, i)) for i in results]
    #     results = [Categoria(**i) for i in results]
    #     return results

    def get_by_nome(self, nome):
        query = self._SELECT_BY_NOME
        cursor = self.connection.cursor()
        cursor.execute(query, (nome,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    # def get_all(self):
    #     query = self._SELECT_ALL
    #     cursor = self.connection.cursor()
    #     cursor.execute(query)
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = [dict(zip(cols, i)) for i in results]
    #     results = [Categoria(**i) for i in results]
    #     return results

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    # def get_all(self):
    #     query = self._SELECT_ALL
    #     cursor = self.connection.cursor()
    #     cursor.execute(query)
    #     results = cursor.fetchall()
    #     cols = [desc[0] for desc in cursor.description]
    #     results = dict(zip(cols, results))
    #     return results

    def get_categoria_por_id(self, id):

        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchone()
        if not results:
            return None
        cols = [desc[0] for desc in cursor.description]
        results = dict(zip(cols, results))

        return results

    def delete_categoria_by_id(self, id):
        if self.get_categoria_por_id(id):
            query = self._DELETE_BY_ID
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, (id,))  # Quando tenta apagar uma referencia da erro em tempo de execução
                self.connection.commit()
                return True
            except:
                return False
        return False

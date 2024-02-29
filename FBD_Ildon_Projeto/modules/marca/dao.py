from modules.marca.modelo import Marca
from modules.marca.sql import SQLMarca
from server.connect import Connect


class DAOMarca(SQLMarca):
    def __init__(self):
        self.connection = Connect().get_instance()

    def create_table(self):
        return self._CREATE_TABLE

    def get_by_cnpj(self, cnpj):
        query = self._SELECT_BY_CNPJ
        cursor = self.connection.cursor()
        cursor.execute(query, (cnpj,))
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    def salvar(self, marca: Marca):
        if not isinstance(marca, Marca):
            raise Exception("Tipo inválido")
        query = self._INSERT_INTO
        cursor = self.connection.cursor()
        cursor.execute(query, (marca.nome, marca.cnpj))
        self.connection.commit()
        return marca

    def get_all(self):
        query = self._SELECT_ALL
        cursor = self.connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        cols = [desc[0] for desc in cursor.description]
        results = [dict(zip(cols, i)) for i in results]
        return results

    def get_marca_por_id(self, id):

        query = self._SELECT_BY_ID
        cursor = self.connection.cursor()
        cursor.execute(query, (id,))
        results = cursor.fetchone()
        if not results:
            return None
        cols = [desc[0] for desc in cursor.description]
        results = dict(zip(cols, results))

        return results

    def delete_marca_by_id(self, id):
        if self.get_marca_por_id(id):
            query = self._DELETE_BY_ID
            cursor = self.connection.cursor()
            try:
                cursor.execute(query, (id,))  # Quando tenta apagar uma referencia da erro em tempo de execução
                self.connection.commit()
                return True
            except:
                return False
        return False

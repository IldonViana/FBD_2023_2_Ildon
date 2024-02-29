import psycopg2


class Connect:

    def __init__(self):
        info_server = dict(
            dbname="FBD_projeto",
            user="postgres", password="lolfdp33",
            host="localhost", port="5432"
        )
        self._connection = psycopg2.connect(**info_server)

    def create_tables(self):
        from modules.marca.dao import DAOMarca
        from modules.categoria.dao import DAOCategoria
        from modules.produto.dao import DAOProduto
        from modules.estoque.dao import DAOEstoque
        cursor = self._connection.cursor()
        cursor.execute(DAOMarca().create_table())
        cursor.execute(DAOCategoria().create_table())
        cursor.execute(DAOProduto().create_table())
        cursor.execute(DAOEstoque().create_table())
        self._connection.commit()
        cursor.close()

    def get_instance(self):
        return self._connection

    def init_database(self, version='v1'):
        if version == 'v1':
            self.create_tables()
        if version == 'v2':
            self.update_database()

    def update_database(self):
        pass

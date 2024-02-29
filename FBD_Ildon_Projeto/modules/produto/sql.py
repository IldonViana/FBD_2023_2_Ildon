from modules.marca.sql import SQLMarca
from modules.categoria.sql import SQLCategoria


class SQLProduto:
    _TABLE_NAME = 'produto'
    _COL_ID = 'id'
    _COL_NOME = 'nome'
    _COL_ID_MARCA = 'id_marca'
    _COL_ID_CATEGORIA = 'id_categoria'
    _REFERENCES_MARCA = f'{SQLMarca._TABLE_NAME}({SQLMarca._COL_ID})'
    _REFERENCES_CATEGORIA = f'{SQLCategoria._TABLE_NAME}({SQLCategoria._COL_ID})'
    _CAMPOS_OBRIGATORIOS = [_COL_NOME]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'(id serial primary key, ' \
                    f'{_COL_NOME} varchar(255), ' \
                    f'{_COL_ID_MARCA} int REFERENCES {_REFERENCES_MARCA}, ' \
                    f'{_COL_ID_CATEGORIA} int REFERENCES {_REFERENCES_CATEGORIA}' \
                    f');'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_NOME},{_COL_ID_MARCA},{_COL_ID_CATEGORIA}) values(%s,%s,%s)'
    _SELECT_BY_NOME = f"SELECT * from {_TABLE_NAME} where {_COL_NOME} ilike %s"
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f"SELECT * from {_TABLE_NAME} where {_COL_ID}=%s"
    _DELETE_BY_ID = f"DELETE from {_TABLE_NAME} where {_COL_ID}=%s"
    _UPDATE_BY_ID = (f"UPDATE {_TABLE_NAME} SET {_COL_NOME} = %s, {_COL_ID_MARCA} = %s,"
                     f" {_COL_ID_CATEGORIA} = %s  WHERE {_COL_ID} = %s")

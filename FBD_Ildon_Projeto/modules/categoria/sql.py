class SQLCategoria:
    _TABLE_NAME = 'categoria'
    _COL_ID = 'id'
    _COL_NOME = 'nome'
    _CAMPOS_OBRIGATORIOS = [_COL_NOME]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'({_COL_ID} serial primary key, ' \
                    f'{_COL_NOME} varchar(255));'

    _INSERT_INTO = f'INSERT INTO {_TABLE_NAME}({_COL_NOME}) values(%s)'
    _SELECT_BY_NOME = f"SELECT * from {_TABLE_NAME} where {_COL_NOME} ilike %s"
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f"SELECT * from {_TABLE_NAME} where {_COL_ID}=%s"
    _DELETE_BY_ID = f"DELETE from {_TABLE_NAME} where {_COL_ID}=%s"

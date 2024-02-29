from modules.produto.sql import SQLProduto


class SQLEstoque:
    _TABLE_NAME = 'estoque'
    _COL_ID = 'id'
    _COL_QUANT_LOTE = 'quant_lote'
    _COL_QUANT_DISPONIVEL = 'quant_disponivel'
    _COL_PRECO_VENDA = 'preco_venda'
    _COL_ID_PRODUTO = 'id_produto'
    _REFERENCES_PRODUTO = f'{SQLProduto._TABLE_NAME}({SQLProduto._COL_ID})'
    _CAMPOS_OBRIGATORIOS = [_COL_QUANT_LOTE, _COL_ID_PRODUTO, _COL_PRECO_VENDA]

    _CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_TABLE_NAME} ' \
                    f'(id serial primary key, ' \
                    f'{_COL_QUANT_LOTE} int, ' \
                    f'{_COL_QUANT_DISPONIVEL} int, ' \
                    f'{_COL_PRECO_VENDA} float, ' \
                    f'{_COL_ID_PRODUTO} int REFERENCES {_REFERENCES_PRODUTO}' \
                    f');'

    _INSERT_INTO = (f'INSERT INTO {_TABLE_NAME}({_COL_ID_PRODUTO},{_COL_QUANT_LOTE},'
                    f'{_COL_QUANT_DISPONIVEL},{_COL_PRECO_VENDA}) values(%s,%s,%s,%s)')
    _SELECT_BY_ID_PRODUTO = f"SELECT * from {_TABLE_NAME} where {_COL_ID_PRODUTO}=%s"
    _SELECT_ALL = f"SELECT * from {_TABLE_NAME}"
    _SELECT_BY_ID = f"SELECT * from {_TABLE_NAME} where {_COL_ID}=%s"
    _DELETE_BY_ID = f"DELETE from {_TABLE_NAME} where {_COL_ID}=%s"

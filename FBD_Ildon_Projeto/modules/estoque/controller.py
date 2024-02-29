from flask import Blueprint, request, jsonify
from modules.estoque.dao import DAOEstoque
from modules.estoque.modelo import Estoque
from modules.estoque.sql import SQLEstoque

from modules.produto.dao import DAOProduto

estoque_controller = Blueprint('estoque_controller', __name__)
dao_estoque = DAOEstoque()
dao_produto = DAOProduto()
module_name = 'estoque'


def get_estoques():
    estoque = dao_estoque.get_all()
    response = jsonify(estoque)
    response.status_code = 200
    return response


def create_estoque():
    data = request.json
    erros = []
    for campo in SQLEstoque._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")
    if not erros:
        if not (dao_produto.get_produto_por_id(data.get('id_produto'))):
            erros.append(f"O id do campo produto não existe")
    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    estoque = Estoque(data['id_produto'], data['quant_lote'], data['preco_venda'])
    dao_estoque.salvar(estoque)
    response = jsonify('OK')
    response.status_code = 201
    return response


@estoque_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_or_create_estoques():
    if request.method == 'GET':
        return get_estoques()
    else:
        return create_estoque()


@estoque_controller.route(f'/{module_name}/id/<id>/', methods=['GET'])
def get_estoques_by_id(id: int):
    estoques = dao_estoque.get_estoque_por_id(id)
    if estoques:
        return estoques
    response = jsonify({})
    response.status_code = 404
    return response


@estoque_controller.route(f'/{module_name}/produto/<id_produto>/', methods=['GET'])
def get_estoque_by_produto(id_produto: int):
    estoques = dao_estoque.get_by_id_produto(id_produto)
    if estoques:
        return estoques
    response = jsonify({})
    response.status_code = 404
    return response


@estoque_controller.route(f'/{module_name}/delete_id/<id>/', methods=['DELETE'])
def delete_categoria_by_id(id: int):
    status = dao_estoque.delete_estoque_by_id(id)
    if status:
        response = jsonify('Apagado com sucesso')
        response.status_code = 201
        return response
    response = jsonify('Não foi possível apagar')
    response.status_code = 404
    return response

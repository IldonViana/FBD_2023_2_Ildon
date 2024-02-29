from flask import Blueprint, request, jsonify
from modules.produto.dao import DAOProduto
from modules.produto.modelo import Produto
from modules.produto.sql import SQLProduto

from modules.marca.dao import DAOMarca
from modules.categoria.dao import DAOCategoria

produto_controller = Blueprint('produto_controller', __name__)
dao_produto = DAOProduto()
dao_marca = DAOMarca()
dao_categoria = DAOCategoria()
module_name = 'produto'


def get_produtos():
    produtos = dao_produto.get_all()
    # results = [produto.__dict__ for produto in produtos]
    response = jsonify(produtos)
    response.status_code = 200
    return response


def create_produto():
    data = request.json
    erros = []
    for campo in SQLProduto._CAMPOS_OBRIGATORIOS:
        if campo not in data.keys() or not data.get(campo, '').strip():
            erros.append(f"O campo {campo} é obrigatorio")
    if not erros:
        if not (dao_marca.get_marca_por_id(data.get('id_marca'))):
            erros.append(f"O id do campo marca não existe")
        if not (dao_categoria.get_categoria_por_id(data.get('id_categoria'))):
            erros.append(f"O id do campo categoria não existe")
    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    produto = Produto(data['nome'], data['id_marca'], data['id_categoria'])
    dao_produto.salvar(produto)
    response = jsonify('OK')
    response.status_code = 201
    return response


@produto_controller.route(f'/{module_name}/', methods=['GET', 'POST'])
def get_or_create_produtos():
    if request.method == 'GET':
        return get_produtos()
    else:
        return create_produto()


@produto_controller.route(f'/{module_name}/id/<id>/', methods=['GET'])
def get_produto_by_id(id: int):
    produto = dao_produto.get_produto_por_id(id)
    if produto:
        return produto
    response = jsonify({})
    response.status_code = 404
    return response


@produto_controller.route(f'/{module_name}/nome/<nome>/', methods=['GET'])
def get_produto_by_nome(nome: str):
    produto = dao_produto.get_by_nome(nome)
    if produto:
        return produto
    response = jsonify({})
    response.status_code = 404
    return response


@produto_controller.route(f'/{module_name}/delete_id/<id>/', methods=['DELETE'])
def delete_produto_by_id(id: int):
    status = dao_produto.delete_produto_by_id(id)
    if status:
        response = jsonify('Apagado com sucesso')
        response.status_code = 201
        return response
    response = jsonify('Não foi possível apagar')
    response.status_code = 404
    return response


@produto_controller.route(f'/{module_name}/update_id/<id>/', methods=['PATCH'])
def update_produto_by_id(id: int):
    data = request.json
    erros = []
    if not data.get('nome'):
        data['nome'] = dao_produto.get_produto_por_id(id)['nome']
    if data.get('id_marca'):
        if not (dao_marca.get_marca_por_id(data.get('id_marca'))):
            erros.append(f"O id do campo marca não existe")
    else:
        data['id_marca'] = dao_produto.get_produto_por_id(id)['id_marca']
    if data.get('id_categoria'):
        if not (dao_categoria.get_categoria_por_id(data.get('id_categoria'))):
            erros.append(f"O id do campo categoria não existe")
    else:
        data['id_categoria'] = dao_produto.get_produto_por_id(id)['id_categoria']
    if erros:
        response = jsonify(erros)
        response.status_code = 401
        return response

    produto = Produto(data['nome'], data['id_marca'], data['id_categoria'])
    dao_produto.update_produto_by_id(produto, id)

    response = jsonify('OK')
    response.status_code = 201
    return response

from flask import Flask
from modules.marca.controller import marca_controller
from modules.categoria.controller import categoria_controller
from modules.produto.controller import produto_controller
from modules.estoque.controller import estoque_controller
from server.connect import Connect

app = Flask(__name__)
app.register_blueprint(marca_controller)
app.register_blueprint(categoria_controller)
app.register_blueprint(produto_controller)
app.register_blueprint(estoque_controller)
Connect().init_database('v2')
app.run(debug=True)

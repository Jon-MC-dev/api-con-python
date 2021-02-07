import json
# importaciones de la bd
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from entidades.Productos import Productos
from entidades.Categorias import Categorias
from entidades.Marcas import Marcas
# importaciones de api
from flask_restful import Resource, Api
from rutas.Producto import Producto
from rutas.Categoria import Categoria


app = Flask(__name__)
link = "mysql+pymysql://root@localhost/flaskmysql"
app.config['SQLALCHEMY_DATABASE_URI'] = link
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Objetos que regresan el SQLAlchemy y el Marshmallow(Squema)
obj_Marcas = Marcas(db, ma)
obj_Categorias = Categorias(db, ma)
obj_Productos = Productos(db, ma)

# esquemas

# esquemas de muchos
esquema_categorias = obj_Categorias.CategoriaSquema(many=True)
esquema_productos = obj_Productos.ProductoSquema(many=True)

db.create_all() # crea las entidades por si no existen

# La api como tal
api = Api(app)

ruta_producto = Producto(Resource, db, obj_Productos).RutaProducto
ruta_categoria = Categoria(Resource, db, obj_Categorias).RutaCategoria
#
api.add_resource(ruta_producto, '/productos')
api.add_resource(ruta_categoria, '/categoria')

if __name__ == '__main__':
    app.run(debug=True)
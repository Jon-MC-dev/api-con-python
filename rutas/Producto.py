from flask import jsonify, request
from sqlalchemy.exc import IntegrityError

class Producto:
    RutaProducto = None  # Clase interna
    #

    def __init__(self, Resource, db_alquemy, objProducto):
        class RutaProducto(Resource):
            objProducto_db = None
            objProducto_ma = None
            def __init__(self):
                self.objProducto_db = objProducto.ProductosModel
                self.objProducto_ma = objProducto.ProductoSquema
            def get(self):
                todos = self.objProducto_db.query.all()
                resultado = self.objProducto_ma(many=True).dump(todos)
                return jsonify(resultado)

            def post(self):
                print(request.json['codigo_barras'])
                codigo_barras = request.json['codigo_barras']
                descripcion = request.json['descripcion']
                detalles_adicionales = request.json['detalles_adicionales']
                existencias = request.json['existencias']
                id_categoria = request.json['id_categoria']
                id_marca = request.json['id_marca']
                modelo = request.json['modelo']
                nuevoProducto = objProducto.ProductosModel(id_categoria, id_marca, modelo, existencias, descripcion, codigo_barras, detalles_adicionales)
                db_alquemy.session.add(nuevoProducto)
                try:
                    db_alquemy.session.commit()
                except IntegrityError as e:
                    print(e)

                return objProducto.ProductoSquema().jsonify(nuevoProducto)

        self.RutaProducto = RutaProducto
        #
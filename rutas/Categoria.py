from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
import json


class Categoria:
    RutaCategoria = None

    def __init__(self, Resource, db_alquemy, objCategoria):
        class RutaCategoria(Resource):
            CategoriaModel = None
            CategoriaSquema = None

            def __init__(self):
                self.CategoriaModel = objCategoria.CategoriaModel
                self.CategoriaSquema = objCategoria.CategoriaSquema

            def get(self):
                todos = self.CategoriaModel.query.all()
                resultado = self.CategoriaSquema(many=True).dump(todos)
                return jsonify(resultado)

            def post(self):
                nombreCategoria = request.json['nombre']
                nueva_categoria = self.CategoriaModel(nombreCategoria)
                db_alquemy.session.add(nueva_categoria)
                error = ""
                try:
                    db_alquemy.session.commit()
                except IntegrityError as e:
                    error = "El nombre de la categoria ya existe"
                    print(e)

                respuesta = self.CategoriaSquema().jsonify(nueva_categoria).get_json()
                return json.dumps({'obj': respuesta, 'error': error}, sort_keys=True)

        self.RutaCategoria = RutaCategoria

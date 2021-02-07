from flask import jsonify, request
from sqlalchemy.exc import IntegrityError
import json

class Marca:
    RutaMarca = None
    def __init__(self, Resource, db_alquemy, objMarca):
        class RutaMarca(Resource):
            MarcaModel = None
            MarcaSquema = None

            def __init__(self):
                self.MarcaModel = objMarca.MarcaModel
                self.MarcaSquema = objMarca.MarcaSquema

            def get(self):
                todos = self.MarcaModel.query.all()
                resultado = self.MarcaSquema(many=True).dump(todos)
                return jsonify(resultado)

            def post(self):
                nombreMarca = request.json['nombre']
                nueva_marca = self.MarcaModel(nombreMarca)
                db_alquemy.session.add(nueva_marca)
                error = ""
                try:
                    db_alquemy.session.commit()
                except IntegrityError as e:
                    error = "El nombre de la marca ya existe"
                    print(e)

                respuesta = self.MarcaSquema().jsonify(nueva_marca).get_json()
                return json.dumps({'obj': respuesta,'error': error})


        self.RutaMarca = RutaMarca
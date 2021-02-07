from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app = Flask(__name__)
link = "mysql+pymysql://root@localhost/flaskmysql"
app.config['SQLALCHEMY_DATABASE_URI'] = link
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Tareas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(70), unique=True)
    descripcion = db.Column(db.String(100))

    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion


db.create_all()


class EsquemaTareas(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'descripcion')


esquemaTarea = EsquemaTareas()
esquemaTareas = EsquemaTareas(many=True)


@app.route('/tareas', methods=['POST'])
def crearTareas():
    titulo = request.json['titulo']
    descripcion = request.json['descripcion']
    nueva_tarea = Tareas(titulo, descripcion)
    db.session.add(nueva_tarea)
    db.session.commit()

    return esquemaTarea.jsonify(nueva_tarea)


@app.route('/tareas', methods=['GET'])
def obtenerTareas():
    todas = Tareas.query.all()
    resultado = esquemaTareas.dump(todas)
    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)

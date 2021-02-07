class Marcas:
    MarcaModel = None
    MarcaSquema = None
    def __init__(self, db, ma):
        class MarcaModel(db.Model):
            __tablename__ = "tbl_marcas"

            id_marca = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(45),unique=True)
            productos = db.relationship('ProductosModel', backref='MarcaModel')

            def __init__(self, nombre):
                self.nombre = nombre
        class MarcaSquema(ma.Schema):
            class Meta:
                fields = ('id_marca', 'nombre')

        self.MarcaModel = MarcaModel
        self.MarcaSquema = MarcaSquema

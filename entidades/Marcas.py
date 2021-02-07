class Marcas:
    MarcaModel = None
    MarcaSquema = None
    def __init__(self, db, ma):
        class MarcaModel(db.Model):
            __tablename__ = "tbl_marcas"

            id_marca = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(45))
            productos = db.relationship('ProductosModel', backref='MarcaModel')

            def __init__(self, id_marca, nombre):
                self.id_marca = id_marca
                self.nombre = nombre
        class MarcaSquema(ma.Schema):
            class Meta:
                fields = ('id_marca', 'nombre')

        self.MarcaModel = MarcaModel
        self.MarcaSquema = MarcaSquema

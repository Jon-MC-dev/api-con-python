class Categorias:
    CategoriaModel = None
    CategoriaSquema = None
    def __init__(self,db,ma):
        class CategoriaModel(db.Model):
            __tablename__ = "tbl_categorias"

            categoria_id = db.Column(db.Integer, primary_key=True)
            nombre = db.Column(db.String(40))
            productos = db.relationship('ProductosModel', backref='CategoriaModel')

            def __init__(self, nombre):
                self.nombre = nombre

        class CategoriaSquema(ma.Schema):
            class Meta:
                fields = ('categoria_id', 'nombre')

        self.CategoriaModel = CategoriaModel
        self.CategoriaSquema = CategoriaSquema
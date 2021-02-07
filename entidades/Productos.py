class Productos:
    ProductosModel = None
    ProductoSquema = None
    def __init__(self, bdatos, marsh):
        class ProductosModel(bdatos.Model):
            __tablename__ = "tbl_productos"

            id_producto = bdatos.Column(bdatos.Integer, primary_key=True, autoincrement=True)
            id_categoria = bdatos.Column(bdatos.Integer,bdatos.ForeignKey('tbl_categorias.categoria_id'), nullable=False)
            id_marca = bdatos.Column(bdatos.Integer, bdatos.ForeignKey('tbl_marcas.id_marca'), nullable=False)
            modelo = bdatos.Column(bdatos.String(45))
            existencias = bdatos.Column(bdatos.Integer)
            descripcion = bdatos.Column(bdatos.String(45))
            codigo_barras = bdatos.Column(bdatos.String(45))
            detalles_adicionales = bdatos.Column(bdatos.String(45))

            def __init__(self, id_categoria, id_marca, modelo, existencias, descripcion, codigo_barras, detalles_adicionales):
                # self.id_producto = id_producto
                self.id_categoria = id_categoria
                self.id_marca = id_marca
                self.modelo = modelo
                self.existencias = existencias
                self.descripcion = descripcion
                self.codigo_barras = codigo_barras
                self.detalles_adicionales = detalles_adicionales

        class ProductoSquema(marsh.Schema):
            class Meta:
                fields = ('id_producto', 'id_categoria', 'id_marca', 'modelo', 'existencias', 'descripcion', 'codigo_barras', 'detalles_adicionales')

        self.ProductosModel = ProductosModel
        self.ProductoSquema = ProductoSquema
from app import db

class CatOrganigrama(db.Model):
    __tablename__ = 'CAT_ORGANIGRAMA'
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String(20), nullable=True)
    nombre = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f'<CatOrganigrama {self.codigo} - {self.nombre}>'

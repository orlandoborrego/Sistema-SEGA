from app import db
from datetime import datetime

class Hipervinculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entidad = db.Column(db.String(200), nullable=False)         
    tipo_documento = db.Column(db.String(100), nullable=False)   
    fecha = db.Column(db.String(50), nullable=True)              
    url_pdf = db.Column(db.String(500), nullable=True)          
    observaciones = db.Column(db.Text, nullable=True)           
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', backref='hipervinculos')
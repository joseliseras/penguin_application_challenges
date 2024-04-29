from flask_sqlalchemy import SQLAlchemy

# Instanciar la base de datos
db = SQLAlchemy()

# Definir el modelo de la base de datos
class Reservacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    telefono = db.Column(db.String(250))
    email = db.Column(db.String(250))
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    num_personas = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Reservacion {self.id}>'

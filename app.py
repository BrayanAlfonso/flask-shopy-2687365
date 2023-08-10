from flask import Flask;
from flask_sqlalchemy import SQLAlchemy;
from flask_migrate import Migrate;
from datetime import datetime;

#Creacón y configuración de la app

#Creación del objeto
app = Flask(__name__)

#Para definir a que pase de datos nos vamos a conectar
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3307/flask_shopy_2687365'

#Establecer una configuración para sql admin
#Crear los objetos de sqlalchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Creación de modelos o entidades

#tabla de clientes
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String(100), unique= True)
    email=db.Column(db.String(120), unique= True)
    password=db.Column(db.String(128))

#Tabla de productos

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Numeric(precision=10, scale=2))
    imagen=db.Column(db.String(100))
    
    

#Tabla de ventas

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id=db.Column(db.ForeignKey('cliente.id'))
    

#Tabla detalles
class detalles(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    producto_id=db.Column(db.ForeignKey('producto.id'))
    venta_id=db.Column(db.ForeignKey('venta.id'))   

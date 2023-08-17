from flask import Flask, render_template;
from flask_wtf import FlaskForm;
from wtforms import StringField, SubmitField;
from flask_sqlalchemy import SQLAlchemy;
from flask_migrate import Migrate;
from datetime import datetime;
from flask_bootstrap import Bootstrap;


#Creacón y configuración de la app

#Creación del objeto
app = Flask(__name__)

#Para definir a que pase de datos nos vamos a conectar
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost:3307/flask_shopy_2687365'
app.config["SECRET_KEY"] = "Brayan123@"
bootstrap = Bootstrap(app)

#Establecer una configuración para sql admin
#Crear los objetos de sqlalchemy y migrate

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Creación de modelos o entidades

#tabla de clientes
class Cliente(db.Model):
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key= True)
    username=db.Column(db.String(100), unique= True)
    email=db.Column(db.String(120), unique= True)
    password=db.Column(db.String(128))

#Tabla de productos

class Producto(db.Model):
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key= True)
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Numeric(precision=10, scale=2))
    imagen=db.Column(db.String(100))
    
    

#Tabla de ventas

class Venta(db.Model):
    __tablename__="ventas"
    id = db.Column(db.Integer, primary_key= True)
    fecha = db.Column(db.DateTime, default = datetime.utcnow)
    cliente_id=db.Column(db.ForeignKey('clientes.id'))
    

#Tabla detalles 
class Detalle(db.Model):
    __tablename__="detalles"
    id = db.Column(db.Integer, primary_key= True)
    producto_id=db.Column(db.ForeignKey('productos.id'))
    venta_id=db.Column(db.ForeignKey('ventas.id'))   


#Definir el formulario de registro de productos
class NuevoProductoFrom (FlaskForm):
    nombre = StringField("Nombre de producto")
    precio = StringField("Precio del producto")
    submit = SubmitField("Registrar")

@app.route("/registrar_producto", methods=['GET', 'POST'])
def registrar():
    form = NuevoProductoFrom()
    p=Producto()
    
    if form.validate_on_submit():
        #Cuando se de click en el boton se registrara
        form.populate_obj(p)
        db.session.add(p)
        db.session.commit()
        return "producto registrado"
    return render_template("registrar.html",
                            form = form)
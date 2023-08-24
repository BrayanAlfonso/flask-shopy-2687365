from . import productos
from flask import render_template
from .forms import NewProductForm

#Crear las rutas del blueprint
@productos.route('/crear')
def crear():
    form=NewProductForm()
    return render_template("new.html", form=form)
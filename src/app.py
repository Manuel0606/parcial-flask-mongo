from flask import Flask, render_template, request, redirect, url_for, flash
from config import *
from registro import Registro
import time

db_conection = Conexion()
app = Flask(__name__)
app.secret_key = 'some_secret'

def mensaje_segun_altura(altura):
    text=""
    ALTURA = {
        "baja": 1.50,
        "media": 1.70,
        "alta": 1.90,
        "muy_alta": 2.30
    }
    if altura <= ALTURA["baja"]:
        text = "Persona de altura baja"
    elif altura <= ALTURA["media"]:
        text = "Persona de altura media"
    elif altura <= ALTURA["alta"]:
        text = "Persona alta"
    elif altura <= ALTURA["muy_alta"]:
        text = "Persona muy alta"
    else:
        text = "Persona demasiado alta"
    return text

def validarDatos(nombre, altura):
    try: 
        altura = float(altura)
        validacion = True if altura > 0.0 else False
        validacion = True if len(nombre) > 0 else False
        return validacion
    except:
        return False
    
@app.route('/registro_altura')
def registroAltura():
    return render_template('registro_altura.html')

@app.route('/registro', methods=['POST'])
def registro():
    registros = db_conection['Datos']
    nombre = request.form['nombre']
    altura = request.form['altura']

    validacion = validarDatos(nombre=nombre, altura=altura)

    if not validacion :
        flash('Datos invalidos')
        return redirect(url_for('registroAltura'))

    if nombre and altura :
        mensaje = mensaje_segun_altura(float(altura))
        print(mensaje)
        flash(mensaje)
        registro = Registro(nombre, altura)
        registros.insert_one(registro.formato_doc())
        return redirect(url_for('registroAltura'))
    else:
        return 'Error'


@app.route('/registro_por_parametros/<string:nombre>/<float:altura>')
def registro_por_parametros(nombre="", altura=0.0):
    registros = db_conection['Datos']
    if nombre and altura :
        mensaje = mensaje_segun_altura(float(altura))
        print(mensaje)
        flash(mensaje)
        registro = Registro(nombre, altura)
        registros.insert_one(registro.formato_doc())
        return redirect(url_for('registroAltura'))
    else:
        return 'Error'

@app.route('/')
def index():
    return render_template('index.html')
def error_404(error):
    return render_template('error_404.html'), 404

if __name__ == '__main__':
  app.register_error_handler(404, error_404)
  app.run(debug=True, port=9999)

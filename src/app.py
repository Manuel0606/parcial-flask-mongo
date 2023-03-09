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
        validacion = True if altura > 0 else False
        validacion = True if nombre.len() > 0 else False
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/andres')
def felipe():
    biografia = """
    Nací el 28 de Octubre de 2001, pasé mi niñez y parte de mi adolescencia en Bogotá, luego vine a vivir a Chiquinquirá a terminar mis estudios de la secundaria, allí fue donde aprendí a jugar basketball.
    Mis pasatiempos son el basketball, la computación, la música y el emprendimiento.
    En mis metas se encuentra el lograr aportar mis conocimientos y habilidades en beneficio de la sociedad.
    """
    foto_url="images/foto_andres.jpg"
    data = {
        'nombre': 'Andres',
        'nombreCompleto':'Andrés Felipe Carranza Ruiz',
        'biografia':biografia,
        'foto_url':foto_url
    }
    return render_template('usuario.html', data=data)

@app.route('/manuel')
def manuel():
    biografia = """
    Nací el 06 de Abril de 2002, pasé mi niñez y parte de mi adolescencia en Pamplona, Cúcuta, Bucaramanga, San Alberto y Guateque, luego llegué a vivir a Ubaté a iniciar mis estudios universitarios.
    Algunos de mis pasatiempos son el basketball, los videojuegos, la computación y la música.
    Mis metas son alcanzar el nivel senior en desarrollo web.
    """
    foto_url="images/foto_manuel.jpeg"
    data = {
        'nombre': 'Manuel',
        'nombreCompleto':'Manuel Alejandro Comezaña Quintero',
        'biografia':biografia,
        'foto_url':foto_url
    }
    return render_template('usuario.html', data=data)
  
def error_404(error):
    return render_template('error_404.html'), 404

if __name__ == '__main__':
  app.register_error_handler(404, error_404)
  app.run(debug=True, port=9999)

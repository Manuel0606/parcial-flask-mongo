from flask import Flask, render_template, request, redirect, url_for
from config import *
from registro import Registro

db_conection = Conexion()
app = Flask(__name__)

@app.route('/registro_usuario')
def registroUsuario():
    return render_template('registro.html')

@app.route('/registro', methods=['POST'])
def registro():
    registros = db_conection['Registro']
    nombre = request.form['nombre']
    correo = request.form['correo']
    mensaje = request.form['mensaje']

    if nombre and correo and mensaje:
        registro = Registro(nombre, correo, mensaje)
        registros.insert_one(registro.formato_doc())
        return redirect(url_for('registroUsuario'))
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
  
if __name__ == '__main__':
  app.run(debug=True, port=6001)

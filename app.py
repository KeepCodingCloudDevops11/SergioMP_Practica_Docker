from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import logging
from pythonjsonlogger import jsonlogger
import os

# Carga las variables env
load_dotenv()

app = Flask(__name__)

# Conexión base de datos. 
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}/{os.getenv('DATABASE_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar SQLAlchemy
db = SQLAlchemy(app)

# Configuración de logging en formato JSON
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# Creación de la clase person con los atributos nombre y país 
class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    pais = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Persona {self.nombre} de {self.pais}>'

# Ruta para añadir una nueva persona
@app.route('/add_persona', methods=['POST'])
def add_persona():
    nombre = request.form.get('nombre')
    pais = request.form.get('pais')
    if not nombre or not pais:
        logger.warning("Intento de añadir una persona sin nombre o país", extra={'nombre': nombre, 'pais': pais})
        return jsonify({'error': 'Falta información'}), 400
    persona = Persona(nombre=nombre, pais=pais)
    db.session.add(persona)
    db.session.commit()
    logger.info("Persona añadida correctamente", extra={'nombre': nombre, 'pais': pais})
    return jsonify({'message': 'Persona añadida!'}), 201

# Ruta para eliminar una persona por su ID
@app.route('/delete_persona/<int:id>', methods=['DELETE'])
def delete_persona(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()
    logger.info("Persona eliminada correctamente", extra={'id': id, 'nombre': persona.nombre, 'pais': persona.pais})
    return jsonify({'message': 'Persona eliminada!'}), 200

# Ruta raíz para comprobación rápida de que la app está funcionando
@app.route('/')
def index():
    logger.info("Página principal accedida")
    return "¡Hola Mundo!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

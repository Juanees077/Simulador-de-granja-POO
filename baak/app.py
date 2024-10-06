from flask import Flask, jsonify, request
from flask_cors import CORS
from simulador import Granja, Animal

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

granja = Granja()

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/animales', methods=['GET', 'POST', 'OPTIONS'])
def animales():
    if request.method == 'OPTIONS':
        return '', 200
    elif request.method == 'GET':
        return jsonify([animal.to_dict() for animal in granja.animales])
    elif request.method == 'POST':
        data = request.json
        nuevo_animal = Animal(data['tipo'], data['edad'], data['peso'], data['raza'])
        granja.agregar_animal(nuevo_animal)
        return jsonify(nuevo_animal.to_dict()), 201

@app.route('/simular', methods=['POST', 'OPTIONS'])
def simular_dia():
    if request.method == 'OPTIONS':
        return '', 200
    resultado = granja.simular_dia()
    return jsonify({
        'animales': [animal.to_dict() for animal in granja.animales],
        'clima': resultado.get('clima', None)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
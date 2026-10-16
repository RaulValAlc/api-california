from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
import urllib.request

app = Flask(__name__)

# fragmento del ejercicio 8
MODELO_PATH = 'modelo_california.pkl'
URL_MODELO = 'https://github.com/RaulValAlc/api-california/raw/refs/heads/main/modelo_california.pkl'

if not os.path.exists(MODELO_PATH):
    print("Modelo no encontrado en local. Descargando desde GitHub...")
    urllib.request.urlretrieve(URL_MODELO, MODELO_PATH)
    print("Descarga completada.")
# ---------------------------------

modelo = joblib.load(MODELO_PATH)

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API funcionando correctamente"})

@app.route('/predict', methods=['POST'])
def predict():
    datos = request.get_json()
    caracteristicas = np.array(datos['features']).reshape(1, -1)
    prediccion = modelo.predict(caracteristicas)
    return jsonify({"prediccion": float(prediccion[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
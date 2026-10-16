from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
modelo = joblib.load('modelo_california.pkl')

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "API funcionando"})

@app.route('/predict', methods=['POST'])
def predict():
    datos = request.get_json()
    caracteristicas = np.array(datos['features']).reshape(1, -1)
    prediccion = modelo.predict(caracteristicas)
    return jsonify({"prediccion": float(prediccion[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
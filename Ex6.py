# Utilize a API pública: https://api.agify.io?name=Victor
# Crie um endpoint: GET /previsao-idade/{nome}
# Que retorna: { "nome": "Victor", "idade_prevista": 34 } - Use requests.

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/previsao-idade/<string:nome>', methods=['GET'])
def consomeAPI(nome):
    url = f'https://api.agify.io?name={nome}'

    response = requests.get(url)
    
    if response.status_code != 200:
        return jsonify({"erro": "Erro ao consultar API externa"}), 500

    resposta = response.json()

    pessoa = {
        'nome': resposta['name'],
        'idade_prevista': resposta['age']
    }

    return jsonify(pessoa), 200


if __name__ == '__main__':
    app.run(debug=True)
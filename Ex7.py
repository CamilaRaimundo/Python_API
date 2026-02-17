# Crie um endpoint: GET /cep/{cep}
# Que consuma: https://viacep.com.br/ws/{cep}/json/
# E retorne apenas: { "logradouro": "...", "bairro": "...", "cidade": "...", "estado": "..." }

from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/cep/<string:cep>', methods=['GET'])
def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"erro": "Erro ao consultar API externa"}), 500

    dados = response.json()

    if "erro" in dados:
        return jsonify({"erro": "CEP não encontrado"}), 404

    resultado = {
        "logradouro": dados.get("logradouro"),
        "bairro": dados.get("bairro"),
        "cidade": dados.get("localidade"),
        "estado": dados.get("uf")
    }

    return jsonify(resultado), 200

if __name__ == '__main__':
    app.run(debug=True)
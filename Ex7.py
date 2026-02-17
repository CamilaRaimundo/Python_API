# Crie um endpoint: GET /cep/{cep}
# Que consuma: https://viacep.com.br/ws/{cep}/json/
# E retorne apenas: { "logradouro": "...", "bairro": "...", "cidade": "...", "estado": "..." }

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/cep/<string:cep>', methods=['GET'])
def consomeAPI(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    return response.json() if response.status_code == 200 else None 


if __name__ == '__main__':
    app.run(debug=True)
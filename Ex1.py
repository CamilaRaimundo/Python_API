# Crie uma API utilizando Flask/FastAPI com os seguintes endpoints:
    # GET / → retorna { "message": "API funcionando" }
    # GET /status → retorna: { "status": "online", "version": "1.0" }

from flask import Flask, request, jsonify

# Flask → cria a aplicação
# request → acessa dados da requisição (query params, JSON, etc.)
# jsonify → transforma dicionários Python em JSON


# cria a aplicação Flask (instância)
app = Flask(__name__)

# Endpoints são os caminhos da URL que sua API disponibiliza. Por padrão são GET
@app.route('/funcionando')
def index():
    dados = {'mensagem': 'API funcionando'} #isso é um dicionário Python
    return jsonify(dados), 200, {'Content-Type': 'application/json; charset=utf-8'} #transforma em JSON e o retorna no endpoint

@app.route('/infos', methods=['GET']) #pode ser adicionado o método
def informacoes():
    info = {'status': 'online', 'version': '1.0'}
    return jsonify(info), 200, {'Content-Type': 'application/json; chatset=utf-8'}


# sobe um servidor local em: http://localhost:5000
if __name__ == '__main__':
    app.run(debug=True)
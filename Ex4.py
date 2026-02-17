# Crie um endpoint: POST /produtos
    # Recebe: { "nome": "Notebook", "preco": 3500 }
    # Retorna: { "id": 1, "nome": "Notebook", "preco": 3500 }
# Use lista em memória para armazenar produtos.


from flask import Flask, request, jsonify

app = Flask(__name__)

produtos = [] #lista para armazenar os produtos  

@app.route('/produto', methods=['POST'])
def criar_produto():
    try: # testa se o body foi enviado
        # Lê o JSON enviado no corpo da requisição e converte para um dicionário Python
    

        dados_produto = request.get_json()
        dados = {
            'id': len(produtos) + 1,
            'nome': dados_produto['nome'],
            'preco': dados_produto['preco']
        }
        produtos.append(dados)
    
        return jsonify(dados), 201
    
    except Exception as e: # se der erro, exibe
        return jsonify({"erro": str(e)}), 500
    

@app.route('/produtos', methods=['GET'])
def exibe_produtos():
    return jsonify(produtos), 200


if __name__ == '__main__':
    app.run(debug=True)
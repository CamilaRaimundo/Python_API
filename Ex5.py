from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = []

# POST /usuarios
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados_usuario = request.get_json()

    if not dados_usuario or 'nome' not in dados_usuario or 'idade' not in dados_usuario:
        return jsonify({"erro": "JSON inválido"}), 400

    usuario = {
        'id': len(usuarios) + 1,
        'nome': dados_usuario['nome'],
        'idade': dados_usuario['idade']
    }

    usuarios.append(usuario)

    return jsonify(usuario), 201


# GET /usuarios
@app.route('/usuarios', methods=['GET'])
def exibe_usuarios():
    return jsonify(usuarios), 200


# GET /usuarios/<id>
@app.route('/usuarios/<int:id>', methods=['GET'])
def buscar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            return jsonify(usuario), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


# PUT /usuarios/<id>
@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_usuario(id):
    dados = request.get_json()

    for usuario in usuarios:
        if usuario['id'] == id:
            usuario['nome'] = dados.get('nome', usuario['nome'])
            usuario['idade'] = dados.get('idade', usuario['idade'])
            return jsonify(usuario), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


# DELETE /usuarios/<id>
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    for usuario in usuarios:
        if usuario['id'] == id:
            usuarios.remove(usuario)
            return jsonify({"mensagem": "Usuário removido"}), 200

    return jsonify({"erro": "Usuário não encontrado"}), 404


if __name__ == '__main__':
    app.run(debug=True)
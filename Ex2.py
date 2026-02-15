# Implemente: GET /alunos/{nome}
# Deve retornar: {"aluno": "Victor", "disciplina": "Tecnologias e Programação Integrada" }

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alunos', methods=['GET'])
def parametro():
    nome = request.args.get('nome', 'Aluno') #recebe parâmetro pela URL. Se não enviar, usa o valor padrão "Aluno"
    disciplina = 'Tecnologias e Programação Integrada'
    dados = {'Aluno': nome, 'Disciplina': disciplina}
    
    return jsonify(dados), 200

if __name__ == '__main__':
    app.run(debug=True)
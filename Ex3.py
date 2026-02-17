# Implemente: GET /media?nota1=7&nota2=9
# Retornar: { "media": 8.0, "situacao": "Aprovado" }
# Regras: Média ≥ 7 → Aprovado / Média < 7 → Reprovado

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/media', methods=['GET'])
def parametro():
    nota1 = request.args.get('nota1', 0)
    nota2 = request.args.get('nota2', 0)

    # os valores recebidos vem como String, é necessário fazer a conversão explícita para float, possibilitando o cálculo
    media = (float(nota1) + float(nota2)) / 2 #calcula a média das notas 

    if media >= 7:
        dados = {'Média': media, 'Situação': 'Aprovado!'}
    else:
        dados = {'Média': media, 'Situação': 'Reprovado!'}
    
    return jsonify(dados), 200, {'Content-Type': 'application/json; chatset=utf-8'}


if __name__ == '__main__':
    app.run(debug=True)
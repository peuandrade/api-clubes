from flask import Flask, request, jsonify
import json

app = Flask(__name__)

clubes = {
    "Flamengo": {
        "historia": "Campeão da Libertadores de 2019.",
        "fundacao": "15/11/1895",
        "estadio": "Maracanã",
        "ídolo": "Zico"
    },
    "Palmeiras": {
        "historia": "Campeão da Libertadores em 2020 e 2021.",
        "fundacao": "26/08/1914",
        "estadio": "Allianz Parque",
        "ídolo": "Marcos"
    },
    "Corinthians": {
        "historia": "Campeão Mundial em 2012.",
        "fundacao": "01/09/1910",
        "estadio": "Neo Química Arena",
        "ídolo": "Sócrates"
    },
    "São Paulo": {
        "historia": "Tricampeão da Libertadores e do Mundial.",
        "fundacao": "25/01/1930",
        "estadio": "Morumbi",
        "ídolo": "Rogério Ceni"
    },
    "Vasco": {
        "historia": "Campeão da Libertadores em 1998.",
        "fundacao": "21/08/1898",
        "estadio": "São Januário",
        "ídolo": "Roberto Dinamite"
    }
}

@app.route('/clube', methods=['GET'])
def get_clube_info():
    nome_clube = request.args.get('nome')

    if not nome_clube:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório."}), 400

    nome_clube_formatado = nome_clube.title()
    info = clubes.get(nome_clube_formatado)

    if info:
        return app.response_class(
            response=json.dumps({
                "clube": nome_clube_formatado,
                **info
            }, ensure_ascii=False, indent=2),
            mimetype='application/json'
        )
    else:
        return app.response_class(
            response=json.dumps({
                "erro": f"O clube '{nome_clube}' não foi encontrado na nossa base, campeão!"
                }, ensure_ascii=False, indent=2),
            mimetype='application/json'), 404

if __name__ == '__main__':
    app.run(debug=True)
# clase 6
from flask import Flask, request, jsonify

app = Flask(__name__)

alumnos = [{"name": "Pepe Garcia"}, {"name": "Nicole"}]

@app.route('/', methods=["GET", "POST", "DELETE"])
def list_alumnos():
    if request.method == "GET":
        return jsonify(alumnos)
    elif request.method == "POST":
        data = request.form
        alu = data["name"]
        alumnos.append({"name": alu})
        return jsonify(alumnos), 201

@app.route('/<alumno>', methods=["GET", "DELETE"])
def edit_alumnos(alumno):

    if request.method == "GET":
        for x in alumnos:
            if x['name'] == alumno:
                return jsonify(x), 200
        
        return jsonify({"msg": "not found"}), 404 # deberia ser 204

    elif request.method == "DELETE":
        for i in range(0, len(alumnos)):
            if alumnos[i]["name"] == alumno:
                del(alumnos[i])
                return jsonify(alumnos), 200
        
        return jsonify({"msg": "not found"}), 404 # deberia ser 204

if __name__ == "__main__":
    app.run(port=5000, debug=True)
from flask import Flask, jsonify, request # type: ignore

app = Flask(__name__)



  # Variable global todos
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)


    # Agregar el nuevo todo a la lista
    todos.append(request_body)
    
    # Devolver la lista actualizada
    return jsonify(todos)


# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)


